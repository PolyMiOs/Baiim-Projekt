# Laboratorium: Analiza i symulacja ataków Denial of Service (DoS)

## Przygotowanie środowiska

### Docker

Aby przystąpić do laboratorium musisz mieć zainstalowany `docker` i `docker-compose`, a usługa dockera powinna zostać włączona. 
Następnie, aby zbudować i postawić kontenery skorzystaj z polecenia:

```bash
docker-compose up -d
```

**UWAGA!** Ze względu na tematykę, istnieje prawdopodobieństwo, że w trakcie laboratorium któryś z serwerów nie będzie w stanie obsługiwać kolejnych zapytań. W takim wypadku, należy usunąć instancje kontenerów (i postawić je na nowo)

```bash
docker-compose down
docker-compose up -d
```

### Python

Tworzenie środowiska wirtualnego

```bash
python -m venv .venv
source .venv/bin/activate
```

## Opis Laboratorium

Masz przygotowane dwa serwery **www**. Pierwszy pod adresem `127.0.0.1:8080`, drugi pod `https://127.0.0.1`. 

- Serwer http na porce 8080 działa pod protokołem HTTP/1.1 (Flask)
- Serwer https działa pod HTTP/2 (nodejs)

Do wykonania masz **cztery zadania**. 
Zadania nr 1, 2 i 4 polegają na uzupełnieniu brakujących elementów kodu, zgodnie ze wskazówkami **TODO** - forma znana z zajęć z kryptografii. 
Zadanie nr 3 zakłada wysłanie odpowiedniego żądania POST przy pomocy `curl`.

**WAŻNE!** Zalecane jest stałe sprawdzanie statystyk postawionych serwerów. Można to zrobić przy pomocy `docker stats`. 
Dodatkowo, w trakcie ataku dobrze jest sprawdzić, czy serwer jest w stanie obsłużyć wasze żądanie.
Należy pamiętać, że **nie wszystkie zadania zakładają całkowite przytłoczenie procesora** (patrz: zadanie 2).

---

## Zadanie 1: HTTP flood

Atakowany serwer: `127.0.0.1:8000`
Skrypt do uzupełnienia: `http_flood_attack.py`

Wiemy, że wskazany serwer wykonuje pewne ciężkie operacje pod endpointem `/heavy`. Twoim zadaniem jest zwykłe zasypanie go taką ilością żądań, która całkowicie zablokuje jego funkcjonowanie.

Aby zweryfikować poprawne działanie, sprawdź statystyki w `docker stats` i spróbuj wysłać jakieś żądanie.
Więcej informacji można znaleźć [tutaj](https://www.cloudflare.com/learning/ddos/http-flood-ddos-attack/)

## Zadanie 2: Low and slow

Atakowany serwer: `127.0.0.1:8000`
Skrypt do uzupełnienia: `lownslow.py`

Tym razem, zastosujemy metodę **low and slow**. Ataki tego typu wymierzone są w serwery oparte na wątkach. Mają one na celu wszystkich wątków powolnymi żadaniami, przesyłając bajt po bajcie. W ten sposób, połączenie jest ciągle zajęte przez pojedynczego hosta.

Warto zwrócić uwagę na statystyki kontenera. Czy serwer jest w stanie obsłużyć żądania? Na jakim poziomie zużycia procesora pracuje?

Więcej informacji można znaleźć [tutaj](https://www.cloudflare.com/learning/ddos/ddos-low-and-slow-attack/)

## Zadanie 3: ReDos

Atakowany serwer: `https://127.0.0.1`
Komenda do użycia: `curl -k -X POST -d "<regex>" https://127.0.0.1/search`

Operacje wykonywane po stronie serwera są z perspektywy użytkownika bardzo wygodne - strona powinna ładować się szybciej na słabszych komputerach. W takim wypadku nie należy jednak zapominać o bezpieczeństwie, w szczególności w wypadku, w którym dane wejściowe użytkownika mają wpływ na żłożoność algorytmiczną zadań.

Serwer https przyjmuje żądania POST pod endpointem `/search`. Umożliwia on nam wysłanie własne wyrażenie regularne, które przeszukuje zamieszczony tam skrypt *Pana Tadeusza*. 
Czy jesteś w stanie wysłać takie wyrażenie regularne, które całkowicie przytłoczy serwer (wystarczy pojedyncze żądanie)?

Więcej informacji można znaleźć [tutaj](https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS)

<details>
    <summary> Rozwiązanie zadania </summary>
    ```regex
    ^(([a-z ])+)+$
    ```
</details>

## Zadanie 4: Rapid reset

Atakowany serwer: `https://127.0.0.1`
Skrypt do uzupełnienia: `rapidreset.py`

Po wstępnym zebraniu informacji, dowiedziałeś/aś się, że serwer HTTP/2 pracuje na nodejs w wersji 18.15.
Jest on zatem podatny na ataki typu [rapid reset](https://www.cve.org/CVERecord?id=CVE-2023-44487)

Twoim zadaniem jest ciągłe otwieranie i zamykanie strumienia HTTP/2 tak, aby serwer nie był w stanie nadążyć. 

Więcej informacji można znaleźć [tutaj](https://blog.cloudflare.com/technical-breakdown-http2-rapid-reset-ddos-attack/)
