import streamlit as st

st.set_page_config(page_title="Moje Deskovky", page_icon="🎲", layout="wide")

if 'aktualni_stranka' not in st.session_state:
    st.session_state.aktualni_stranka = 'Menu'

def zpet_do_menu():
    st.session_state.aktualni_stranka = 'Menu'

# ==========================================
# HLAVNÍ MENU
# ==========================================
if st.session_state.aktualni_stranka == 'Menu':
    st.markdown("### Dostupné hry - pro pravidla a rady klikněte na vybranou hru")
    
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
# ZOBRAZENÍ HER
# ==========================================

# Tady přidáváme sidebar, aby se VŽDY ukázala ta ikonka menu
with st.sidebar:
    st.button("⬅️ Zpět na hlavní menu", on_click=zpet_do_menu, use_container_width=True)
    st.markdown("---")
    st.write("Navigace v pravidlech je v záložkách nahoře.")

if st.session_state.aktualni_stranka == 'Kocky':
    with open("Kocky.py", encoding="utf-8") as f:
        exec(f.read(), globals())

elif st.session_state.aktualni_stranka == 'MrtvyMuz':
    with open("Karty.py", encoding="utf-8") as f:
        exec(f.read(), globals())

elif st.session_state.aktualni_stranka == 'Atlantis':
    with open("atlantis.py", encoding="utf-8") as f:
        exec(f.read(), globals())
