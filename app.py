import streamlit as st
import os

# Konfigurace stránky
st.set_page_config(
    page_title="Moje Deskovky", 
    page_icon="🎲", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# CSS pro skrytí nepotřebných lišt, ale ponechání funkčního menu
hide_st_style = """
            <style>
            footer {visibility: hidden;}
            header {visibility: hidden !important;}
            [data-testid="stToolbar"] {visibility: hidden !important;}
            [data-testid="stDecoration"] {visibility: hidden !important;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Inicializace stavu
if 'aktualni_stranka' not in st.session_state:
    st.session_state.aktualni_stranka = 'Menu'

def zpet_do_menu():
    st.session_state.aktualni_stranka = 'Menu'

# ==========================================
# HLAVNÍ MENU (Rozcestník)
# ==========================================
if st.session_state.aktualni_stranka == 'Menu':
    # Vizuální navádění pro hráče
    st.info("💡 **Tipy a rady:** Pro zobrazení strategických rad klikněte vlevo nahoře na ikonu menu (čárky/šipka).")
    
    st.markdown("### 🎲 Dostupné hry - pro pravidla a rady klikněte na vybranou hru:")
    st.write("") 
    
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
            
    st.stop() # Zastaví vykreslování, aby se pod dlaždicemi neukázalo nic dalšího

# ==========================================
# BOČNÍ PANEL (Vždy přítomný)
# ==========================================
with st.sidebar:
    st.subheader("📋 RADY PRO HRÁČE")
    st.button("⬅️ Zpět na hlavní menu", on_click=zpet_do_menu, use_container_width=True)
    st.markdown("---")
    st.write("Zde najdete strategické tipy, které se dynamicky mění podle toho, jakou hru zrovna prohlížíte.")

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
