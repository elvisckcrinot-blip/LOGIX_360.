import streamlit as st

st.set_page_config(page_title="LOGIX 360 | Hub", layout="wide", page_icon="📦")

st.title("📦 LOGIX 360 : Hub SCM 4.0")
st.markdown("---")

st.write("""
### Bienvenue dans le futur de la Supply Chain Industrielle.
Cette plateforme fusionne les standards du **MIT MicroMasters** avec l'intelligence artificielle 
pour piloter la performance logistique au Bénin et vers la zone ZLECAF.

**Utilisez la barre latérale pour naviguer entre les interfaces stratégiques.**
""")

# Un petit Dashboard de résumé peut être ajouté ici
col1, col2, col3 = st.columns(3)
col1.metric("Statut Système", "Optimal ✅")
col2.metric("Moteur IA", "Random Forest Actif 🤖")
col3.metric("Région", "Bénin / ZLECAF 🌍")
