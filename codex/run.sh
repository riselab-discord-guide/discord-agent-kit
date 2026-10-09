#!/usr/bin/env bash
# Start the Codex bridge using the settings in codex/.env
cd "$(dirname "$0")"
set -a; source .env; set +a
exec python3 bridge.py
