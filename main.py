import asyncio
from workflow import run_workflow


if __name__ == "__main__":

    transcript = """
Dobra.

No to dzień dobry wszystkim serdeczne.

Po co jest ta sesja w ogóle i co zamierzamy tutaj obgadać? Zamysł był taki, żeby poruszyć kwestię używania kopii lota CLI, czyli wersji konsolowej command line owej i pokazać przykładowe just case, na jakim ja teraz pracuję i w jaki sposób ona mi pomaga, ale to będzie dosyć myślę uniwersalny.

I czemu w ogóle o tym co pilocie spieraj pewnie większość z was już pracowała na używając ko pilota w idę dajcie znać czy ktoś z was nie używał w ko pilota jako plugin na przykład w intel'a.

Czy ktoś z was nie używał jeszcze tego?

Maciek nie używał dobra?

Zreszta używała ok.

Dobra Witek nie używam. No właśnie widzę jak jeszcze nie używam ok to dla referencji tak tylko szybko pokażę.

Że te takie klasyczne klasyczna, no nazwijmy to klasyczna wersja kopa lota, z którą większość osób u nas jest zaznajomiona. To jest ten panel na przykład w inteligo, gaju, też w innych ideon pojawia się jako w formie różnych pluginów. No i tutaj mamy tak kopali lota, mamy różne jego tryby.

Mówię ten tryb agenta jest najbardziej praktyczny, bo pozwala agentowi na działanie w naszym kodzie dosłownie tworzenie rzeczy i tak dalej, robienie, uruchomienie komend i tak dalej to jest ten tryb agenta, który na którym teraz całe te nasze industri pieje.

Jacek Budzyński:
Żeby odpalić ko papilotach stąd boksie to ciężko go zapytać to sandboksowa no nie?

Tak no tak, tak to sam boss mordzia jak włączę tą stronkę co tu mam ten no to taki brudnopis trochę był podeślę to bo to się może przydać. Tu jest Link do tego sandboxa.

Jacek Budzyński:
Tak podeślij garaże na spotkanie.

Jest.
Instrukcja w sandboxie jak go uruchomić to jest proste i to jest rozwiązanie też kopalń w tym napisane przez tutaj przez nas, więc ono działa prawdopodobnie coś z tym pomyślimy, bo tu też mógł dzisiaj wspomniał.

To są jakieś rozwiązania, daytona, są różne rozwiązania, generalnie doker nawet ma jakiś native support dla sandboksów ja chciałem mieć uraz, może Jestem skrzywiony, chciałem mieć uaj tą datą chyba też się da. Przepraszam da zrobić uaj, ale ja chciałem mieć te okienka, mamy tu stan, pamiętam między tymi sesjami, a jak mi nawet wszystko wykasuje to nic się nie stanie, bo to jest sam box nie.

Jacek Budzyński:
No to znaczy, pewnie można było to jeszcze na zasadzie wirtualnej maszynę po prostu zrobić, no nie?

Można by jasne, no ja chciałem. Ja mam tu przez przeglądarkę widok.

Jacek Budzyński:
To wtedy też byś miał ujął, ujął tak u i byś miał taki jak wy no standardowym systemie, no nie, więc to też jest jakaś opcja jakiś.

Tak.

No ale format też mam właśnie ten sam bookstagram zrobiony, nie, że tu masz normalnie to jest jakieś tam lubuntu chyba czy nie pamiętam już które i jest normalnie. No tyle, że używany bardziej nie, bo tak to ktoś ty teraz chodzisz jak córa uruchamiać tego entry, tego tam tam jest klient.

Jacek Budzyński:
O inaczej mógłbyś mieć na przykład maszynę w sensie obraz maszyny od razu z zainstalowanym wszystkim i tak dalej też na przykład.

Można być, no jest wiele. Słuchaj, jest podejście, wiele jeszcze będziemy sparować, to dalej. To jest jedno z prostu jedno z rozwiązań.

Jacek Budzyński:
Nie jasne, jasne.

Tu jeszcze możemy przez miałem już jesteśmy poczekać, ale tak możemy sobie w te komendy zerknąć, ewentualnie nie pokątnie w nich powiedzieliśmy.

To ja tylko powiem, że na przykład te skille, które mamy tam jako repozytorium to już dostępne. Ja ja mam podpięte jako symboli glinki do tego katalogu kopalin lot i i to to jest też fajne i to.

Sam tego nie wymyśliłem też tylko to oczywiście klop też wymyślił.

Bo tak po prostu mam sklonowane repozytorium bez swoich projektów i mam zrobionego symbolicznego linka tam, bo katalogu kopa pilot nie i po prostu automatycznie też jak przyjdzie nowy skill spóbuję repo i on jest dostępny nie.

Spoko pomysł no spoko pomysł.

Miałem składem d plikiem, ale teraz w nowej wersji kopalni lokalizowane już łyka też klubem Pekinie.

Spoko pomysł dobry. No słuchajcie są te komenty różne, przez parę przeszliśmy agent kills chyba wam pokazałem MCPM cpk nie pogadaliśmy, już chyba nie będziemy gadać, te słowo też się pojawia, wiele razy też jest wiele burzliwych dyskusji o cpk.

Pluginy są jakieś a nie instalowałem żadnych tutaj model warzno Komenda taski to są pentagram taski disa można podejrzeć.

Można powiedzieć jolo.

Jakieś katalogi do do tego kuriera można wznawiać sesję stare to się przydaje jak po dniu wracasz po paru dniach chcesz do starej sesji wrócić regium i wracasz? To jest fajne kontekst. To co pokazywaliśmy juz zycz zobaczymy ile spaliliśmy do ręki model chyba zrobił.

Józef ile no.

Czy premium questy?

I zobaczy tutaj, słuchaj o haiku używał ja w sumie to musiałem, żeby nie robił chyba, ale to nieważne 9 milionów haiku, Zero questów premium 3 miliony opus sa 3 premium questa nie ten hit jest pudel model generalnie nie.

No miałeś tego hajsu w tym w tym.

Myślę, że miałeś.

Może miałem no dobra, no mniejsza z tym tak z tą sobie sami samemu warto wyczuć, którego modelu kiedy używasz.

Będziemy powoli kończyć, czy jest jakaś Komenda ważna?

Ważniejsze chyba to, żeby trzymać ten kontekst z niskiej, nie żeby nie spadać ten w ten bardzo.

Trzymać niskiego kontekst.

I zachęcam więc się.

Zachęcam do zrobienia sobie agentów PR swój Plan albo jakieś procesy, które chcecie sterować. Niewiele fortu serio, a według mnie do takiego riserczu do i też do implementacji. Według mnie na przyszłość przecież też jak implementuje musisz.

Znać powiązania w pojebanie to się przyda po prostu.

No to tak, no to w przyszłym tygodniu będziemy pokazywać, że tam mamy 3 agentów. Tak naprawdę dewelopera pije, ma i testera.

No może ich nawet więcej.

Czy takie role same nie tyle znajomość planu co rola taka deweloperska? No tak też się robi, tak.

Dobra, myślę, że nie będziemy przedłużać, chyba że jakieś pytania jeszcze.

Dobra robota, sejm nie ma prawdę.

Żeby się połapać w tym wszystkim w całym tym spaghettii tych zależności tomera.

Myślę, że się przyda, przynajmniej mi się przydaje, tak powiem.

To dzięki wszystkim.

Czwartek dziku jakieś jakieś komentarz? Może tu dziku nasz guru jajowe.

Bartłomiej Jadwiszczak:
Spoko spoko, super dzięki.

Jacek Budzyński:
Działać dzięki."""
    mode = "kt"   # sprint | kt | general
    detect_language=True

    mode = "kt"  # sprint | kt | general

    result = asyncio.run(
        run_workflow(transcript, session_mode="kt")
    )

    print("\n========== FINAL OUTPUT ==========\n")
    print(result)