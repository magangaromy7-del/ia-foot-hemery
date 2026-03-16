import streamlit as st
import pandas as pd

# Style Forebet - Configuration Large
st.set_page_config(page_title="Master Predicts | Stats & Pronos", layout="wide", page_icon="⚽")

st.title("🔢 Master Predicts : Intelligence Artificielle")
st.write(f"Dernière mise à jour des données : {pd.Timestamp.now().strftime('%d/%m/%Y')}")

# --- CHARGEMENT DES DONNÉES ---
try:
    # Lecture du fichier CSV que tu viens de créer
    df = pd.read_csv("matchs.csv")
    
    st.subheader("📅 Prédictions Mathématiques (Algorithme Forebet)")
    
    # Affichage du tableau interactif et stylisé
    st.dataframe(
        df, 
        column_config={
            "Match": st.column_config.TextColumn("Match", width="medium"),
            "1_pct": st.column_config.ProgressColumn("Victoire Dom. (%)", format="%d%%", min_value=0, max_value=100),
            "X_pct": st.column_config.ProgressColumn("Nul (%)", format="%d%%", min_value=0, max_value=100),
            "2_pct": st.column_config.ProgressColumn("Victoire Ext. (%)", format="%d%%", min_value=0, max_value=100),
            "Score_Prédit": st.column_config.TextColumn("Score Exact"),
            "Météo": st.column_config.TextColumn("Météo"),
            "Confiance": st.column_config.TextColumn("Fiabilité")
        },
        hide_index=True,
        use_container_width=True
    )

except Exception as e:
    # Message si le fichier matchs.csv n'est pas encore trouvé ou mal écrit
    st.warning("⚙️ Configuration en cours...")
    st.info("Le tableau s'affichera dès que le fichier 'matchs.csv' sera détecté sur GitHub.")

# --- SECTION ANALYSEUR MANUEL (En bas de page) ---
st.divider()
st.subheader("🔍 Analyseur de Match Personnalisé")
with st.expander("Vous ne trouvez pas un match ? Calculez-le ici"):
    col1, col2 = st.columns(2)
    with col1:
        equipe_nom = st.text_input("Nom de l'équipe", "Équipe A")
        force_att = st.slider("Puissance de l'Attaque", 0, 100, 70)
    with col2:
        equipe_ext = st.text_input("Adversaire", "Équipe B")
        force_def = st.slider("Solidité de la Défense", 0, 100, 60)
    
    if st.button("Lancer l'Analyse"):
        # Petit calcul mathématique rapide
        proba = round((force_att / (force_def + 1)) * 50 + 20)
        if proba > 100: proba = 95
        st.success(f"L'IA prévoit **{proba}%** de chances de victoire pour **{equipe_nom}**.")

# --- PIED DE PAGE ---
st.sidebar.markdown("### À propos")
st.sidebar.write("Application Développé par **Hemery Dallah MAGANGA YABRE**")
