import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import plotly.express as px

st.set_page_config(page_title="Analytique | LOGIX 360", layout="wide")

st.title("🔬 Interface Analytique (SC0x)")
st.markdown("---")

# --- 1. ANALYSE DE PROFITABILITÉ (Gazole & Marge Nette) ---
st.header("💰 1. Optimisation du Centre de Profit")
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        gazole = st.number_input("Prix Gazole/Essence (FCFA/L)", value=707)
        conso_moyenne = st.number_input("Consommation (L/100km)", value=35)
    with col2:
        charges_fixes = st.number_input("Charges Fixes par trajet (FCFA)", value=85005)
        distance = st.number_input("Distance (km)", value=750)
    with col3:
        marge_cible = st.slider("Marge Nette visée (%)", 5, 50, 15)
        
    # Calcul rigoureux
    cout_carburant = (distance / 100) * conso_moyenne * gazole
    cout_total = cout_carburant + charges_fixes
    prix_prestation = cout_total / (1 - (marge_cible / 100))
    
    st.metric("Prix de Prestation Recommandé", f"{prix_prestation:,.0f} FCFA", 
              delta=f"Marge: {prix_prestation - cout_total:,.0f} FCFA")

# --- 2. MOTEUR PRÉDICTIF IA (Random Forest & Saisonnalité) ---
st.markdown("---")
st.header("🤖 2. IA : Prévision de la Demande Saisonnière")
st.info("Algorithme : Random Forest Regressor — Analyse des cycles (Coton, Cajou).")

# Simulation de données d'entraînement (Mois, Tendance Marché -> Demande)
X_train = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]])
y_train = np.array([120, 150, 400, 450, 300, 200, 150, 100, 110, 250, 350, 200]) # Volumes

rf_model = RandomForestRegressor(n_estimators=100, random_state=42).fit(X_train, y_train)

mois_pred = st.select_slider("Projection sur le mois :", options=range(1, 13))
demande_predite = rf_model.predict([[mois_pred]])[0]

# --- 3. Z-SCORE DYNAMIQUE (Stock de Sécurité) ---
st.markdown("---")
st.header("🛡️ 3. Z-Score Dynamique : Optimisation des Stocks")
col_a, col_b = st.columns(2)

with col_a:
    taux_service = st.selectbox("Niveau de Service visé", [0.90, 0.95, 0.98, 0.99])
    # Table Z-Score simplifiée
    z_table = {0.90: 1.28, 0.95: 1.64, 0.98: 2.05, 0.99: 2.33}
    z = z_table[taux_service]
    
    sigma = st.number_input("Écart-type de la demande (Sigma)", value=demande_predite * 0.15)
    lead_time = st.number_input("Délai d'approvisionnement (Jours)", value=10)
    
    safety_stock = z * sigma * np.sqrt(lead_time)
    st.metric("Stock de Sécurité (Safety Stock)", f"{safety_stock:.2f} Unités")

with col_b:
    # Graphique de sensibilité Profit vs Gazole (La corrélation)
    gazole_range = np.linspace(600, 1000, 20)
    profits = [prix_prestation - ((distance / 100) * conso_moyenne * p + charges_fixes) for p in gazole_range]
    fig = px.line(x=gazole_range, y=profits, title="Impact du Gazole sur le Profit Net",
                  labels={'x': 'Prix Gazole (FCFA)', 'y': 'Profit Net (FCFA)'}, template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)
        
