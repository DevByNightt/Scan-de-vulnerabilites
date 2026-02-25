<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=24&duration=3000&pause=1000&color=3498DB&center=true&vCenter=true&width=700&lines=Outil+de+Scan+de+Vuln%C3%A9rabilit%C3%A9s;D%C3%A9tection+de+Services+%26+Banni%C3%A8res;Python+Multi-Thread+%2B+Rapports+PDF" alt="Typing SVG" />
</p>

<h1 align="center">🛡️ <span style="color:#3498DB;">Scanner de Vulnérabilités Python</span></h1>
<p align="center">Outil multi-thread pour le scan de ports, la détection de services vulnérables et la génération de rapports.</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Actif-27AE60?style=for-the-badge&logo=checkmarx&logoColor=white" alt="Status"/>
  <img src="https://img.shields.io/badge/Projet-Perso-3498DB?style=for-the-badge&logo=bookstack&logoColor=white" alt="Projet"/>
  <img src="https://img.shields.io/badge/Langage-Python_3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Rapport-PDF_(fpdf2)-E74C3C?style=for-the-badge&logo=adobeacrobatreader&logoColor=white" alt="PDF"/>
  <img src="https://img.shields.io/badge/OS-Windows_%7C_Linux-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="OS"/>
</p>

---

### 🎯 À propos du projet

🚀 **Scanner de Vulnérabilités** est un projet étudiant conçu pour auditer la sécurité d'une machine cible. Il permet aux utilisateurs et administrateurs d'analyser **rapidement** une plage de ports et de vérifier si les services en cours d'exécution sont connus comme vulnérables.

📊 **Pourquoi ce projet ?**
* 🔍 **Contexte** : Fournir une approche d'audit réseau automatisée, avec un système de "Banner Grabbing".
* ⚙️ **Fonctionnalités** : Scan de ports multi-thread, récupération des bannières de services, détection via base de données CVE locale (JSON).
* 🔄 **Rapidité et Légèreté** : Écrit en Python standard (`socket`, `concurrent.futures`), il évite les lourdes dépendances et s'exécute sur Windows et Linux.
* 🌐 **Rapports Propres** : Création et formatage automatique d'un rapport de synthèse au format PDF recensant toutes les trouvailles et failles potentielles.

> "Du scan réseau à la synthèse des vulnérabilités, l'audit est entièrement documenté."

---

### 🛠️ Stack Technique

<div align="center">

**💡 Cœur du Scanner**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Sockets](https://img.shields.io/badge/R%C3%A9seau-Sockets_TCP-FF6F00?style=for-the-badge&logo=cisco&logoColor=white)
![JSON](https://img.shields.io/badge/BDD-JSON_Local-2E7D32?style=for-the-badge&logo=json&logoColor=white)

**🧮 Scripts & Modules**

![Threads](https://img.shields.io/badge/Scan-Multi--Thread-9C27B0?style=for-the-badge&logo=thealgorithms&logoColor=white)
![fpdf2](https://img.shields.io/badge/Rapport-fpdf2-E74C3C?style=for-the-badge&logo=pdf&logoColor=white)
![argparse](https://img.shields.io/badge/CLI-Argparse-007396?style=for-the-badge&logo=gnubash&logoColor=white)

</div>

---

### 📂 Navigation dans le projet

<div align="center">

| Fichier/Dossier | Description |
| :--- | :--- |
| `main.py` | Point d'entrée & Analyseur CLI principal. |
| `scanner.py` | Logique d'audit réseau et multi-threading. |
| `detector.py` | Comparaison et logique d'analyse de risques. |
| `vulnerability_db.json` | Base de données locale de failles connues (CVE). |
| `report.py` | Modèle de document PDF (Style `fpdf2`). |
| `dummy_server.py` | Serveur factice pour les tests locaux. |

</div>

---

### ⚡ Démarrage rapide

#### 1. Installation des Dépendances
Le script nécessite uniquement la librairie gérant les PDF (`fpdf2`).
```bash
# S'assurer d'être à la racine du projet
pip install -r requirements.txt
```

#### 2. Exécution du Scanner
La syntaxe d'appel est simple, modifiable via plusieurs arguments.
```bash
# Exemple de base : Scanner les ports locaux standards (1 à 1024)
python main.py localhost
```

**Options Avancées :**
```bash
# Renseignement des ports et threads
python main.py 127.0.0.1 -p 80-443 -t 100

# Générer un PDF avec un nom spécifique
python main.py scanme.nmap.org -p 1-1000 -o audit_result.pdf
```

#### 3. Démonstration Locale (Dummy Server)
Pour valider l'outil de détection, nous fournissons un service vulnérable émulé :
```bash
# 1. Dans un premier terminal (Lancer le faux service vulnérable vsFTPd 2.3.4)
python dummy_server.py

# 2. Dans un second terminal (Scanner le port spécifique)
python main.py localhost -p 8880-8890

# 3. Ouvrez report.pdf !
```

---

### 📄 Licence & Usage

<div align="center">

Projet réalisé dans le cadre d'un **Projet personnelle en Sécurité / Programmation Python**.
Ce scanner est fourni à des fins d'apprentissage et d'audit légal (sur des machines vous appartenant ou avec autorisation).

</div>

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:2C3E50,100:3498DB&height=120&section=footer&text=Outils-de-Scan%20|Par DevByNightt&fontColor=ffffff&fontSize=16&animation=fadeIn" />
</p>


