import streamlit as st
import random

# Configuration de la page
st.set_page_config(page_title="Master Predicts Pro", page_icon="⚽")

st.title("⚽ Master Predicts : IA Analyse Expert")
st.write("Analyse complète des probabilités pour le match.")

# --- SECTION : ENTRÉE DES DONNÉES ---
st.subheader("📊 Entrez les forces en présence")

col1, col2 = st.columns(2)

with col1:
    domicile = st.text_input("Équipe à Domicile", "Real Madrid")
    force_dom = st.slider(f"Niveau d'attaque ({domicile})", 1, 100, 75)
    defense_dom = st.slider(f"Niveau défense ({domicile})", 1, 100, 70)

with col2:
    exterieur = st.text_input("Équipe à l'Extérieur", "Barcelone")
    force_ext = st.slider(f"Niveau d'attaque ({exterieur})", 1, 100, 72)
    defense_ext = st.slider(f"Niveau défense ({exterieur})", 1, 100, 65)

# --- CALCUL DE L'ANALYSE ---
if st.button("🚀 GÉNÉRER L'ANALYSE COMPLÈTE"):
    # Logique de calcul pour le score
    buts_dom = round((force_dom / (defense_ext + 10)) * 2)
    buts_ext = round((force_ext / (defense_dom + 10)) * 1.8)
    
    # Calcul des autres statistiques
    total_buts = buts_dom + buts_ext
    possession_dom = round(50 + (force_dom - force_ext) / 5)
    tirs_cadres_dom = round(buts_dom * 2.5 + random.randint(1, 3))
    tirs_cadres_ext = round(buts_ext * 2.5 + random.randint(1, 3))

    st.divider()
    
    # AFFICHAGE DU PRONOSTIC
    st.header("🏆 Pronostic Final")
    st.subheader(f"Score Exact : {domicile} {buts_dom} - {buts_ext} {exterieur}")
    
    # AFFICHAGE DES DÉTAILS
    col_a, col_b, col_c = st.columns(3)
    
    with col_a:
        st.metric("Total Buts", f"+ {total_buts - 0.5}")
    with col_b:
        st.metric("Possession", f"{possession_dom}%", f"{100-possession_dom}%", delta_color="normal")
    with col_c:
        st.metric("Tirs Cadrés", f"{tirs_cadres_dom} - {tirs_cadres_ext}")

    st.info(f"💡 **Conseil d'expert** : Basé sur l'analyse, le pronostic le plus sûr est : **{'+ 1,5 buts' if total_buts > 1 else 'Match fermé'}**.")

st.sidebar.write("Développé par **Hemery Maganga**")
st.sidebar.info("Utilisez les sliders pour simuler la forme actuelle des équipes.")
        
st.divider()
st.caption("Application développée par HEMERY DALLAH - Étudiant IT")
