import streamlit as st
import os

# Konfigurace stránky
st.set_page_config(page_title="Ostrov koček - Průvodce pro nováčky", page_icon="🐈", layout="wide")

# --- POMOCNÁ FUNKCE PRO OBRÁZKY ---
def nahraj_obrazek(nazev_souboru, popisek):
    if os.path.exists(nazev_souboru):
        # Opravený parametr pro moderní verze Streamlitu
        st.image(nazev_souboru, caption=popisek, use_container_width=True)
    else:
        st.info(f"🖼️ [Zde se zobrazí obrázek: {nazev_souboru}]")
        st.caption(popisek)

# --- INTERAKTIVNÍ SLOVNÍČEK & TIPY V BOČNÍM PANELU ---
st.sidebar.header("💡 Strategické tipy pro nováčky")
st.sidebar.markdown("Rozbalte si oblast, která vás zajímá:")

with st.sidebar.expander("Proč zakrývat krysy? 🐀"):
    st.warning("""
    **Tip ke krysám:** Každá nezakrytá krysa na konci hry znamená **-1 bod**. 
    Nezdá se to moc, ale na lodi je jich celkem 19! Pokud si nedáte pozor, můžete kvůli krysám ztratit klidně 10–15 bodů, což často rozhoduje o vítězi. Snažte se dílky pokládat tak, abyste krysy průběžně udupávali.
    """)

with st.sidebar.expander("Jak fungují sekce (místnosti)? 📦"):
    st.error("""
    **Tip k sekcím lodi:** Loď je rozdělena na 7 uzavřených sekcí. Pokud na konci hry zůstane v sekci byť jen **jediné prázdné políčko**, sekce se považuje za neúplnou a dostanete **-5 bodů**!
    * **Strategie:** Je mnohem lepší kompletně zaplnit 3 sekce a zbytek nechat poloprázdný, než mít všech 7 sekcí zaplněných z 90 %. Soustřeďte se na postupné dokončování místností.
    """)

with st.sidebar.expander("K čemu jsou dobré Měděné poklady? 🪙"):
    st.success("""
    **Tip k měděným pokladům:** Tyto malé dílky (velikost 1 nebo 2 čtverečky) sice samy o sobě nepřinášejí žádné body, ale jsou **klíčem k vítězství**. 
    Používejte je na ucpávání drobných děr kolem krys nebo v rozích sekcí, kam by se vám už žádný velký dílek kočky nevešel. Získáte je tak, že překryjete předtištěnou mapu na lodi kočkou STEJNÉ barvy.
    """)

with st.sidebar.expander("Oshaxové – Vyplatí se? 🐯"):
    st.info("""
    **Tip k Oshaxům:** Oshaxové (hnědé karty) jsou drazí na pořízení, ale fungují jako žolíci. Můžete jim určit libovolnou barvu.
    * **Využití:** Použijte je k propojení dvou oddělených skupinek koček stejné barvy, nebo k okamžitému zvětšení rodiny těsně před koncem hry. Zachrání vás také v situaci, kdy vám ostatní hráči z nabídky vyfoukli barvu, kterou sbíráte.
    """)

# --- HLAVNÍ OBSAH APLIKACE ---
st.title("Ostrov koček – Detailní průvodce pro nováčky 🐈")
st.markdown("Vítejte na Ostrově koček! Tento interaktivní dashboard vás provede pravidly krok za krokem a ukáže vám skryté strategie.")

sekce_menu = st.radio(
    "Vyberte herní kapitolu:", 
    ["Přehled komponentů a karet", "Příprava hry", "Podrobný průběh dne a Rychlost", "Pravidla skládání", "Bodování a kalkulačka"], 
    horizontal=True
)

st.divider()

# --- 1. PŘEHLED KOMPONENTŮ A KARET ---
if sekce_menu == "Přehled komponentů a karet":
    st.header("1. Co najdete v krabici & Význam karet")
    
    tab1, tab2 = st.tabs(["Herní materiál", "Detailní průvodce Kartami objevů"])
    
    with tab1:
        st.subheader("Herní materiál")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            nahraj_obrazek("Figurky.jpg", "30 figurek koček (slouží k označení barev a pořadí)")
            nahraj_obrazek("vethuv_clun.jpg", "1 Vethův člun (odpočítává čas do konce hry)")
        with col2:
            nahraj_obrazek("dilky_kocek.jpg", "85 dílků koček (polyomino tvary, které skládáte na loď)")
            nahraj_obrazek("zlate_poklady.jpg", "25 dílků zlatých pokladů (přinášejí 3 body)")
        with col3:
            nahraj_obrazek("zeton_ryb.jpg", "42 žetonů ryb (platidlo za karty a odchyt koček)")
            nahraj_obrazek("oshaxove.jpg", "6 dílků oshaxů (velcí kočičí žolíci)")
        with col4:
            nahraj_obrazek("medene_poklady.jpg", "44 dílků měděných pokladů (na ucpávání mezer)")
            nahraj_obrazek("trvanlive_kose.jpg", "10 žetonů trvanlivých košů")

    with tab2:
        st.subheader("Karty objevů – Srdce celé hry")
        st.markdown("""
        Karty objevů získáváte během draftu ve Fázi 2. Každá karta má v levém horním rohu **cenu v rybách**, kterou musíte zaplatit, abyste si ji nechali v ruce. 
        Dělí se do 5 základních typů podle barev rámování:
        """)
        
        nahraj_obrazek("karty_prehled.jpg", "Ukázka různých typů karet objevů")
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            * **🟢 Zelené karty (Odlovu):** Obsahují symboly košů (celých nebo poškozených) a bot (Rychlost). Jsou naprosto klíčové, protože bez košů nemůžete zachraňovat kočky z nabídky!
            * **🔵 Modré karty (Úkolů):** Tyto karty vám říkají, za co dostanete na konci hry bonusové body. Mohou být *Osobní* (plníte je tajně jen vy) nebo *Veřejné* (může je splnit kdokoliv u stolu a všichni o nich vědí).
            * **🟤 Hnědé karty (Oshaxů):** Umožní vám spřátelit se s Oshaxem. Karta vám dovolí vzít si velký dílek žolíkové kočky a umístit jej na loď.
            """)
        with c2:
            st.markdown("""
            * **🟡 Žluté karty (Pokladů):** Umožní vám vzít si z nabídky pod ostrovem Zlaté poklady nebo specifické kombinace měděných pokladů a naložit je na palubu.
            * **🟣 Fialové karty (Univerzální):** Tyto karty mají mocné okamžité efekty a jako jediné je můžete zahrát **kdykoliv** (např. i během tahu jiného hráče, pokud to text dovoluje).
            """)
            
        st.success("""
        **💡 TIP PRO DRAFT KARET:** Jako nováček si vždy hlídejte rovnováhu. Pokud si nakoupíte samé modré karty úkolů, sice budete mít potenciál na spoustu bodů, ale pokud vám nezbydou ryby a zelené karty s koši, nezachráníte žádnou kočku a vaše loď zůstane prázdná (což vás bude stát hromadu záporných bodů)!
        """)

# --- 2. PŘÍPRAVA HRY ---
elif sekce_menu == "Příprava hry":
    st.header("2. Jak hru nachystat na stůl")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Střed stolu")
        st.markdown("""
        1. **Ostrov:** Desku ostrova položte doprostřed. Prostor nalevo od ní je **Levá zóna**, prostor napravo je **Pravá zóna**.
        2. **Vethův člun:** Postavte na pole číslo 5 na počítadle dnů (hra se odpočítává pozpátku dolů).
        3. **Pytlík:** Do plátěného pytlíku nasypte všechny barevné kočky a zlaté poklady.
        4. **Nabídka pod ostrovem:** Volně pod ostrov vyskládejte dílky Oshaxů a hromádky měděných pokladů podle tvarů.
        """)
    with col2:
        st.subheader("Plocha hráče")
        st.markdown("""
        1. Každý si vezme **1 náhodnou loď**.
        2. Každý dostane **1 žeton trvanlivého koše** otočený zelenou stranou nahoru.
        3. Hráči si zvolí barvu, vezmou si dvě figurky – jednu dají před sebe a druhou položí na tlapky na desce ostrova (určení pořadí).
        """)
        
    st.info("💡 **TIP PRO ZAČÁTEK:** Hráč, který naposledy hladil skutečnou kočku, se stává začínajícím hráčem pro první den a jeho figurka jde na desce ostrova nejvýše!")

# --- 3. PODROBNÝ PRŮBĚH DNE A RYCHLOST ---
elif sekce_menu == "Podrobný průběh dne a Rychlost":
    st.header("3. Průběh kola a klíčová mechanika Rychlosti")
    
    st.markdown("""
    Na začátku každého dne (kola) se nejprve **doplní kočky na ostrov**. Vytáhněte z pytlíku kočky a dejte **2 kočky na hráče do levé zóny** a **2 kočky na hráče do pravé zóny** (např. ve 3 hráčích: 6 koček vlevo, 6 koček vpravo). Pokud vytáhnete zlatý poklad, dejte ho pod ostrov a táhněte náhradu.
    """)
    
    with st.expander("Fáze 1: Rybaření 🐟"):
        st.markdown("""
        Každý hráč dostane ze zásoby **20 ryb**. Ryby jsou vaše jediné platidlo. Na konci dne nepropadají, přenášejí se do dalšího kola.
        """)
        
    with st.expander("Fáze 2: Průzkum ostrova (Draft karet) 🗺️"):
        st.markdown("""
        1. Každý dostane **7 karet**. Vybere si 2, které si chce nechat, a zbylých 5 pošle sousedovi. 
        2. Z obdržených 5 karet si vybere 2, zbylé 3 pošle dál.
        3. Z obdržených 3 karet si vybere 2, zbylou 1 pošle dál.
        4. Nyní máte v ruce 7 karet. Podívejte se na ceny v levém horním rohu. Zaplaťte banku ryby za karty, které si chcete nechat. Ty, které nechcete, tajně odhoďte lícem dolů.
        
        **💡 TIP PRO NOVÁČKY:** Nemusíte si kupovat všechny karty! Pokud si koupíte moc karet, nezbydou vám ryby na samotný odchyt koček. Ideální je nechat si 3–4 karty a zbytek ryb si pošetřit.
        """)

    with st.expander("Fáze 3: Úkoly 📜"):
        st.markdown("""
        Všechny modré karty úkolů musíte vyložit teď. Osobní úkoly dejte před sebe lícem dolů, veřejné doprostřed stolu a nahlas je přečtěte.
        """)

    st.subheader("🔥 Fáze 4: Záchrana koček & Mechanika Rychlosti")
    st.markdown("""
    Tohle je nejdůležitější moment dne. Nejprve všichni hráči **tajně vyberou zelené karty odlovu**, které chtějí v tomto kole použít, a položí je lícem dolů. Poté se naráz otočí.
    
    **Jak se určuje pořadí tahů (Rychlost):**
    Každý hráč si sečte hodnoty u symbolu **boty** na svých otočených zelených kartách. Hráč s nejvyšším součtem posune svou figurku na desce ostrova na nejvyšší pozici a bude v tomto dni zachraňovat kočky jako první! V případě shody rozhoduje to, kdo byl rychlejší v předchozím dni.
    """)
    
    st.error("""
    **🚨 DŮLEŽITÉ PRAVIDLO PRO ODLOV KOČEK:**
    Hráči se střídají po jedné kočce. Ve svém tahu můžete zachránit 1 kočku:
    * Kočka z **Levé zóny** stojí **3 ryby**.
    * Kočka z **Pravé zóny** stojí **5 ryb**.
    * K odchytu musíte vyčerpat **1 koš** (otočit trvanlivý žeton, nebo zahodit kartu s jednorázovým košem, nebo zahodit dvě karty poškozených košů).
    
    **Strategický tip:** Být první v pořadí (mít vysokou rychlost) se neuvěřitelně vyplatí, pokud je v levé zóně za levné 3 ryby přesně ten dílek, který potřebujete do své rodiny. Pokud jste pomalí, ostatní vám ty nejlepší tvary vyfouknou a vám zbudou jen ty, které se vám na loď nehodí.
    """)

    with st.expander("Fáze 5: Vzácné objevy 👑"):
        st.markdown("""
        V pořadí podle rychlosti můžete zahrát hnědé karty Oshaxů nebo žluté karty pokladů a umístit tyto speciální dílky na loď.
        """)

# --- 4. PRAVIDLA SKLÁDÁNÍ ---
elif sekce_menu == "Pravidla skládání":
    st.header("4. Geometrická pravidla: Jak správně zaplnit loď")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Základní pravidla pokládání")
        st.markdown("""
        * Dílky můžete libovolně natáčet a převracet (i rubovou stranou nahoru).
        * **První dílek** můžete položit kamkoliv na loď.
        * **Každý další dílek** musí alespoň jednou stranou čtverečku sousedit s jakýmkoliv dílkem, který už na lodi leží. Dotýkat se pouze rohem nestačí!
        * Dílky nesmí přesahovat okraj lodi ani se překrývat.
        """)
    with col2:
        st.subheader("Bonusy za mapy 🗺️")
        st.markdown("""
        Na lodi máte předtištěno 5 barevných map. Pokud na políčko s mapou položíte kočku **přesně téže barvy** (např. červená kočka zakryje červenou mapu), okamžitě si vezmete z nabídky pod ostrovem **1 libovolný měděný poklad** a hned ho položíte na loď. 
        Pokud mapu zakryjete jinou barvou kočky, mapa je znehodnocena a žádný bonus nedostanete.
        """)
        
    st.success("""
    **💡 STRATEGICKÝ TIP PRO SKLÁDÁNÍ:**
    Snažte se udržet rodiny koček pohromadě (rodina = alespoň 3 sousedící dílky stejné barvy). Na začátku hry doporučujeme vybrat si 2, maximálně 3 barvy koček, které budete sbírat do velkých rodin. Pokud budete brát od každé barvy trochu, vaše rodiny budou malé, nezískáte za ně skoro žádné body a loď se vám zablokuje.
    """)

# --- 5. BODOVÁNÍ A KALKULAČKA ---
elif sekce_menu == "Bodování a kalkulačka":
    st.header("5. Závěrečné vyhodnocení skóre")
    
    st.markdown("""
    Na konci 5. dne hra končí. Vezměte si zápisník bodů a spočítejte výsledek. Pro zjednodušení můžete použít kalkulačku níže:
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("➕ Kladné body")
        rodiny_b = st.number_input("Body za kočičí rodiny (sečtěte z lodi):", min_value=0, value=0, step=1)
        with st.expander("Zobrazit bodovací tabulku rodin"):
            st.markdown("""
            (Rodina = sousedící dílky stejné barvy)
            * **3 kočky:** 8 bodů
            * **4 kočky:** 11 bodů
            * **5 koček:** 15 bodů
            * **6 koček:** 20 bodů
            * **7 koček:** 25 bodů
            * **Každá další kočka v rodině:** +5 bodů
            """)
        
        poklady_b = st.number_input("Počet naložených Zlatých pokladů:", min_value=0, value=0, step=1)
        st.caption("Každý naložený zlatý poklad vám přinese fixně **3 body**.")
        
        ukoly_b = st.number_input("Celkový zisk bodů ze všech splněných úkolů:", min_value=0, value=0, step=1)
        
    with col2:
        st.subheader("➖ Záporné body (Penalizace)")
        krysy_b = st.number_input("Počet viditelných (nezakrytých) krys:", min_value=0, value=0, step=1)
        st.caption("Za každou krysu, kterou jste na lodi nezašlapali kočkou nebo pokladem, ztrácíte **1 bod**.")
        
        sekce_b = st.number_input("Počet neúplně zaplněných sekcí (místností):", min_value=0, max_value=7, value=0, step=1)
        st.caption("Loď má 7 sekcí. Za každou místnost, kde vám zůstalo aspoň jedno volné políčko, ztrácíte **5 bodů**!")

    # Výpočet skóre
    celkove_skore = rodiny_b + (poklady_b * 3) + ukoly_b - krysy_b - (sekce_b * 5)
    
    st.divider()
    st.metric(label="🏆 VAŠE FINÁLNÍ DOSAŽENÉ SKÓRE", value=celkove_skore)
    
    if celkove_skore > 60:
        st.balloons()
