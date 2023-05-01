import os
from dotenv import load_dotenv


load_dotenv()

class Settings:
    POSTGRESQL_USER: str = os.environ.get('POSTGRESQL_USER')
    POSTGRESQL_PASSWORD: str = os.environ.get('POSTGRESQL_PASSWORD')
    POSTGRESQL_SERVER: str = os.environ.get('POSTGRESQL_SERVER')
    POSTGRESQL_DB: str = os.environ.get('POSTGRESQL_DB')
    POSTGRESQL_PORT: str = os.environ.get('POSTGRESQL_PORT')
    # POSTGRESQL_SSL_MODE: str = os.environ.get('POSTGRESQL_SSL_MODE') not using for local development
    POSTGRESQL_URL: str = f"postgresql://{POSTGRESQL_USER}:{POSTGRESQL_PASSWORD}@{POSTGRESQL_SERVER}:{POSTGRESQL_PORT}/{POSTGRESQL_DB}"

    POSTGRESQL_INVENTORY_TABLE: str = os.environ.get('POSTGRESQL_INVENTORY_TABLE')


settings = Settings()