import streamlit as st
import pandas as pd

# 1. Configuration de la page
st.set_page_config(
    page_title="Master Predicts | Dashboard Pro",
    layout="wide",
    page_icon="⚽"
)

# --- STYLE CSS POUR LES CARTES ---
st.markdown("""
    <style>
    .stMetric { background-color: #f0f2f6; padding: 10px; border-radius: 10px; border: 1px solid #ddd; }
    </style>
    """, unsafe_allow_html=True)

# 2. Chargement des données
try:
    df = pd.read_csv("match.csv")
    
    # 3. Barre latérale (Sidebar) pour les filtres
    st.sidebar.header("⚙️ Configuration")
    
    # Recherche par équipe
    search = st.sidebar.text_input("🔍 Rechercher une équipe", "")
    
    # Filtre par fiabilité
    min_conf = st.sidebar.select_slider(
        "Filtrer par fiabilité",
        options=["⭐⭐⭐", "⭐⭐⭐⭐"],
        value="⭐⭐⭐"
    )

    # Application des filtres
    if search:
        df = df[df['Match'].str.contains(search, case=False)]
    
    df = df[df['Confiance'] >= min_conf]

    # 4. En-tête du site
    st.title("🔢 Master Predicts : Analyses Automatiques")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Matchs analysés", len(df))
    col2.metric("Source", "API Mondiale")
    col3.metric("Expert", "HEMERY DALLAH")

    st.divider()

    # 5. Affichage du tableau principal
    st.dataframe(
        df, 
        column_config={
            "Logo": st.column_config.ImageColumn(" ", width="small"),
            "Match": st.column_config.TextColumn("⚽ Match", width="large"),
            "1_pct": st.column_config.ProgressColumn("1 (%)", format="%d%%", min_value=0, max_value=100, color="blue"),
            "X_pct": st.column_config.ProgressColumn("X (%)", format="%d%%", min_value=0, max_value=100, color="gray"),
            "2_pct": st.column_config.ProgressColumn("2 (%)", format="%d%%", min_value=0, max_value=100, color="red"),
            "Score_Prédit": st.column_config.TextColumn("📊 Score", width="small"),
            "Total_Buts": st.column_config.TextColumn("Buts", width="small"),
            "Confiance": st.column_config.TextColumn("Fiabilité", width="small")
        },
        hide_index=True,
        use_container_width=True
    )

except Exception:
    st.info("🔄 Le robot Master Predicts prépare les matchs. Revenez dans un instant !")

# 6. Bouton WhatsApp et Signature
st.divider()
st.markdown(f"""
    <div style="text-align: center;">
        <a href="https://wa.me/?text=Regarde%20les%20pronos%20sur%20Master%20Predicts%20!" target="_blank">
            <button style="background-color: #25D366; color: white; border: none; padding: 15px; border-radius: 10px; font-weight: bold; width: 50%; cursor: pointer; font-size: 18px;">
                📲 Partager sur WhatsApp
            </button>
        </a>
        <br><br>
        <p style="font-size: 18px; font-weight: bold; color: #555;">🚀 Application développée par</p>
        <p style="font-size: 26px; font-weight: bold; color: #000; letter-spacing: 2px;">HEMERY DALLAH MAGANGA YABRR</p>
        <p style="font-style: italic; color: #888;">Étudiant en Informatique</p>
    </div>
    """, unsafe_allow_html=True)
