# src/analyzer.py
import logging

class PacketAnalyzer:
    def analyze_packet(self, packet):
        # Analyse basique pour démonstration
        if packet.haslayer('ARP'):
            self.detect_arp_spoofing(packet)
        # Ajouter d'autres analyses selon vos besoins

    def detect_arp_spoofing(self, packet):
        logging.warning("Détection possible d'ARP spoofing!")

    def detect_port_scan(self, packet):
        logging.warning("Détection possible d'un scan de port!")

    def detect_sql_injection(self, packet):
        logging.warning("Tentative d'injection SQL détectée!")
