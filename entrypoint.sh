#!/bin/sh

set -e

echo "Running database initialisation..."
python -m init.main
echo "Database initialisation complete."

exec "$@"