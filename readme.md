
Autor: Bartłomiej Niezbecki

## Etapy wykonania zadania
1. Utworzono plik `zadanie2.yml`, który definiuje łańcuch GitHub Actions.

2. W pliku workflow:
   - użyto `docker/build-push-action` do budowania obrazu dla architektur `linux/amd64` i `linux/arm64`
   - włączono cache dla builda z wykorzystaniem `docker.io/<nazwa_uzytkownika>/cache:latest`
   - wykonano push do rejestrów:
     - DockerHub: `docker.io/<użytkownik>/zadanie2chmura`
     - GHCR: `ghcr.io/chwasters/zadanie2chmura`
   - użyto `docker/scout-action` do sprawdzenia podatności obrazu
   - pipeline przerywa budowanie, jeśli wykryje zagrożenia CVE o poziomie HIGH lub CRITICAL

3. Do działania pipeline dodano następujące sekrety w GitHub Actions:
   - `DOCKER_USERNAME` i `DOCKERHUB_TOKEN` do logowania do DockerHub
   - `GHCR_TOKEN` (Personal Access Token) do logowania do GitHub Container Registry
   - `WEATHER_API_KEY` do działania aplikacji

4. Pipeline został uruchomiony automatycznie po wypchnięciu zmian do gałęzi `main`.
   - Budowa i push obrazu zakończyły się powodzeniem.
   - Docker Scout wykrył krytyczne podatności, przez co push został wstrzymany (zgodnie z założeniami).

## Podsumowanie

Repozytorium spełnia wszystkie wymagania:
- zawiera kod źródłowy, Dockerfile i pliki konfiguracji,
- zawiera poprawny plik workflow dla GitHub Actions,
- pipeline został uruchomiony i poprawnie zadziałał.
