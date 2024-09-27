# tests/test_sniffer.py
import unittest
from src.sniffer import PacketSniffer

class TestPacketSniffer(unittest.TestCase):
    def test_initialization(self):
        sniffer = PacketSniffer(interface="lo")
        self.assertEqual(sniffer.interface, "lo")

if __name__ == "__main__":
    unittest.main()
