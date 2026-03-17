import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# 1. Configuration de la page
st.set_page_config(page_title="Master Predicts", layout="centered", page_icon="⚽")

# --- STYLE CSS ---
st.markdown("""
    <style>
    .match-card {
        background-color: #1e1e1e;
        border-radius: 12px;
        padding: 12px;
        margin-bottom: 10px;
        border: 1px solid #333;
        color: white;
    }
    .live-badge { 
        background-color: #ff0000; color: white; padding: 2px 6px; border-radius: 4px; 
        font-size: 10px; font-weight: bold; animation: blinker 1.5s linear infinite;
    }
    @keyframes blinker { 50% { opacity: 0; } }
    .live-score { font-size: 18px; font-weight: bold; color: #00ff00; margin-left: 10px; }
    .time { color: #888; font-size: 11px; font-weight: bold; }
    .team-row { display: flex; align-items: center; margin: 6px 0; }
    .team-logo { width: 22px; height: 22px; margin-right: 12px; object-fit: contain; }
    .team-name { font-size: 14px; font-weight: 500; flex-grow: 1; }
    .badge-container { display: flex; gap: 6px; }
    .prono-badge { background-color: #2e2e2e; padding: 2px 6px; border-radius: 4px; font-size: 10px; color: #ffd700; border: 1px solid #444; }
    .goals-badge { background-color: #004d40; padding: 2px 6px; border-radius: 4px; font-size: 10px; color: #00e676; border: 1px solid #00796b; }
    
    .footer-signature {
        text-align: center;
        margin-top: 40px;
        padding-bottom: 30px;
        border-top: 1px solid #333;
        padding-top: 20px;
    }
    .footer-text { color: #666; font-size: 10px; letter-spacing: 1px; margin-bottom: 5px; }
    .footer-name { color: #ffffff; font-weight: bold; font-size: 16px; letter-spacing: 2px; }
    </style>
    """, unsafe_allow_html=True)

# 2. Chargement des données
try:
    df = pd.read_csv("match.csv")
    dates_disponibles = sorted(df['Date'].unique())
    aujourdhui = datetime.now().strftime('%Y-%m-%d')
    
    st.title("⚽ Master Predicts")

    noms_onglets = []
    for d in dates_disponibles:
        if d == aujourdhui: noms_onglets.append("DIRECT / AUJOURD'HUI")
        else: noms_onglets.append(datetime.strptime(d, '%Y-%m-%d').strftime('%d %b.').upper())

    if noms_onglets:
        tabs = st.tabs(noms_onglets)
        for i, tab in enumerate(tabs):
            with tab:
                date_selectionnee = dates_disponibles[i]
                df_filtre = df[df['Date'] == date_selectionnee]

                for index, row in df_filtre.iterrows():
                    teams = row['Match'].split(" vs ")
                    est_live = row.get('Etat') == "LIVE"
                    score_display = str(row['Score_Live']) if est_live else "vs"
                    badge_live = '<span class="live-badge">● LIVE</span>' if est_live else f'<span class="time">{row["Ligue"].upper()}</span>'

                    st.markdown(f"""
                        <div class="match-card">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                                <div>{badge_live}</div>
                                <div class="badge-container">
                                    <div class="prono-badge">🎯 Prono: {row['Score_Prédit']}</div>
                                    <div class="goals-badge">⚽ Buts: {row['Total_Buts']}</div>
                                </div>
                            </div>
                            <div class="team-row">
                                <img src="{row['Logo']}" class="team-logo">
                                <div class="team-name">{teams[0]}</div>
                                {f'<div class="live-score">{score_display.split("-")[0]}</div>' if est_live else ''}
                            </div>
                            <div class="team-row">
                                <img src="https://cdn-icons-png.flaticon.com/512/53/53254.png" class="team-logo" style="filter: invert(1); opacity:0.2;">
                                <div class="team-name">{teams[1]}</div>
                                {f'<div class="live-score">{score_display.split("-")[1]}</div>' if est_live else ''}
                            </div>
                            <div style="margin-top: 8px; font-size: 10px; color: #666; border-top: 1px solid #333; padding-top: 8px; display: flex; justify-content: space-between;">
                                <span>PROBA: 1:{row['1_pct']}% | X:{row['X_pct']}% | 2:{row['2_pct']}%</span>
                                <span style="color: #ffd700;">{row['Confiance']}</span>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
    else:
        st.info("Lance le 'Run workflow' sur GitHub pour afficher les matchs.")

except Exception as e:
    st.info("En attente des données... Relance le workflow sur GitHub.")

# 3. Signature finale
st.markdown("""
    <div class="footer-signature">
        <p class="footer-text">APPLICATION DÉVELOPPÉE PAR</p>
        <p class="footer-name">HEMERY DALLAH</p>
    </div>
    """, unsafe_allow_html=True)
