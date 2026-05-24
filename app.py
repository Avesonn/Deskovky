import streamlit as st
import os
import datetime

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
# OPRAVENÉ CSS A POČÍTADLO
# ==========================================
css_finta = """
<style>
/* Vynutí široké zobrazení na PC (roztáhne obsah) */
.block-container {
    max-width: 95rem !important;
    padding-top: 2rem !important;
}

/* Skryjeme POUZE tlačítko Deploy a patičku */
.stDeployButton {display: none !important;}
footer {display: none !important;}

/* Styl pro počítadlo vpravo dole */
.pocitadlo {
    position: fixed;
    bottom: 10px;
    right: 15px;
    font-size: 11px;
    color: #888888;
    z-index: 100;
}
</style>
"""
st.markdown(css_finta, unsafe_allow_html=True)

# ==========================================
# POČÍTADLO ZOBRAZENÍ A UKLÁDÁNÍ
# ==========================================
SOUBOR_POCITADLA = "pocitadlo.txt"

# Vytvoření souboru, pokud neexistuje
if not os.path.exists(SOUBOR_POCITADLA):
    with open(SOUBOR_POCITADLA, "w") as f:
        f.write("0")

# Zvýšení počtu jen při první návštěvě relace
if 'navsteva_zapocitana' not in st.session_state:
    with open(SOUBOR_POCITADLA, "r") as f:
        obsah = f.read().strip()
        pocet = int(obsah) if obsah else 0
    pocet += 1
    with open(SOUBOR_POCITADLA, "w") as f:
        f.write(str(pocet))
    st.session_state.navsteva_zapocitana = True
    st.session_state.aktualni_pocet = pocet
else:
    with open(SOUBOR_POCITADLA, "r") as f:
        obsah = f.read().strip()
        st.session_state.aktualni_pocet = int(obsah) if obsah else 0

# Vykreslení počítadla na obrazovku
st.markdown(f'<div class="pocitadlo">Zobrazení stránky: {st.session_state.aktualni_pocet}</div>', unsafe_allow_html=True)

# ==========================================
# PAMĚŤ STAVU A NAVIGACE
# ==========================================
if 'aktualni_stranka' not in st.session_state:
    st.session_state.aktualni_stranka = 'Menu'

def zpet_do_menu():
    st.session_state.aktualni_stranka = 'Menu'

# ==========================================
# HLAVNÍ MENU
# ==========================================
if st.session_state.aktualni_stranka == 'Menu':
    st.markdown("### 🎲 Vyberte hru:")
    
    # První řádek her
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
            st.session_state.aktualni_stranka = 'atlantis'
            st.rerun()
            
    st.write("") # Mezera mezi řádky
    
    # Druhý řádek her
    col4, col5, col6 = st.columns(3)
    
    with col4:
        if st.button("🌍 Small world", use_container_width=True):
            st.session_state.aktualni_stranka = 'small'
            st.rerun()
    with col5:
        if st.button("🪴 Pokojovky", use_container_width=True):
            st.session_state.aktualni_stranka = 'pokoj'
            st.rerun()
    with col6:
        st.empty() # Necháme prázdné pro hezké zarovnání zleva doleva
        
    st.divider()
    st.info("ℹ️ **Navigace:** Po výběru hry najdete strategické tipy v postranním panelu (na mobilu vlevo nahoře pod ikonou menu).")
    
    # ==========================================
    # SEKCE PRO PŘIPOMÍNKY
    # ==========================================
    st.write("")
    with st.expander("📝 Máte připomínku nebo jste našli chybu?"):
        st.write("Chybí vám něco v pravidlech nebo je něco nejasné? Napište mi to sem!")
        with st.form("pripominky_form", clear_on_submit=True):
            text_pripominky = st.text_area("Vaše zpráva:", placeholder="Např.: U hry Pokojovky chybí bodování...")
            odeslano = st.form_submit_button("Odeslat připomínku")
            
            if odeslano:
                if text_pripominky.strip() == "":
                    st.warning("Prosím, napište nejdříve nějaký text.")
                else:
                    # Uložení připomínky do textového souboru
                    with open("pripominky.txt", "a", encoding="utf-8") as f:
                        dnes = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
                        f.write(f"[{dnes}] {text_pripominky}\n---\n")
                    st.success("Díky! Vaše připomínka byla v pořádku odeslána a uložena.")

    # ==========================================
    # TAJNÁ ADMINISTRACE (Pro čtení připomínek)
    # ==========================================
  st.write("")
    with st.expander("🔒 Tajná administrace"):
        heslo = st.text_input("Zadejte heslo:", type="password")
        
        # Ověření přes tajné úložiště Streamlitu
        if heslo == st.secrets["ADMIN_HESLO"]: 
            st.success("Přístup povolen.")
            
            st.subheader("📝 Přijaté připomínky:")
            try:
                with open("pripominky.txt", "r", encoding="utf-8") as f:
                    obsah = f.read()
                    st.text(obsah if obsah.strip() else "Zatím tu nic není.")
            except FileNotFoundError:
                st.write("Zatím tu nic není.")
                
            st.divider()
            st.subheader("📊 Statistiky:")
            try:
                with open("pocitadlo.txt", "r") as f:
                    st.write(f"Počet načtení: **{f.read().strip()}**")
            except:
                st.write("Počítadlo zatím nemá data.")
                
        elif heslo != "":
            st.error("Špatné heslo!")

    st.stop() # Zastaví vykreslování hlavní stránky, aby se neukazovaly další kódy

# ==========================================
# BOČNÍ PANEL A OTEVÍRÁNÍ HER
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

elif st.session_state.aktualni_stranka == 'atlantis':
    with open("atlantis.py", encoding="utf-8") as f:
        exec(f.read(), globals())

elif st.session_state.aktualni_stranka == 'small':
    with open("small.py", encoding="utf-8") as f:
        exec(f.read(), globals())

elif st.session_state.aktualni_stranka == 'pokoj':
    with open("Pokoj.py", encoding="utf-8") as f:
        exec(f.read(), globals())
