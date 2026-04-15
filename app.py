import streamlit as st

# Configuration de la page (Doit être la toute première commande Streamlit)
st.set_page_config(
    page_title="LOGIX 360 | Hub SCM 4.0",
    page_icon="📦",
    layout="wide"
)

# Style CSS personnalisé pour un look industriel
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.image("https://www.mit.edu/themes/mit/assets/favicon.ico", width=50) # Clin d'oeil au MIT
st.sidebar.title("LOGIX 360")
st.sidebar.info("Plateforme de pilotage Logistique Avancée - Standard MIT SCM")

# --- MAIN CONTENT ---
st.title("📦 LOGIX 360 : Hub Global Supply Chain 4.0")
st.markdown("---")

# Section Vision
col_v1, col_v2 = st.columns([2, 1])

with col_v1:
    st.write("""
    ### L'Intelligence Artificielle au service de l'Industrie Béninoise.
    LOGIX 360 n'est pas un simple outil de gestion, c'est un **Système d'Aide à la Décision (DSS)**. 
    Il fusionne la rigueur mathématique du **MIT MicroMasters** avec la puissance du **Machine Learning** pour optimiser vos flux sur l'axe Cotonou-Malanville et vers la zone **ZLECAF**.
    """)
    
    st.info("💡 **Conseil du jour :** Les prédictions IA indiquent une hausse de la variabilité sur le corridor Nord pour le mois prochain. Vérifiez vos stocks de sécurité dans l'interface Analytique.")

with col_v2:
    st.image("https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&q=80&w=400", 
             caption="Optimisation Logistique Régionale")

# --- DASHBOARD DE SYNTHÈSE (KPIs) ---
st.markdown("### 📊 État du Réseau en Temps Réel")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.metric("Disponibilité Flotte", "92%", "+2%")
with kpi2:
    st.metric("OEE/TRG Moyen", "78%", "-1.5%")
with kpi3:
    st.metric("Niveau de Service", "96.5%", "Optimal")
with kpi4:
    st.metric("Saturation Corridor", "42 Unités", "Stable")

# --- NAVIGATION RAPIDE ---
st.markdown("---")
st.write("### 🚀 Accès Rapide aux Interfaces")
c1, c2, c3, c4, c5 = st.columns(5)

c1.button("🔬 Analytique", use_container_width=True)
c2.button("⚙️ Opérationnelle", use_container_width=True)
c3.button("🌍 Stratégique", use_container_width=True)
c4.button("⚡ Dynamique", use_container_width=True)
c5.button("🛡️ Systèmes", use_container_width=True)

st.markdown("---")
st.caption("Développé par Elvis CRINOT | Expert Logistics & Supply Chain 4.0")
              
