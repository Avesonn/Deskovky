import streamlit as st

# ==========================================
# KONFIGURACE A CSS
# ==========================================
st.set_page_config(page_title="Duše hrdiny Průvodce", page_icon="⚔️", layout="wide", initial_sidebar_state="expanded")

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
    
    with st.expander("Temná strana má velkou moc"):
        st.write("""
        * Nebojte se posouvat na stupnici Zkázy (korupce) směrem dolů! Přístup k runám Temna vám může pomoci porazit i ty nejtěžší Výzvy.
        * **Pozor na samotné dno:** Pokud ale spadnete úplně na dno stupnice Zkázy, na konci hry nebudete mít z karet Hrdinů žádné body a zablokujete si nákup temných run! Temnotu využívejte, ale s mírou.
        """)

    with st.expander("Sbírejte Příběhové ikony"):
        st.write("""
        * Body z Výzev a Vlastností jsou fajn, ale největší balík bodů se skrývá ve skládání stejných Příběhových ikon na okraji karet.
        * Pokud se vám podaří nasbírat 3, 4 nebo i více ikon stejného druhu, naskočí vám na konci hry obrovský bodový bonus. Soustřeďte se na 1-2 symboly a ty cíleně vyhledávejte.
        """)

    with st.expander("Neškudlete Zkušenosti"):
        st.write("""
        * Žetony Zkušeností (krystaly) jsou na konci hry sice za 1 bod, ale BĚHEM hry mají mnohem větší hodnotu! 
        * Utrácejte je za aktivování schopností na vašich kartách, za nákup silných Run Temna do těžkých hodů, nebo za Putování (odhození překážející karty z nabídky).
        """)

# ==========================================
# HLAVNÍ OBSAH (Záložky)
# ==========================================
st.title("⚔️ Duše hrdiny (Call to Adventure)")
st.write("Vytvořte hrdinu s epickým osudem! Přehledný průvodce pravidly a unikátním systémem házení run pro úplné nováčky.")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["🌱 O hře a Příprava", "🔄 Průběh tahu a Děje", "🔮 Škola házení run", "🏆 Bodování", "❓ Časté dotazy (FAQ) & Kooperace"])

# Záložka 1: O hře a Příprava
with tab1:
    st.markdown("### 📖 O čem hra je a co je vaším cílem?")
    st.write("Duše hrdiny je v podstatě karetní RPG, kde si každý hráč buduje svou vlastní postavu od úplné nuly (skromného původu) až po epického hrdinu (nebo padoucha). Během hry budete svou postavu vylepšovat (získávat Vlastnosti) a posílat ji do nebezpečných situací (čelit Výzvám).")
    st.markdown("""
    **Váš cíl:** Vybudovat postavu s co nejvyšším skóre Osudu (Vítěznými body). Body získáváte za překonávání výzev, sbírání stejných příběhových symbolů a plnění svého tajného životního cíle. Hra končí, jakmile někdo svou postavu kompletně 'dopíše' (získá 9 karet do svého příběhu).
    """)
    
    st.markdown("---")
    
    st.markdown("### 🛠️ Jak si hru připravit na stůl?")
    
    st.markdown("#### 1. Tvorba Hrdiny (Vaše postava)")
    st.markdown("""
    1. Každému hráči rozdejte **2 karty Původu, 2 karty Motivace a 2 karty Osudu**.
    2. Každý hráč si z těchto dvojic vybere vždy jen **jednu kartu, kterou si nechá**. Zbytek se vrátí do krabice.
    3. Vybrané karty si položte na svou desku hráče zleva doprava: 
        * **Původ (vlevo)** - Lícem nahoru (všichni to vidí)
        * **Motivace (uprostřed)** - Lícem nahoru
        * **Osud (vpravo)** - Lícem DOLŮ! (Toto je váš tajný cíl, podívat se na něj smíte jen vy).
    4. Každý hráč dostane **3 žetony Zkušeností (krystaly)** a nasadí si plastový ukazatel na prostřední (neutrální) políčko stupnice Zkázy na levém okraji své desky.
    5. Rozdejte každému 1 kartu Hrdiny (do ruky, tajně).
    """)

    st.markdown("#### 2. Příprava herního plánu (Nabídky)")
    st.markdown("""
    Rozdělte karty příběhu na 3 hromádky podle římských číslic vzadu (Děj I, Děj II, Děj III). Do těchto balíčků rovnou zamíchejte i karty Spojenců a Protivníků. Z každého balíčku vyložte pod sebe řadu karet (4 karty pro 2-3 hráče, 5 karet pro 4 hráče).
    """)
    st.warning("""
    **DŮLEŽITÉ PRAVIDLO PRO OTOČENÍ KARET:**
    * **První řada (Děj I):** Tyto karty otočte lícem nahoru.
    * **Druhá řada (Děj II) a Třetí řada (Děj III):** Tyto karty nechte zatím ležet **LÍCEM DOLŮ (skryté)**. Hrdinové na začátku své cesty ještě nemohou řešit pokročilé úkoly!
    """)
    st.info("💡 **Hra je připravena!** Začíná hráč, který jako poslední dočetl nějakou knihu nebo román.")

# Záložka 2: Průběh tahu a Děje
with tab2:
    st.markdown("### 🔄 Co děláte ve svém tahu?")
    st.write("Když jste na řadě, máte před sebou jedno hlavní rozhodnutí: Získáte **Vlastnost**, nebo budete čelit **Výzvě**? (Vybírat můžete vždy JEN z těch karet na stole, které jsou otočené lícem nahoru).")
    
    st.markdown("---")

    st.markdown("#### MOŽNOST A: Získání Vlastnosti (Bez házení)")
    st.write("Některé karty v nabídce nemají u sebe žádné číslo obtížnosti ani dvě cesty. To jsou Vlastnosti. Neháže se na ně!")
    st.markdown("""
    * Pokud chcete Vlastnost získat, musíte **splnit její podmínky** (většinou mít u sebe už určité runy nebo ikony příběhu).
    * Pokud podmínku splňujete, prostě si kartu vezmete a zasunete si ji pod svou aktuální kartu postavy (V Ději I se zasouvá pod Původ). Zasunete ji tak, aby horní okraj karty (s bonusy a ikonami) koukal ven a obohatil vašeho hrdinu.
    """)

    st.markdown("#### MOŽNOST B: Čelení Výzvě (Házení runami)")
    st.write("Výzvy jsou karty s číslem obtížnosti vlevo uprostřed. Dávají vám vždy na výběr ze **dvou Cest** (horní a dolní text).")
    st.markdown("""
    1. **Vyberte si cestu:** Řekněte, jestli se pokoušíte o horní, nebo dolní cestu Výzvy.
    2. **Zkontrolujte obtížnost:** Číslo vlevo je základní obtížnost. *(Pokud je u vaší vybrané cesty navíc malá lebka, obtížnost se zvyšuje o +1).*
    3. **Hoďte runami:** Použijte základní runy, přidejte své vlastnosti, případně dokupte runy Temna a hoďte.
    4. **Výsledek:**
        * **Úspěch (hodil jsem stejně nebo víc):** Výzvu jste překonali! Zasuňte si kartu pod postavu tak, aby koukala ven jen ta polovina cesty, kterou jste zvládli.
        * **Neúspěch (hodil jsem méně):** Výzvu zahodíte úplně pryč ze hry. Jako bolestné ale získáte **1 žeton Zkušenosti (krystal)**.
    """)

    st.markdown("---")
    
    st.markdown("### ⚠️ Speciální karty na stole (Spojenci a Protivníci)")
    st.write("Když na konci tahu doplňujete prázdná místa na stole z balíčku, mohou se objevit tyto zvláštní karty. Nehrají se jako běžné Výzvy!")
    
    colA, colB = st.columns(2)
    with colA:
        st.info("""
        **🤝 Spojenci (Pomocníci)**
        * *Nachází se v:* Děj I a Děj II.
        * **Kam s ním na stole:** Jakmile se Spojenec otočí, hráč na tahu ho musí rovnou vzít a **zasunout pod libovolnou kartu Výzvy**, která zrovna leží na stole! Výzva tím získá parťáka.
        * **Co to dělá:** Tato Výzva se tím stává těžší (získá symbol lebky = obtížnost +1).
        * **Jak ho získat:** Kdo tuto vylepšenou Výzvu porazí, získá Výzvu a k ní jako odměnu i tohoto Spojence.
        * **Kam se dává po zisku:** Získaného Spojence nezasouváte do příběhu! **Položíte si ho vedle své desky**. Poskytuje vám schopnost, kterou můžete kdykoliv využívat (často za odhození karty nebo zaplacení krystalu).
        """)
        
    with colB:
        st.error("""
        **👹 Protivníci (Nepřátelé)**
        * *Nachází se v:* Děj II a Děj III.
        * **Kam s ním na stole:** Zůstává ležet normálně v řadě jako běžná karta.
        * **Co to dělá:** Je to speciální Výzva, která má jen jednu cestu (porazit ho). Hlavně ale **okamžitě začne škodit VŠEM hráčům u stolu**. Má na sobě text, který platí po celou dobu, dokud Protivník leží v nabídce!
        * **Jak ho získat:** Musíte na něj zaútočit runami úplně stejně jako na běžnou Výzvu.
        * **Kam se dává po zisku:** Když ho porazíte, přestane všem škodit. Kartu si **zasunete pod svou postavu** jako jakoukoliv běžnou Výzvu (získáte z něj ikony a body do příběhu).
        """)

    st.markdown("---")

    st.markdown("#### Doplňkové akce v tahu")
    st.markdown("""
    * **Putování (Max. JEDNOU za tah):** Zaplaťte 1 krystal, vyhoďte 1 libovolnou kartu z nabídky na stole úplně pryč a nahraďte ji novou ze stejného balíčku.
    * **Zahrání karty Hrdiny/Antihrdiny:** Zahrání je zdarma. Vždy zkontrolujte na kartě, KDY přesně se smí zahrát (některé jen před hodem, některé po hodu).
    * **Využití schopnosti:** Můžete využít textové schopnosti, které už máte na svých získaných kartách nebo na vyložených Spojencích.
    """)

    st.markdown("#### ⏳ Odemčení dalších Dějů (Kdy se otáčí skryté karty?)")
    st.write("Vaše postava se vyvíjí a nemůže věčně zůstat v prvním aktu.")
    st.success("""
    * **Otočení Děje II:** Jakmile první hráč u stolu nasbírá svou celkově 3. kartu a zasune ji pod svůj Původ, **okamžitě se otočí celá řada karet Děj II lícem nahoru**. Od této chvíle si z ní mohou brát i ostatní hráči. Stejně se pak odemyká i Děj III.
    * **Zákaz braní z minulosti:** Jakmile VY OSOBNĚ získáte 3 karty v Ději I, vaše první kapitola je uzavřena. **Od této chvíle už si NESMÍTE brát žádné další karty z Děje I.** Vaše další karty už musíte brát z Děje II a zasouvat je pod Motivaci.
    * **Úklid stolu:** Jakmile mají všichni hráči u stolu hotový Děj I (všichni v něm mají 3 karty), zbylé karty Děje I se z nabídky vyhodí pryč, aby nepřekážely.
    """)

# Záložka 3: Runy
with tab3:
    st.markdown("### 🔮 Škola házení run (Jak se to počítá?)")
    st.write("Ve hře Duše hrdiny se neháže kostkami, vrháte oboustranné plastové destičky – runy. Naučit se, jaké runy si smíte vzít do ruky, je to nejdůležitější pravidlo celé hry.")

    st.markdown("#### Krok 1: Jaké runy si mohu vzít do ruky?")
    st.markdown("""
    Při pokusu o jakoukoliv Výzvu si ruku plníte postupně ze 3 různých zdrojů:
    
    1. **Runy Záře (Základní 3 runy):** Tyto tři základní (světlé) runy berete do ruky **VŽDY A ÚPLNĚ PŘI KAŽDÉ VÝZVĚ**. Tvoří váš základní hod.
    2. **Runy Vlastností (Podle vašich schopností):** Podívejte se na kartu Výzvy. Pod číslem obtížnosti jsou nakreslené symboly vlastností (např. Síla, Charisma), které vám v této výzvě pomohou. Za každou tuto ikonu, kterou už máte u sebe dříve nasbíranou na kartách, si smíte vzít **1 příslušnou barevnou runu** (max. 3 od jednoho druhu).
    3. **Runy Temna (Za krystaly):** Až 3x za tah můžete zaplatit **1 žeton Zkušenosti (krystal)** a přidat si do ruky 1 tmavou runu Temna.
    """)
    
    st.error("""
    **⛔ STOPKA PRO PŘÍLIŠNÉ ZLO:** pokud váš plastový ukazatel na stupnici Zkázy klesne na úplně nejnižší možnou pozici (překročili jste hranici hanebnosti a propadli čistému zlu), **již NESMÍTE utrácet krystaly zkušeností za nákup run Temna!** Vaše možnost povolávat temné síly je dočasně zablokována, dokud se pomocí nějaké Ctnosti neposunete na stupnici o úroveň výše.
    """)

    st.markdown("---")

    st.markdown("#### Krok 2: Výsledky na runách (Co může padnout?)")
    st.write("Vezměte všechny nasbírané runy a hoďte je na stůl. Strana s prázdným kolečkem nebo čistá strana neznamená nic (0 bodů). Počítáte úspěchy z lícových stran:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**⚪ Runy Záře (Základní)**")
        st.markdown("""
        * **1 zásek (trojúhelník):** Hodnota **+1 bod** do hodu.
        * **Prázdná strana:** Hodnota **0 bodů**.
        * **Symbol Slunce ☀️ nebo Měsíce 🌙:** Hodnota **0 bodů**, ale okamžitě si berete z banky **1 žeton Zkušenosti (krystal)**! *(Pozor: tyto základní runy vás nikam neposouvají po stupnici dobra a zla, slouží jen jako zdroj krystalů).*
        """)

    with col2:
        st.markdown("**⚫ Runy Temna**")
        st.markdown("""
        * **1 bod:** Hodnota **+1 bod** do hodu.
        * **2 body + posun dolů:** Hodnota **+2 body** do hodu, ALE musíte okamžitě posunout svůj ukazatel na stupnici Zkázy **o jeden stupeň níže směrem ke zlu**!
        """)

    with col3:
        st.markdown("**🟠 Runy Vlastností (Barevné)**")
        st.markdown("""
        * **Standardní runy (1. a 2. v sadě):** Dávají do hodu buď **+1 bod**, nebo **+2 body** (podle počtu puntíků/symbolů).
        * **Třetí (Speciální) runa v sadě:** Pokud máte 3 ikony stejné vlastnosti, házíte touto speciální runou. Ta dává buď **+2 body**, nebo **0 bodů + speciální bonus** podle typu vlastnosti.
        * *Příklad (Oranžová Síla):* Padne buď **+2 k síle**, nebo **0 k síle, ale získáte žeton Zkušenosti (krystal)**. U Inteligence/Moudrosti by to byla karta Hrdiny, u Obratnosti/Charismatu karta Antihrdiny.
        """)

# Záložka 4: Bodování
with tab4:
    st.markdown("### 🏆 Ukončení hry a Vyhlášení vítěze")
    st.write("Hra spěje ke konci, jakmile nějaký hráč vloží 3. kartu příběhu pod svou kartu Osudu (Tím úspěšně odehrál i Děj III a jeho příběh je dopsán). Ostatní hrají poslední tah. Pak se odhalí skryté karty Osudu.")

    st.markdown("#### Jak si spočítat výsledný OSUD (Skóre):")
    st.markdown("""
    Své body získáte součtem z mnoha různých míst. Postupujte popořadě:
    
    1. **Triumf a Tragédie z karet:** Sečtěte všechny ikonky zlatých sluncí (Triumf) a fialových měsíců (Tragédie) úplně na VŠECH vašich kartách v příběhu. Každá ikonka je 1 bod.
    2. **Karty Hrdinů a Antihrdinů:** Všechny karty s těmito efekty, které jste během hry zahráli (leží vedle vás), vám přidají přesně **+1 bod** bez ohledu na vaši aktuální pozici na stupnici Zkázy.
    3. **Krystaly:** Každý váš neutracený žeton Zkušenosti má hodnotu **+1 bod**.
    4. **Stupnice Zkázy:** Podívejte se, kde leží váš ukazatel. Přičtěte body Triumfu nebo Tragédie z tohoto jednoho konkrétního políčka, kde stojíte (body se nesčítají!). Pokud jste na úplném černém dnu, váš modifikátor z tohoto políčka je 0 bodů.
    5. **Tajná karta Osudu:** Nyní si spočítejte body za splnění podmínek ze své skryté karty Osudu na základě požadavků, které jste splnili.
    6. **Sady Příběhových ikon:** Sečtěte si, kolikrát se daná ikona na okrajích vašich karet opakuje (Božství, Spravedlnost, Příroda, Elixír, Majestát, Podlost):
        * 1 ikona stejného druhu = 0 bodů
        * 2 ikony stejného druhu = **2 body**
        * 3 ikony = **4 body**
        * 4 ikony = **8 bodů**
    """)
    st.info("Hráč s nejvyšším skóre vyhrává. Na úplný závěr každý hráč ostatním vypráví příběh svého hrdiny přesně podle karet, jak je za sebou získal!")

# Záložka 5: FAQ a Kooperace
with tab5:
    st.markdown("### ❓ Často kladené otázky (FAQ)")
    
    with st.expander("Když získám runu Vlastnosti, bráním jinému hráči v jejím použití?"):
        st.write("**Ne.** Všechny runové kameny v krabici jsou sdílené. Ikony na vašich kartách vám pouze dávají povolení si danou runu z hromádky vzít, když zrovna házíte vy. Po hodu ji vrátíte zpět ostatním.")

    with st.expander("Mohu mít na kartách více než tři ikony run od jedné Vlastnosti?"):
        st.write("**Ano.** Do ruky pro jeden hod si sice můžete vzít maximálně 3 runy dané vlastnosti, ale jakékoliv další ikony navíc se vám skvěle počítají na konci hry do úkolů z vaší karty Osudu.")

    with st.expander("Kdy přesně mohu hrát karty Hrdinů a Antihrdinů během Výzvy?"):
        st.write("""
        Vždy sledujte text na kartě:
        * **„Before you attempt a challenge“ (Před pokusem):** Musíte kartu zahrát ještě předtím, než vezmete runy do ruky a hodíte.
        * **„As you are facing a challenge“ (Když čelíte):** Můžete kartu zahrát až POTÉ, co jste runy hodili na stůl. Můžete tak zachránit nepodařený hod ještě před jeho vyhodnocením.
        """)

    with st.expander("Když se pokouším o Výzvu, mohu přidat pouze runy uvedené na Cestě, kterou jsem si zvolil?"):
        st.write("**Ne.** Přidáváte runy vlastností, které jsou vyobrazené na levé straně karty Výzvy (hned pod obtížností). Tyto vlastnosti platí pro obě cesty společně.")

    with st.expander("Pokud mi během Výzvy padne na runě symbol pro líznutí karty, kdy si ji beru?"):
        st.write("Okamžitě. Pokud si takto líznete kartu s textem „As you are facing a challenge“, můžete ji dokonce rovnou v tomto rozdělaném hodu zahrát a zachránit se.")

    with st.expander("Když mě karta přiměje zopakovat Výzvu, musím znovu platit za runy Temna?"):
        st.write("**Ne.** Všechny runy Temna, které jste si pro tento pokus už jednou koupili, vám zůstávají v ruce i pro druhý opravný hod. Dokonce můžete dokoupit další runy Temna (pokud jste ještě nedosáhli limitu 3 nebo dnea stupnice).")

    with st.expander("Mohu skočit do vyššího Děje, i když nemám dokončený ten předchozí?"):
        st.write("**Ano, ale má to háček.** Pokud jiný hráč už odemkl Děj II, vy se můžete pokusit získat kartu z Děje II, i když máte v Ději I teprve dvě karty. Tuto kartu si ale musíte zasunout **pod svůj Původ (Děj I)**, nikoliv pod Motivaci! Riskujete navíc, že karty z vyšších Dějů jsou výrazně obtížnější.")

    st.markdown("---")
    st.markdown("### 🤝 Kooperativní režim")
    st.write("Můžete spojit síly a jako skupina hrdinů porazit jednoho mocného Protivníka (Adversary).")
    st.markdown("""
    * **Příprava:** Na začátku hry vyberete jednu kartu hlavního Protivníka a položíte ho doprostřed stolu. Vedle něj připravíte jeho speciální balíček záškodnických karet Antihrdinů.
    * **Útoky hry:** Kdykoliv kdokoliv ve hře vrhne základní runy Záře a padne mu symbol pro líznutí karty, NEBERE si kartu pro sebe, ale okamžitě otočí vrchní kartu z balíčku Protivníka, která týmu uškodí.
    * **Pomoc přátelům:** Vaše karty Hrdinů a Antihrdinů, které normálně cílí na 'vás', můžete v tomto režimu hrát ve prospěch jakéhokoliv jiného hráče u stolu.
    * **Závěrečná bitva:** Do posledního kola se nesmíte o Výzvu Protivníka pokusit. Jakmile kterýkoliv hráč získá celkově 8 karet do svého příběhu, spustí se poslední kolo. V něm musí všichni hráči povinně zaútočit přímo na kartu Protivníka a překonat jeho obří obtížnost. Pokud ho porazíte, vyhráváte všichni společně!
    """)