import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# 1. Configuration
st.set_page_config(page_title="Master Predicts", layout="centered", page_icon="⚽")

# --- STYLE CSS ---
st.markdown("""
    <style>
    .match-card {
        background-color: #1e1e1e;
        border-radius: 15px;
        padding: 15px;
        margin-bottom: 12px;
        border: 1px solid #333;
        color: white;
    }
    .time { color: #888; font-size: 12px; font-weight: bold; }
    .team-row { display: flex; align-items: center; margin: 8px 0; }
    .team-logo { width: 25px; height: 25px; margin-right: 12px; object-fit: contain; }
    .team-name { font-size: 15px; font-weight: 500; flex-grow: 1; }
    .badge-container { display: flex; gap: 8px; }
    .prono-badge { background-color: #2e2e2e; padding: 3px 7px; border-radius: 5px; font-size: 10px; color: #ffd700; border: 1px solid #444; }
    .goals-badge { background-color: #004d40; padding: 3px 7px; border-radius: 5px; font-size: 10px; color: #00e676; border: 1px solid #00796b; }
    </style>
    """, unsafe_allow_html=True)

# 2. Chargement et Préparation des Dates
try:
    df = pd.read_csv("match.csv")
    
    # Création des options de filtrage (Aujourd'hui, Demain, etc.)
    aujourdhui = datetime.now().strftime('%Y-%m-%d')
    demain = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
    
    st.title("⚽ Master Predicts")
    
    # Barre de sélection de la date (Filtre horizontal)
    dates_disponibles = sorted(df['Date'].unique())
    noms_dates = []
    for d in dates_disponibles:
        if d == aujourdhui: noms_dates.append("Aujourd'hui")
        elif d == demain: noms_dates.append("Demain")
        else: noms_dates.append(datetime.strptime(d, '%Y-%m-%d').strftime('%d %b'))

    choix_date = st.select_slider(
        "📅 Choisir la date des matchs",
        options=dates_disponibles,
        format_func=lambda x: "Aujourd'hui" if x == aujourdhui else ("Demain" if x == demain else datetime.strptime(x, '%Y-%m-%d').strftime('%d %b'))
    )

    # Filtrage du DataFrame
    df_filtre = df[df['Date'] == choix_date]

    if df_filtre.empty:
        st.warning("Aucun match prévu pour cette date.")
    else:
        # 3. Affichage des CARTES
        for index, row in df_filtre.iterrows():
            teams = row['Match'].split(" vs ")
            st.markdown(f"""
                <div class="match-card">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                        <div class="time">{row['Ligue']}</div>
                        <div class="badge-container">
                            <div class="prono-badge">🎯 {row['Score_Prédit']}</div>
                            <div class="goals-badge">⚽ {row['Total_Buts']}</div>
                        </div>
                    </div>
                    <div class="team-row"><img src="{row['Logo']}" class="team-logo"><div class="team-name">{teams[0]}</div></div>
                    <div class="team-row"><img src="https://cdn-icons-png.flaticon.com/512/53/53254.png" class="team-logo" style="filter: invert(1); opacity:0.3;"><div class="team-name">{teams[1]}</div></div>
                    <div style="margin-top: 8px; font-size: 11px; color: #888; border-top: 1px solid #333; padding-top: 8px; display: flex; justify-content: space-between;">
                        <span>📈 1:{row['1_pct']}% | X:{row['X_pct']}% | 2:{row['2_pct']}%</span>
                        <span style="color: #ffd700;">{row['Confiance']}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)

except Exception as e:
    st.info("Sélectionnez une date pour voir les pronostics.")

# 4. Signature
st.markdown(f"""
    <div style="text-align: center; margin-top: 30px; padding-bottom: 50px;">
        <p style="font-weight: bold; color: white; font-size: 14px;">HEMERY DALLAH </p>
    </div>
    """, unsafe_allow_html=True)
