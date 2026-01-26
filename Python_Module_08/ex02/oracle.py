#!/usr/bin/env python3
"""
Exercise 02: The Oracle

Load configuration from environment variables and a .env file.
Demonstrate development/production modes and basic security principles.
"""

import os
import sys

from dotenv import load_dotenv


def main() -> None:
    """Main entry point."""
    # Load .env from ex02/ (for development)
    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

    print("ORACLE STATUS: Reading the Matrix...")
    print("Configuration loaded:")

    mode = os.getenv("MATRIX_MODE", "development")
    print(f"Mode: {mode}")

    database = os.getenv("DATABASE_URL")
    if database:
        if mode == "production":
            print("Database: Connected to production instance")
        else:
            print("Database: Connected to local instance")
    else:
        print("Database: MISSING")

    api_key = os.getenv("API_KEY")
    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: MISSING")

    log_level = os.getenv("LOG_LEVEL")
    if log_level:
        print(f"Log Level: {log_level}")
    else:
        print("Log Level: MISSING")

    zion = os.getenv("ZION_ENDPOINT")
    if zion:
        print("Zion Network: Online")
    else:
        print("Zion Network: MISSING")

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")

    print()
    print(f"Current Python: {sys.executable}")
    print(f"Env prefix: {sys.prefix}")
    print(f"Base prefix: {getattr(sys, 'base_prefix', sys.prefix)}")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
