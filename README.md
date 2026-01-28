# Laboratorium: Analiza i symulacja ataków Denial of Service (DoS)

## 1. Cel zajęć
Celem laboratorium jest praktyczne zrozumienie ataków typu DoS w różnych warstwach modelu OSI:
* **Warstwa 4 (Transportowa):** Atak SYN Flood (TCP).
* **Warstwa 7 (Aplikacji):** Atak HTTP Flood (Resource Exhaustion).

---

## 2. Środowisko (Serwer Ofiary)

Serwer pracuje w środowisku Python (Flask). Twoim zadaniem jest zaobserwowanie, jak pojedynczy proces serwera radzi sobie z nadmiarem zapytań.

**Kod serwera (`server.py`):**
```python
from flask import Flask
import hashlib

app = Flask(__name__)

@app.route('/')
def home():
    return "Serwer dziala! Sprobuj mnie powalic na /heavy."

@app.route('/heavy')
def heavy_task():
    data = "some_random_data_to_hash"
    # Symulacja ciężkiej pracy procesora
    for _ in range(100_000):
        data = hashlib.sha256(data.encode()).hexdigest()
    return f"Operacja zakonczona."

if __name__ == '__main__':
    # threaded=False sprawia, że serwer przetwarza tylko 1 żądanie na raz
    app.run(host='0.0.0.0', port=8080, threaded=False)
