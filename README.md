# Snake

W celu uruchomienia gry należy pobrać pliki z folderu Snake_Codes. Wszystkie pliki muszą znajdować się w jednym folderze.

Po pobraniu należy uruchomić plik Snake_Main.py, który uruchomi interfejs gry.


Sprawozdanie

WSB Merito

Programista Python Developer – grupa 1

Joanna Banachowicz

1) Wstęp
W ramach projektu zdecydowałam się stworzyć własną wersję gry ‘Snake’. Gra posiada pięć poziomów trudności. Stworzyłam także interfejs, który umożliwia wybór poziomu, klawiszy sterujących oraz sprawdzenie najlepszych graczy. Grę oparłam o bibliotekę pygame oraz pygame_gui. Link do repozytorium, w którym jest cały kod gry: https://github.com/JoannaBanach/Snake.git

2) Opis szczegółowy
Gra została podzielona na kilka modułów:

a) Klasa Obstacle

Klasa zawiera funkcjonalności:
- Tworzenia przeszkody w jednej z czterech ćwiartek pola, po którym porusza się wąż.
- Wylosowanie miejsca, gdzie znajduje się przeszkoda oraz wylosowanie jej wielkości
- Przekazanie współrzędnych przeszkody.
- Rysowanie przeszkody.

b) Klasa Apple

Klasa zawiera funkcjonalności:
- Losowe generowanie, gdzie jabłko będzie się znajdowało.
- Losowanie współrzędnych jabłka obejmuje sprawdzenie, gdzie w obecnym momencie znajduje się wąż oraz przeszkody i inne jabłka, jeśli dany poziom je zawiera.
- Zmiana koloru jabłka z czerwonego na zielone, gdy jego zjedzenie jest premiowane dodatkowymi punktami.
- Przekazywanie współrzędnych jabłka.
- Rysowanie jabłka.

c) Klasa SaveScore

Klasa zawiera funkcjonalności:

- Sprawdzenie, czy plik zawierający najlepsze wyniki istnieje.
- Utworzenie pliku, jeśli nie istnieje.
- Uzupełnienie brakujących zakładek do każdego poziomu gry.
- Zapisywanie wyniku gry, przypisując go do odpowiedniego poziomu i właściwego zajętego miejsca.
- Zwrócenie zajętego miejsca.
- Sprawdzenie najlepszego wyniku dla każdego poziomu.

d) Klasa Snake

Klasa zawiera funkcjonalności:

- Podklasa SnakePart, która zawiera współrzędne pojedynczej części węża.
- Utworzenie węża i jego wyglądu.
- Poruszanie się węża.
- Powiększenie węża.
- Sprawdzenie długości węża.
- Sprawdzenie czy wąż zjadł jabłko lub wpadł na przeszkodę bądź granicę planszy.
- Przekazanie współrzędnych węża.

e) Klasa SnakeGame

Klasa zawiera funkcjonalności:

- Utworzenie planszy, po której porusza się wąż.
- Wyświetlanie bieżącego wyniku.
- Przyspieszanie prędkości węża na żądanie gracza lub w przypadku poziomu Hard i Super Hard także zwiększanie prędkości dodatkowo co 15 sekund.
- Definiowanie ile jabłek i przeszkód będzie zawierać poziom gry oraz czy będą pojawiać się zielone jabłka specjalne.
- Wyświetlanie obecnego stanu gry: położenia jabłek, węża i przeszkód.

f) Klasa SnakeGUI

Klasa odpowiada za utworzenie trzech interfejsów:

- Interfejs początkowy, który umożliwia:

i) wprowadzenie imienia lub pseudonimu gracza,

i) wybór klawiszy sterujących,

i) wybór poziomu gry,

i) wywołanie sprawdzenia najlepszych wyników dla każdego poziomu,

i) rozpoczęcie gry.

- Interfejs wyświetlający najlepsze wyniki dla każdego poziomu. Interfejs zawiera przycisk umożliwiający powrót do głównego interfejsu.
- Interfejs informujący o zakończeniu gry. Wyświetlana jest zdobyta ilość punktów oraz zajęte miejsce, pod warunkiem, że zajęło się jedno z pierwszych dziesięciu miejsc. Interfejs zawiera przycisk umożliwiający powrót do głównego interfejsu.
Do klasy zostały utworzone dodatkowe pliki z ustawieniami, jak powinny wyglądać na interfejsach pola tekstowe, przyciski i listy wybieralne. Dzięki temu wygląd wszystkich interfejsów jest spójny.

3) Podsumowanie gry

Gra posiada zdefiniowane trzy poziomy:

- Super Easy - nie posiada granicy planszy (wąż pojawia się po przeciwnej stronie). Na planszy jest umieszczonych 5 jabłek.
- Easy – także nie posiada granicy planszy, natomiast na planszy jest jedno jabłko.
- Medium – zdefiniowane granice planszy. Na planszy jest jedno jabłko, które okazjonalnie staje się premiowanym zielonym jabłkiem.
- Hard – zdefiniowane granice planszy oraz cztery przeszkody. Na planszy są trzy jabłka, z czego jedno okazjonalnie staje się premiowanym zielonym jabłkiem. Prędkość węża jest zwiększa co 15 sekund o 1.
- Super Hard – zdefiniowane granice planszy oraz cztery przeszkody Na planszy jest jedno jabłko, które okazjonalnie staje się premiowanym zielonym jabłkiem. Prędkość węża jest mnożona co 15 sekund razy 1.2.
Interfejsy użytkownika są spójne pod względem wyglądu i są intuicyjne w użyciu. Bardzo wyraźnie widać, gdzie na planszy znajduje się wąż. Jabłko i przeszkody można odróżnić poprzez odmienne kolory. Gra zawiera elementy losowości umiejscowienia jabłek i przeszkód. Gracz może przyspieszać prędkość węża przez ponowne naciśnięcie przycisku w kierunku, w którym aktualnie porusza się wąż.
W kodzie zostały użyte klasy, funkcje klas, importowanie modułów wbudowanych oraz z plików, zastosowano kwargsy, pętle for i while oraz konstrukcje warunkowe.

4) Podsumowanie projektu

Projekt okazał się wyzwaniem, gdyż początkowo kod zawierał kilka różnych klas Snake oraz SnakeGame dla każdego poziomu. Utrudniało to wprowadzanie zmian w kodzie. Zdecydowałam się na zredukowanie ilości klas, dzięki czemu kod zyskał dużą elastyczności i kod nie powtarza się w kilku miejscach. Projekt był doskonałą okazją do wypróbowania umiejętności zdobytych w trakcie zajęć oraz integracji wiedzy o poszczególnych bibliotekach. Dodatkowo był okazją do samodzielnego pogłębienia wiedzy o funkcjach i bibliotekach, które nie zostały omówione.


