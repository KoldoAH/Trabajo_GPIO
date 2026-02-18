# Trabajo_GPIO

Repositorio para subir las prácticas de la asignatura GPIO.

## Requisitos

- Docker Desktop instalado y corriendo

## Poner en marcha la primera vez

```bash
docker compose build --no-cache
docker compose up -d
```

si no funciona, probar con sudo

```bash
sudo docker compose build --no-cache
sudo docker compose up -d
```

## Acceder a la aplicación

| Recurso | URL                            |
| ------- | ------------------------------ |
| API     | http://localhost:5001/         |
| Swagger | http://localhost:5001/swagger/ |
| Frontend | http://localhost:5002/         |

## Parar la aplicación

```bash
docker compose down
```
