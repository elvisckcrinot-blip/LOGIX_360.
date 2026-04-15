import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

st.set_page_config(page_title="Analytique | LOGIX 360", layout="wide")

st.title("🔬 Interface Analytique")
st.markdown("---")

# --- SECTION 1 : MODÉLISATION DU PROFIT ---
st.header("💰 Optimisation du Centre de Profit")
col1, col2 = st.columns(2)

with col1:
    st.write("### Paramètres de Coût")
    gazole = st.number_input("Prix du Gazole/Essence (FCFA/L)", value=707)
    charges_fixes = st.number_input("Charges Fixes (FCFA)", value=85005)
    distance = st.slider("Distance du trajet (km)", 1, 1500, 750)

with col2:
    st.write("### Analyse de Marge")
    # Calcul simplifié basé sur ton PoC
    cout_total = (gazole * 0.4 * distance) + charges_fixes
    st.metric("Coût Opérationnel Estimé", f"{cout_total:,.0f} FCFA")
    st.success("Calcul basé sur les standards de transport Nord-Sud.")

# --- SECTION 2 : RANDOM FOREST & SAISONNALITÉ ---
st.markdown("---")
st.header("🤖 IA : Prévision de la Variabilité Saisonière")
st.info("Le Random Forest ajuste ici votre Stock de Sécurité en fonction des cycles agricoles.")

# Simulation de données pour l'IA
def train_rf_model():
    # Données fictives : [Mois, Prix Carburant] -> Variabilité observée
    X = np.array([[1, 700], [4, 707], [8, 700], [10, 715], [12, 707]])
    y = np.array([25, 45, 30, 55, 35]) # Sigma (%)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

model = train_rf_model()
mois_actuel = st.select_slider("Sélectionner le mois de l'année", options=range(1, 13))
pred_sigma = model.predict([[mois_actuel, gazole]])[0]

st.metric("Coefficient de Variabilité (Sigma) prédit", f"{pred_sigma:.2f} %")
st.write(f"**Conseil LOGIX 360 :** En mois {mois_actuel}, prévoyez un stock de sécurité majoré de {pred_sigma/2:.1f}% pour compenser la saisonnalité.")
  
