import streamlit as st

# Konfigurace stránky
st.set_page_config(page_title="Atlantis - Průvodce pro nováčky", page_icon="🌊", layout="wide")

# --- INTERAKTIVNÍ SLOVNÍČEK & STRATEGICKÉ TIPY V BOČNÍM PANELU ---
st.sidebar.header("💡 Strategické tipy pro nováčky")
st.sidebar.markdown("Rozbalte si oblast, která vás zajímá:")

with st.sidebar.expander("🥇 Vyplatí se spěchat do cíle, nebo jít postupně?"):
    st.info("""
    **Strategické doporučení:** V této hře se jednoznačně vyplatí **dostat první figurku na Pevninu co nejrychleji**! 
    
    Jakmile totiž máte v cíli alespoň jednoho svého obyvatele, váš „karetní motor“ se nastartuje a na konci každého tahu si lížete o jednu kartu navíc. Získáte tak obrovskou taktickou výhodu.
    
    **Velké varování:** Jakmile ale první figurka dorazí do cíle, nenechávejte zbylé dvě figurky trčet vzadu u Atlantidy. Pokud by se stalo, že soupeř hru náhle ukončí, vaši opozdilci by museli přeletět celou mapu plnou trhlin bez možnosti hrát karty. Cena za tyto trhliny by vás stála všechny nasbírané body.
    
    **Ideální plán:** Rychlý sprint s první figurkou do cíle pro zisk karet -> a následný postupný, bezpečný přesun zbylých dvou figurek s využitím získané převahy.
    """)

with st.sidebar.expander("Kdy postavit most? 🌉"):
    st.warning("""
    **Tip k mostům:** Každý hráč má na celou hru jen jeden jediný most. Neplýtvejte jím hned na začátku na malé trhliny!
    * Nejlepší je počkat, až se uprostřed cesty vytvoří obrovská propast (několik spojených trhlin), jejíhož překročení by vás stálo velké množství bodů. 
    * Pamatujte, že váš most mohou zdarma využívat i soupeři, takže ho stavte ideálně ve chvíli, kdy jste sami pozadu a potřebujete nutně dohnat čelo závodu.
    """)

with st.sidebar.expander("Skákání přes hlavy (Komba) 🦘"):
    st.success("""
    **Tip k pohybu:** Pokud zahrajete kartu a symbol vás pošle na políčko, kde už někdo stojí, nesmíte tam zůstat. Musíte zahrát další kartu a skočit dál!
    * **Strategie:** Tohle je nejlepší způsob, jak ušetřit karty a přesunout se obrovským skokem dopředu. Využívejte zácpy na cestě vytvořené soupeři ve svůj prospěch!
    """)

# --- HLAVNÍ OBSAH APLIKACE ---
st.title("Atlantis 🌊🏛️")
st.markdown("Interaktivní průvodce pravidly a pomocník pro bodování. Zachraňte svůj lid z potápějící se Atlantidy!")

sekce_menu = st.radio(
    "Vyberte herní kapitolu:", 
    ["1. Cíl hry a Základy", "2. Příprava hry (Sestavení trasy)", "3. Průběh tahu a Cíl", "4. Trhliny a Mosty", "5. Konec hry a Kalkulačka"], 
    horizontal=True
)

st.divider()

# --- 1. CÍL HRY A ZÁKLADY ---
if sekce_menu == "1. Cíl hry a Základy":
    st.header("1. Cíl hry a základní pojmy pro nováčky")
    
    st.subheader("🎯 Cíl hry")
    st.markdown("""
    Bájná Atlantida se potápí do oceánu! Vaším cílem je **přesunout své 3 figurky obyvatel dopředu po kartičkách cest z potápějící se Atlantidy na stabilní Pevninu**. 
    Během tohoto útěku sbíráte cenné předměty. Za vámi se ale trasa propadá do moře a tvoří se vodní trhliny. Vítězí hráč, který na konci hry nasbírá poklady a karty s nejvyšší hodnotou.
    """)
    
    st.subheader("📖 Slovníček pojmů (Co je co?)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("""
        **🟫 Kartičky cesty (Kartonové žetony / Poklady)**
        To jsou ty tlusté kartonové čtverečky, které na začátku rozložíte na stůl a které tvoří samotnou trasu. Na sobě mají číslo (body). Tyto čtverečky nikdy neberete do ruky jako karty! Figurky po nich chodí, a když z nich odejdete, získáte je jako poklad.
        """)
        st.info("""
        **🃏 Pohybové karty (Papírové karty v ruce)**
        To jsou klasické tenké papírové karty. Držíte je skrytě v ruce. Mají na sobě stejné symboly jako žetony na stole a hrajete je výhradně k tomu, abyste s figurkami mohli hýbat kupředu.
        """)
        
    with col2:
        st.error("""
        **🟦 Vodní plocha (Trhlina)**
        Když někdo z cesty sebere tlustý žeton předmětu, vznikne na stole prázdné místo. Do této díry se položí modrý čtvereček vody. Přeskočit tuto vodu při útěku stojí body!
        """)
        st.warning("""
        **🌉 Most**
        Dřevěná maketa mostu. Každý máte jen jeden na celou hru. Když ho položíte přes vodu, může přes tuto trhlinu už navždy kdokoliv přecházet úplně zadarmo.
        """)

# --- 2. PŘÍPRAVA HRY ---
elif sekce_menu == "2. Příprava hry (Sestavení trasy)":
    st.header("2. Sestavení únikové cesty")
    st.markdown("Příprava trasy vyžaduje přesný postup, aby herní zážitek správně fungoval. Postupujte bod po bodu:")
    
    st.markdown("""
    * **1. Příprava žetonů:** Roztřiďte tlusté herní čtverečky (žetony) podle písmen (A, B) na jejich zadní straně a obě hromádky zamíchejte odděleně.
    * **2. Start:** Umístěte velkou kartičku Atlantidy na okraj stolu.
    * **3. První polovina trasy (Karty A):** Začněte od Atlantidy a skládejte žetony „A“ lícem nahoru v tomto pořadí:
        * Položte **10 hromádek** (v každé hromádce jsou **2 žetony na sobě**).
        * Navžte **10 samostatných žetonů**.
        * Položte **6 hromádek** (opět po **2 žetonech na sobě**).
    * **4. První trhlina:** Hned za tyto žetony položte **1 modrou kartičku vodní plochy**.
    * **5. Druhá polovina trasy (Karty B):** Pokračujte ve stavbě žetony „B“ lícem nahoru:
        * Položte **6 hromádek** po **2 žetonech na sobě**.
        * Navžte **10 samostatných žetonů**.
        * Na závěr položte **10 hromádek** po **2 žetonech na sobě**.
    * **6. Cíl:** Na úplný konec této dlouhé řady položte velkou kartičku Pevniny.
    * **7. Voda do zásoby:** Zbývající modré kartičky vodní plochy dejte doprostřed stolu, ať jsou po ruce.
    * **8. Figurky a Mosty:** Každý hráč si postaví své **3 figurky na Atlantidu** a vezme si **1 most**. 
    * **9. Rozdání karet:** Zamíchejte tenké karty pohybu. Začínající hráč dostane **4 karty**, druhý hráč **5 karet**, třetí **6 karet** atd.
    """)

# --- 3. PRŮBĚH TAHU A CÍL ---
elif sekce_menu == "3. Průběh tahu a Cíl":
    st.header("3. Průběh jednoho tahu a dosažení Pevniny")
    
    st.subheader("🔄 Co dělá hráč ve svém tahu?")
    st.markdown("Hra běží po směru hodinových ručiček. Ve svém tahu musíte provést tyto akce v přesném pořadí:")
    
    with st.expander("Krok 1: Volba figurky a pohyb vpřed 🏃‍♂️"):
        st.markdown("""
        * Vyberte si jednu ze svých 3 figurek, která ještě není v cíli.
        * Vyložte z ruky na stůl lícem nahoru **1 pohybovou kartu**.
        * Pohněte figurkou dopředu na nejbližší žeton trasy, který ukazuje **stejný symbol** jako vaše zahraná karta.
        * Pokud je políčko volné, pohyb končí. Pokud tam už někdo stojí, musíte z ruky zahrát další kartu a skočit na další symbol, dokud nestojíte na zcela prázdném žetonu!
        """)
        
    with st.expander("Krok 2: Zisk kartičky cesty (Sběr bodů) 💰"):
        st.markdown("""
        * Jakmile vaše figurka dokončí pohyb a stojí na prázdném místě, podívejte se **přímo za ni**.
        * Vezměte si **první neobsazený žeton cesty**, který leží na trase hned za vaší figurkou, a položte si ho před sebe. To jsou vaše vítězné body! (Pokud ležely dva na sobě, berete jen ten horní).
        * Do vzniklé mezery ihned vložte modrý žeton vodní plochy – cesta se potopila a vznikla trhlina.
        """)
        
    with st.expander("Krok 3: Dobrání nových karet na konci tahu 🃏"):
        st.markdown("""
        * Všechny karty, které jste v tomto tahu vyložili, odhoďte.
        * Standardně si z balíčku doberete **1 novou kartu**. 
        * *Pozor: Pokud už ale máte nějaké figurky bezpečně v cíli na Pevnině, v tomto kroku získáte obrovskou výhodu (viz detaily níže)!*
        """)

    st.subheader("✨ Co se děje, když figurka dorazí na Pevninu (do cíle)?")
    st.markdown("""
    Dosažení Pevniny je klíčovým momentem celé hry. Jakmile vaše figurka překročí poslední žeton trasy, děje se následující:
    
    * **Jak se do cíle dostat:** Pokud zahrajete kartu se symbolem, který se již na zbývající trase vůbec nevyskytuje, vaše figurka skočí rovnou na Pevninu.
    * **Okamžitá odměna za příchod:** I za tento skok získáváte poklad! Berete si poslední volný žeton trasy, který ležel nejblíže k Pevnině.
    * **Trvalý bonus na konci každého tahu:** Toto je ta největší odměna. Za každého úspěšně zachráněného obyvatele si na konci svého tahu (v Kroku 3) lížete karty navíc:
        * 1️⃣ Máte **1 figurku** na pevnině -> doberete si **2 karty** (místo jedné).
        * 2️⃣ Máte **2 figurky** na pevnině -> doberete si **3 karty**.
        * 3️⃣ Jakmile na pevninu dorazí vaše **3. figurka**, doberete si 4 karty a **hra okamžitě končí**!
    """)

# --- 4. TRHLINY A MOSTY ---
elif sekce_menu == "4. Trhliny a Mosty":
    st.header("4. Jak funguje překonávání vody (Trhliny)")
    st.markdown("""
    Jak hráči sbírají žetony cesty, trasa se trhá a zaplavuje vodou. Pokud vaše figurka při svém pohybu musí přeletět přes modrá políčka vody, musíte za tento přechod zaplatit.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Placení mýtného za vodu 💸")
        st.markdown("""
        Velikost vodní plochy nerozhoduje. Cenu určují výhradně pevné žetony trasy na okrajích vody.
        * **Pravidlo ceny:** Podívejte se na žeton těsně před vodou a žeton těsně za vodou. **Cena přechodu se rovná té NIŽŠÍ hodnotě z těchto dvou žetonů**.
        * **Čím platit:** Platíte svými dříve získanými žetony (číslo = hodnota) nebo kartami z ruky (každá 1 karta z ruky = 1 bod).
        * Žetony a karty použité k zaplacení se trvale vyřadí do krabice. Peníze se nevracejí.
        """)
    with col2:
        st.subheader("Stavba mostu (Zdarma) 🌉")
        st.markdown("""
        * Ve svém tahu můžete na jakoukoliv trhlinu umístit svůj dřevěný žeton mostu.
        * Od této chvíle mohou tuto trhlinu využívat **všichni hráči zcela zdarma**.
        * I když se tato trhlina později rozroste (přibude další voda), přechod v místě mostu zůstává navždy bezplatný.
        """)

# --- 5. KONEC HRY A KALKULAČKA ---
elif sekce_menu == "5. Konec hry a Kalkulačka":
    st.header("5. Vyhodnocení hry a Kalkulačka bodů")
    
    st.markdown("""
    Hra končí vteřinu poté, co jeden z hráčů dostane na Pevninu svou poslední, třetí figurku. V ten moment nastává **Závěrečný přesun opozdilců**:
    
    1. Všichni ostatní hráči musí své zbylé figurky z cesty přesunout rovnou na Pevninu.
    2. V této fázi už se **nehrají žádné karty pohybu** a nikdo už nezískává žádné nové žetony pokladů z trasy.
    3. Opozdilci však **musí kompletně zaplatit cenu za všechny trhliny**, které jim stály v cestě! Platit mohou nasbíranými žetony nebo kartami z ruky. Pokud nemají čím zaplatit, zapíší si chybějící hodnotu jako **záporné body**.
    """)
    
    st.subheader("🔢 Kalkulačka pokladů")
    st.markdown("Sečtěte si své body a zjistěte, kdo se stal nejbohatším zachráncem Atlantidy:")
    
    col1, col2 = st.columns(2)
    with col1:
        body_z_zetonu = st.number_input("Sečtěte všechna čísla na vašich získaných tlustých žetonech cesty:", min_value=0, value=0, step=1)
        body_z_karet = st.number_input("Počet tenkých karet pohybu, které vám zůstaly v ruce (1 karta = 1 bod):", min_value=0, value=0, step=1)
    with col2:
        minus_body = st.number_input("Záporné body (penalizace, pokud jste na konci hry neměli čím zaplatit trhliny):", min_value=0, value=0, step=1)
        
    # Výpočet skóre
    konecne_skore = body_z_zetonu + body_z_karet - minus_body
    
    st.divider()
    st.metric(label="🏆 VAŠE CELKOVÉ DOSAŽENÉ SKÓRE", value=konecne_skore)
    st.caption("V případě remízy vítězí všichni hráči se stejným nejvyšším počtem bodů. Nevyužitý most nepřináší žádný bonus.")
    
    if konecne_skore > 40:
        st.balloons()