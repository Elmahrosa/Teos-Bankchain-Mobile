#!/usr/bin/env bash
set -euo pipefail

BRANCH="scaffold/backend-health"
ROOT="$(pwd)"

# Safety: require clean working tree
if [ -n "$(git status --porcelain)" ]; then
  echo "Please commit or stash changes before running this script."
  exit 1
fi

git checkout -b "$BRANCH"

# Create directories
mkdir -p backend/app backend/tests .github/workflows docker/backend android ios blockchain compliance docs

# backend app
cat > backend/app/main.py <<'PY'
from fastapi import FastAPI

app = FastAPI(title="TEOS Backend (health)")

@app.get("/health")
async def health():
    return {"status": "ok"}
PY

# requirements
cat > backend/requirements.txt <<'REQ'
fastapi
uvicorn[standard]
pytest
httpx
REQ

# test
cat > backend/tests/test_health.py <<'TST'
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}
TST

# GitHub Actions CI workflow
cat > .github/workflows/ci.yml <<'YML'
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.11"
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r backend/requirements.txt
      - name: Run tests
        run: |
          pytest -q
YML

# Dockerfile
mkdir -p docker/backend
cat > docker/backend/Dockerfile <<'DOCK'
FROM python:3.11-slim

WORKDIR /app

COPY backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY backend ./backend

CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
DOCK

# docker-compose
cat > docker-compose.yml <<'DC'
version: "3.8"
services:
  backend:
    build:
      context: .
      dockerfile: docker/backend/Dockerfile
    ports:
      - "8000:8000"
    environment:
      - ENV=dev
DC

# .gitignore
cat > .gitignore <<'IGN'
# Python
__pycache__/
*.py[cod]
.env
.venv/
venv/
*.egg-info/

# IDEs
.vscode/
.idea/

# Android / iOS common
*.keystore
IGN

# Placeholder READMEs
cat > android/README.md <<'A_R'
# Android module (placeholder)
This directory will hold the native Android app (Kotlin/Jetpack Compose).
To contribute: create a Kotlin Android project under this folder and add build/run steps.
A_R

cat > ios/README.md <<'I_R'
# iOS module (placeholder)
This directory will hold the native iOS app (Swift/SwiftUI).
To contribute: add an Xcode project here and include build/run docs.
I_R

cat > blockchain/README.md <<'B_R'
# Blockchain connectors (placeholder)
Implements connectors to Ethereum, Pi Network, Bitcoin, etc.
Suggested layout:
- connectors/
- tests/
- docker/
B_R

cat > compliance/README.md <<'C_R'
# Compliance (placeholder)
KYC/AML modules, monitoring, regulatory adapters.
Include README that describes how to run the compliance simulator locally.
C_R

cat > docs/README.md <<'D_R'
# Docs
Project docs live here: architecture, API references, compliance guides.
D_R

# Commit & push
git add .
git commit -m "Add backend health endpoint, tests, CI workflow, docker and placeholders for modules"
git push --set-upstream origin "$BRANCH"

echo "Created branch $BRANCH and pushed to origin. Open a PR from this branch to main."
