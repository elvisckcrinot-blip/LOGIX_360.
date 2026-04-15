import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Dynamique | LOGIX 360", layout="wide")

st.title("⚡ Interface Dynamique (SC3x)")
st.markdown("---")

# --- 1. TRACKING CORRIDOR & LOI DE LITTLE ---
st.header("🛣️ 1. Suivi de Flux & Loi de Little")
st.info("Analyse de la fluidité du corridor via la relation : Stock (L) = Débit (λ) x Temps de passage (W)")

col1, col2, col3 = st.columns(3)
with col1:
    debit = st.number_input("Débit d'entrée (Camions/Jour)", value=15)
with col2:
    temps_passage = st.number_input("Temps moyen de trajet (Jours)", value=4)
with col3:
    # L = λ * W
    wip = debit * temps_passage
    st.metric("En-cours sur le Corridor (L)", f"{wip:.0f} Camions")

st.write("### Visualisation du Flux de Transit")
fig_flow = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = wip,
    title = {'text': "Saturation du Corridor (Unités)"},
    gauge = {'axis': {'range': [None, 100]},
             'steps' : [
                 {'range': [0, 40], 'color': "lightgreen"},
                 {'range': [40, 70], 'color': "orange"},
                 {'range': [70, 100], 'color': "red"}],
             'threshold' : {'line': {'color': "black", 'width': 4}, 'thickness': 0.75, 'value': 90}}))
st.plotly_chart(fig_flow, use_container_width=True)

# --- 2. SIMULATION DE MONTE CARLO (Résilience) ---
st.markdown("---")
st.header("🎲 2. Simulation de Monte Carlo : Stress Test")
st.write("Simulation de 1000 scénarios pour évaluer le risque de rupture de flux.")

col_sim1, col_sim2 = st.columns([1, 2])
with col_sim1:
    iter = st.slider("Nombre d'itérations", 100, 5000, 1000)
    delai_moyen = st.number_input("Délai moyen cible (Jours)", value=5)
    incertitude = st.slider("Incertitude sur le corridor (%)", 10, 100, 30) / 100

# Calcul Monte Carlo
simulations = np.random.normal(delai_moyen, delai_moyen * incertitude, iter)
prob_retard = (simulations > (delai_moyen * 1.5)).mean() * 100

with col_sim2:
    st.write(f"### Résultat de la Simulation ({iter} trajets)")
    st.write(f"Probabilité de retard critique (> {delai_moyen * 1.5} jrs) : **{prob_retard:.1f}%**")
    
    # Histogramme des délais simulés
    st.bar_chart(np.histogram(simulations, bins=20)[0])

# --- 3. TOUR DE CONTRÔLE ZLECAF (Continuité) ---
st.markdown("---")
st.header("🌍 3. Tour de Contrôle ZLECAF")
st.write("Monitoring de la continuité logistique sur les frontières.")

frontieres = pd.DataFrame({
    'Frontière': ['Malanville (Bénin/Niger)', 'Sèmè-Kraké (Bénin/Nigeria)', 'Hilla-Condji (Bénin/Togo)'],
    'Temps Moyen Douane (Hrs)': [24, 48, 12],
    'Statut': ['Fluide', 'Congestionné', 'Fluide']
})

def color_statut(val):
    color = 'red' if val == 'Congestionné' else 'green'
    return f'color: {color}'

st.dataframe(frontieres.style.applymap(color_statut, subset=['Statut']), use_container_width=True)
