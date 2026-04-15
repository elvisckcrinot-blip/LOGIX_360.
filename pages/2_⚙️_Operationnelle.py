import streamlit as st
import pandas as pd
import math

st.set_page_config(page_title="Opérationnelle | LOGIX 360", layout="wide")

st.title("⚙️ Interface Opérationnelle")
st.markdown("---")

# --- SECTION 1 : SMART INVENTORY (WILSON/EOQ) ---
st.header("📦 Optimisation des Stocks (Modèle Wilson)")
st.info("Ce module calcule la Quantité Économique de Commande (EOQ) pour minimiser les coûts totaux.")

col1, col2, col3 = st.columns(3)

with col1:
    D = st.number_input("Demande annuelle (Unités)", value=12000, step=100)
    S = st.number_input("Coût de passation d'une commande (FCFA)", value=5000, step=500)
    
with col2:
    C = st.number_input("Prix d'achat unitaire (FCFA)", value=1500, step=100)
    i = st.slider("Taux de possession annuel (%)", 1, 50, 15) / 100

# Calcul de l'EOQ (Formule de Wilson)
# Q* = sqrt((2 * D * S) / (C * i))
if C * i > 0:
    eoq = math.sqrt((2 * D * S) / (C * i))
    
    with col3:
        st.metric("Quantité Idéale (EOQ)", f"{eoq:.0f} unités")
        st.warning(f"Passer {D/eoq:.1f} commandes par an pour optimiser vos coûts.")

# --- SECTION 2 : REGISTRE DE DOCKING UNIVERSEL ---
st.markdown("---")
st.header("🚛 Registre de Docking & Flux Physique")
st.write("Gestion des entrées/sorties et affectation des quais de déchargement.")

# Création d'un tableau interactif pour le Docking
if 'docking_data' not in st.session_state:
    st.session_state.docking_data = pd.DataFrame(columns=["Camion ID", "Marchandise", "Quai", "Statut", "Heure Arrivée"])

with st.expander("➕ Enregistrer un nouveau mouvement"):
    c1, c2, c3 = st.columns(3)
    camion = c1.text_input("Immatriculation")
    produit = c2.selectbox("Type de Marchandise", ["Maïs", "Soude", "Coton", "Ciment", "Autre"])
    quai = c3.selectbox("Affectation Quai", ["Quai A1", "Quai A2", "Quai B1", "Quai B2"])
    
    if st.button("Valider l'affectation"):
        new_row = {"Camion ID": camion, "Marchandise": produit, "Quai": quai, "Statut": "En cours", "Heure Arrivée": "16:15"}
        st.session_state.docking_data = pd.concat([st.session_state.docking_data, pd.DataFrame([new_row])], ignore_index=True)
        st.success(f"Camion {camion} affecté au {quai}")

st.table(st.session_state.docking_data)

# --- SECTION 3 : LEAN DASHBOARD (MUDA) ---
st.markdown("---")
st.header("📉 Performance Lean (Détection des Gaspillages)")
muda_type = st.multiselect("Identifier les gaspillages observés aujourd'hui (MUDA) :", 
                           ["Surproduction", "Attentes", "Transport inutile", "Stocks excessifs", "Mouvements inutiles", "Défauts"])

if muda_type:
    st.error(f"Attention : {len(muda_type)} sources de gaspillage identifiées. Action corrective requise.")
  
