# WattWise AI — Smart Manufacturing Energy Copilot

Demo-ready AI/ML energy optimization platform for small manufacturing plants.

## Features
- Factory energy command center dashboard
- Machine-level energy monitoring
- Anomaly detection using baseline deviation
- Explainable AI-style root-cause recommendations
- Estimated cost and CO2 impact
- Ask the Factory assistant
- FastAPI backend + React/TypeScript frontend
- Synthetic telemetry dataset

## Run
### Backend
```bash
cd backend
python -m venv .venv
# Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

Open the Vite URL. The UI includes demo data and works without the backend; the backend provides matching API endpoints for future integration.

> Demo values are simulated. Replace them with real PLC/MQTT/sensor telemetry before operational use.
