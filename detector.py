import json
import os

class Detector:
    def __init__(self, db_path="vulnerability_db.json"):
        self.db_path = db_path
        self.db = self._load_db()

    def _load_db(self):
        """Charge la base de données de vulnérabilités depuis le JSON."""
        if os.path.exists(self.db_path):
            with open(self.db_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            print(f"[!] Attention : Fichier de base de données introuvable ({self.db_path}).")
            return {}

    def analyze(self, scan_results):
        """Analyse les bannières pour y trouver des logiciels vulnérables."""
        vulnerabilities = []
        
        for result in scan_results:
            port = result['port']
            banner = result['banner']
            
            if not banner:
                continue

            # Comparaison de la bannière avec la base de vulnérabilités
            for vuln_key, vulns in self.db.items():
                if vuln_key.lower() in banner.lower():
                    for v in vulns:
                        vulnerabilities.append({
                            "port": port,
                            "banner_matched": vuln_key,
                            "full_banner": banner,
                            "cve": v.get("cve", "N/A"),
                            "severity": v.get("severity", "Inconnue"),
                            "description": v.get("description", "")
                        })
                        
        return vulnerabilities
