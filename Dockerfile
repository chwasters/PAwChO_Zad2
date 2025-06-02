FROM python:3.9-alpine AS builder

LABEL org.opencontainers.image.authors="Bartłomiej Niezbecki"
LABEL org.opencontainers.image.description="Aplikacja pogodynka"

WORKDIR /build

RUN apk add --no-cache --virtual .build-deps gcc musl-dev

# Kopiowanie i instalacja zależności
COPY requirements.txt .
RUN pip wheel --no-cache-dir --wheel-dir /build/wheels -r requirements.txt

# Etap finalny
FROM python:3.9-alpine

LABEL org.opencontainers.image.authors="Bartłomiej Niezbecki"
LABEL org.opencontainers.image.description="Aplikacja pogodynka"

ENV PORT=5000 
WORKDIR /app

# Kopiowanie zbudowanych pakietów i instalacja
COPY --from=builder /build/wheels /wheels
RUN pip install --no-cache /wheels/* && \
    rm -rf /wheels /root/.cache

COPY app.py .
COPY templates templates/

# heatlhcheck
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD wget -q --spider http://localhost:${PORT}/ || exit 1

EXPOSE ${PORT}

CMD ["python", "app.py"]