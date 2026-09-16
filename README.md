# Cloud Inventory API

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/ysabsanchez/cloud-inventory-api)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/ysabsanchez/cloud-inventory-api)
[![Release](https://img.shields.io/badge/release-v1.0--GA-success.svg)](https://github.com/ysabsanchez/cloud-inventory-api)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A high-performance cloud inventory management microservice built for scalable, distributed enterprise operations.

## Release Notes — Version 1.0.0 (General Availability)
The `v1.0.0` release stabilizes core endpoints, provides production readiness, and establishes trunk-based delivery pipelines:
- **Core Endpoints**: Fully validated `/health`, `/api/v1/inventory`, and `/api/v1/warehouses`.
- **Feature Flag Architecture**: Integrated JSON-driven feature flag evaluation engine (`config.json`).
- **Resilience**: Added error handling, logging instrumentation, and fallback routes.
- **Trunk-Based Release Line**: Maintained strictly for production deployment and emergency cherry-picks.

## Overview
The **Cloud Inventory API** provides centralized endpoints to register warehouses, track real-time stock levels, manage SKU metadata, and broadcast inventory delta events across distributed logistics services.

## Tech Stack
- **Language**: Python 3.12+
- **API Framework**: FastAPI / ASGI
- **Data Serialization**: Pydantic v2
- **Configuration Management**: JSON / YAML Environment Overrides
- **Testing**: PyTest, Coverage.py

## API Endpoints (v1.0 Production)

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| `GET` | `/health` | System health & cluster heartbeat | No |
| `GET` | `/api/v1/inventory` | Retrieve paginated stock list by SKU | Bearer Token |
| `POST` | `/api/v1/inventory/sync` | Ingest batch inventory delta records | Bearer Token |
| `GET` | `/api/v1/warehouses` | List registered fulfillment centers | Bearer Token |

### Sample Health Check Response
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "database": "connected",
  "timestamp": "2026-09-16T10:25:00Z"
}
```

## Configuration & Feature Flag Overrides
The application supports dynamic runtime feature flags loaded via `config.json`:

| Flag Name | Default | Description |
| :--- | :--- | :--- |
| `ENABLE_V2_INVENTORY_ENGINE` | `false` | Enables high-throughput async delta processing engine |
| `BETA_ANALYTICS_EXPORT` | `true` | Allows export of warehouse telemetry to cloud storage |
| `MAINTENANCE_MODE` | `false` | Safely routes requests to fallback read-only mirror |

## Getting Started

### Prerequisites
- Python 3.10 or higher
- Git 2.25+

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ysabsanchez/cloud-inventory-api.git
   cd cloud-inventory-api
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Service
```bash
python main.py
```

## Branching & Release Strategy
This project follows **Trunk-Based Development**. Releases are branched directly from `main` as short-lived release branches (`release/v1.0`), allowing rapid production hardening while active continuous integration continues unobstructed on the trunk.
