
from setuptools import setup, find_packages

setup(
    name="network_sniffer",
    version="0.1.0",
    description="Un analyseur de paquets réseau pour surveiller le trafic et détecter les comportements suspects.",
    author="Juzo | Tobi",
    author_email="externout@proton.me",
    packages=find_packages(),
    install_requires=[
        "scapy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
