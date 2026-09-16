"""
Cloud Inventory API - Main Application Service
Demonstrates Trunk-Based Development with Runtime Feature Flag Toggles.
"""

from feature_flags import flags

def get_app_info():
    return {
        "app_name": "Cloud Inventory API",
        "version": "1.0.0",
        "status": "online",
        "active_engine": "v2-async" if flags.is_enabled("ENABLE_V2_INVENTORY_ENGINE") else "v1-standard",
        "telemetry_stream": flags.is_enabled("ENABLE_REALTIME_TELEMETRY"),
        "analytics_export": flags.is_enabled("BETA_ANALYTICS_EXPORT")
    }

def run_service():
    print("=========================================================")
    print("  Booting Cloud Inventory API Microservice (v1.0.0)")
    print("=========================================================")
    app_info = get_app_info()
    for k, v in app_info.items():
        print(f"  * {k:20}: {v}")
    print("=========================================================")
    print("Service successfully initialized and listening on port 8000.")

if __name__ == "__main__":
    run_service()
