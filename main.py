"""
Cloud Inventory API - Entry point
"""

def get_app_info():
    return {
        "app_name": "Cloud Inventory API",
        "version": "0.1.0",
        "status": "online"
    }

if __name__ == "__main__":
    info = get_app_info()
    print(f"Starting {info['app_name']} v{info['version']}...")
