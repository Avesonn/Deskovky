import streamlit as st
import os

# Konfigurace
st.set_page_config(
    page_title="Moje Deskovky", 
    page_icon="🎲", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# CSS pro skrytí nepotřebného
hide_st_style = """
            <style>
            footer {visibility: hidden;}
            header {visibility: hidden !important;}
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
    st.info("ℹ️ **Jak na pravidla a rady:**")
    st.write("Klikněte na hru výše. Poté uvidíte pravidla a v levém menu (na mobilu pod ikonou čárek v rohu) najdete strategické tipy pro nováčky.")
    st.stop()

# ==========================================
# SIDEBAR A HRY
# ==========================================
with st.sidebar:
    st.subheader("📋 RADY PRO HRÁČE")
    st.button("⬅️ Zpět na hlavní menu", on_click=zpet_do_menu, use_container_width=True)
    st.markdown("---")
    st.write("Zde najdete strategické tipy, které se dynamicky mění podle hry.")

if st.session_state.aktualni_stranka == 'Kocky':
    with open("Kocky.py", encoding="utf-8") as f:
        exec(f.read(), globals())

elif st.session_state.aktualni_stranka == 'MrtvyMuz':
    with open("Karty.py", encoding="utf-8") as f:
        exec(f.read(), globals())

elif st.session_state.aktualni_stranka == 'Atlantis':
    with open("atlantis.py", encoding="utf-8") as f:
        exec(f.read(), globals())
