from flask import Flask, render_template, request, jsonify
import requests
import datetime
import logging
import os
import sys

# Konfiguracja logowania
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)


AUTOR = "Bartłomiej Niezbecki"
PORT = int(os.environ.get("PORT", 5000))

API_KEY = os.environ.get("WEATHER_API_KEY")
if not API_KEY:
    raise ValueError("Brak klucza API. Ustaw WEATHER_API_KEY.")

KRAJE_MIASTA = {
    "Polska": ["Warszawa", "Lublin", "Chełm", "Zamość", "Gdańsk"],
    "Dania": ["Kopenhaga", "Aalborg", "Odense", "Esbjerg", "Aarhus"],
    "Niemcy": ["Berlin", "Monachium", "Hamburg", "Frankfurt", "Kolonia"],
    "Szwajcaria": ["Zurych", "Genewa", "Bazylea", "Bern", "Lucerna"],
    "Austria": ["Wiedeń", "Graz", "Linz", "Salzburg", "Innsbruck"],
    "Czechy": ["Praga", "Brno", "Ołomuniec", "Liberec", "Ostrawa"],
    "Słowacja": ["Bratysława", "Koszyce", "Nitra", "Trnawa", "Zilina"]
}

@app.route('/health')
def health_check():
    return jsonify({"status": "OK"}), 200

@app.route('/')
def index():
    return render_template('index.html', kraje_miasta=KRAJE_MIASTA)

@app.route('/pogoda', methods=['POST'])
def pogoda():
    miasto = request.form.get('miasto')
    
    if not miasto:
        return jsonify({"error": "Nie wybrano miasta"}), 400
    
    # Pobieranie danych pogodowych z OpenWeatherMap oraz ewntualne błędy
    try:
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={miasto}&appid={API_KEY}&units=metric&lang=pl"
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f"Błąd podczas pobierania danych pogodowych: {e}")
        return jsonify({"error": "Błąd pobierania danych pogodowych"}), 500
    
    dane_pogodowe = response.json()
        
    # Przygotowanie danych do wyświetlenia
    pogoda_info = {
        "miasto": miasto,
        "temperatura": dane_pogodowe["main"]["temp"],
        "odczuwalna": dane_pogodowe["main"]["feels_like"],
        "wilgotność": dane_pogodowe["main"]["humidity"],
        "ciśnienie": dane_pogodowe["main"]["pressure"],
        "opis": dane_pogodowe["weather"][0]["description"],
        "wiatr": dane_pogodowe["wind"]["speed"]
    }
    
    return jsonify(pogoda_info)

if __name__ == "__main__":
    # Logowanie informacji o uruchomieniu
    data_uruchomienia = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logger.info(f"Data uruchomienia: {data_uruchomienia}")
    logger.info(f"Autor: {AUTOR}")
    logger.info(f"Nasłuchiwanie na porcie TCP: {PORT}")
    
    # Uruchomienie aplikacji
    app.run(host="0.0.0.0", port=PORT)