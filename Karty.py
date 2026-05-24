import streamlit as st

# Konfigurace stránky
st.set_page_config(page_title="Karty mrtvého muže - Průvodce pro nováčky", page_icon="🏴‍☠️", layout="wide")

# --- INTERAKTIVNÍ SLOVNÍČEK & TIPY V BOČNÍM PANELU ---
st.sidebar.header("💡 Strategické tipy pro nováčky")
st.sidebar.markdown("Rozbalte si oblast, která vás zajímá:")

with st.sidebar.expander("Základní pravidlo: Kdy přestat? 🛑"):
    st.warning("""
    **Tip k riskování:** Největší chybou nováčků je přílišná chamtivost. Pamatujte, že ve hře je 10 barev (symbolů).
    * Pokud máte vyložené **3 různé karty**, šance na to, že si vytáhnete stejnou barvu (a o vše přijdete), už je poměrně velká.
    * U **4 vyložených karet** už velmi vážně uvažujte o ukončení tahu a sebrání kořisti.
    """)

with st.sidebar.expander("Kombo: Truhla + Klíč 🗝️"):
    st.success("""
    **Tip k nejlepšímu kombu ve hře:** Pokud se vám podaří v jednom tahu vyložit Truhlu i Klíč, vyhráli jste jackpot! 
    * Když tah dobrovolně ukončíte a vezmete si kořist, vezmete si z odhazovacího balíčku tolik dalších karet, kolik jste jich právě vyložili.
    * **Strategie pro děti i dospělé:** Pokud máte na stole Klíč i Truhlu, už NEHRAJTE DÁL a hned ukončete tah! Neriskujte ztrátu tohoto komba.
    """)

with st.sidebar.expander("Šavle vs. Dělo ⚔️"):
    st.info("""
    **Rozdíl v útoku:**
    * **Dělo:** Slouží k oslabení soupeře. Karta prostě zmizí na odhazovací balíček. Zničte soupeřům jejich karty s nejvyššími čísly (např. 7, 8 nebo 9).
    * **Šavle:** Slouží k vašemu obohacení. Ukradnete kartu soupeři a ihned ji hrajete, jako byste si ji lízli vy! 
    * **Pozor u Šavle:** Nesmíte ukrást barvu, kterou už máte v aktuálním tahu před sebou, jinak byste propadli!
    """)

with st.sidebar.expander("Záchranná brzda: Kotva ⚓"):
    st.error("""
    **Tip ke Kotvě:** Kotva vám dává svobodu riskovat! 
    Jakmile vyložíte Kotvu, cokoliv, co jste vyložili *před* ní, máte už v bezpečí. I když v dalším tahu narazíte na stejnou barvu a praskne vám balonek (propadnete), karty před Kotvou si odnesete. Po vyložení Kotvy se tedy vyplatí tahat dál agresivněji.
    """)

# --- HLAVNÍ OBSAH APLIKACE ---
st.title("Karty mrtvého muže 🏴‍☠️")
st.markdown("Interaktivní průvodce pravidly a pomocník pro počítání kořisti pro pirátskou hru plnou riskování!")

sekce_menu = st.radio(
    "Vyberte herní kapitolu:", 
    ["1. Cíl hry a Základy", "2. Příprava hry", "3. Průběh tahu (Riskování)", "4. Efekty karet (Symboly)", "5. Bodování", "6. Všechny varianty hry"], 
    horizontal=True
)

st.divider()

# --- 1. CÍL HRY A ZÁKLADY ---
if sekce_menu == "1. Cíl hry a Základy":
    st.header("1. Cíl hry a základní pojmy pro nováčky")
    
    st.subheader("🎯 Cíl hry")
    st.markdown("""
    Jste piráti a vaším cílem je **nasbírat ten největší a nejcennější poklad** dříve, než dojde dobírací balíček karet. 
    Karty se dělí do 10 různých barev (symbolů). Na konci hry si každou barvu dáte na vlastní hromádku a **z každé hromádky se vám bude počítat jen ta jedna karta, která má nejvyšší číslo**. Kdo má v součtu nejvíce bodů, vyhrává!
    """)
    
    st.subheader("📖 Slovníček pro děti (i dospělé)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("""
        **💰 Kořist (Poklad)**
        Karty, které jste úspěšně získali, leží bezpečně u vás a už vám je nikdo (skoro nikdo) nevezme. Skládáte si je do hromádek podle barev, aby na vás vždy koukalo nejvyšší číslo.
        """)
        st.info("""
        **🃏 Řada (Na stole)**
        Když jste na tahu, otáčíte karty doprostřed stolu. Těmto kartám se říká řada. Zatím **nejsou vaše**! Jsou v ohrožení, dokud tah neukončíte.
        """)
        
    with col2:
        st.error("""
        **💥 Propadnutí (Když balonek praskne!)**
        Tato hra je jako nafukování balonku. Otáčením karet balonek přifukujete – může být obrovský! Ale pokud z balíčku otočíte kartu se symbolem/barvou, **která už na stole v řadě leží**, balonek praskne! Všechny karty z řady musíte vyhodit a nezískáte vůbec nic.
        """)
        st.warning("""
        **🛑 Ukončení tahu (Beru kořist)**
        Pokud máte v řadě vyložené karty a bojíte se, že další kartou už "balonek praskne", prostě řeknete: „Končím!“ Všechny karty z řady si vezmete k sobě a přidáte je do své bezpečné Kořisti. Tím jste svůj tah úspěšně dokončili.
        """)

# --- 2. PŘÍPRAVA HRY ---
elif sekce_menu == "2. Příprava hry":
    st.header("2. Příprava hry před první partií")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Herní materiál")
        st.markdown("""
        * **60 karet kořisti:** Ve hře je celkem 10 různých barev (symbolů). Od každého symbolu je přesně 6 karet. Běžné karty mají hodnoty 2 až 7 (Mořské panny mají 4 až 9).
        * **Karty postav a pravidel:** Slouží pro pokročilé varianty hry (viz sekce 6). Pro první hru je nechte v krabici.
        """)
        
    with col2:
        st.subheader("Příprava krok za krokem")
        st.markdown("""
        1. **Tvorba odhazovacího balíčku:** Než začnete, roztřiďte 60 karet kořisti podle 10 symbolů. Od každého z 10 symbolů najděte kartu s **nejnižší hodnotou** (většinou je to číslo 2, u mořské panny 4). 
        2. Těchto 10 nejnižších karet dejte na jednu hromádku lícem nahoru doprostřed stolu. To je **Odhazovací balíček** (tzv. Smetiště).
        3. **Tvorba dobíracího balíčku:** Zbylých 50 karet důkladně zamíchejte. Položte je lícem dolů doprostřed stolu. To je váš **Dobírací balíček**.
        4. Nechte si uprostřed stolu místo, kam budete vykládat karty během tahu.
        """)
        
    st.info("💡 **Proč se vyřazuje těch 10 karet na začátku?** Aby na Smetišti už od prvního kola něco bylo a daly se tak naplno využívat efekty karet jako je Mapa nebo Klíč!")

# --- 3. PRŮBĚH TAHU (RISKOVÁNÍ) ---
elif sekce_menu == "3. Průběh tahu (Riskování)":
    st.header("3. Jak se to hraje? (Průběh tahu)")
    st.markdown("""
    Ve hře se střídáte v tazích. Když jste na řadě, otáčíte z dobíracího balíčku vždy jen **jednu kartu** a vyložíte ji před sebe do řady.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Krok 1: Kontrola barvy")
        st.markdown("""
        Pokaždé, když otočíte novou kartu, zkontrolujte ji:
        * ❌ **Je tahle barva už vyložená v mé řadě?** -> **PROPADLI JSTE!** Váš tah okamžitě končí. Všechny karty z řady hoďte na odhazovací balíček a nic nezískáte.
        * ✅ **Tato barva tu ještě není:** -> Karta je platná. **Ihned vyhodnoťte efekt karty** (viz další záložka).
        """)
    with col2:
        st.subheader("Krok 2: Riskovat, nebo brát?")
        st.markdown("""
        Pokud jste právě vyhodnotili efekt karty a nepropadli jste, musíte se rozhodnout:
        * 🎲 **A) Hrát dál:** Otočíte další kartu a riskujete prasknutí balonku.
        * 🛑 **B) Ukončit tah:** Vezmete si VŠECHNY právě vyložené karty z řady, roztřídíte si je doma do hromádek podle barev (nejvyšší číslo nahoru) a na řadě je další hráč.
        """)

# --- 4. EFEKTY KARET (SYMBOLY) ---
elif sekce_menu == "4. Efekty karet (Symboly)":
    st.header("4. Co dělají jednotlivé karty (Efekty symbolů)")
    st.markdown("Jakmile bezpečně vyložíte novou kartu, okamžitě a povinně uděláte to, co znamená její obrázek:")
    
    c1, c2 = st.columns(2)
    
    with c1:
        with st.expander("🔮 Křišťálová koule"):
            st.write("Tajně se podívejte na úplně vrchní kartu dobíracího balíčku. Teprve pak se rozhodněte, zda ji otočíte do hry, nebo ji tam necháte ležet a raději hned ukončíte tah a shrábnete kořist.")
        with st.expander("🪝 Hák"):
            st.write("Musíte vzít jednu kartu ze svého vlastního pokladu (z toho, co jste získali v minulých kolech) a vyložit ji do řady. Znovu tím spustíte její efekt! (Na konci tahu si ji zase vezmete zpátky do pokladu).")
        with st.expander("⚓ Kotva"):
            st.write("Bod záchrany! Cokoliv, co leží v řadě PŘED Kotvou, je odteď v bezpečí. Pokud za chvíli propadnete, neztratíte úplně všechno – karty, které ležely před Kotvou, si smíte vzít.")
        with st.expander("💣 Dělo"):
            st.write("Útok na kamaráda! Vyberte si jednoho soupeře. Podívejte se na jeho poklad a odhoďte mu jednu jeho vrchní kartu (nejlépe tu s nejvyšším číslem) na odhazovací balíček. Zničili jste mu body!")
        with st.expander("🧜‍♀️ Mořská panna"):
            st.write("Mořská panna nedělá vůbec nic. Nemá žádnou speciální moc. Místo toho má ale vyšší čísla! Zatímco ostatní karty končí na čísle 7, panny mají hodnoty až do 9. Jsou to hromady bodů na konec hry.")

    with c2:
        with st.expander("🗝️ Klíč (Funguje s Truhlou)"):
            st.write("Když vyložíte jen Klíč, nic se nestane. Ale pokud máte v jedné řadě Klíč **A ZÁROVEŇ** Truhlu, je to super! Když si na konci tahu vezmete kořist, smíte si z odhazovacího balíčku navíc nabrat tolik dalších karet, kolik jich bylo v řadě.")
        with st.expander("🧰 Truhla (Funguje s Klíčem)"):
            st.write("Stejné jako Klíč. Pokud máte Truhlu i Klíč současně, dostanete obrovský bonus karet ze Smetiště (odhazovacího balíčku).")
        with st.expander("🐙 Kraken"):
            st.write("Kraken vás nutí riskovat! Jakmile vyložíte Krakena, NESMÍTE hned utéct s pokladem. Musíte z balíčku otočit a do řady přidat ještě alespoň dvě další karty (pokud ovšem cestou nepropadnete).")
        with st.expander("🗺️ Mapa"):
            st.write("Vezměte si 3 náhodné karty z odhazovacího balíčku (Smetiště). Jednu z nich si vyberte, dejte ji do své řady a ihned udělejte její efekt. Zbylé dvě karty vraťte na Smetiště.")
        with st.expander("⚔️ Šavle"):
            st.write("Krádež! Seberte vrchní kartu z pokladu kteréhokoliv soupeře. Tuto ukradenou kartu vyložte do své řady a hned udělejte její efekt. Dejte si ale pozor: Nesmíte ukrást barvu, kterou už zrovna v této řadě máte (sami byste se tak vyřadili)!")

# --- 5. BODOVÁNÍ A KALKULAČKA ---
elif sekce_menu == "5. Bodování":
    st.header("5. Konec hry a Finální počítání skóre")
    
    st.markdown("""
    Hra končí okamžitě ve chvíli, kdy jeden z hráčů chce otočit kartu, ale **dobírací balíček je prázdný**. 
    Kdo má nejvíc bodů? Každý hráč se podívá na svůj poklad. **Sečte si všechna čísla, která vidí na vrchu svých barevných hromádek.** Karty schované zespodu se nepočítají!
    """)
    
    st.subheader("🔢 Kalkulačka kořisti")
    st.markdown("Zadejte hodnotu vrchní karty pro každou barvu, kterou vlastníte (pokud nějakou barvu vůbec nemáte, nechte tam 0):")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        b1 = st.number_input("🔮 Křišťálová koule", min_value=0, max_value=7, value=0)
        b2 = st.number_input("🪝 Hák", min_value=0, max_value=7, value=0)
        b3 = st.number_input("⚓ Kotva", min_value=0, max_value=7, value=0)
        b4 = st.number_input("💣 Dělo", min_value=0, max_value=7, value=0)
        
    with col2:
        b5 = st.number_input("🧜‍♀️ Mořská panna", min_value=0, max_value=9, value=0)
        b6 = st.number_input("🗝️ Klíč", min_value=0, max_value=7, value=0)
        b7 = st.number_input("🧰 Truhla", min_value=0, max_value=7, value=0)
        
    with col3:
        b8 = st.number_input("🐙 Kraken", min_value=0, max_value=7, value=0)
        b9 = st.number_input("🗺️ Mapa", min_value=0, max_value=7, value=0)
        b10 = st.number_input("⚔️ Šavle", min_value=0, max_value=7, value=0)

    # Výpočet skóre
    celkove_skore = b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9 + b10
    
    st.divider()
    st.metric(label="🏆 TVOJE FINÁLNÍ SKÓRE", value=celkove_skore)
    st.caption("Úplně nejvyšší možný zisk v normální hře je 72 bodů.")
    
    if celkove_skore > 50:
        st.balloons()

# --- 6. VŠECHNY VARIANTY HRY ---
elif sekce_menu == "6. Všechny varianty hry":
    st.header("6. Kompletní přehled pokročilých variant (Když už vás základ omrzí)")
    
    with st.expander("👤 1. Karty postav (Každý hráč má jinou schopnost)"):
        st.markdown("""
        V krabici je **16 (příp. 17) karet unikátních pirátů**. 
        * **Příprava:** Na začátku hry rozdejte každému hráči náhodně 2 karty postav. Hráč si je tajně prohlédne, vybere si z nich 1, za kterou bude celou hru hrát, a druhou vrátí tajně do krabice.
        * **Efekt:** Každý pirát (postava) má na sobě napsanou speciální dovednost, která pro něj platí po celou hru (např. Dělo mu pálí dvakrát, nebo je imunní vůči Krakenovi). Odhalte své postavy těsně před začátkem hry!
        """)
        
    with st.expander("🧜‍♀️ 2. Aktivní Mořská panna (Speciální schopnost pro Panny)"):
        st.markdown("""
        Pokud vám vadí, že Mořská panna nic nedělá, zkuste tuto oficiální variantu:
        * **Příprava:** Z balíčku vyberte Mořské panny s hodnotami **8 a 9** a vyhoďte je do krabice. Nahraďte je doplňkovými kartami Mořských panen s hodnotami **2 a 3**.
        * **Nové pravidlo:** Pokaždé, když ve svém tahu vyložíte Mořskou pannu, můžete vzít jednu libovolnou jinou kartu ve vaší probíhající řadě, přesunout ji *až za* Mořskou pannu a **ZNOVU POUŽÍT JEJÍ EFEKT!** (Je to extrémně silné s Dělem nebo Šavlí).
        """)
        
    with st.expander("📜 3. Karty volitelných pravidel (6 karet)"):
        st.markdown("""
        Těchto 6 speciálních karet plošně mění pravidla pro **všechny hráče** po celou partii.
        * **Jak na to:** Před začátkem hry náhodně vylosujte 1 (nebo i více) z těchto 6 karet, položte ji lícem nahoru doprostřed stolu a přečtěte nahlas její efekt. 
        * Toto pravidlo pak upravuje klasickou hru pro všechny účastníky (např. všichni mohou zkoušet štěstí i po Krakenovi jinak, nebo se mění systém propadnutí).
        """)
        
    with st.expander("🏴‍☠️ 4. Pirátská Party Game (Až pro 8 hráčů!)"):
        st.markdown("""
        Máte u stolu 5, 6, 7 nebo 8 pirátů? Hra se dá hrát i ve velkém, jen potřebujete **dvě základní sady (krabice)** hry.
        * **Příprava Smetiště (Odhazovacího balíčku):** Vyberte 20 nejnižších karet (od každé barvy dvě nejnižší) a dejte je na odhazovací balíček.
        * **Dobírací balíček:** Zbytek ze dvou krabic (100 karet) smíchejte a vytvořte obří dobírací balíček.
        * **Postavy:** Smíchejte obě sady postav a rozdejte každému hráči 2 na výběr.
        * Dál se už hraje normálně. Bude to obrovský chaos!
        """)