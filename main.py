import argparse
import sys
import os
from scanner import Scanner
from detector import Detector
from report import ReportGenerator

def main():
    # Définition de l'interface ligne de commande (CLI)
    parser = argparse.ArgumentParser(
        description="Outil de scan de vulnerabilites en Python (Projet Etudiant)"
    )
    parser.add_argument("target", help="L'adresse IP ou le nom de domaine cible")
    parser.add_argument("-p", "--ports", default="1-1024", help="Plage de ports a scanner (ex: 1-1000). Par defaut: 1-1024")
    parser.add_argument("-t", "--threads", type=int, default=50, help="Nombre de threads maximum. Par defaut: 50")
    parser.add_argument("-o", "--output", default="report.pdf", help="Fichier PDF de sortie. Par defaut: report.pdf")

    args = parser.parse_args()

    # Analyse argument de plage de ports
    try:
        start_port, end_port = map(int, args.ports.split('-'))
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            raise ValueError
    except ValueError:
        print("[!] Erreur: La plage de ports est invalide. Utilisez le format 'start-end' (ex: 1-1024).")
        sys.exit(1)

    print(f"\n{'='*50}")
    print(f" SCANNER DE VULNERABILITES - PROJET ETUDIANT")
    print(f"{'='*50}\n")
    
    # --- ETAPE 1 : SCAN DES PORTS ---
    scanner = Scanner(args.target, start_port, end_port)
    scan_results = scanner.run(max_threads=args.threads)
    
    print(f"[*] Scan termine. {len(scan_results)} ports ouverts trouves.\n")
    
    # --- ETAPE 2 : ANALYSE DES VULNERABILITES ---
    print(f"[*] Analyse des bannieres pour detecter des vulnerabilites...")
    detector_db_path = os.path.join(os.path.dirname(__file__), "vulnerability_db.json")
    detector = Detector(db_path=detector_db_path)
    vulnerabilities = detector.analyze(scan_results)
    
    if vulnerabilities:
        print(f"[!] {len(vulnerabilities)} vulnerabilite(s) potentielle(s) detectee(s) !")
    else:
        print("[-] Aucune vulnerabilite connue n'a ete trouvee pour les services detectes.")
        
    # --- ETAPE 3 : GENERATION DU RAPPORT PDF ---
    print(f"\n[*] Generation du rapport PDF: {args.output}")
    report_gen = ReportGenerator(args.target, scan_results, vulnerabilities)
    report_gen.generate(args.output)
    
    print("\n[+] Processus termine avec succes.")

if __name__ == "__main__":
    main()
