from fpdf import FPDF
from datetime import datetime
import os

class BasePDF(FPDF):
    def header(self):
        self.set_font("Helvetica", 'B', 15)
        self.set_text_color(41, 128, 185) # Bleu style moderne
        self.cell(0, 10, "Rapport de Scan de Vulnerabilites", border=False, ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

class ReportGenerator:
    def __init__(self, target, scan_results, vulnerabilities):
        self.target = target
        self.scan_results = scan_results
        self.vulnerabilities = vulnerabilities
        self.date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def generate(self, output_path="report.pdf"):
        pdf = BasePDF()
        pdf.add_page()
        
        # --- Section 1: Informations Générales ---
        pdf.set_font("Helvetica", 'B', 12)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(0, 10, "1. Informations Generales", ln=True)
        
        pdf.set_font("Helvetica", '', 11)
        pdf.cell(0, 8, f"Cible scannee : {self.target}", ln=True)
        pdf.cell(0, 8, f"Date d'execution : {self.date_str}", ln=True)
        pdf.cell(0, 8, f"Nombre de ports ouverts : {len(self.scan_results)}", ln=True)
        # Afficher en rouge s'il y a des vulnérabilités
        if self.vulnerabilities:
            pdf.set_text_color(231, 76, 60)
        pdf.cell(0, 8, f"Vulnerabilites detectees : {len(self.vulnerabilities)}", ln=True)
        pdf.set_text_color(0, 0, 0)
        pdf.ln(5)

        # --- Section 2: Ports Ouverts ---
        pdf.set_font("Helvetica", 'B', 12)
        pdf.cell(0, 10, "2. Ports Ouverts et Services (Bannieres)", ln=True)
        pdf.set_font("Courier", '', 10)
        
        if not self.scan_results:
            pdf.cell(0, 6, "Aucun port ouvert detecte.", ln=True)
        else:
            for res in self.scan_results:
                port = res['port']
                # Nettoyage de la bannière pour éviter les caractères ASCII problématiques
                banner = res['banner'].replace('\n', ' ').replace('\r', '') if res['banner'] else "Aucune banniere"
                # Tronquer si trop long
                if len(banner) > 80: 
                    banner = banner[:77] + "..."
                
                pdf.cell(0, 6, f"> Port {port:<5} : {banner}", ln=True)
        pdf.ln(5)

        # --- Section 3: Vulnérabilités ---
        pdf.set_font("Helvetica", 'B', 12)
        pdf.cell(0, 10, "3. Details des Vulnerabilites", ln=True)
        
        if not self.vulnerabilities:
            pdf.set_font("Helvetica", 'I', 11)
            pdf.set_text_color(39, 174, 96) # Vert
            pdf.cell(0, 10, "Excellente nouvelle : aucune vulnerabilite connue n'a ete identifiee.", ln=True)
        else:
            for v in self.vulnerabilities:
                pdf.set_font("Helvetica", 'B', 11)
                
                # Couleur selon la sévérité
                if "Critique" in v['severity']:
                    pdf.set_text_color(192, 57, 43) # Rouge foncé
                elif "Haute" in v['severity']:
                    pdf.set_text_color(231, 76, 60) # Rouge
                else:
                    pdf.set_text_color(243, 156, 18) # Orange
                    
                pdf.cell(0, 8, f"[+] Port {v['port']} - {v['banner_matched']} (Gravite: {v['severity']})", ln=True)
                
                pdf.set_text_color(0, 0, 0)
                pdf.set_font("Helvetica", '', 10)
                pdf.cell(0, 6, f"    CVE utilisee : {v['cve']}", ln=True)
                
                # Multi_cell pour la description qui peut être longue
                pdf.set_x(15)
                pdf.multi_cell(0, 6, f"Description : {v['description']}")
                pdf.ln(2)

        try:
            pdf.output(output_path)
            print(f"[*] Rapport genere avec succes : {os.path.abspath(output_path)}")
        except Exception as e:
            print(f"[!] Erreur lors de la generation du PDF : {e}")
