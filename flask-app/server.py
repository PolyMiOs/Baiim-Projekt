from flask import Flask, request
import time
import hashlib

app = Flask(__name__)

@app.route('/')
def home():
    return "Serwer dziala! Sprobuj mnie powalic na /heavy."

@app.route('/heavy')
def heavy_task():
    # Symulacja pracy: hashowanie danych 100 000 razy
    data = "some_random_data_to_hash"
    for _ in range(100_000):
        data = hashlib.sha256(data.encode()).hexdigest()
    
    return f"Operacja zakonczona. Wynik: {data[:10]}..."

if __name__ == '__main__':
    # threaded=False -> serwer bedzie obslugiwal tylko jedno zadanie na raz
    app.run(host='0.0.0.0', port=8080, threaded=False)