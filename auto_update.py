import requests
import pandas as pd
import random
from datetime import datetime, timedelta

# ==========================================
# TA CONFIGURATION - "X-Auth-Token"
# ==========================================
API_TOKEN = " 9ca5bcac82e444c5810061edf4aff13f"
# ==========================================

date_debut = datetime.now().strftime('%Y-%m-%d')
date_fin = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
HEADERS = {"X-Auth-Token": API_TOKEN}

def calculer_prono_intelligent(h_rank, a_rank):
    diff = a_rank - h_rank
    base_win = 40 + (diff * 2)
    p1 = max(20, min(75, base_win + random.randint(-5, 5)))
    px = random.randint(20, 30)
    p2 = 100 - p1 - px
    
    if p1 > 60: score, conf = "2-0", "⭐⭐⭐⭐"
    elif p1 > 45: score, conf = "2-1", "⭐⭐⭐⭐"
    elif p2 > 45: score, conf = "0-1", "⭐⭐⭐"
    else: score, conf = "1-1", "⭐⭐⭐"
    
    buts = "+2.5" if (p1 + p2) > 70 else "-2.5"
    return p1, px, p2, score, buts, conf

def update_data():
    print("📡 Récupération des scores et pronostics...")
    try:
        url_matches = f"https://api.football-data.org/v4/matches?dateFrom={date_debut}&dateTo={date_fin}"
        response = requests.get(url_matches, headers=HEADERS)
        data = response.json()
        matchs_extraits = []

        for m in data.get('matches', []):
            # Récupération du score réel
            etat = m['status'] # 'IN_PLAY', 'FINISHED', 'TIMED', etc.
            s_home = m['score']['fullTime']['home'] if m['score']['fullTime']['home'] is not None else 0
            s_away = m['score']['fullTime']['away'] if m['score']['fullTime']['away'] is not None else 0
            
            # Calcul du prono
            p1, px, p2, prono_score, buts, conf = calculer_prono_intelligent(random.randint(1,20), random.randint(1,20))
            
            matchs_extraits.append({
                "Logo": m['homeTeam']['crest'],
                "Date": m['utcDate'][:10],
                "Ligue": m['competition']['name'],
                "Match": f"{m['homeTeam']['name']} vs {m['awayTeam']['name']}",
                "Score_Live": f"{s_home}-{s_away}",
                "Etat": "LIVE" if etat in ['IN_PLAY', 'PAUSED'] else ("FINI" if etat == 'FINISHED' else "PRE"),
                "1_pct": p1, "X_pct": px, "2_pct": p2,
                "Score_Prédit": prono_score,
                "Total_Buts": buts,
                "Confiance": conf
            })

        if matchs_extraits:
            df = pd.DataFrame(matchs_extraits)
            df.to_csv("match.csv", index=False)
            print(f"✅ Mise à jour réussie : {len(matchs_extraits)} matchs.")
            
    except Exception as e:
        print(f"❌ Erreur : {e}")

if __name__ == "__main__":
    update_data()
