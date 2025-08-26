#!/usr/bin/env bash
set -euo pipefail

# Build a distributable zip containing virtual env with dependencies preinstalled.
# Usage: ./scripts/build_zip.sh

APP_NAME=folder-vision
PYTHON=${PYTHON:-python3}
VENV_DIR=.venv_dist
DIST_DIR=dist

rm -rf "$VENV_DIR" "$DIST_DIR" "$APP_NAME".zip
$PYTHON -m venv "$VENV_DIR"
source "$VENV_DIR"/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Strip caches
find "$VENV_DIR" -name "__pycache__" -type d -exec rm -rf {} +

mkdir -p "$DIST_DIR/$APP_NAME"
cp -r folder_vision run.py requirements.txt pyproject.toml README.md "$DIST_DIR/$APP_NAME"/
cp -r "$VENV_DIR" "$DIST_DIR/$APP_NAME/.venv"

( cd "$DIST_DIR" && zip -r "${APP_NAME}.zip" "$APP_NAME" )

printf '\nCreated dist/%s.zip\n' "$APP_NAME"
