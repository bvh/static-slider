#!/usr/bin/env bash

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

if [ ! -f "$SCRIPT_DIR/.env" ]; then
    echo "Error: .env file not found. Copy .env.example to .env and fill in your values." >&2
    exit 1
fi

source "$SCRIPT_DIR/.env"
SOURCE_PATH="$SCRIPT_DIR/public/"

echo "rsync -avz --delete --exclude '.*' $SOURCE_PATH $REMOTE_HOST:$REMOTE_PATH"
rsync -avz --delete --exclude '.*' "$SOURCE_PATH" "$REMOTE_HOST:$REMOTE_PATH"
