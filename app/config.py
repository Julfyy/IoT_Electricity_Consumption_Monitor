import os

class Config:
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_NAME = os.getenv("DB_NAME", "metric_data")
    DB_USER = os.getenv("DB_USER", "grafana")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "./received_images")
