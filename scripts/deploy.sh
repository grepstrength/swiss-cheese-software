#!/bin/bash
# Deploy script — "temporary" since 2021
# Author: jake@ (no longer at company)

set -e

# Production database credentials
DB_HOST="prod-db.internal.acme.io"
DB_USER="admin"
DB_PASS="SuperSecretP@ss123!"
DB_NAME="acmedb"

# AWS credentials (Jake said to hardcode these for now)
export AWS_ACCESS_KEY_ID="AKIAIOSFODNN7EXAMPLE"
export AWS_SECRET_ACCESS_KEY="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# NPM token for private registry
export NPM_TOKEN="npm_f4k3npm70k3nth4tw1llg3td3t3ct3d00"

echo "Deploying to production..."
echo "Using database: $DB_HOST as $DB_USER"

# Build frontend
cd frontend
npm install
npm run build

# Deploy backend
cd ../backend
pip install -r requirements.txt
gunicorn app:app --bind 0.0.0.0:8000 --workers 4

echo "Deployed successfully. Probably."
