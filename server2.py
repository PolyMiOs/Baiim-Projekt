from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import hashlib

app = Flask(__name__)

# Inicjalizacja limitera
# get_remote_address oznacza, że identyfikujemy napastnika po jego IP
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)

@app.route('/')
def home():
    return "Serwer bezpieczny. Przejdź na /heavy, ale nie przesadzaj!"

@app.route('/heavy')
# TUTAJ JEST OBRONA: Tylko 2 zapytania na minutę dla jednego IP
@limiter.limit("2 per minute")
def heavy_task():
    data = "some_random_data_to_hash"
    for _ in range(100_000):
        data = hashlib.sha256(data.encode()).hexdigest()
    
    return f"Operacja zakończona. Wynik: {data[:10]}..."

# Obsługa błędu przekroczenia limitu (żeby ładnie wyglądało w przeglądarce)
@app.errorhandler(429)
def ratelimit_handler(e):
    return "STOP! Wykryto zbyt wiele zapytań. Atak DDoS powstrzymany.", 429

if __name__ == '__main__':
    # threaded=True pozwala obsługiwać normalnych użytkowników, 
    # podczas gdy inni są blokowani przez limiter.
    app.run(host='0.0.0.0', port=8080, threaded=True)