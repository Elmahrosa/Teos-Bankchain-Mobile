run-backend:
    uvicorn backend.src.main:app --reload

test-backend:
    pytest backend/tests

docker-up:
    docker-compose up -d

docker-down:
    docker-compose down
