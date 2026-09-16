# Cloud Inventory API

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/ysabsanchez/cloud-inventory-api)
[![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)](https://github.com/ysabsanchez/cloud-inventory-api)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A high-performance cloud inventory management microservice built for scalable, distributed enterprise operations.

## Overview
The **Cloud Inventory API** provides centralized endpoints to register warehouses, track real-time stock levels, manage SKU metadata, and broadcast inventory delta events across distributed logistics services.

## Tech Stack
- **Language**: Python 3.12+
- **API Framework**: FastAPI / ASGI
- **Data Serialization**: Pydantic v2
- **Configuration Management**: JSON / YAML Environment Overrides
- **Testing**: PyTest, Coverage.py

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
This project follows **Trunk-Based Development** paired with short-lived feature branches and configuration-driven feature flags for seamless continuous integration and zero-downtime delivery.
