import streamlit as st
import pandas as pd
from datetime import datetime

# 1. Config
st.set_page_config(page_title="Master Predicts LIVE", layout="centered")

# --- CSS PRO ---
st.markdown("""
    <style>
    .card {
        background-color: #121212;
        border: 1px solid #222;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 15px;
        text-align: center;
    }
    .live-tag {
        background-color: #ff0000;
        color: white;
        padding: 3px 8px;
        border-radius: 5px;
        font-size: 10px;
        font-weight: bold;
        animation: blink 1.2s infinite;
    }
    @keyframes blink { 0% {opacity: 1;} 50% {opacity: 0.3;} 100% {opacity: 1;} }
    .score { font-size: 24px; font-weight: bold; color: #00ff00; letter-spacing: 5px; }
    .team-name { font-size: 16px; color: white; font-weight: 500; }
    .footer { text-align: center; color: #555; font-size: 12px; margin-top: 50px; }
    </style>
    """, unsafe_allow_html=True)

# 2. Interface
st.title("⚽ Master Predicts")
if st.button("🔄 Actualiser les scores"):
    st.rerun()

try:
    df = pd.read_csv("match.csv")
    aujourdhui = datetime.now().strftime('%Y-%m-%d')
    
    # Filtrer uniquement pour aujourd'hui pour le mode LIVE
    df_live = df[df['Date'] == aujourdhui]

    if not df_live.empty:
        for _, row in df_live.iterrows():
            teams = row['Match'].split(" vs ")
            est_live = row.get('Etat') == "LIVE"
            
            # Affichage de la carte
            st.markdown(f"""
            <div class="card">
                <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                    <span style="color: #888; font-size: 12px;">{row['Ligue']}</span>
                    {"<span class='live-tag'>● LIVE</span>" if est_live else ""}
                </div>
                <div style="display: flex; justify-content: space-around; align-items: center;">
                    <div class="team-name">{teams[0]}</div>
                    <div class="score">{row['Score_Live'] if est_live else 'VS'}</div>
                    <div class="team-name">{teams[1]}</div>
                </div>
                <div style="margin-top: 15px; border-top: 1px solid #222; padding-top: 10px; display: flex; justify-content: space-between; color: #ffd700; font-size: 13px;">
                    <span>🎯 Prono: {row['Score_Prédit']}</span>
                    <span>⚽ Buts: {row['Total_Buts']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.write("Aucun match en direct pour le moment.")

except Exception:
    st.error("Erreur : Lance le 'Run workflow' sur GitHub pour activer les données.")

# 3. Signature
st.markdown('<div class="footer">DÉVELOPPÉ PAR<br><b style="color:#888">HEMERY DALLAH</b></div>', unsafe_allow_html=True)
