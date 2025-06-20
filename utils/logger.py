import logging
from pythonjsonlogger import jsonlogger
import os

class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super().add_fields(log_record, record, message_dict)
        log_record['source'] = 'agentic-ai-scan'

def get_logger(name="scan-agent"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        # Console
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(CustomJsonFormatter(
            fmt='%(asctime)s %(levelname)s %(name)s %(message)s'
        ))
        logger.addHandler(stream_handler)

        # Arquivo JSON
        os.makedirs("outputs", exist_ok=True)
        file_handler = logging.FileHandler("outputs/agentic-scan.log")
        file_handler.setFormatter(CustomJsonFormatter(
            fmt='%(asctime)s %(levelname)s %(name)s %(message)s'
        ))
        logger.addHandler(file_handler)

    return logger
