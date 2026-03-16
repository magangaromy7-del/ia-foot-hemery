import requests
import pandas as pd
import random
from datetime import datetime, timedelta

# ==========================================
# CONFIGURATION - "X-Auth-Token"
# ==========================================
API_TOKEN = "9ca5bcac82e444c5810061edf4aff13f"
# ==========================================

# On demande les matchs d'aujourd'hui + les 7 prochains jours
date_debut = datetime.now().strftime('%Y-%m-%d')
date_fin = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')

URL = f"https://api.football-data.org/v4/matches?dateFrom={date_debut}&dateTo={date_fin}"
HEADERS = {"X-Auth-Token": API_TOKEN}

def generer_analyse(home_team, away_team):
    p1 = random.randint(35, 65)
    px = random.randint(20, 30)
    p2 = 100 - p1 - px
    score = random.choice(["1-0", "2-1", "2-0", "1-1", "0-1", "1-2"])
    buts = "+2.5" if p1 > 48 else "-2.5"
    confiance = "⭐⭐⭐⭐" if p1 > 55 else "⭐⭐⭐"
    return p1, px, p2, score, buts, confiance

def update_data():
    print(f"🚀 Récupération des matchs du {date_debut} au {date_fin}...")
    try:
        response = requests.get(URL, headers=HEADERS)
        data = response.json()
        matchs_extraits = []

        if 'matches' not in data:
            print("⚠️ Erreur API ou aucune donnée reçue.")
            return

        for m in data.get('matches', []):
            competition = m['competition']['name']
            home = m['homeTeam']['name']
            away = m['awayTeam']['name']
            logo = m['homeTeam']['crest']
            # On récupère aussi la date du match
            date_match = m['utcDate'][:10] 
            
            p1, px, p2, score, buts, conf = generer_analyse(home, away)
            
            matchs_extraits.append({
                "Logo": logo,
                "Date": date_match,
                "Ligue": competition,
                "Match": f"{home} vs {away}",
                "1_pct": p1,
                "X_pct": px,
                "2_pct": p2,
                "Score_Prédit": score,
                "Total_Buts": buts,
                "Confiance": conf
            })

        if matchs_extraits:
            df = pd.DataFrame(matchs_extraits)
            # On trie par date pour que ce soit plus clair
            df = df.sort_values(by="Date")
            df.to_csv("match.csv", index=False)
            print(f"✅ Succès ! {len(matchs_extraits)} matchs enregistrés pour la semaine.")
        else:
            print("⚠️ Aucun match trouvé pour cette période.")

    except Exception as e:
        print(f"❌ Erreur : {e}")

if __name__ == "__main__":
    update_data()
