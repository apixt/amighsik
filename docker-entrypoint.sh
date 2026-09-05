#!/bin/bash
set -e

# Install Playwright browsers if not already cached
if [ ! -d "/root/.cache/ms-playwright" ]; then
    echo "[setup] Installing Playwright browsers..."
    playwright install chromium
fi

echo "[setup] Ready to run application"
exec "$@"
