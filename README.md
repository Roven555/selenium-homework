SELENIUMI AUTOMAATTESTIDE DOKUMENTATSIOON
Üldine seadistus ja keskkond
Teek: Selenium WebDriver (selenium)

Brauseri ajam: ChromeDriver (automaatselt hallatav Selenium Manageri poolt)

Keel: Python 3.14

Ülesanne 1: Automaatne veebiotsing ja kuvatõmmis
1. Koodieesmärk
Automatiseerida otsinguprotsess veebis ilma kasutaja sekkumiseta, kontrollida otsingutulemuste laadimist ning salvestada lõpptulemusest tõestuseks pildifail (kuvatõmmis). Märkus: Google'i agressiivse botituvastuse vältimiseks on test viidud üle DuckDuckGo mootorile.

2. Kuidas toimib?
Skript käivitab Chrome'i brauseri akna ja maksimeerib selle (driver.maximize_window()).

Navigeeritakse aadressile https://duckduckgo.com.

Kasutades meetodit find_element(By.NAME, "q"), otsitakse lehe HTML-koodist üles otsingukast (selle atribuut name on alati "q").

Käsk send_keys("Roven") sisestab kasti nime ja submit() saadab vormi teele (simuleerib Enter-klahvi).

Pärast 3-sekundilist ooteaega (time.sleep(3)) teeb programm käsureaga save_screenshot("minu_otsing.png") ekraanipildi ja salvestab selle projektikausta.

3. Testimisplaan
Eeldus: Internetiühendus on olemas ja projekti kaust on kirjutatav.

Testisammud: Käivita terminalis py task1.py.

Oodatav tulemus: Avaneb Chrome, DuckDuckGo otsingukasti ilmub tekst "Roven", leht laeb tulemused ning kausta tekib fail minu_otsing.png.

Ülesanne 2: Andmete kraapimine (Web Scraping)
1. Koodieesmärk
Testida Seleniumi võimekust lugeda veebilehe HTML-struktuurist spetsiifilisi andmeid, need sealt isoleerida ja kuvada loetaval kujul käsureal.

2. Kuidas toimib?
Brauser liigub harjutuslehele https://quotes.toscrape.com.

Funktsiooniga find_elements(By.CLASS_NAME, "text") kogutakse massiivi (listi) kõik elemendid, mis sisaldavad tsitaate.

Samamoodi kogutakse meetodiga By.CLASS_NAME, "author" kokku kõikide autorite nimed.

for-tsükkel käib mõlemad listid paralleelselt läbi, eraldab atribuudiga .text puhastatud teksti ja prindib terminali formaadis "[Tsitaat]" - [Autor].

3. Testimisplaan
Eeldus: Leht quotes.toscrape.com on kättesaadav.

Testisammud: Jälgi skripti käivitamise ajal terminali (CMD) akent.

Oodatav tulemus: Terminali ilmub jutti 10 lehel olevat tsitaati koos autorite nimedega (nt. Albert Einstein, J.K. Rowling).

Ülesanne 3: Elementide dünaamiline lisamine ja kustutamine
1. Koodieesmärk
Kontrollida, kas Selenium suudab manipuleerida veebilehe dünaamiliste elementidega (DOM-puu muutmine reaalajas) ehk elementide loomist ja nende ükshaaval hävitamist.

2. Kuidas toimib?
Liigutakse testlehele /add_remove_elements/.

Programm otsib XPATH-i abil üles nupu: //button[text()='Add Element'].

for-tsükkel klikib sellele nupule 5 korda, tekitades lehele juurde 5 uut "Delete" nuppu.

Seejärel otsitakse käsuga find_elements(By.CLASS_NAME, "added-manually") üles kõik uued tekitatud nupud.

Teine tsükkel klikib igale "Delete" nupule eraldi peale, mis eemaldab need veebilehelt.

3. Testimisplaan
Eeldus: Veebilehitseja on nähtav.

Testisammud: Jälgi testimise ajal Chrome'i akent.

Oodatav tulemus: Veebilehele tekib kiiresti üksteise alla 5 nuppu ja seejärel kustutab robot need automaatselt ükshaaval ära, kuni leht on taas algseisus.

Ülesanne 4: Sisselogimisvormi täitmine ja valideerimine
1. Koodieesmärk
Automatiseerida kasutaja sisselogimise protsess (vormi täitmine) ja valideerida, kas süsteem tuvastab edukalt õiged andmed ning kuvab vastava teavituse.

2. Kuidas toimib?
Brauser avab sisselogimislehe /login.

ID-atribuutide põhjal leitakse väljad "username" ja "password".

Käsk send_keys() kirjutab väljadesse õpetaja antud testandmed (tomsmith ja SuperSecretPassword!).

CSS-selektori abil otsitakse üles sisselogimise nupp ja tehakse sellel klikk.

Pärast lehe laadimist otsitakse teateboksi (ID "flash"), loetakse sealt tekst ja kontrollitakse if-lausega, kas see sisaldab fraasi "You logged into a secure area!".

3. Testimisplaan
Eeldus: Kasutatakse korrektseid testandmeid.

Testisammud: Kontrolli pärast vormi täitumist terminali teadet.

Oodatav tulemus: Veebileht teatab edukast sissepääsust ja terminali prinditakse roheline tuli: TEST ÕNNESTUS: Edukalt sisse logitud!.

Ülesanne 5: Navigatsioon ja märkeruudud (Checkboxes)
1. Koodieesmärk
Testida Seleniumi võimekust navigeerida mööda linke, kontrollida märkeruutude (checkbox) hetkestaatust, muuta nende olekut ja kasutada brauseri sisemist ajalugu tagasiliikumiseks.

2. Kuidas toimib?
Robot naaseb HerokuApp-i pealehele.

Otsitakse elementi lingi teksti järgi (By.LINK_TEXT, "Checkboxes") ja klikitakse sellel, mis suunab brauseri uuele alamlehele.

Otsitakse üles kõik sisendkastid (#checkboxes input).

Tsükkel kontrollib funktsiooniga if not box.is_selected():, kas kast on tühi. Kui kast pole märgitud, teeb robot seal kliki.

Käsk driver.back() simuleerib brauseri "Back" (Tagasi) nupu vajutust, viies boti tagasi avalehele.

3. Testimisplaan
Eeldus: Navigatsioonilingid töötavad.

Testisammud: Jälgi brauseri liikumist lehtede vahel.

Oodatav tulemus: Brauser avab checkboxide lehe, märgib mõlemad kastid aktiivseks, liigub tagasi pealehele ja sulgeb akna puhtalt käsureaga driver.quit().