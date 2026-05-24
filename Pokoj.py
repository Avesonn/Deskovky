import streamlit as st

# ==========================================
# KONFIGURACE A CSS
# ==========================================
st.set_page_config(page_title="Pokojovky Průvodce", page_icon="🌿", layout="wide", initial_sidebar_state="expanded")

css_finta = """
<style>
.block-container {
    max-width: 95rem !important;
    padding-top: 2rem !important;
}
.stDeployButton {display: none !important;}
footer {display: none !important;}
</style>
"""
st.markdown(css_finta, unsafe_allow_html=True)

# ==========================================
# BOČNÍ PANEL S TIPY
# ==========================================
with st.sidebar:
    st.subheader("💡 STRATEGICKÉ TIPY")
    
    with st.expander("Šachovnice a barvy jsou klíč"):
        st.write("""
        * **Květiny neskórují všechno:** Mnoho nováčků se soustředí jen na to, aby vypěstovali co nejvíc rostlin. Přitom obrovské množství bodů leží v Místnostech.
        * **Slaďte to:** Snažte se, aby místnost sousedila s rostlinami **stejné barvy**. Pokud máte oranžovou místnost, obklopte ji oranžovými rostlinami a dovnitř dejte oranžové vybavení (třeba oranžovou kočku). To vám na konci přinese ohromný bodový bonus.
        """)

    with st.expander("Světlo je zadarmo, neplýtvejte tahy"):
        st.write("""
        * Přikládat karty k sobě tak, aby na sebe navazovaly světelné podmínky (sluníčko na sluníčko, stín na stín), je nejrychlejší způsob, jak rostliny vypěstovat.
        * Snažte se nevyužívat žetony nářadí a péče, pokud to není absolutně nutné. Světlo z místností vám dává lístečky "automaticky" a zadarmo při každém přiložení.
        """)

    with st.expander("Šetřete si Palce (Zelené žetony)"):
        st.write("""
        * Palce jsou ve hře neuvěřitelně silná měna, která vám dovoluje ohýbat pravidla. Můžete jich mít maximálně 5.
        * **Nekupujte za ně hlouposti:** Neutrácejte 2 palce za to, abyste dali rostlině 1 lísteček, pokud vám nechybí do jejího dokončení v tomto kole.
        * **Nejlepší využití palců:** Použijte 2 palce k tomu, abyste si z nabídky vzali **kartu a žeton z RŮZNÝCH sloupečků**. Tím vyfouknete soupeři přesně to vybavení, které on potřebuje, a zároveň si vezmete květinu, která se hodí vám.
        """)
        
    with st.expander("Závod o květináče"):
        st.write("""
        * Ve hře jsou dva druhy květináčů. Ty obyčejné (dřevěné) nedávají žádné extra body. Ale ty barevné z nabídky vám dají vítězné body (až 3 body za jeden)!
        * Kdo dřív dokončí rostlinu, ten si vybírá z nabídky květináčů s vyšší hodnotou. Snažte se proto alespoň jednu ze svých počátečních rostlin vypěstovat co nejrychleji, ať získáte 3 body zdarma dřív než soupeř.
        """)

# ==========================================
# HLAVNÍ OBSAH (Záložky)
# ==========================================
st.title("🌿 Pokojovky (Verdant) – Pravidla")
st.write("Vytvořte ten nejútulnější domov plný zeleně, zvířátek a hezkého nábytku. Průvodce hrou vás naučí vše od přípravy až po závěrečné počítání bodů.")

tab1, tab2, tab3, tab4 = st.tabs(["🌱 O hře a Co je v krabici", "📦 Příprava hry", "🔄 Jak se hraje", "🏆 Bodování"])

# Záložka 1: O hře a komponenty
with tab1:
    st.markdown("### 🏡 O čem to vlastně je?")
    st.write("Pokojovky jsou pohodová, ale překvapivě chytrá karetní hra (puzzle). Představte si, že jste se právě nastěhovali do nového prázdného bytu. Vaším úkolem je poskládat si před sebou na stole mřížku karet (pokoje a rostliny) tak, abyste vytvořili dokonalý a harmonický domov. Rostlinám musíte zajistit správné světlo z místností a do prázdných pokojů pořídit hezký nábytek nebo domácí mazlíčky.")
    
    st.markdown("---")
    
    st.markdown("### 🔎 Co najdete v krabici a k čemu to slouží?")
    
    st.markdown("#### 🃏 Karty")
    st.markdown("""
    * **Karty Místností (Pokoje):** Mají určitou barvu a na svých čtyřech stranách mají symboly světla (přímé slunce, polostín, úplný stín). Na každou kartu místnosti se vejde přesně jeden žeton vybavení.
    * **Karty Rostlin (Květiny):** Také mají určitou barvu. V levém horním rohu mají napsáno, jaké přesně potřebují světlo, aby rostly. A v pravém horním rohu (v kroužku) je číslo, které říká, kolik zelených lístečků musíte nasbírat, aby rostlina vyrostla do plné krásy.
    * **Karty Úkolů (Pro pokročilé):** Dávají speciální podmínky pro extra body na konci hry (při prvních hrách je můžete úplně ignorovat).
    """)

    st.markdown("#### 🏺 Květináče (Cílová páska pro rostliny)")
    st.info("Květináč je znakem vašeho úspěchu. Jakmile nasbíráte na rostlině dostatek lístečků (podle čísla v kroužku), rostlina je 'vypěstovaná'. V tu chvíli z ní všechny lístečky sundáte a jako pečeť na ni položíte Květináč.")
    st.markdown("""
    V krabici jsou dva druhy květináčů:
    * **Barevné (Bodované):** Tyto květináče na sobě mají čísla (např. 3, 2, 1) a dávají vám body na konci hry. Před hrou se vyskládají od největšího čísla po nejmenší do společné nabídky. Hráč, který jako první ve hře vypěstuje rostlinu, shrábne ten nejcennější za 3 body!
    * **Obyčejné (Dřevěné barvy):** Těch je hromada a mají hodnotu 0 bodů. Dostanete je ve chvíli, kdy už jste byli moc pomalí a barevné květináče si rozebrali soupeři. Rostlinu s nimi sice dokončíte, ale bodový bonus už nezískáte.
    """)

    st.markdown("#### 🧸 Žetony Vybavení a Péče")
    st.markdown("""
    * **Žetony Vybavení (Nábytek a zvířata):** Tažením ze zeleného pytlíku získáte celkem 9 různých druhů vybavení (např. pes, kočka, **papoušek**, akvárium, gauč, stůl, křeslo, lampa, police). 
        * ⚠️ *Pozor: Žádné zvíře (ani papoušek či pes) nemá žádnou tajnou schopnost! Všechny tyto žetony fungují úplně stejně a umisťujete je do Místností jen proto, abyste na konci hry získali body za shodu barev a za co největší sbírku různých předmětů v bytě.*
    * **Žetony Péče (Konvička, Lopatka, Hnojivo):** Tyto žetony NEJSOU vybavení a nedávají se do pokojů. Jakmile si je vezmete, hned je jednorázově použijete k tomu, abyste na své kytky přidali další lístečky, a pak žeton vyhodíte do krabice.
    * **Dřevěné lístečky:** Znamenají růst rostliny. Pokládáte je přímo na karty květin.
    * **Žetony Palců (Zelené palce):** Univerzální platidlo. Slouží k ohýbání pravidel (viz záložka Jak se hraje). Můžete jich mít maximálně 5.
    """)

# Záložka 2: Příprava hry
with tab2:
    st.markdown("### 🛠️ Jak si hru připravit na stůl?")
    st.write("Příprava Pokojovek je rychlá a jednoduchá. Každý hráč si buduje svůj vlastní byt, ale nakupuje ze společného trhu uprostřed stolu.")
    
    st.markdown("""
    1. **Do začátku pro hráče:** Každý hráč dostane náhodně **1 kartu Místnosti** a **1 kartu Rostliny**. Tyto dvě karty položí před sebe na stůl tak, aby se dotýkaly jednou ze svých stran (nikoliv jen rohem). Tím zakládají svůj domov.
    2. **Rozdělení Palců (Zelených žetonů):** * Hráč, který začíná, nedostane nic. 
        * Všichni ostatní hráči (až na posledního) dostanou 1 žeton palce. 
        * Úplně poslední hráč v pořadí dostane do začátku rovnou 2 žetony palců.
    3. **Společná nabídka (Trh):** Uprostřed stolu vytvořte 4 sloupečky vedle sebe. Každý sloupeček se skládá z:
        * 1 karty Místnosti (nahoře)
        * 1 žetonu vybavení/péče (uprostřed mezi kartami)
        * 1 karty Rostliny (dole)
    4. **Zásoby:** Žetony vybavení tahejte ze zeleného pytlíku. Vedle plánu připravte zásobu lístečků, žetonů palců a **všechny květináče** (ty barevné/bodované vyskládejte podle hodnoty do hromádek, ty obyčejné dejte bokem).
    5. **Kdo začíná?** Hru začíná ten hráč, jehož startovní rostlina má **nejvyšší číslo náročnosti** (číslo v kroužku nahoře na kartě, které určuje, kolik lístečků potřebuje k dokončení).
    """)

# Záložka 3: Průběh tahu
with tab3:
    st.markdown("### 🧩 Pravidlo Šachovnice (Zásadní věc)")
    st.warning("Celá hra se točí kolem mřížky **5 sloupců a 3 řad** (celkem 15 karet před každým hráčem). Při přikládání karet musíte dodržovat **Šachovnicový vzor**: Květina se smí dotýkat pouze Místností. Místnost se smí dotýkat pouze Květin. Dvě stejné karty nesmí nikdy ležet přímo vedle sebe (ani nad sebou).")
    
    st.markdown("---")
    
    st.markdown("### 🔄 Co přesně děláte ve svém tahu?")
    st.write("Až na vás přijde řada, provedete postupně tyto kroky:")
    
    st.markdown("#### 1. Výběr ze společné nabídky")
    st.markdown("""
    Vyberete si JEDEN ze čtyř sloupečků uprostřed stolu. Z tohoto jednoho sloupečku si vezmete **Žeton vybavení/péče** (ten uprostřed) a k němu si vyberete **buď kartu Místnosti, NEBO kartu Rostliny**. Zbylá karta ve sloupečku zůstává ležet. *(Pokud byly na kartě, kterou jste si vzali, nějaké žetony palců, berete si je samozřejmě také).*
    """)

    st.markdown("#### 2. Umístění Karty a Vybavení")
    st.markdown("""
    * **Kartu** okamžitě přiložíte do své mřížky před sebou. Karta se musí dotýkat alespoň jednou stranou už ležících karet a musí dodržet šachovnicový vzor.
    * **Žeton vybavení** (zvířátko, nábytek) musíte položit na jakoukoliv svou Místnost, na které ještě žádný žeton neleží. Místnost pojme jen 1 věc! Pokud žeton nechcete nebo nemůžete umístit, můžete si POUZE JEDEN takový žeton schovat do svého "skladu" (na malou kartičku u sebe) a umístit ho do bytu jindy.
    * **Žeton péče** (hrabičky, konvička) si neschováváte! Okamžitě ho použijete k přidání lístečků na své květiny a hned ho vyhodíte do krabice.
    """)

    st.markdown("#### 3. Zisk lístečků (Zalévání světlem)")
    st.markdown("""
    Získávání lístečků je jádro hry. Jakmile novou kartu přiložíte, podívejte se, jak na sebe navazují světelné symboly na spojnici Místnosti a Rostliny. 
    Pokud symbol na straně Místnosti (slunce/polostín/stín) přesně odpovídá tomu, co Rostlina požaduje ve svém levém horním rohu, získává tato rostlina ihned **1 zelený lísteček**. *(Pokud kartu přiložíte tak chytře, že navazuje na dvě správné strany zároveň, dostane rostlina lístečky dva).*
    """)

    st.markdown("#### 4. Vypěstování Květiny (Předání květináče)")
    st.markdown("""
    Jakmile se vám podaří na rostlinu nasbírat tolik lístečků, jaké je její číslo náročnosti, je hotová!
    1. Všechny lístečky z ní sundejte a vraťte do banky.
    2. Vezměte si z nabídky **bodovaný květináč** s tou aktuálně nejvyšší možnou hodnotou (pokud už barevné došly, vezměte si obyčejný dřevěný) a položte ho na kartu. Tato rostlina už vám do konce hry ze světla nepřinese další lístečky, je totiž v květináči kompletně hotová.
    """)
    
    st.markdown("---")

    st.markdown("### 👍 Jak využít Palce (Speciální akce)")
    st.info("Kdykoliv BĚHEM svého tahu můžete zaplatit 2 zelené žetony palců bance a provést jednu z těchto speciálních akcí (Můžete jich udělat i víc, pokud máte dost palců. Na konci tahu můžete v ruce držet maximálně 5 palců):")
    st.markdown("""
    * **Zalévání:** Přidáte 1 lísteček na libovolnou svou nedokončenou květinu.
    * **Úklid žetonů:** Vyhodíte z nabídky uprostřed stolu libovolný počet žetonů vybavení a vytáhnete z pytlíku nové.
    * **Úklid karet:** Vyhodíte z nabídky libovolný počet karet Místností nebo Rostlin (smíte vyhodit pouze ty, na kterých neleží žádný palec) a nahradíte je novými z balíčku.
    * **Krádež napříč sloupci:** Obejmutí pravidel! Nemusíte si brát kartu a žeton ze stejného sloupce. Můžete si vzít vybavení z jednoho sloupce a kartu z úplně jiného.
    """)

    st.markdown("#### 5. Konec tahu a doplnění nabídky")
    st.markdown("""
    Na tu jedinou kartu, která po vás ve sloupci osamocena zbyla, **položíte 1 žeton palce z banky**. Tím ji zatraktivníte pro další hráče. Z balíčků a pytlíku pak doplníte chybějící kartu a žeton, aby byly všechny sloupce pro dalšího hráče opět kompletní. Hraje další hráč po levici.
    """)

# Záložka 4: Bodování
with tab4:
    st.markdown("### 🏆 Jak hra končí a za co se boduje?")
    st.write("Hra okamžitě končí v momentě, kdy všichni hráči odehrají svůj 13. tah. Tou dobou má naprosto každý hráč před sebou dokonalou mřížku o velikosti 3x5 (protože 2 karty jste měli na začátku + 13 tahů = 15 karet).")
    
    st.markdown("Vezměte si bodovací bloček, který je v krabici, a postupně si sečtěte body za těchto 6 kategorií:")
    
    st.markdown("""
    1. **Vypěstované rostliny:** Sečtěte velké číslo v listu na všech svých rostlinách, na kterých leží Květináč.
    2. **Lístečky z nedokončených rostlin:** Podívejte se na kytky, které nemají květináč a nepodařilo se je vypěstovat. Každé 2 lístečky na těchto kytkách znamenají 1 Vítězný bod (půlky se zaokrouhlují dolů).
    3. **Hodnota květináčů:** Sečtěte vítězné body, které jsou natištěné na vašich získaných květináčích. (Obyčejné dřevěné jsou za 0).
    4. **Vybavení a zvířátka (Různorodost):** Podívejte se na žetony ve svých místnostech. Čím více RŮZNÝCH druhů vybavení (kočka, pes, papoušek, křeslo...) máte, tím více bodů dostanete. Pokud máte jen 1 druh = 1 bod. Pokud se vám podařilo do bytu propašovat všech 9 různých druhů = masivních 25 bodů!
    5. **Shoda barev (Květina + Místnost):** Toto je největší zdroj bodů, na který se zapomíná! Projděte každou svou místnost a podívejte se na její barvu. Získáte **1 bod za KAŽDOU rostlinu stejné barvy**, která s touto místností přímo sousedí.
        * *Bonus:* Pokud je navíc v této místnosti položený žeton vybavení, který má TAKÉ stejnou barvu jako místnost, hodnota se zdvojnásobí – získáte **2 body za každou takovou sousedící rostlinu**!
    6. **Sbírka všech barev (Bonus za set):** Pokud se vám podařilo mít ve svém bytě alespoň 1 Květinu od každé z 5 barev, získáte bonus 3 body. To samé platí pro Místnosti – pokud máte 5 místností různých barev, získáte další bonus 3 body.
    """)