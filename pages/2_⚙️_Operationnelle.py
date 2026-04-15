import streamlit as st
import pandas as pd
import numpy as np
import math

st.set_page_config(page_title="Opérationnelle | LOGIX 360", layout="wide")

st.title("⚙️ Interface Opérationnelle (SC1x)")
st.markdown("---")

# --- 1. SMART INVENTORY (Modèle Wilson / EOQ) ---
st.header("📦 1. Automatisation du Réapprovisionnement (EOQ)")
st.info("Calcul de la Quantité Économique de Commande pour minimiser les coûts de possession et de passation.")

col1, col2, col3 = st.columns(3)
with col1:
    D = st.number_input("Demande Annuelle (Unités)", value=15000)
    S = st.number_input("Coût de Passation (FCFA/Commande)", value=7500)
with col2:
    C = st.number_input("Valeur Unitaire (FCFA)", value=2500)
    h_rate = st.slider("Taux de Possession (%)", 5, 40, 18) / 100
with col3:
    # Formule Wilson : sqrt((2*D*S)/(C*h))
    h = C * h_rate
    eoq = math.sqrt((2 * D * S) / h)
    st.metric("EOQ (Quantité Optimale)", f"{eoq:.0f} Unités")
    st.write(f"**Nombre de commandes/an :** {D/eoq:.1f}")

# --- 2. REGISTRE DE DOCKING UNIVERSEL ---
st.markdown("---")
st.header("🚛 2. Registre de Docking & Temps de Cycle")
st.write("Suivi des flux physiques et affectation dynamique des quais.")

# Initialisation du registre via session_state
if 'docking_db' not in st.session_state:
    st.session_state.docking_db = pd.DataFrame(columns=["Camion", "Produit", "Quai", "Statut", "Tps_Attente (min)"])

with st.expander("📥 Enregistrer un flux entrant/sortant", expanded=False):
    c1, c2, c3 = st.columns(3)
    id_camion = c1.text_input("ID Camion (ex: RB 4567)")
    type_p = c2.selectbox("Marchandise", ["Coton", "Ciment", "Noix de Cajou", "Maïs", "Huile de Palme"])
    q_af = c3.selectbox("Quai", ["Quai 01", "Quai 02", "Quai 03", "Zone Transit"])
    
    if st.button("Valider l'affectation"):
        new_entry = pd.DataFrame([[id_camion, type_p, q_af, "En cours", np.random.randint(5, 45)]], 
                                 columns=["Camion", "Produit", "Quai", "Statut", "Tps_Attente (min)"])
        st.session_state.docking_db = pd.concat([st.session_state.docking_db, new_entry], ignore_index=True)

st.dataframe(st.session_state.docking_db, use_container_width=True)

# --- 3. LEAN DASHBOARD (TRG/OEE & MUDA) ---
st.markdown("---")
st.header("📉 3. Lean Dashboard & Performance (OEE)")
col_lean1, col_lean2 = st.columns(2)

with col_lean1:
    st.write("### Suivi du Taux de Rendement Global (TRG)")
    dispo = st.slider("Disponibilité (%)", 0, 100, 85) / 100
    perf = st.slider("Performance (%)", 0, 100, 90) / 100
    qualite = st.slider("Qualité (%)", 0, 100, 98) / 100
    oee = dispo * perf * qualite
    st.metric("OEE / TRG Actuel", f"{oee*100:.1f} %", delta="Cible: 85%")

with col_lean2:
    st.write("### Analyse des MUDA (Gaspillages)")
    muda_list = st.multiselect("Identifier les pertes détectées :", 
                               ["Surproduction", "Attentes", "Transports Inutiles", "Stocks", "Mouvements", "Défauts", "Sous-utilisation"])
    if muda_list:
        st.warning(f"Alerte Lean : {len(muda_list)} sources de gaspillage impactent la productivité.")
    else:
        st.success("Aucun MUDA critique détecté aujourd'hui.")
    
