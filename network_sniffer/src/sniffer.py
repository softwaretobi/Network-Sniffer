# src/sniffer.py
from scapy.all import sniff
import logging

# Configurez le logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PacketSniffer:
    def __init__(self, interface=None):
        self.interface = interface

    def start_sniffing(self):
        logging.info("Démarrage de la capture des paquets...")
        sniff(iface=self.interface, prn=self.packet_handler, store=False)

    def packet_handler(self, packet):
        logging.info(f"Paquet capturé: {packet.summary()}")
        # Vous pouvez appeler l'analyseur ici si nécessaire
