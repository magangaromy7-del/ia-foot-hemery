import streamlit as st
import pandas as pd

# 1. Configuration de la page
st.set_page_config(page_title="Master Predicts", layout="centered", page_icon="⚽")

# --- STYLE CSS POUR LES CARTES (Pour ressembler à ton image) ---
st.markdown("""
    <style>
    .match-card {
        background-color: #2e2e2e;
        border-radius: 15px;
        padding: 15px;
        margin-bottom: 10px;
        border: 1px solid #333;
        color:black;
    }
    .time { color: #888; font-size: 14px; font-weight: bold; margin-bottom: 5px; }
    .team-row { display: flex; align-items: center; margin: 8px 0; }
    .team-logo { width: 25px; height: 25px; margin-right: 15px; object-fit: contain; }
    .team-name { font-size: 16px; font-weight: 500; flex-grow: 1; }
    .prono-badge { 
        background-color: #2e2e2e; 
        padding: 5px 10px; 
        border-radius: 8px; 
        font-size: 12px; 
        color: #ffd700; 
        border: 1px solid #444;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Chargement des données
try:
    df = pd.read_csv("match.csv")
    
    st.title("⚽ Master Predicts")
    st.write(f"Pronostics de la semaine")

    # 3. Affichage sous forme de CARTES
    for index, row in df.iterrows():
        # On sépare les équipes (le script auto_update met "Equipe A vs Equipe B")
        teams = row['Match'].split(" vs ")
        home_team = teams[0]
        away_team = teams[1]
        
        # Affichage de la carte
        st.markdown(f"""
            <div class="match-card">
                <div style="display: flex; justify-content: space-between;">
                    <div class="time">📅 {row['Date']} | {row['Ligue']}</div>
                    <div class="prono-badge">🎯 Score : {row['Score_Prédit']}</div>
                </div>
                <div class="team-row">
                    <img src="{row['Logo']}" class="team-logo">
                    <div class="team-name">{home_team}</div>
                </div>
                <div class="team-row">
                    <img src="https://cdn-icons-png.flaticon.com/512/53/53254.png" class="team-logo" style="filter: invert(1);">
                    <div class="team-name">{away_team}</div>
                </div>
                <div style="margin-top: 10px; font-size: 12px; color: #aaa; border-top: 1px solid #333; padding-top: 10px;">
                    📈 1: {row['1_pct']}% | X: {row['X_pct']}% | 2: {row['2_pct']}% | {row['Confiance']}
                </div>
            </div>
            """, unsafe_allow_html=True)

except Exception as e:
    st.info("🔄 Le robot prépare les nouvelles cartes de matchs...")

# 4. Signature Hemery
st.markdown(f"""
    <div style="text-align: center; margin-top: 30px;">
        <p style="color: #888;">APPLICATION Développé par</p>
        <p style="font-weight: bold; color: white;">HEMERY DALLAH </p>
    </div>
    """, unsafe_allow_html=True)
