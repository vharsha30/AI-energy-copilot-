# ⚡ WattWise AI — Energy Copilot for Smart Manufacturing

> **AI-powered energy intelligence for factories — detect energy waste, understand why it happens, and discover opportunities to reduce cost and carbon emissions.**

WattWise AI is an AI/ML-powered energy monitoring and optimization platform designed for manufacturing environments.

Instead of simply displaying electricity consumption, WattWise AI analyzes machine-level telemetry to identify unusual energy usage, highlight potential sources of waste, estimate cost and CO₂ impact, and provide actionable recommendations through an AI Copilot.

## 🚀 What Problem Does It Solve?

Manufacturing machines can consume significant amounts of electricity even when they are:

* Running without production
* Operating during unnecessary idle periods
* Consuming more energy than their normal baseline
* Showing unusual operating patterns
* Contributing to avoidable energy costs and emissions

Traditional dashboards show **what happened**.

WattWise AI aims to answer:

> **Which machine is wasting energy, why is it happening, and what can we do about it?**

---

## ✨ Key Features

### 📊 Factory Energy Dashboard

Monitor the overall energy profile of a manufacturing facility.

* Total energy consumption
* Estimated electricity cost
* CO₂ footprint
* Machine-level energy usage
* Energy deviation from baseline
* Detected anomalies

### 🤖 AI Energy Copilot

Ask questions about the factory's energy performance in natural language.

Example:

> **Why did energy consumption increase today?**

The Copilot analyzes the available telemetry and identifies machines contributing to abnormal consumption.

### 🔎 Machine-Level Anomaly Detection

WattWise compares machine energy consumption against expected baseline behavior.

Example:

```text
Compressor 02

Energy Consumption: 74 kWh
Expected Baseline: 51 kWh
Deviation: +45.1%
Idle Time: 62%
Production Output: 0 units

Status: High Priority
```

The combination of high energy usage, excessive idle time, and zero production output makes the machine a potential energy-waste source.

### 💰 Savings Estimation

The system estimates potential financial savings from reducing inefficient machine operation.

### 🌱 CO₂ Impact

Energy consumption is converted into an estimated carbon footprint, helping visualize the environmental impact of energy waste.

### 📈 Energy Analytics

Interactive charts allow users to compare:

* Actual energy consumption
* Expected baseline
* Machine performance
* Energy trends

---

## 🧠 How It Works

```text
Machine Telemetry
       │
       ▼
┌───────────────────┐
│ Data Processing   │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ Energy Baselines  │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ Anomaly Detection │
└─────────┬─────────┘
          │
          ▼
┌──────────────────────┐
│ AI Insight Generation│
└──────────┬───────────┘
           │
           ▼
┌──────────────────────────┐
│ Recommendations & Savings│
└──────────────────────────┘
```

The architecture is designed so that simulated telemetry can later be replaced with real industrial data sources such as sensors, PLCs, or MQTT streams.

---

## 🏭 Example Insight

Suppose a compressor normally consumes approximately **51 kWh**, but the current telemetry shows **74 kWh**.

WattWise AI identifies:

* 45.1% energy deviation
* 62% idle operation
* 0 production output

The system can then recommend investigating:

* Unnecessary operating schedules
* Unloaded compressor operation
* Compressed-air leaks
* Pressure settings
* Maintenance requirements

This converts raw telemetry into an actionable energy-management insight.

---

## 💬 AI Copilot Examples

### Question

```text
Which machine is wasting the most energy?
```

### Example Response

```text
Compressor 02 has the highest energy deviation,
consuming approximately 45% more energy than its
baseline. It also has 62% idle time and zero output,
making it a high-priority machine to investigate.
```

### Question

```text
How much can we save?
```

### Example Response

```text
Based on the current simulated telemetry, the estimated
potential saving is approximately ₹8,400 per month.

The actual saving will depend on the factory's electricity
tariff, machine operating schedule, and real telemetry.
```

---

## 🛠️ Tech Stack

### Frontend

* React
* TypeScript
* Vite
* Recharts
* Lucide React
* CSS

### Backend

* Python
* FastAPI
* Uvicorn
* Pydantic

### AI / ML Direction

* Machine-level anomaly detection
* Baseline deviation analysis
* Energy optimization
* Explainable recommendations
* Natural-language AI Copilot

---

## 📂 Project Structure

```text
WattWise-AI/
│
├── frontend/
│   ├── src/
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   └── styles.css
│   ├── package.json
│   ├── tsconfig.json
│   └── vite.config.ts
│
├── backend/
│   ├── main.py
│   └── requirements.txt
│
├── data/
│   └── sample_telemetry.csv
│
├── docs/
│   └── HACKATHON_DEMO.md
│
└── README.md
```

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/wattwise-ai-energy-copilot.git

cd wattwise-ai-energy-copilot
```

### 2. Start the Backend

```bash
cd backend

python -m venv .venv
```

#### Windows

```bash
.venv\Scripts\activate
```

#### Install dependencies

```bash
pip install -r requirements.txt
```

#### Start FastAPI

```bash
uvicorn main:app --reload --port 8000
```

Backend:

```text
http://localhost:8000
```

---

### 3. Start the Frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Open the local URL shown by Vite.

---

## 📡 API Endpoints

### Health Check

```http
GET /api/health
```

### Factory Overview

```http
GET /api/overview
```

### AI Copilot

```http
GET /api/copilot?question=Why did energy consumption increase today?
```

---

## 📊 Demo Telemetry

The current demo includes simulated machine telemetry containing:

```text
Timestamp
Machine
Energy Consumption
Baseline Energy
Idle Percentage
Temperature
Production Output
```

Example:

```csv
timestamp,machine,energy_kwh,baseline_kwh,idle_pct,temperature_c,output_units
2026-09-29 11:00,Compressor 02,56,39,51,39,0
2026-09-29 12:00,Compressor 02,61,42,62,40,0
```

> **Note:** The current demonstration uses simulated telemetry. Temperature and energy values are not connected to live industrial sensors.

---

## 🔮 Future Improvements

WattWise AI is designed to evolve from a prototype into a real industrial energy-intelligence platform.

### Planned improvements

* [ ] Real-time MQTT sensor integration
* [ ] PLC/SCADA data integration
* [ ] Real-time temperature and energy monitoring
* [ ] Isolation Forest / Autoencoder anomaly detection
* [ ] Energy consumption forecasting
* [ ] Machine failure correlation
* [ ] SHAP-based explainability
* [ ] What-if savings simulator
* [ ] Automated optimization recommendations
* [ ] Peak-demand prediction
* [ ] Multi-factory monitoring
* [ ] Historical energy analytics
* [ ] Cloud deployment
* [ ] Role-based factory dashboards

---

## 🌱 Sustainability Impact

WattWise AI focuses on reducing energy waste rather than simply monitoring consumption.

By identifying machines that consume energy inefficiently, the platform can help organizations:

**Reduce Energy Waste → Reduce Operating Cost → Reduce CO₂ Emissions**

The system can also provide measurable before-and-after comparisons after optimization actions are implemented.

---


## 👩‍💻 Author

**Harsha V**

AI/ML Engineer | Generative AI | Computer Vision | Intelligent Systems

GitHub: `@vharsha30`

---

## ⭐ If You Like This Project

If you find WattWise AI interesting, consider giving the repository a ⭐ and following the project as it evolves toward real-time industrial energy intelligence.
