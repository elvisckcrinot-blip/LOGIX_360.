import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Systèmes | LOGIX 360", layout="wide")

st.title("🛡️ Interface Systèmes (SC4x)")
st.markdown("---")

# --- 1. IoT GATEWAY (Monitoring Capteurs) ---
st.header("🌐 1. IoT Gateway : Monitoring en Temps Réel")
st.info("Centralisation des données télématiques et capteurs de cargaison.")

col1, col2, col3 = st.columns(3)

# Simulation de flux IoT
with col1:
    temp = st.metric("Température Conteneur (Cotonou)", "24.5 °C", "0.2 °C")
with col2:
    humid = st.metric("Humidité (Malanville)", "45 %", "-2 %")
with col3:
    choc = st.metric("Détecteur de Chocs", "Inactif ✅", delta_color="normal")

st.write("### Journal de Bord IoT")
log_iot = pd.DataFrame({
    # CORRECTION ICI : 'h' minuscule au lieu de 'H'
    'Horodatage': pd.date_range(start='2026-04-15 10:00', periods=4, freq='h'),
    'Capteur': ['GPS-01', 'TEMP-04', 'SHOCK-02', 'GPS-01'],
    'Événement': ['Entrée Zone GDIZ', 'Seuil Alerte (28°C)', 'Mouvement détecté', 'Sortie Zone GDIZ']
})
st.table(log_iot)

# --- 2. CONNECTEUR EDI & DÉMATÉRIALISATION ---
st.markdown("---")
st.header("📄 2. Connecteur EDI : Dématérialisation Douanière")
st.write("Génération de la liasse documentaire pour le transit régional.")

uploaded_file = st.file_uploader("Télécharger la lettre de voiture ou facture (PDF/JPG)", type=["pdf", "jpg", "png"])

if uploaded_file is not None:
    with st.spinner('Analyse OCR et intégration EDI en cours...'):
        time.sleep(2)
        st.success("Document numérisé. Données extraites pour transmission SYDONIA/ZLECAF.")

c1, c2 = st.columns(2)
with c1:
    if st.button("Générer Bordereau de Suivi (BSTF)"):
        st.download_button("Télécharger le BSTF", "Données simulées", file_name="BSTF_LOGIX360.txt")
with c2:
    st.button("Synchroniser avec le Guichet Unique")

# --- 3. HUB DE SÉCURITÉ & ACCÈS ---
st.markdown("---")
st.header("🔐 3. Hub de Sécurité & Intégrité")
st.write("Gestion des accès et journal d'audit (Blockchain-ready).")

col_sec1, col_sec2 = st.columns(2)

with col_sec1:
    st.write("### Contrôle d'Accès")
    role = st.selectbox("Simuler un rôle utilisateur :", ["Superviseur Logistique", "Opérateur de Quai", "Agent Douane"])
    if role == "Superviseur Logistique":
        st.write("🔓 Accès complet aux 5 interfaces.")
    else:
        st.write("🔒 Accès restreint aux modules opérationnels.")

with col_sec2:
    st.write("### Intégrité des Données")
    st.code("Hash SHA-256 : 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8")
    st.success("Toutes les transactions de stock sont horodatées et immuables.")
