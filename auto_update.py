import requests
import pandas as pd
import random

# =========================================================
# CONFIGURATION - "X-Auth-Token"
# =========================================================
API_TOKEN = "9ca5bcac82e444c5810061edf4aff13f"
# =========================================================

URL = "https://api.football-data.org/v4/matches"
HEADERS = {"X-Auth-Token": API_TOKEN}

def generer_analyse(home_team, away_team):
    """Simule une analyse Master Predicts (IA)"""
    p1 = random.randint(35, 65)
    px = random.randint(20, 30)
    p2 = 100 - p1 - px
    
    scores_possibles = ["1-0", "2-1", "2-0", "1-1", "0-1", "1-2"]
    score = random.choice(scores_possibles)
    buts = "+2.5" if p1 > 48 else "-2.5"
    confiance = "⭐⭐⭐⭐" if p1 > 55 else "⭐⭐⭐"
    
    return p1, px, p2, score, buts, confiance

def update_data():
    print("🚀 Connexion à l'API Football-Data en cours...")
    try:
        response = requests.get(URL, headers=HEADERS)
        if response.status_code != 200:
            print(f"❌ Erreur API : {response.status_code}. Vérifie ta clé !")
            return

        data = response.json()
        matchs_extraits = []

        # On récupère les matchs du jour et de demain
        for m in data.get('matches', []):
            home = m['homeTeam']['name']
            away = m['awayTeam']['name']
            logo = m['homeTeam']['crest'] # Lien du logo officiel
            
            # Analyse auto
            p1, px, p2, score, buts, conf = generer_analyse(home, away)
            
            matchs_extraits.append({
                "Logo": logo,
                "Match": f"{home} vs {away}",
                "1_pct": p1,
                "X_pct": px,
                "2_pct": p2,
                "Score_Prédit": score,
                "Total_Buts": buts,
                "Confiance": conf
            })

        if not matchs_extraits:
            print("⚠️ Aucun match trouvé pour aujourd'hui.")
            return

        # Création du fichier CSV
        df = pd.DataFrame(matchs_extraits)
        df.to_csv("match.csv", index=False)
        print(f"✅ Succès ! {len(matchs_extraits)} matchs mondiaux ajoutés au site.")

    except Exception as e:
        print(f"❌ Erreur critique : {e}")

if __name__ == "__main__":
    update_data()
