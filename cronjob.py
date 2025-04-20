import time
from invoice import create_invoices
from datetime import datetime
from logger import logger

def start_cronjob():
    duration_hours = 24
    interval_seconds = 3 * 60 * 60
    iterations = duration_hours // 3

    for i in range(iterations):
        logger.info(f"Execution {i+1}/{iterations} started:")
        create_invoices()
        if i < iterations - 1:
            time.sleep(interval_seconds)
