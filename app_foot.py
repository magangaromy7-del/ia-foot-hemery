import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# 1. Configuration
st.set_page_config(page_title="Master Predicts", layout="centered", page_icon="⚽")

# --- STYLE CSS (Simplifié pour éviter les bugs) ---
st.markdown("""
    <style>
    .match-card {
        background-color: #1e1e1e;
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 15px;
        border: 1px solid #333;
        color: white;
    }
    .live-badge { background-color: #ff0000; color: white; padding: 2px 6px; border-radius: 4px; font-size: 10px; font-weight: bold; }
    .team-name { font-size: 16px; font-weight: bold; color: white; }
    .score-live { font-size: 20px; font-weight: bold; color: #00ff00; }
    .footer-name { text-align: center; color: white; font-weight: bold; margin-top: 30px; border-top: 1px solid #333; padding-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 2. Chargement des données
try:
    df = pd.read_csv("match.csv")
    dates_disponibles = sorted(df['Date'].unique())
    aujourdhui = datetime.now().strftime('%Y-%m-%d')
    
    st.title("⚽ Master Predicts")

    # Création des onglets
    noms_onglets = []
    for d in dates_disponibles:
        if d == aujourdhui: noms_onglets.append("AUJOURD'HUI")
        else: noms_onglets.append(datetime.strptime(d, '%Y-%m-%d').strftime('%d %b'))

    if noms_onglets:
        tabs = st.tabs(noms_onglets)
        for i, tab in enumerate(tabs):
            with tab:
                date_sel = dates_disponibles[i]
                df_filtre = df[df['Date'] == date_sel]

                for index, row in df_filtre.iterrows():
                    teams = row['Match'].split(" vs ")
                    est_live = row.get('Etat') == "LIVE"
                    
                    # On utilise st.container pour stabiliser l'affichage
                    with st.container():
                        st.markdown(f"""
                            <div class="match-card">
                                <div style="display: flex; justify-content: space-between;">
                                    <span style="color: #888; font-size: 12px;">{row['Ligue']}</span>
                                    {"<span class='live-badge'>● LIVE</span>" if est_live else ""}
                                </div>
                                <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px;">
                                    <div class="team-name">{teams[0]}</div>
                                    <div class="score-live">{row['Score_Live'] if est_live else 'vs'}</div>
                                    <div class="team-name">{teams[1]}</div>
                                </div>
                                <div style="margin-top: 15px; display: flex; justify-content: space-between; font-size: 12px; color: #ffd700;">
                                    <span>🎯 Prono: {row['Score_Prédit']}</span>
                                    <span>⚽ Buts: {row['Total_Buts']}</span>
                                    <span>⭐ {row['Confiance']}</span>
                                </div>
                            </div>
                            """, unsafe_allow_html=True)
    else:
        st.info("Aucun match trouvé. Relance le workflow sur GitHub.")

except Exception as e:
    st.error(f"Erreur de données. Relance le workflow.")

# 3. Signature
st.markdown('<div class="footer-name">DÉVELOPPÉ PAR HEMERY DALLAH</div>', unsafe_allow_html=True)
