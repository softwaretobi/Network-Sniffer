# 🌐 Network Sniffer

Un analyseur de paquets réseau écrit en Python pour surveiller le trafic sur un réseau local et détecter des comportements suspects. 

## 🚀 Table des Matières

- [Fonctionnalités](#-fonctionnalités)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Exemple de Script](#-exemple-de-script)
- [Contribuer](#-contribuer)
- [Supportez le Projet](#-supportez-le-projet)

## ⭐ Fonctionnalités

- 🔍 Capture des paquets réseau en temps réel.
- 🚨 Analyse des paquets pour détecter des attaques telles que :
  - ARP Spoofing
  - Scans de port
  - Tentatives d'injection SQL
- 📊 Génération de rapports et alertes en cas de comportements suspects.

## ⭐ Prochainement 
- (MitM) - Add
- (Distributed Denial of Service) - Mitigation Basique
- DNS Spoofing - Add
- (RCE)


## 📦 Installation

Pour installer le module, exécutez la commande suivante dans votre terminal :

```bash
pip install git+https://github.com/softwaretobi/Network-Sniffer.git
```



## 🛠️ Utilisation

Voici comment utiliser le module dans un script Python :

1. Importez le module :

```python
from network_sniffer.sniffer import PacketSniffer
```

2. Initialisez le sniffer avec l'interface réseau souhaitée (par exemple, `lo` pour localhost) :

```python
sniffer = PacketSniffer(interface="lo")
```

3. Démarrez la capture des paquets :

```python
sniffer.start_sniffing()
```

## 💻 Exemple de Script

Voici un exemple complet de script que vous pouvez exécuter :

```python
# script_exemple.py
from network_sniffer.sniffer import PacketSniffer

def main():
    # Initialisation du sniffer
    sniffer = PacketSniffer(interface="lo")  # Changez "lo" par votre interface réseau
    print("Démarrage de la capture des paquets. Appuyez sur Ctrl+C pour arrêter.")
    
    # Démarrer le sniffer
    try:
        sniffer.start_sniffing()
    except KeyboardInterrupt:
        print("Capture des paquets arrêtée.")

if __name__ == "__main__":
    main()
```

### 📝 Exécution du Script

Pour exécuter le script, ouvrez votre terminal et exécutez la commande suivante :

```bash
python test.py
```

### ⚠️ Remarque

Pour exécuter le sniffer, vous devrez probablement le faire avec des privilèges d'administrateur. Utilisez `sudo` sur Linux/MacOS :

```bash
sudo python test.py
```

## 🤝 Contribuer

Les contributions sont les bienvenues ! Si vous souhaitez contribuer à ce projet, veuillez suivre les étapes suivantes :

1. Forkez le dépôt.
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/nouvelle-fonctionnalité`).
3. Faites vos modifications et commitez-les (`git commit -m 'Ajout d'une nouvelle fonctionnalité'`).
4. Poussez vers la branche (`git push origin feature/nouvelle-fonctionnalité`).
5. Ouvrez une Pull Request.

## 💖 Supportez le Projet

Si vous appréciez ce projet et souhaitez le soutenir, n'hésitez pas à lui donner une étoile ⭐ sur GitHub ! Cela nous aide à toucher plus de personnes et à améliorer le projet.

Merci d'avoir pris le temps de consulter ce projet. Vos retours sont toujours les bienvenus ! 🙌
