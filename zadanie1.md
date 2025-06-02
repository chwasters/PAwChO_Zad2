# Sprawozdanie – Zadanie 1 Aplikacja pogodowa

## Autor:
**Bartłomiej Niezbecki**

**Repozytorium z kodem źródłowym (GitHub):**  
  https://github.com/chwasters/PAwChO_Zad1Obo

**Obraz kontenera na DockerHub:**  
  https://hub.docker.com/r/bniezbecki/pogodynka


### a) Budowanie obrazu:
docker build -t aplikacja-pogoda:latest .


### b) Uruchomienie kontenera:
docker run -d -p 5000:5000 -e WEATHER_API_KEY= :)) --name aplikacja-pogoda

### Komentarz: 
Uruchamiamy kontener o nazwie aplikacja-pogoda, mapując port 5000 kontenera na port 5000 hosta. Przełącznik -d oznacza tryb pracy w tle oraz podajemy klucz api

### c) Logi:
docker logs pogoda

### d) Sprawdzenia warstwy i rozmiaru:
docker images (rozmiar i ID)
docker history 18886dd90011(Ilość warstw) 

Reszta kodu znajduje się w repozytorium:

app.py – główny plik aplikacji

Dockerfile – plik budujący obraz

requirements.txt – zależności Pythona

templates/ – folder z szablonami HTML