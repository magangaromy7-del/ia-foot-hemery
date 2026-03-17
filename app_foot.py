import streamlit as st
import pandas as pd

# 1. Configuration de la page
st.set_page_config(page_title="Master Predicts", layout="centered", page_icon="⚽")

# --- STYLE CSS AMÉLIORÉ ---
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
    .time { color: #888; font-size: 13px; font-weight: bold; }
    .team-row { display: flex; align-items: center; margin: 10px 0; }
    .team-logo { width: 28px; height: 28px; margin-right: 15px; object-fit: contain; }
    .team-name { font-size: 17px; font-weight: 500; flex-grow: 1; }
    .badge-container { display: flex; gap: 10px; }
    .prono-badge { 
        background-color: #2e2e2e; 
        padding: 4px 8px; 
        border-radius: 6px; 
        font-size: 11px; 
        color: #ffd700; 
        border: 1px solid #444;
    }
    .goals-badge {
        background-color: #004d40;
        padding: 4px 8px;
        border-radius: 6px;
        font-size: 11px;
        color: #00e676;
        border: 1px solid #00796b;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Chargement des données
try:
    df = pd.read_csv("match.csv")
    
    st.title("⚽ Master Predicts")
    st.write(f"Analyses intelligentes de la semaine")

    # 3. Affichage des CARTES
    for index, row in df.iterrows():
        teams = row['Match'].split(" vs ")
        home_team = teams[0]
        away_team = teams[1]
        
        st.markdown(f"""
            <div class="match-card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                    <div class="time">📅 {row['Date']} | {row['Ligue']}</div>
                    <div class="badge-container">
                        <div class="prono-badge">🎯 Score: {row['Score_Prédit']}</div>
                        <div class="goals-badge">⚽ Buts: {row['Total_Buts']}</div>
                    </div>
                </div>
                <div class="team-row">
                    <img src="{row['Logo']}" class="team-logo">
                    <div class="team-name">{home_team}</div>
                </div>
                <div class="team-row">
                    <img src="https://cdn-icons-png.flaticon.com/512/53/53254.png" class="team-logo" style="filter: invert(1); opacity: 0.5;">
                    <div class="team-name">{away_team}</div>
                </div>
                <div style="margin-top: 10px; font-size: 12px; color: #aaa; border-top: 1px solid #333; padding-top: 10px; display: flex; justify-content: space-between;">
                    <span>📈 1: {row['1_pct']}% | X: {row['X_pct']}% | 2: {row['2_pct']}%</span>
                    <span style="color: #ffd700;">{row['Confiance']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

except Exception:
    st.info("🔄 Mise à jour des pronostics en cours...")

# 4. Signature
st.markdown(f"""
    <div style="text-align: center; margin-top: 30px; padding-bottom: 50px;">
        <p style="color: #666; font-size: 12px; margin-bottom: 5px;">APPLICATION DÉVELOPPÉE PAR</p>
        <p style="font-weight: bold; color: white; letter-spacing: 1px;">HEMERY DALLAH MAGANGA YABRR</p>
    </div>
    """, unsafe_allow_html=True)
