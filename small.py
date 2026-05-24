import streamlit as st

# ==========================================
# KONFIGURACE A CSS
# ==========================================
st.set_page_config(page_title="Small World Encyklopedie", page_icon="🌍", layout="wide", initial_sidebar_state="expanded")

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
# DATABÁZE RAS (CZ / EN)
# ==========================================
rasy = {
    "Amazonky / Amazons (+6)": "Začínáte s +4 žetony (celkem 10). Tyto 4 žetony navíc můžete použít POUZE pro útok, nikoliv pro obranu. Na konci vašeho tahu, při přeskupování vojsk, musíte 4 žetony z mapy stáhnout a vzít si je zpět do ruky (v každém regionu musíte nechat aspoň 1 žeton, pokud to jde).",
    "Barbaři / Barbarians (+9)": "Na konci svého tahu vůbec nesmíte přeskupovat vojska (ani přesouvat žetony z jednoho dobytého území na druhé). Pokud navíc selže váš poslední pokus o útok pomocí hodu kostkou, nepoužité žetony vám zůstanou v ruce a jsou mimo hru až do začátku vašeho dalšího tahu.",
    "Bílé paní / White Ladies (+2)": "Jakmile odejdou do úpadku, stanou se zcela imunními vůči naprosto všem útokům a speciálním schopnostem soupeřů. Nikdo už jim území nevezme.",
    "Cikánky / Gypsies (+6)": "Do každého území, které se rozhodnete opustit (vezmete z něj všechny své vojáky), položíte 1 minci ze společné banky. Toto území už v tomto tahu nesmíte dobýt zpět. Na konci vašeho tahu si všechny tyto mince vezmete rovnou k sobě do zásoby.",
    "Elfové / Elves (+11)": "Jsou nesmrtelní. Když soupeř dobude jakékoliv vaše území, nevracíte 1 žeton do krabice (jak je běžné). Místo toho si vezmete VŠECHNY žetony z dobytého území bezpečně do ruky pro pozdější nasazení.",
    "Ghůlové / Ghouls (+10)": "Při odchodu do úpadku vám na mapě zůstanou VŠECHNY žetony (nestahujete je na jeden). A co víc, i v úpadku s nimi můžete v každém tahu normálně útočit a dobývat další území! Tento útok probíhá na začátku tahu, ještě před tahem vaší nové aktivní rasy. S Ghůly můžete dokonce zaútočit i na svou vlastní aktivní rasu.",
    "Goblini / Goblins (+6)": "Při dobývání jakéhokoliv území, na kterém leží cizí rasa v úpadku, potřebujete k úspěchu o 1 žeton méně (vždy ale musíte použít minimálně 1 žeton).",
    "Hobiti / Halflings (+11)": "Mohou na mapu poprvé vstoupit naprosto kdekoliv (nemusí začínat na okraji mapy ani na pobřeží). Na první 2 území, která dobudou, umístí Hobití nory. Tato dvě území jsou pak absolutně imunní vůči dobytí i všem schopnostem soupeřů, dokud jsou Hobiti vaší aktivní rasou.",
    "Homunkulové / Homunculi (+5)": "Kdykoliv tuto rasu někdo při výběru nových národů přeskočí, musí na ni kromě vítězné mince položit i 1 žeton Homunkula z krabice (pokud ještě nějaké zbyly). Hráč, který si tuto rasu nakonec vybere, získá nejen mince, ale i všechny tyto nasbírané žetony Homunkulů do své základní armády.",
    "Igorové / Igors (+4)": "Sbíráte všechny mrtvé žetony (od soupeřů, Zapomenutých kmenů i své vlastní), které byly zabity během vašeho tahu. Na začátku vašeho dalšího tahu můžete tyto nasbírané žetony vyměnit za nové Igory. Směnný kurz odpovídá počtu hráčů ve hře (např. ve hře 4 hráčů dáte 4 libovolné mrtvé žetony za 1 nového Igora z krabice). Můžete takto získat i více Igorů najednou.",
    "Kněžky / Priestesses (+4)": "Při odchodu do úpadku vezmete z každého svého obsazeného území přesně 1 žeton. Všechna území opustíte a z těchto žetonů postavíte 'Slonovinovou věž' na jednom jediném vybraném území. V každém dalším tahu vám tato věž vydělá tolik mincí, kolik je v ní žetonů. Pozor, věž může být soupeřem dobyta jako jakékoliv jiné území.",
    "Koboldi / Kobolds (+11)": "Pro obsazení a následné udržení každého území musíte VŽDY použít minimálně 2 žetony Koboldů. Nikdy nesmí na území stát jen jeden (dokud jste aktivní). Při odchodu do úpadku už ale na každém území ponecháte jen jeden žeton, jako všechny ostatní rasy.",
    "Kostlivci / Skeletons (+6)": "Jejich armáda neustále roste. Během fáze přeskupování vojsk získáte 1 nového Kostlivce z krabice za každé 2 neprázdné regiony (kde někdo předtím stál), které jste v tomto tahu dovedli dobýt.",
    "Kouzelníci / Wizards (+10)": "Magie jim sype peníze. Každý magický region (symbol fialové hvězdy), který ovládáte, vám na konci tahu přinese 1 vítěznou minci navíc.",
    "Krysáci / Ratmen (+13)": "Nemají vůbec žádnou speciální vlastnost. Jejich jedinou a obrovskou výhodou je to, že jich je zkrátka strašně moc.",
    "Křováci / Shrubmen (+6)": "Příroda je chrání. Všechna lesní území, která svými Křováky obsadíte, se stávají okamžitě imunními vůči jakémukoliv dobytí nebo speciálním schopnostem nepřátel. A co víc, tato imunita platí i poté, co Křováci odejdou do úpadku!",
    "Ledové čarodějky / Ice Witches (+5)": "Na konci každého svého tahu obdržíte 1 'zimní značku' za každý váš obsazený zdroj magie. Tyto značky pak rovnou rozmístíte na svá nebo i sousední území. Zimní značka trvale zvyšuje obranu území o +1 a pokud leží na nepřátelském území, snižuje soupeři výdělek o 1 minci. Značky mizí až s odchodem čarodějek do úpadku.",
    "Leprikóni / Leprechauns (+6)": "Při přeskupování vojsk můžete do libovolného počtu svých území umístit po jednom hrnci zlata. Pokud tam tento hrnec vydrží do začátku vašeho dalšího tahu, přemění se na 1 vítěznou minci pro vás. Pokud ale území s hrncem dobude soupeř, hrnec a minci získá on!",
    "Lidé / Humans (+10)": "Zemědělství je jejich síla. Každý farmářský region (symbol pšenice), který ovládáte, vám na konci tahu přinese 1 vítěznou minci navíc.",
    "Mágové / Sorcerers (+5)": "Jednou za tah můžete ukrást území KAŽDÉMU z vašich soupeřů (max. 1 území na každého hráče za kolo). Stačí najít území, které s vámi sousedí a stojí na něm POUZE JEDEN osamocený nepřátelský žeton (nesmí tam být hora ani pevnost). Tento žeton vrátíte soupeři do krabice a nahradíte ho jedním svým Mágem z vaší zásoby v krabici. Tím je území vaše.",
    "Obři / Giants (+6)": "Mají výškovou převahu. Dobývání jakéhokoliv území, které přímo sousedí s horou, kterou ovládáte, vás stojí o 1 žeton méně (vždy ale musíte použít minimálně 1 žeton).",
    "Orkové / Orcs (+5)": "Válka se jim vyplácí. Každý neprázdný region (kde před vaším útokem stál nepřítel nebo Zapomenutý kmen), který jste v tomto tahu dobyli, vám na konci tahu přinese 1 vítěznou minci navíc.",
    "Péráci / Slingmen (+5)": "Skáčou přes překážky. Mohou dobývat i území, která jsou od nich vzdálená o 1 políčko (přeskočíte 1 území nebo jezero, ale nikdy ne moře). Při dobytí území tímto skokem získáte okamžitě 1 vítěznou minci z banky.",
    "Pygmejové / Pygmies (+6)": "Smrt je pro ně jen začátek. Kdykoliv zemře nějaký váš Pygmej, hodíte Kostkou posil. Číslo, které padne, určuje, kolik nových Pygmejů si hned vezmete z krabice. Nasadíte je na mapu na konci tahu právě hrajícího hráče.",
    "Skagy / Skags (+5)": "Při dobytí nového území na něj umístíte skrytou značku kořisti lícem dolů. Podívat se na ni můžete jen vy. Soupeř ji uvidí, až když na území zaútočí. Pokud je to značka 'Útok Skagů', soupeřův útok okamžitě selže, ztratí 1 žeton a do konce tahu na toto území nesmí útočit. Pokud je to jiná značka, útočník získá území i nakreslené mince (0-3). Mince si odhalíte a seberete vy, pokud s rasou jdete do úpadku.",
    "Skřítci / Pixies (+11)": "Jsou neposední. Při fázi přeskupování vojsk smíte nechat na každém svém území POUZE 1 žeton. Všechny ostatní žetony Skřítků musíte vzít do ruky a jsou mimo hru až do začátku vašeho dalšího tahu.",
    "Tritoni / Tritons (+6)": "Voda je jejich živel. Dobývání pobřežních území (takových, co přímo sousedí s mořem nebo jezerem) vás stojí o 1 žeton méně (vždy ale musíte použít minimálně 1 žeton).",
    "Trolové / Trolls (+5)": "Staví si pevné příbytky. Na každé své dobytě území položíte Trolí doupě. To automaticky zvyšuje obranu o +1 (jako by tam stál další žeton). Doupě na místě zůstává i poté, co Trolové odejdou do úpadku. Zmizí, až když území dobude soupeř nebo jej sami opustíte.",
    "Trpaslíci / Dwarves (+3)": "Těží i po smrti. Každý důl (symbol zkřížených krumpáčů), který ovládáte, vám na konci tahu přinese 1 vítěznou minci navíc. A to nejlepší – tato schopnost funguje i ve chvíli, kdy jsou Trpaslíci v úpadku!"
}

# ==========================================
# DATABÁZE SCHOPNOSTÍ (CZ / EN)
# ==========================================
schopnosti = {
    "Alchymističtí / Alchemist (4)": "Vyrábí zlato z ničeho. Na konci každého vašeho tahu, po dobu co je tento národ aktivní, dostanete z banky automaticky 2 vítězné mince navíc.",
    "Bahenní / Swamp (4)": "Na konci vašeho tahu získáte 1 vítěznou minci navíc za naprosto každý bažinatý region, který aktuálně ovládáte.",
    "Behemotí (Obludní) / Behemoth (5)": "Dostanete k dispozici pár obřích Behemotů (2 sloupečky žetonů). Výška sloupečku se rovná počtu bažin, které zrovna ovládáte. Tyto sloupečky fungují jako masivní podpora pro útok i obranu, ale NIKDY se nesmí rozdělit. Na území musí mít Behemoti vždy jako doprovod aspoň 1 žeton vaší rasy. Pokud je území s Behemotem dobyto, ztratíte žeton rasy a Behemoti ustoupí do bezpečí.",
    "Dějepisečtí (Historiografičtí) / Historian (5)": "Sledují dějiny. Jakmile si tuto schopnost z nabídky vyberete, získáte ihned 1 minci za každou rasu, která se momentálně nachází v úpadku. Poté (dokud jste aktivní) dostanete 1 minci pokaždé, když jakýkoliv hráč na mapě (včetně vás) pošle svou rasu do úpadku.",
    "Diplomatičtí / Diplomat (5)": "Na konci vašeho tahu si můžete vybrat jednoho soupeře, na jehož aktivní rasu jste v tomto tahu NEZAÚTOČILI. Tento vybraný soupeř se stává vaším spojencem a nesmí na vaši aktivní rasu ve svém dalším tahu zaútočit. Pokud má ale soupeř na mapě navíc Ghůly v úpadku, ti na vás zaútočit mohou!",
    "Dušetkliví / Soul-Touch (5)": "Když jde váš národ s touto schopností do úpadku, automaticky tím na mapě znovu obživne (aktivuje se) vaše PŘEDCHOZÍ rasa, která už v úpadku byla. Na začátku vašeho příštího tahu nebudete vybírat novou rasu, ale rovnou budete hrát s touto oživenou (můžete žetony otočit nebo si je vzít do ruky k novému nasazení).",
    "Houfy (Rekal) / Hordes Of (5)": "Dostanete do začátku 2 žetony houfů (hord). Můžete je používat úplně stejně, jako by to byli vaši normální vojáci. Jakmile s touto rasou odejdete do úpadku, žetony houfů z mapy navždy zmizí.",
    "Hrdinní / Heroic (5)": "Na konci svého tahu umístíte své 2 Hrdiny do dvou libovolných území, která ovládáte. Tato dvě území se okamžitě stávají naprosto imunními vůči všem útokům a schopnostem soupeřů. Imunita trvá tak dlouho, dokud z nich Hrdiny nepřesunete jinam. Hrdinové zmizí, jakmile jdete do úpadku.",
    "Imperiální / Imperial (4)": "Rozpínání se obrovsky vyplácí. Na konci každého vašeho tahu si spočítejte svá území. Za každé území NAVÍC nad rámec prvních tří dostanete 1 minci. (Tedy za 4 území = +1 mince, za 5 území = +2 mince atd.).",
    "Jezdečtí / Mounted (5)": "Koně jim dávají převahu v otevřeném terénu. K dobytí jakékoliv farmy (pšenice) nebo kopce vám stačí o 1 žeton národa méně, než je obvyklé (vždy ale musíte použít minimálně 1 žeton).",
    "Katapultující / Catapult (4)": "Získáte jeden Katapult, který si jednou za tah můžete umístit do svého území. S katapultem můžete dobýt území, které je od vás vzdálené o 1 políčko (přeskočíte 1 region nebo jezero, ale ne moře). K dobytí vám stačí o 1 žeton méně (min. 1). Území, kde katapult fyzicky stojí, je navíc imunní proti všem útokům a schopnostem! Katapult mizí v úpadku.",
    "Kopcoví / Hill (4)": "Na konci vašeho tahu získáte 1 vítěznou minci navíc za naprosto každý kopcovitý region, který aktuálně ovládáte.",
    "Kočovní / Bivouacking (5)": "Během fáze přeskupování vojsk máte k dispozici 5 žetonů Polních táborů, které můžete libovolně rozmístit do svých území. Každý tábor zvyšuje obranu území o +1. Můžete dokonce umístit i více táborů na jedno území a udělat ho nedobytným. Tábory můžete v každém tahu stěhovat. Mizí, jakmile jdete do úpadku.",
    "Lávoví / Lava (4)": "Sopka bouchla! Na konci svého tahu můžete za každou vaši horu položit 1 žeton lávy na libovolné sousední nepřátelské území. Soupeř neutrpí ztráty (vezme si vojáky zpět do ruky), ale území s lávou je absolutně neprůchodné pro kohokoliv až do začátku vašeho příštího tahu. Pak si lávu stáhnete k sobě.",
    "Lesní / Forest (4)": "Na konci vašeho tahu získáte 1 vítěznou minci navíc za naprosto každý lesní region, který aktuálně ovládáte.",
    "Létající / Flying (5)": "Křídla jim dávají naprostou volnost. Můžete svými vojsky dobývat jakýkoliv region na celé mapě (kromě moře). Nemusíte se držet pravidla, že nové území musí sousedit s tím vaším předchozím.",
    "Loupeživí (Pillaging) / Pillaging (5)": "Za každé NEPRÁZDNÉ území (takové, na kterém před vaším útokem stál aspoň 1 žeton soupeře nebo Zapomenutého kmene), které v tomto tahu dobudete, dostanete na konci tahu 1 vítěznou minci navíc.",
    "Loupeživí (Plenící) / Ransacking (4)": "Kradou z cizích kapes! Kdykoliv úspěšně dobudete území, na kterém stál aktivní národ vašeho soupeře, musí vám on sám vzít 1 vítěznou minci ze své vlastní tajné hromádky a zaplatit vám ji (pokud nějaké mince má). U ras v úpadku se nekrade.",
    "Mírumilovní / Peace Loving (4)": "Na konci vašeho tahu obdržíte z banky automaticky 3 vítězné mince, pokud jste v tomto tahu nezaútočili na ŽÁDNÝ aktivní národ kteréhokoliv ze soupeřů. Pozor: Útočit na Zapomenuté kmeny nebo národy, které jsou již v úpadku, můžete naprosto beztrestně – o bonus 3 mincí nepřijdete.",
    "Mořští / Seafaring (5)": "Voda je jejich domov. Můžete bez problémů dobývat moře a jezera (počítají se prostě jako prázdná území bez bonusů). Tato vodní území vám zůstanou a budou vám každé kolo sypat peníze i poté, co váš národ odejde do úpadku.",
    "Napodobující / Copycat (4)": "Kradou cizí schopnosti! Na začátku každého svého tahu umístíte zrcátko na jakoukoliv ze schopností, která právě leží nevyužitá v nabídce vedle plánu. Až do začátku vašeho dalšího tahu získáváte všechny výhody této schopnosti. V dalším tahu si můžete vybrat jinou.",
    "Nájezdničtí (Drancující) / Marauding (5)": "Útočí ve dvou vlnách. Poté co skončíte své běžné dobývání, ještě než si vůbec zkusíte hodit kostkou pro poslední útok, si můžete vzít svá vojska zpět do ruky (na každém území musíte nechat aspoň 1) a začít úplně nové dobyvačné kolo! Teprve až dokončíte tento druhý zájezd, můžete v případě potřeby zkusit štěstí s kostkou.",
    "Námezdní / Mercenary (4)": "Penězi si kupují snazší cestu. Kdykoliv se pokusíte o dobytí území, můžete zaplatit do banky 1 vítěznou minci, čímž se potřebný počet vojáků pro toto dobytí sníží o 2 (vždy ale musíte k útoku použít minimálně 1 žeton). Můžete se takto rozhodnout i po hodu kostkou při posledním útoku!",
    "Obchodující / Merchant (2)": "Na konci svého tahu si poctivě sečtete svá území a získáte 1 vítěznou minci navíc za KAŽDÉ území, které aktuálně ovládáte.",
    "Oheň vrhající / Fireball (5)": "Při fázi přeskupování vojsk získáte z banky 1 značku Ohnivé koule za každý váš magický zdroj. V dalších tazích můžete tyto Ohnivé koule použít k útoku – každá se počítá za 2 vojáky. Po použití ale shoří a odhodíte ji zpět. Pro obsazení dobytého území musíte mít vždy po ruce aspoň 1 reálný žeton rasy.",
    "Opevnění / Fortified (3)": "Jednou za tah můžete na jakékoliv své území umístit Pevnost. Dokud je vaše rasa aktivní, sype vám Pevnost na konci každého tahu 1 minci navíc. Navíc neustále (i po vašem odchodu do úpadku) zvyšuje obranu území o +1. Na celé mapě může stát naráz jen 6 pevností. Zmizí po dobytí území soupeřem.",
    "Podzemní / Underworld (5)": "K dobytí jakékoliv jeskyně vám vždy stačí o 1 žeton národa méně (vždy ale minimálně 1). Pro tento národ se navíc všechny jeskyně na mapě počítají, jako by navzájem sousedily, takže můžete snadno přeskakovat z jednoho konce podzemí na druhý.",
    "Prokletí / Cursed (0)": "Máte smůlu. Tato schopnost nedává absolutně žádnou herní výhodu ani žetony navíc. Dělá jediné – pokud ji někdo nechce a rozhodne se ji v nabídce při nákupu nové rasy přeskočit, musí na ni místo 1 mince položit rovnou 3 vítězné mince!",
    "Přízrační / Spirit (5)": "Smrt je nevyžene. Normálně platí, že jakmile na mapu pošlete rasu do úpadku, vaše PŘEDCHOZÍ rasa v úpadku automaticky umírá a zmizí z mapy. Přízraky se ale tohoto limitu neúčastní! Pokud s nimi jdete do úpadku, zůstávají na mapě a nadále vám vydělávají peníze, a vy můžete v budoucnu vesele poslat do úpadku další rasy.",
    "Udatní / Stout (4)": "Mají neskutečnou výdrž. Zatímco ostatní ztratí celý tah tím, že nahlásí odchod do úpadku, Udatní mohou do úpadku odejít až na samém KONCI svého tahu – to znamená, že nejdřív normálně zaútočí, obsadí nová území, seberou za ně peníze a TEPRVE POTÉ zalezou do úpadku. Šetří tím tak celé jedno zbytečné kolo!",
    "Úplatní / Corrupt (4)": "Kdykoliv se soupeři podaří prolomit vaši obranu a dobýt území, které drží vaše AKTIVNÍ rasa, musí vám za tento drzý čin rovnou zaplatit 1 vítěznou minci.",
    "Útoční / Commando (4)": "Jsou vycvičení k zabíjení. Dobytí JAKÉHOKOLIV sousedního území vás vždy stojí o 1 žeton národa méně (vždy ale musíte do boje poslat minimálně 1 žeton).",
    "Vládci draků / Dragon Master (5)": "Mají na povel to nejstrašnější stvoření. Jednou za tah můžete dobýt jedno území za pomoci JEDINÉHO žetonu vojáka (bez ohledu na to, jak masivní obranu tam měl soupeř připravenou). Ihned tam umístíte žeton Draka. Území s Drakem je absolutně imunní vůči dobytí i jakékoliv magii soupeřů. Draka můžete každý tah přesunout. Mizí, až když odejdete do úpadku.",
    "Vlkodlačí / Were- (4)": "Měsíc jim dává sílu. Během každého SUDÉHO kola hry (v noci) vás dobytí všech území stojí rovnou o 2 žetony národa méně (vždy ale minimálně 1). V lichých kolech (ve dne) tato schopnost nijak nepomáhá.",
    "Vodní / Aquatic (5)": "Moře je krmí. Na konci tahu dostanete 1 minci navíc za každý váš pobřežní region (region přímo sousedící s vodou). Naopak, za každý region ve vnitrozemí (bez přístupu k vodě) dostanete o 1 minci MÉNĚ, než je obvyklé.",
    "Zabarikádovaní / Barricade (4)": "Méně je někdy více. Na konci svého tahu získáte 3 vítězné mince navíc z banky, pokud v tu chvíli ovládáte 4 nebo MÉNĚ území.",
    "Zámožní / Wealthy (4)": "Na konci svého PRVNÍHO tahu (a pouze tohoto prvního tahu) získáte jednorázovou finanční injekci – celých 7 vítězných mincí navíc z banky.",
    "Zuřiví / Berserk (4)": "Do boje jdou jako smyslů zbavení. S Kostkou posil se nehází jen při posledním útoku, ale PŘED KAŽDÝM jedním útokem! Vyberete cíl, hodíte kostkou a číslo, které padne, přičtete ke svým vojákům. Pokud to stačí, vyhrajete. Pokud i tak máte málo vojáků, váš útok definitivně selhal, tah končí a zbylé vojáky necháte tam, kde byli."
}

# ==========================================
# BOČNÍ PANEL S TIPY A KOMBACEMI
# ==========================================
with st.sidebar:
    st.subheader("💡 STRATEGICKÉ TIPY")
    
    with st.expander("🎲 Kdy vlastně házet Kostkou posil?"):
        st.error("""
        **Pozor: Kostkou nemůžete házet, kdykoliv se vám zachce!**
        
        Kostku posil smíte použít **VÝHRADNĚ a pouze na váš ÚPLNĚ POSLEDNÍ útok** v daném kole. 
        
        Nesmíte si hodit uprostřed tahu, abyste "ušetřili" vojáky na další útoky. Kostka slouží jen jako poslední záchrana ve chvíli, kdy už vám v ruce zbylo příliš málo žetonů na normální dobytí, ale máte alespoň jednoho vojáka a chcete zkusit štěstí.
        
        *(Výjimku tvoří pouze schopnost 'Zuřiví / Berserk', která vám naopak nařizuje házet před naprosto každým útokem).*
        """)

    with st.expander("Kdy je správný čas jít do úpadku?"):
        st.write("""
        * **Kalkulačka 3 mincí:** Položte si otázku – vydělá mi má současná rasa v dalším kole méně než 3 nebo 4 mince? Nemám už v ruce dost vojáků na další útoky? Pokud je odpověď 'Ano', okamžitě hlaste úpadek.
        * **Zaseknutí na mapě:** Pokud jste se roztáhli do 5 území, na každém leží jeden váš voják v obraně a vy si tak do ruky pro útok nemáte koho vzít, váš tah by byl zbytečný. Běžte do úpadku, ať vám to staré impérium generuje peníze samo a vy si vezmete čerstvé síly.
        * **Mějte na paměti ztracené kolo:** Kolo, ve kterém hlásíte úpadek, je kolo, kde nevyděláte nic za aktivní rasu. Vaše nová rasa, kterou si pořídíte o kolo později, by tedy měla být dost silná na to, aby vám tento "nulový" tah finančně vynahradila.
        """)
        
    with st.expander("Nezapomínejte na Zapomenuté"):
        st.write("""
        * Území, kde sídlí Zapomenutý kmen (nebo cizí rasa v úpadku), je často tou nejlepší možnou kořistí. Vždy je tam totiž pouze jeden jediný osamocený obránce, takže vás dobytí stojí minimum sil.
        * Další obrovská výhoda: Vybíjením Zapomenutých kmenů nikomu ze živých soupeřů reálně neškodíte. Minimalizujete tak šanci, že se vám bude někdo hned v dalším kole vztekle mstít. V prvním kole hry byste měli políčka Zapomenutých kmenů doslova luxovat.
        """)

    with st.expander("Peníze se povalují na stole"):
        st.write("""
        * Nebojte se v nabídce cíleně vybrat "slabší" rasu nebo schopnost, pokud vidíte, že už na ní leží hromada mincí (často tam jsou 4 nebo 5 mincí od soupeřů, co ji přeskočili). Tyto mince jdou totiž rovnou k vám do kapsy a občas vydělají víc než složité dobývání.
        """)
        
    with st.expander("🔥 Zabijácká komba (Největší hrozby)"):
        st.write("""
        Některé kombinace ras a schopností jsou natolik zničující, že dokážou úplně samy vyhrát hru. Pokud tyto páry uvidíte na stole, kupte je dřív, než to udělá někdo jiný!
        
        * **Létající + Cokoliv s tvrdou obranou (Tábory, Trolové, Pevnosti):** S křídly skáčete po celé mapě a vybíráte si jen to nejlepší. Jakmile získáte izolované, dobře placené místo uprostřed ničeho, zakopáte se tam pomocí obranného bonusu. Soupeřům se většinou nevyplatí plýtvat vojsky, aby k vám došli přes půl mapy.
        * **Diplomatičtí + Ghůlové (nebo Přízrační):** Naprosto frustrující kombo pro soupeře. Ghůlové v úpadku vám na mapě zabírají spoustu místa a dál s nimi drze útočíte. Se svou novou aktivní rasou někoho silně udeříte, ale na konci tahu mu pomocí Diplomacie s úsměvem zakážete, aby vám útok oplatil.
        * **Zámožní (Wealthy) + Rasy s málem žetonů (Mágové, Obři):** Zámožní vám dají hned v prvním kole jednorázovou injekci 7 mincí. Tato schopnost se skvěle hodí na rasy, u kterých dopředu víte, že mají malou armádu a nepřežijí dlouho. Hrajete je jako raketu – vyletí, nasypou ohromné bohatství z prvního tahu, a hned ve druhém tahu je bez milosti pošlete do úpadku a přesednete na něco silnějšího.
        * **Podzemní (Underworld) + Trolové:** Celá síť jeskyní se počítá, jako by na sebe navazovala. S Troly zalezete do podzemí, obsadíte každý kout na různých koncích mapy a do každého hnízda postavíte Trolí doupě. Z této podzemní pevnosti vás bude stát soupeře neskutečné úsilí vůbec dostat.
        * **Alchymističtí + Rasy na výdrž (Hobiti, Trolové):** Alchymisté vám bez jakékoliv námahy posílají 2 mince každé kolo, co jste na mapě. Potřebujete tedy jediné – přežít co nejdéle. Hobití nory (absolutní imunita) nebo Trolí doupata (+1 obrana) jsou ideální zárukou dlouhověkosti.
        """)

# ==========================================
# HLAVNÍ OBSAH (Záložky)
# ==========================================
st.title("🌍 Small World – Kompletní Příručka")
st.write("Sjednocená databáze pravidel ze základní hry i všech rozšíření. Ideální nástroj pro rychlou orientaci nováčků i veteránů u herního stolu.")

tab1, tab2, tab3 = st.tabs(["🛡️ Rasy", "✨ Schopnosti", "📜 Detailní Pravidla a Boj"])

# Záložka 1: Rasy
with tab1:
    st.info("💡 **Co znamená číslo v závorce u názvu rasy?** Například Amazons **(+6)** určuje, kolik žetonů vojáků vám dává samotná rasa. K tomuto číslu musíte VŽDY přičíst ještě číslo z vybrané schopnosti, čímž získáte velikost vaší armády pro začátek.")
    
    hledat_rasu = st.text_input("Zadejte název rasy (CZ nebo EN):", key="rasa_search").lower()
    
    for rasa, popis in sorted(rasy.items()):
        if hledat_rasu in rasa.lower():
            with st.expander(f"**{rasa}**"):
                st.write(popis)

# Záložka 2: Schopnosti
with tab2:
    st.info("💡 **Co znamená číslo v závorce u schopnosti?** Například Alchemist **(4)** určuje počet dodatečných vojáků. Toto číslo sečtěte s číslem vaší vybrané rasy, a získáte tak finální počet žetonů, se kterými vstoupíte na mapu.")
    
    hledat_schopnost = st.text_input("Zadejte název schopnosti (CZ nebo EN):", key="schopnost_search").lower()
    
    for schopnost, popis in sorted(schopnosti.items()):
        if hledat_schopnost in schopnost.lower():
            with st.expander(f"**{schopnost}**"):
                st.write(popis)

# Záložka 3: Do hloubky vysvětlená pravidla
with tab3:
    st.markdown("### 🧮 Kolik vojáků (žetonů) si mám na začátku vzít?")
    st.success("Čísla uvedená v této aplikaci v závorkách nejsou pro parádu – určují celkovou velikost vaší armády! **Vždy sečtěte číslo Rasy a číslo Schopnosti.**\n\n**Příklad:** Pokud si vyberete Amazonky (+6) a schopnost Létající (5), vezmete si z krabice na stůl přesně 11 žetonů Amazonek. Nic víc do začátku nedostanete, toto je vaše celá armáda pro dobývání.")

    st.markdown("---")
    
    st.markdown("### 🏆 Cíl hry a jak vyhrát")
    st.write("Ve Small Worldu se hraje na nemilosrdný byznys – svět je příliš malý na to, abyste se do něj vešli všichni. Vaším absolutně jediným cílem je **získat na konci hry co nejvíce Vítězných mincí**. Žádná smrt nebo vyřazení neexistuje, všechno je o penězích.")
    st.markdown("""
    * Hra má předem pevně stanovený počet kol (podle mapy a hráčů hrajete většinou 8, 9 nebo 10 tahů). Jakmile ukazatel tahu dosáhne konce a všichni dohrají své poslední kolo, hra okamžitě končí.
    * Všechny mince, které si během tahů nastřádáte, držíte v tajnosti. Až na úplném konci je všichni hráči odhalí, spočítají a ten s největší hromádkou peněz odchází jako vítěz.
    """)
    
    st.markdown("---")
    
    st.markdown("#### 🛒 Jak probíhá nákup a příprava nové rasy?")
    st.write("Na úplném začátku hry (nebo vždy, když vaše předchozí rasa odejde do úpadku a skončí), si musíte koupit rasu novou. Na okraji stolu leží sloupec 6 kombinací – každá se skládá z Tabulky Rasy a z Žetonu Schopnosti, který se k ní náhodně přiřadil. Vybíráte vždy celou tuto dvojici najednou.")
    st.markdown("""
    1. **První pozice je zdarma:** Nabídka funguje jako pás. Rasa úplně nahoře je zadarmo, rovnou si ji můžete vzít.
    2. **Poplatek za přeskočení:** Pokud se vám líbí až třetí rasa v pořadí, musíte zaplatit za ty, které nechcete. Vezmete si své mince a položíte 1 minci na první rasu a 1 minci na druhou rasu. Až pak si vezmete tu vysněnou třetí.
    3. **Nákup jako investice:** Pokud si naopak vyberete rasu, na které už leží mince od ostatních hráčů (protože ji před vámi přeskočili), stane se úžasná věc. Tuto rasu si berete k sobě a všechny tyto **mince si shrábnete do své pokladnice**. Okamžitě se vám počítají do vašeho vítězného skóre.
    """)

    st.markdown("---")
    
    st.markdown("#### ⚔️ Boj: Jak se dobývá území? (Žádné kostky, tvrdá matematika)")
    st.write("Boj ve Small Worldu je fantastický tím, že v něm není prakticky žádná náhoda. Dopředu přesně víte, jestli území dokážete obsadit, nebo ne.")
    st.markdown("""
    * **První vstup na mapu:** Vaše úplně první runda dobývání MUSÍ začít buď na okrajovém políčku mapy, nebo na políčku s pobřežím u moře. Jakékoliv další území, které se rozhodnete v témže tahu dobýt, už na toto první dobytí musí přímo navazovat (sousední políčko).
    * **Pravidlo 2 vojáků:** Abyste vstoupili na naprosto čisté, opuštěné území, musíte k tomu z ruky vydat přesně **2 své žetony**. Ty tam položíte a je to vaše.
    * **Pravidlo +1 za každou překážku:** Zde přichází taktika. Za každou překážku nebo jednotku, která na daném území leží, musíte připlatit dalšího vojáka k těm základním dvěma.
    """)
    st.info("""
    **DŮKLADNÝ PŘÍKLAD BOJE:** Rozhodnete se zaútočit na pohoří, na kterém navíc leží 2 žetony nepřátelských vojáků a jeden žeton Pevnosti. Kolik vojáků budete na takový masivní útok potřebovat z ruky vy?
    * 2 žetony (základ za prosté vstoupení na jakékoliv území)
    * +1 žeton (protože to je Horstvo)
    * +2 žetony (za každého ze 2 nepřátelských vojáků na kopci)
    * +1 žeton (za Pevnost, která území brání)
    
    = **Potřebujete celkem 6 vojáků**. Pokud jich máte v ruce 6 nebo více, prostě je vezmete, plácnete je na území a území je bez milosti vaše. Pokud jich máte v ruce jen 5, je to málo. Tento útok je nemožný a vůbec nesmíte zaútočit.
    """)
    
    st.markdown("#### 🎲 Kostka posil (Jediná výjimka pro štěstí)")
    st.warning("""
    **Pravidlo pro kostku:** Kostku nesmíte používat kdykoliv se vám zachce! Používá se výhradně a pouze pro váš **ÚPLNĚ POSLEDNÍ ÚTOK v daném kole**, pokud vám zbylo málo žetonů na jisté dobytí.
    """)
    st.markdown("""
    Během vašeho kola postupně z ruky ubíráte vojáky a pokládáte je na dobývaná území. Nakonec vám zbyde třeba už jen 1 voják. S ním byste normálně nic nedobyli (potřebujete aspoň 2). V tuto chvíli ale můžete zariskovat svůj poslední útok:
    * Nahlásíte nahlas své cílové území (třeba prázdné území za 2 žetony).
    * Máte v ruce 1 vojáka.
    * Vezmete speciální Kostku posil (na níž jsou čísla od 0 do 3) a hodíte.
    * Pokud vám padne například 2, přičtete to ke svému jedinému vojákovi v ruce (1 + 2 = 3 síla). Páni, stačí to! Vezmete toho svého 1 posledního reálného vojáka, položíte ho na území a je vaše. Tím váš tah definitivně končí.
    * Pokud by padla 0, váš útok se nezdařil. Tohoto svého posledního nevyužitého vojáka prostě přidáte jako posilu do obrany k jakémukoliv svému již dobytého území.
    """)

    st.markdown("---")

    st.markdown("#### 💀 Co se přesně děje s poraženými vojáky?")
    st.write("Když někdo prorazí vaši obranu a vezme vám území, o celou svou armádu na daném políčku nepřijdete, ale utržíte bolestivé ztráty.")
    st.markdown("""
    1. **Daň ze smrti:** Okamžitě vezměte všechny své poražené žetony z právě dobytého území. **Jeden jediný z nich trvale umírá** – vrátíte ho zpět do krabice mimo hru. (Pozn.: Pokud u vás stál jen jeden osamocený obránce, např. žeton Zapomenutého kmene, do ruky se nevrací nic a on umírá nadobro).
    2. **Útěk z bojiště:** Pokud vám na políčku po smrti 1 vojáka ještě nějaký zbyl, ponecháte si tyto přeživší žetony stranou (mimo mapu) u sebe v ruce.
    3. **Nový protiútok (Nasazení):** Záchranná akce přichází na řadu až ve chvíli, kdy útočník COMPLETNĚ ukončí svůj tah a vše si přeskupí. Tehdy vy, jakožto napadený, vezmete své zachráněné vojáky, kteří vám zbyli v ruce, a okamžitě s nimi posílíte obranu na jakýchkoliv OSTATNÍCH územích, které vám na mapě ještě zbyly.
    """)
    
    st.markdown("---")

    st.markdown("#### 📉 Úpadek: Kdy odejít do důchodu a jak na to?")
    st.write("Rychle zjistíte, že se s jednou rasou nedá hrát věčně. Ztrácíte vojáky v boji, zanecháváte je rozprostřené na dobytých územích kvůli obraně, až najednou zjistíte, že nemáte v ruce skoro nikoho a nikam nedojdete. Čas ohlásit Úpadek.")
    st.markdown("""
    Namísto toho, abyste se snažili v novém kole nesmyslně útočit s hrstkou unavených vojáků, prohlásíte, že vaše rasa odchází do úpadku. Tento tah se hraje úplně jinak:
    
    1. **Smrštění obránců:** Z každého území, které aktuálně vaše rasa okupuje, sundejte všechny žetony vojáků tak, aby na naprosto každém vašem území zůstal přesně JEDEN jediný voják. Tyto zbylé (osamocené) vojáky obraťte vzhůru nohama na jejich šedou, nebarevnou stranu (Úpadek).
    2. **Odkopnutí schopnosti:** Žeton vaší unikátní schopnosti zahoďte stranou do krabice. Vaše rasa ji už nadobro ztratila a nefunguje jí.
    3. **Staré mrtvoly musí pryč:** Na herní mapě smíte mít VŽDY jen jednu rasu v úpadku. Pokud se na mapě ještě krčí nějací zašedlí vojáci z vašeho dřívějšího úpadku o pár kol dříve, musí teď bezpodmínečně vyklidit prostor a celou starou rasu vracíte do krabice (pokud nehrajete za Přízračné).
    4. **Důchod z peněz:** V tomto kole jste neútočili a zdánlivě nic nedělali, ALE za všechna svá zašedlá území na konci tahu **stále získáte plnohodnotně peníze** (1 území v úpadku = 1 mince). 
    
    A co dál? Vaše stará rasa už žije jen pasivně, na místech se jen tiše a odevzdaně brání. Ale vy, jako hráč, si v začátku dalšího tahu za peníze vyberete novou, čerstvou krev z nabídky 6 ras na okraji stolu a celý kolotoč dobývání s plnou armádou začíná nanovo!
    """)