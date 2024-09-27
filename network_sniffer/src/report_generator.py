# src/report_generator.py
import logging

class ReportGenerator:
    @staticmethod
    def generate_alert(message):
        logging.error(f"ALERTE: {message}")

    @staticmethod
    def generate_report(packet_summary):
        logging.info(f"Rapport de paquet: {packet_summary}")
