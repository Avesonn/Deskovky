import streamlit as st
import os

# Konfigurace - layout="wide" zajistí roztažení na celou šířku PC
st.set_page_config(
    page_title="Moje Deskovky", 
    page_icon="🎲", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# Deaktivace set_page_config pro tvé podřazené soubory s hrami
st.set_page_config = lambda *args, **kwargs: None

# ==========================================
# OPRAVENÉ CSS - ŠÍŘKA A MOBILNÍ MENU
# ==========================================
css_finta = """
<style>
/* 1. Vynutí široké zobrazení na PC (roztáhne obsah) */
.block-container {
    max-width: 95rem !important;
    padding-top: 2rem !important;
}

/* 2. Skryjeme POUZE tlačítko Deploy a patičku. 
      Celé menu necháváme být, aby se na mobilu ukázala ikonka pro otevření rad! */
.stDeployButton {display: none !important;}
footer {display: none !important;}
</style>
"""
st.markdown(css_finta, unsafe_allow_html=True)

# Paměť stavu
if 'aktualni_stranka' not in st.session_state:
    st.session_state.aktualni_stranka = 'Menu'

def zpet_do_menu():
    st.session_state.aktualni_stranka = 'Menu'

# ==========================================
# HLAVNÍ MENU
# ==========================================
if st.session_state.aktualni_stranka == 'Menu':
    st.markdown("### 🎲 Vyberte hru:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🐈 Ostrov Koček", use_container_width=True):
            st.session_state.aktualni_stranka = 'Kocky'
            st.rerun()
    with col2:
        if st.button("🏴‍☠️ Karty mrtvého muže", use_container_width=True):
            st.session_state.aktualni_stranka = 'MrtvyMuz'
            st.rerun()
    with col3:
        if st.button("🌊 atlantis", use_container_width=True):
            st.session_state.aktualni_stranka = 'Atlantis'
            st.rerun()
            
    st.divider()
    st.info("ℹ️ **Navigace:** Po výběru hry najdete strategické tipy v postranním panelu (na mobilu vlevo nahoře pod ikonou menu).")
    st.stop()

# ==========================================
# BOČNÍ PANEL A HRY
# ==========================================
with st.sidebar:
    st.subheader("📋 RADY PRO HRÁČE")
    st.button("⬅️ Zpět na hlavní menu", on_click=zpet_do_menu, use_container_width=True)
    st.markdown("---")

if st.session_state.aktualni_stranka == 'Kocky':
    with open("Kocky.py", encoding="utf-8") as f:
        exec(f.read(), globals())

elif st.session_state.aktualni_stranka == 'MrtvyMuz':
    with open("Karty.py", encoding="utf-8") as f:
        exec(f.read(), globals())

elif st.session_state.aktualni_stranka == 'Atlantis':
    with open("atlantis.py", encoding="utf-8") as f:
        exec(f.read(), globals())
