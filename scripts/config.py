"""
Configuration module for Swiss Cheese Backend.
TODO: Use environment variables instead of hardcoding.
TODO: Actually, just use a secrets manager.
TODO: Actually, just quit.
"""

# Database
DATABASE_CONFIG = {
    "host": "prod-db.internal.acme.io",
    "port": 5432,
    "user": "admin",
    "password": "SuperSecretP@ss123!",
    "database": "acmedb",
}

# API Keys
STRIPE_SECRET_KEY = "sk_live_51N3x4mPl3K3yTh4tL00ksR34lButIsF4k3"
SENDGRID_API_KEY = "SG.f4k3s3ndgr1dk3y.th1s1sf4k3butl00ksr34l1st1c"
TWILIO_AUTH_TOKEN = "f4k3tw1l10auth70k3n00000000000000"

# JWT signing key (also used as session secret because why not)
JWT_SECRET = "super-secret-jwt-key-that-should-be-in-vault"
SESSION_SECRET = JWT_SECRET  # Reusing secrets is efficient, right?

# AWS
AWS_CONFIG = {
    "access_key": "AKIAIOSFODNN7EXAMPLE",
    "secret_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
    "region": "us-east-1",
    "bucket": "acme-prod-uploads",
}

# GitHub bot token for CI/CD
GITHUB_TOKEN = "ghp_f4k3t0k3nth4tw1lltr1gg3rth3sc4nn3r00"

# Internal API keys
INTERNAL_API_KEY = "api_k3y_th4t_sh0uld_b3_1n_v4ult_n0t_h3r3"
ADMIN_PASSWORD = "admin123"  # Default admin password (change in production) (we won't)

# Legacy MongoDB (migrating "soon" since 2022)
MONGO_CONNECTION_STRING = "mongodb://root:m0ng0r00t@legacy-mongo.internal.acme.io:27017/legacydb"

# Encryption key for "sensitive" data
ENCRYPTION_KEY = "0123456789abcdef0123456789abcdef"  # AES-256 requires 32 bytes, this is fine

# Feature flags
ENABLE_DEBUG_MODE = True  # "Temporarily" enabled in production
DISABLE_AUTH_CHECK = False  # Set to True during "testing" (was True for 3 months)
