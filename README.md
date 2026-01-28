# Laboratorium: Analiza i symulacja ataków Denial of Service (DoS)

## 1. Cel zajęć
Celem laboratorium jest praktyczne zrozumienie ataków typu DoS w różnych warstwach modelu OSI:
* **Warstwa 4 (Transportowa):** Atak SYN Flood wykorzystujący luki w protokole TCP.
* **Warstwa 7 (Aplikacji):** Atak HTTP Flood celujący w zasoby procesora (CPU Bound).

---

## 2. Przygotowanie środowiska (Ofiara)

Serwer został napisany w Node.js (Express), aby zademonstrować architekturę jednowątkową (Event Loop), która jest szczególnie podatna na blokowanie.

### Kroki wstępne:
1. Zainstaluj bibliotekę Express:  
   `npm install express`
2. Zapisz poniższy kod jako `server.js` i uruchom:  
   `node server.js`

```javascript
const express = require('express');
const crypto = require('crypto');
const app = express();

app.get('/', (req, res) => {
    res.send("Serwer działa poprawnie! (Strona lekka)");
});

app.get('/heavy', (req, res) => {
    let data = "test_data";
    // Symulacja ciężkiego zadania CPU (haszowanie)
    for (let i = 0; i < 200000; i++) {
        data = crypto.createHash('sha256').update(data).digest('hex');
    }
    res.send("Obliczenia zakończone.");
});

app.listen(8080, '0.0.0.0', () => {
    console.log("Serwer ofiary nasłuchuje na porcie 8080...");
});
