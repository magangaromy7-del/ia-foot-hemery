import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(page_title="Master Predicts | Stats", layout="wide", page_icon="⚽")

st.title("🔢 Master Predicts : Analyses de Demain")
st.write(f"Pronostics basés sur l'IA - Mise à jour : {pd.Timestamp.now().strftime('%d/%m/%Y')}")

# Chargement des données
try:
    # On lit ton fichier match.csv
    df = pd.read_csv("match.csv")
    
    # Affichage du tableau stylisé
    st.dataframe(
        df, 
        column_config={
            "Logo": st.column_config.ImageColumn(" ", width="small"),
            "Match": st.column_config.TextColumn("Match", width="medium"),
            "1_pct": st.column_config.ProgressColumn("Victoire Dom. (%)", format="%d%%", min_value=0, max_value=100, color="blue"),
            "X_pct": st.column_config.ProgressColumn("Nul (%)", format="%d%%", min_value=0, max_value=100, color="gray"),
            "2_pct": st.column_config.ProgressColumn("Victoire Ext. (%)", format="%d%%", min_value=0, max_value=100, color="red"),
            "Score_Prédit": st.column_config.TextColumn("Score Exact"),
            "Total_Buts": st.column_config.TextColumn("Total Buts"),
            "Confiance": st.column_config.TextColumn("Fiabilité")
        },
        hide_index=True,
        use_container_width=True
    )

except Exception as e:
    st.error(f"Erreur de lecture du fichier : {e}")
    st.info("Vérifiez que le fichier se nomme bien match.csv sur GitHub.")

# Section "Coupon du Jour"
st.divider()
st.subheader("🔥 Le Coupon Safe de demain")
st.info("Selon l'IA : **Sporting CP** + **Fenerbahce** + **Barcelone**. Côte estimée : 2.10")

# Affichage du tableau verrouillé (ne bouge plus)
    st.dataframe(
        df, 
        column_config={
            "Logo": st.column_config.ImageColumn(" ", width="small"),
            "Match": st.column_config.TextColumn("Match", width="large"), # On donne plus de place aux noms
            "1_pct": st.column_config.ProgressColumn("1 (%)", format="%d%%", min_value=0, max_value=100, color="blue", width="medium"),
            "X_pct": st.column_config.ProgressColumn("X (%)", format="%d%%", min_value=0, max_value=100, color="gray", width="medium"),
            "2_pct": st.column_config.ProgressColumn("2 (%)", format="%d%%", min_value=0, max_value=100, color="red", width="medium"),
            "Score_Prédit": st.column_config.TextColumn("Score", width="small"),
            "Total_Buts": st.column_config.TextColumn("Buts", width="small"),
            "Confiance": st.column_config.TextColumn("Fiabilité", width="small")
        },
        hide_index=True,
        use_container_width=True # Le tableau prend toute la largeur mais les colonnes restent fixes
    )
