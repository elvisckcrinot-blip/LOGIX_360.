import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Stratégique | LOGIX 360", layout="wide")

st.title("🌍 Interface Stratégique (SC2x)")
st.markdown("---")

# --- 1. SÉLECTEUR D'INCOTERMS INTELLIGENT (Expertise ICC 2020) ---
st.header("🚢 1. Système Expert : Sélecteur d'Incoterms")
st.info("Aide à la décision pour sécuriser les transferts de risques et de coûts à l'export (ZLECAF).")

with st.container():
    c1, c2 = st.columns(2)
    with c1:
        st.write("### Responsabilités")
        t_principal = st.radio("Qui paie le transport principal ?", ["Vendeur", "Acheteur"])
        assurance = st.radio("Qui couvre l'assurance ?", ["Vendeur", "Acheteur"])
    with c2:
        st.write("### Dédouanement & Livraison")
        douane_import = st.radio("Qui gère le dédouanement à destination ?", ["Vendeur", "Acheteur"])
        mode_transport = st.selectbox("Mode de transport prévu", ["Terrestre (Route/Rail)", "Maritime", "Aérien", "Multimodal"])

    # Logique décisionnelle rigoureuse
    if t_principal == "Acheteur":
        incoterm, desc = "EXW / FCA", "L'acheteur contrôle la chaîne logistique dès le départ."
    elif douane_import == "Vendeur":
        incoterm, desc = "DDP", "Risque et coût maximum pour le vendeur (rendu dédouané)."
    elif mode_transport == "Maritime":
        incoterm, desc = "CIF / FOB", "Incoterms spécifiques aux flux portuaires (Port de Cotonou)."
    else:
        incoterm, desc = "DAP / CPT", "Optimal pour les livraisons transfrontalières terrestres."

    st.success(f"**Incoterm Recommandé : {incoterm}**")
    st.caption(f"💡 {desc}")

# --- 2. SMART OPTIMIZER (Pénalité de Variabilité Six Sigma) ---
st.markdown("---")
st.header("🧠 2. Smart Optimizer : Planification de Trajet")
st.write("Arbitrage entre le coût direct et le risque de variabilité sur le corridor.")

# Données de simulation Cotonou - Malanville
data = {
    'Option de Route': ['Axe Principal (Goudron)', 'Route Secondaire', 'Contournement'],
    'Coût Fixe (FCFA)': [250000, 180000, 310000],
    'Variabilité ($\sigma$) (%)': [5, 35, 2] # Risque de retard/panne
}
df_routes = pd.DataFrame(data)

st.table(df_routes)

# Application de la pénalité de variabilité (Concept MIT SC2x)
penalite = st.slider("Coefficient d'aversion au risque (Pénalité)", 1, 20, 10)
df_routes['Coût Ajusté (Risque)'] = df_routes['Coût Fixe (FCFA)'] + (df_routes['Variabilité ($\sigma$) (%)'] * penalite * 2000)

meilleur_choix = df_routes.loc[df_routes['Coût Ajusté (Risque)'].idxmin(), 'Option de Route']
st.success(f"**Recommandation LOGIX 360 : {meilleur_choix}** (Meilleur compromis Coût/Fiabilité)")

# --- 3. LANDED COST MANAGER (Calcul Export ZLECAF) ---
st.markdown("---")
st.header("📉 3. Landed Cost Manager (Exportation)")
st.write("Calcul du coût de revient complet à destination pour un pays de la ZLECAF.")

with st.expander("Détails du Coût de Revient"):
    prix_usine = st.number_input("Prix Sortie Usine (FCFA)", value=5000000)
    fret_inter = st.number_input("Transport International (FCFA)", value=450000)
    taxes_zlecaf = st.number_input("Droits et Taxes (Régime préférentiel ZLECAF)", value=25000)
    
    total_landed = prix_usine + fret_inter + taxes_zlecaf
    st.metric("Landed Cost (Coût de revient total)", f"{total_landed:,.0f} FCFA")
      
