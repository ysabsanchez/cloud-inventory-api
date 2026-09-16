"""
Feature Flag Manager for Cloud Inventory API
Enables dynamic runtime toggles without redeploying application code.
Supports Trunk-Based Continuous Delivery.
"""

import json
import os
from pathlib import Path
from typing import Dict, Any, Optional

DEFAULT_CONFIG_PATH = Path(__file__).parent / "config.json"


class FeatureFlagManager:
    """Manages application feature flags with configuration file and environment overrides."""

    def __init__(self, config_path: Path = DEFAULT_CONFIG_PATH):
        self.config_path = config_path
        self._flags: Dict[str, Dict[str, Any]] = {}
        self.environment: str = "development"
        self.version: str = "1.0.0"
        self.load_configuration()

    def load_configuration(self) -> None:
        """Loads feature flags from configuration file."""
        if not self.config_path.exists():
            print(f"[WARN] Config file {self.config_path} not found. Running with default fallbacks.")
            return

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.environment = data.get("environment", "development")
                self.version = data.get("version", "1.0.0")
                self._flags = data.get("feature_flags", {})
                print(f"[INFO] Successfully loaded feature flags for environment: {self.environment}")
        except Exception as e:
            print(f"[ERROR] Failed to parse config file: {e}")

    def is_enabled(self, flag_name: str, default: bool = False) -> bool:
        """
        Check if a feature flag is enabled.
        Priority:
          1. Environment variable override (e.g. FF_ENABLE_V2_INVENTORY_ENGINE=true)
          2. Configuration file setting
          3. Default fallback
        """
        env_override = os.getenv(f"FF_{flag_name.upper()}")
        if env_override is not None:
            enabled = env_override.strip().lower() in ("1", "true", "yes", "on")
            print(f"[FLAG-EVAL] {flag_name} = {enabled} (via Environment Override)")
            return enabled

        if flag_name in self._flags:
            enabled = self._flags[flag_name].get("enabled", default)
            print(f"[FLAG-EVAL] {flag_name} = {enabled} (via config.json)")
            return enabled

        print(f"[FLAG-EVAL] {flag_name} = {default} (via Default Fallback)")
        return default

    def get_flag_details(self, flag_name: str) -> Optional[Dict[str, Any]]:
        """Retrieve metadata for a specific flag."""
        return self._flags.get(flag_name)

    def list_all_flags(self) -> Dict[str, Dict[str, Any]]:
        """Return all defined feature flags."""
        return self._flags


# Global singleton instance
flags = FeatureFlagManager()


if __name__ == "__main__":
    print("=" * 60)
    print(" Cloud Inventory API - Feature Flag Evaluation Demo")
    print("=" * 60)
    print(f"Environment: {flags.environment.upper()} | Version: {flags.version}\n")

    # Evaluate feature flags
    v2_engine = flags.is_enabled("ENABLE_V2_INVENTORY_ENGINE", default=False)
    telemetry = flags.is_enabled("ENABLE_REALTIME_TELEMETRY", default=False)
    analytics = flags.is_enabled("BETA_ANALYTICS_EXPORT", default=False)
    maintenance = flags.is_enabled("MAINTENANCE_MODE", default=False)

    print("\n--- Feature Behavior Execution ---")
    if v2_engine:
        print(">> [V2 Engine] High-throughput async processing pipeline ACTIVE.")
    else:
        print(">> [V1 Engine] Standard transactional processing pipeline ACTIVE (Stable Fallback).")

    if telemetry:
        print(">> [Telemetry] Realtime metrics dispatcher streaming to dashboard.")

    if analytics:
        print(">> [Analytics] Beta Parquet data exporter ENABLED.")

    if maintenance:
        print(">> [Warning] Maintenance mode ACTIVE - system in read-only mode.")
    else:
        print(">> [System Status] All systems operational (Read/Write mode).")

    print("=" * 60)
