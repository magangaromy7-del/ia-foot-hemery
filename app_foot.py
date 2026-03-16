import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="IA Pronos Football", page_icon="⚽")

# --- STYLE PERSONNALISÉ ---
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        background-color: #00ff00;
        color: black;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("⚽ Mon IA de Pronostics Football")
st.write("Bienvenue Hemery ! Cette IA utilise la régression linéaire pour prédire les scores.")

# --- 1. LES DONNÉES D'ENTRAÎNEMENT ---
# X = Tirs cadrés | y = Buts marqués
X = np.array([[2], [4], [5], [7], [8], [10]]) 
y = np.array([0, 1, 1, 2, 3, 4]) 

# Entraînement du modèle
model = LinearRegression()
model.fit(X, y)

# --- 2. INTERFACE UTILISATEUR ---
st.divider()
st.subheader("Entrez les statistiques du match")

# Curseur pour choisir le nombre de tirs
tirs_input = st.slider("Nombre de tirs cadrés prévus pour l'équipe :", 0, 20, 5)

# --- 3. CALCUL ET AFFICHAGE ---
if st.button("Lancer le pronostic IA"):
    # Faire la prédiction
    prediction = model.predict([[tirs_input]])
    
    # On arrondit pour avoir un nombre de buts logique (pas de 1.5 but)
    score_final = max(0, int(round(prediction[0])))
    
    st.balloons() # Petite animation de fête
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Estimation précise", value=f"{prediction[0]:.2f} buts")
    with col2:
        st.metric(label="Pronostic Final", value=f"{score_final} but(s)")

    if score_final >= 2:
        st.success("🔥 ANALYSE : Équipe très offensive, favorable pour un 'Over 1.5' !")
    elif score_final == 1:
        st.info("🛡️ ANALYSE : Match serré, l'équipe est moyennement efficace.")
    else:
        st.warning("⚠️ ANALYSE : Faible efficacité prévue. Attention au 'Under'.")

st.divider()
st.caption("Application développée par Hemery - Étudiant IT")