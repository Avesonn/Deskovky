import streamlit as st
import os

st.set_page_config(page_title="Moje Deskovky", page_icon="🎲", layout="wide")
st.set_page_config = lambda *args, **kwargs: None

# ==========================================
# ODSTRANĚNÍ MOŽNOSTI PROKLIKU NA GITHUB
# ==========================================
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

if 'aktualni_stranka' not in st.session_state:
    st.session_state.aktualni_stranka = 'Menu'

def zpet_do_menu():
    st.session_state.aktualni_stranka = 'Menu'

# ==========================================
# HLAVNÍ MENU (Rozcestník)
# ==========================================
if st.session_state.aktualni_stranka == 'Menu':
    st.markdown("### Dostupné hry - pro pravidla a rady klikněte na vybranou hru")
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
            
    st.stop()

# ==========================================
# ZOBRAZENÍ KONKRÉTNÍ HRY
# ==========================================
st.button("⬅️ Zpět na hlavní menu", on_click=zpet_do_menu)
st.divider()

if st.session_state.aktualni_stranka == 'Kocky':
    with open("Kocky.py", encoding="utf-8") as f:
        exec(f.read(), globals())

elif st.session_state.aktualni_stranka == 'MrtvyMuz':
    with open("Karty.py", encoding="utf-8") as f:
        exec(f.read(), globals())

elif st.session_state.aktualni_stranka == 'Atlantis':
    with open("Atlantis.py", encoding="utf-8") as f:
        exec(f.read(), globals())
