import streamlit as st
import os

# Konfigurace - layout="wide" zajistí roztažení na celou šířku PC
st.set_page_config(
    page_title="Moje Deskovky", 
    page_icon="🎲", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# OPRAVENÉ CSS:
# 1. Necháme hlavičku (header) existovat, jinak se vše zúží.
# 2. Skryjeme jen tlačítka "Deploy" a "View Source", která tě štvala.
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            header {visibility: visible;} 
            footer {visibility: hidden;}
            [data-testid="stToolbar"] {visibility: hidden !important;}
            [data-testid="stDecoration"] {visibility: hidden !important;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

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
    st.info("ℹ️ **Navigace:** Po výběru hry hledejte strategické tipy v levém bočním panelu.")
    st.stop()

# ==========================================
# SIDEBAR (Boční panel pro rady)
# ==========================================
with st.sidebar:
    st.subheader("📋 RADY PRO HRÁČE")
    if st.button("⬅️ Zpět na hlavní menu", use_container_width=True):
        st.session_state.aktualni_stranka = 'Menu'
        st.rerun()
    st.markdown("---")
    st.write("Zde najdete strategické tipy, které se mění podle vybrané hry.")

# ==========================================
# ZOBRAZENÍ KONKRÉTNÍ HRY
# ==========================================
if st.session_state.aktualni_stranka == 'Kocky':
    with open("Kocky.py", encoding="utf-8") as f:
        exec(f.read(), globals())

elif st.session_state.aktualni_stranka == 'MrtvyMuz':
    with open("Karty.py", encoding="utf-8") as f:
        exec(f.read(), globals())

elif st.session_state.aktualni_stranka == 'Atlantis':
    with open("atlantis.py", encoding="utf-8") as f:
        exec(f.read(), globals())
