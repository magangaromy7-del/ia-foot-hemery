import streamlit as st
import pandas as pd

# 1. Configuration de la page
st.set_page_config(page_title="Master Predicts | Stats", layout="wide", page_icon="⚽")

st.title("🔢 Master Predicts : Analyses de Demain")
st.write(f"Pronostics basés sur l'IA - Mise à jour : {pd.Timestamp.now().strftime('%d/%m/%Y')}")

# 2. Chargement des données
try:
    df = pd.read_csv("match.csv")
    
    # Affichage du tableau verrouillé (fixe)
    st.dataframe(
        df, 
        column_config={
            "Logo": st.column_config.ImageColumn(" ", width="small"),
            "Match": st.column_config.TextColumn("Match", width="large"),
            "1_pct": st.column_config.ProgressColumn("1 (%)", format="%d%%", min_value=0, max_value=100, color="blue", width="medium"),
            "X_pct": st.column_config.ProgressColumn("X (%)", format="%d%%", min_value=0, max_value=100, color="gray", width="medium"),
            "2_pct": st.column_config.ProgressColumn("2 (%)", format="%d%%", min_value=0, max_value=100, color="red", width="medium"),
            "Score_Prédit": st.column_config.TextColumn("Score", width="small"),
            "Total_Buts": st.column_config.TextColumn("Buts", width="small"),
            "Confiance": st.column_config.TextColumn("Fiabilité", width="small")
        },
        hide_index=True,
        use_container_width=True
    )
except Exception as e:
    st.error(f"Erreur : {e}")

# 3. Bouton WhatsApp
st.divider()
st.subheader("📢 Partage les pronos avec tes amis")
message_wa = "Salut ! Regarde les pronostics de demain sur Master Predicts : https://master-predicts.streamlit.app/"
lien_wa = f"https://wa.me/?text={message_wa.replace(' ', '%20')}"

st.markdown(f"""
    <a href="{lien_wa}" target="_blank">
        <button style="background-color: #25D366; color: white; border: none; padding: 12px; border-radius: 10px; font-weight: bold; width: 100%; cursor: pointer;">
            📲 Partager sur WhatsApp
        </button>
    </a>""", unsafe_allow_html=True)

# 4. Ton Nom (Signature)
st.divider()
st.markdown("""
    <div style="text-align: center;">
        <p style="font-size: 18px; font-weight: bold; color: #555;">🚀 Application développée par</p>
        <p style="font-size: 24px; font-weight: bold; color: #000;">HEMERY DALLAH MAGANGA YABRE</p>
        <p style="font-style: italic; color: #888;">Étudiant en Informatique -</p>
    </div>
    """, unsafe_allow_html=True)
