Authors : Sebastian Bukowski and Jacek Stachowiak
Copyright : Sebastian Bukowski and Jacek Stachowiak
License : GNU General Public License v3.0
Version : 1.0

# **Środowisko uruchomieniowe**

## **Wymagania:**

**Windows:** potrzebne jest zainstalowanie GITa dla Windows [https://git-for-windows.github.io](https://git-for-windows.github.io/)

* **python** potrzebne jest zainstalowanie Python3 [https://www.python.org/downloads/](https://www.python.org/downloads/)
    * dodatkowo trzeba zainstalować plugin **selenium**, w katalogu głównym Python'a należy wykonać: `pip install selenium==3.6.0`
        * biblioteka **selenium** w wersji 3.6.0.
* **java** w wersji conajmniej **8**
    * do pobrania ze strony [http://www.oracle.com/technetwork/indexes/downloads/index.html#java](http://www.oracle.com/technetwork/indexes/downloads/index.html#java)
* **selenium server** w wersji standalone:
    * do pobrania z [www.seleniumhq.org/download/](http://www.seleniumhq.org/download/)
    * uruchomienie zgodnie z instrukcją na stronie [www.seleniumhq.org/docs/05_selenium_rc.jsp](http://www.seleniumhq.org/docs/05_selenium_rc.jsp):
        `java -jar /path/to/selenium-server-standalone-file.jar`
    * gecko (dla Firefox) i chrome driver:
        * geckodriver do pobrania z [https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)
        * chromedriver do pobrania z [https://sites.google.com/a/chromium.org/chromedriver/](https://sites.google.com/a/chromium.org/chromedriver/)
        
**Linux:**
    
    
   Jak wyżej odpowiedniki dla systemu Linux.

## **Praca z testami**

**Uruchamianie testów**:
* uruchomienie test suite :
    * **python tests_executor.py -tc example_smoke_test_register ** -> zostaną uruchomione smoke testy dla rejestracji klienta w sklepie automationpractice.com.
    * **python tests_executor.py -url https://google.com -tc example_smoke_test_search -> zostaną uruchomione smoke testy dla wyszukiwania frazy pizza w witrynie google.com.
    
**Przełączniki przy uruchamianiu test suitów (konfiguracja):**
* _`--browser / -b`_ -> ustawienie przeglądarki na której mają zostać uruchomione testy, domyslnie **chrome**
* _`--app_url / -url`_ -> adres strony do uruchomienia testów, domyślnie **http://automationpractice.com/index.php**
* _`--grid_url / -gurl`_ -> adres grida, domyślnie lokalny serwer selenium
* _`--test_case / -tc`_ -> wymagane do uruchomienia testów, podajemy zestaw testów. Opcje (przykładowe):
    * print (tylko w konsoli) - drukuje listę dostępnych test_caseów.
    * example_smoke_test_register
    * example_smoke_test_search
* _`--runner / -r`_ -> pozwala wygenerować lub nie raport do html'a. Opcje:
    * html - wygeneruje raport do pliku html
    * unit - nie wygeneruje raportu, wynik zostanie zwrócony tylko do konsoli
* _`--resolution / -res`_ -> pozwala uruchomić testy dla podanej rozdzielczości. Opcje: max, 992, 768, 480.
   
## **Architektura rozwiązania**

#### tests_environment\tests_setup.py
* plik zawiera przedewszystkim funkcje umożliwiające tworzenie sesji przed testem oraz funkcję zamykającą sesję
* inne funkcje konfiguracyjne jak ustawienie wielkości ekranu, dodanie ciasteczka

#### tests_support\extended_selenium_methods.py - plik z komendami seleniowymi, które wykorzystywane są do budowania części wspólnych (Snippets)

#### tests_environment\environment_config.py - plik z zdefiniowanymi argumentami, które umożliwiają uruchomienie odpowiednich testów.

#### tests_cases.py - pliki z zdefiniowanymi test case poprzez które uruchamiane są odpowiednie paczki testów.

#### Katalog **functional_tests**
* katalog zawiera testy 
* katalog podzielony jest na moduły:
    * example_tests -> zawiera przykładowe smoke testy
* każdy test musi:
    * być zawarty w którymś z modułów
* nazewnictwo testów:
    * tak aby mówiły co robi test
    * funkcje, które są testami nazywamy od słowa **test** następnie dalsza nazwa (np. test_order_as_registered)
        * bez słowa **test** w nazwie funkcji metoda zostanie pominięta podczas wywoływania testów 
    
#### Katalog **locators** znajdujący się dla każdego kanału w katalogu **page_objects**
* nazwa pliku zaczyna się od nazwy modułu jakiego dotyczy następnie słowo **locators** np. **cart_locators.py** (dotyczy elementów związanych z koszykiem)
* w klasie zawarte są stałe zwracające lokator danego elementu umożliwiający odnalezienie go na stronie
    * nazewnictwo np **BTN_register** - pierwsza część określa jakiego rodzaju jest to element link/button/input itp.
    druga część czego dotyczy lokator, w tym wypadku będzie to przycisk umożliwiający przejście do formularza rejestracji
    
#### Katalog **page_objects** - podzielony na kanały sprzedaży
* nazewnictwo page_object:
    * plik nazywamy od strony której dotyczy następnie słowo page, np. **register_page.py**
    * klasy nazywamy od nazywy strony której dotyczy następnie słowo page i nazwa kanału, np. **AccountPageObject**
* zawiera małe metody wykonując konkretne operacje na obiektach, np. kliknięcie w przycisk rejestracji.
    
#### Katalog **tests_snippets** - części wspólne wszystkich testów
* nazewnictwo snippetów:
    * plik nazywamy od nazwy snippeta następnie słowo snippet, np. **register_snippet.py**
    * klasy w snippetach nazywam od nazwy snippeta, następnie słowo snippet, np. **RegisterSnippet**
    
#### Assertions
* assercje piszemy jako osobne metody w snippetach których one dotyczą
* nazewnictwo metod assercji - zaczynam od słowa assert i czego dotyczy np. **"assert_prices_with_promo_code"**