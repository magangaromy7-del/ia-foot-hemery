import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# 1. Configuration
st.set_page_config(page_title="Master Predicts", layout="centered", page_icon="⚽")

# --- STYLE CSS POUR LES CARTES ---
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
    .time { color: #888; font-size: 11px; font-weight: bold; }
    .team-row { display: flex; align-items: center; margin: 6px 0; }
    .team-logo { width: 22px; height: 22px; margin-right: 12px; object-fit: contain; }
    .team-name { font-size: 14px; font-weight: 500; flex-grow: 1; }
    .badge-container { display: flex; gap: 6px; }
    .prono-badge { background-color: #2e2e2e; padding: 2px 6px; border-radius: 4px; font-size: 10px; color: #ffd700; border: 1px solid #444; }
    .goals-badge { background-color: #004d40; padding: 2px 6px; border-radius: 4px; font-size: 10px; color: #00e676; border: 1px solid #00796b; }
    
    /* Cacher le menu Streamlit pour faire plus pro */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. Chargement des données
try:
    df = pd.read_csv("match.csv")
    dates_disponibles = sorted(df['Date'].unique())
    
    aujourdhui = datetime.now().strftime('%Y-%m-%d')
    demain = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')

    st.title("⚽ Master Predicts")

    # --- SYSTÈME D'ONGLETS (TABS) COMME SUR L'IMAGE ---
    noms_onglets = []
    for d in dates_disponibles:
        if d == aujourdhui: noms_onglets.append("AUJOURD'HUI")
        elif d == demain: noms_onglets.append("DEMAIN")
        else: noms_onglets.append(datetime.strptime(d, '%Y-%m-%d').strftime('%d %b.').upper())

    # Création des onglets Streamlit
    tabs = st.tabs(noms_onglets)

    for i, tab in enumerate(tabs):
        with tab:
            date_selectionnee = dates_disponibles[i]
            df_filtre = df[df['Date'] == date_selectionnee]

            if df_filtre.empty:
                st.write("Aucun match prévu.")
            else:
                for index, row in df_filtre.iterrows():
                    teams = row['Match'].split(" vs ")
                    st.markdown(f"""
                        <div class="match-card">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px;">
                                <div class="time">{row['Ligue'].upper()}</div>
                                <div class="badge-container">
                                    <div class="prono-badge">🎯 {row['Score_Prédit']}</div>
                                    <div class="goals-badge">⚽ {row['Total_Buts']}</div>
                                </div>
                            </div>
                            <div class="team-row"><img src="{row['Logo']}" class="team-logo"><div class="team-name">{teams[0]}</div></div>
                            <div class="team-row"><img src="https://cdn-icons-png.flaticon.com/512/53/53254.png" class="team-logo" style="filter: invert(1); opacity:0.2;"><div class="team-name">{teams[1]}</div></div>
                            <div style="margin-top: 5px; font-size: 10px; color: #666; border-top: 1px solid #333; padding-top: 5px; display: flex; justify-content: space-between;">
                                <span>PROBA: 1:{row['1_pct']}% | X:{row['X_pct']}% | 2:{row['2_pct']}%</span>
                                <span style="color: #ffd700;">{row['Confiance']}</span>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

except Exception:
    st.info("🔄 Chargement des pronostics...")

# 3. Signature Hemery
st.markdown(f"""
    <div style="text-align: center; margin-top: 20px; padding-bottom: 30px;">
        <p style="font-weight: bold; color: #444; font-size: 12px;">DÉVELOPPÉ PAR HEMERY DALLAH</p>
    </div>
    """, unsafe_allow_html=True)
