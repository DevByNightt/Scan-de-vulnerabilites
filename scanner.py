import socket
import concurrent.futures

class Scanner:
    def __init__(self, target, start_port, end_port, timeout=1.0):
        self.target = target
        self.start_port = start_port
        self.end_port = end_port
        self.timeout = timeout
        self.open_ports = []
        
    def scan_port(self, port):
        """Tente de se connecter à un port spécifique et de récupérer sa bannière."""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((self.target, port))
            
            if result == 0:
                banner = self.grab_banner(sock)
                self.open_ports.append({"port": port, "banner": banner})
            
            sock.close()
        except Exception:
            pass

    def grab_banner(self, sock):
        """Récupère la bannière envoyée par le service après connexion."""
        try:
            sock.settimeout(2.0)
            banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
            return banner
        except Exception:
            return ""

    def run(self, max_threads=50):
        """Exécute le scan en utilisant un pool de threads pour la rapidité."""
        # Résolution de la cible
        try:
            self.target = socket.gethostbyname(self.target)
        except socket.gaierror:
            print(f"Erreur: Impossible de résoudre l'adresse cible {self.target}")
            return []

        print(f"[*] Démarrage du scan sur {self.target} (Ports {self.start_port} à {self.end_port})")
        
        # Scan Multi-thread
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
            executor.map(self.scan_port, range(self.start_port, self.end_port + 1))
            
        # Trie des résultats par port croissant
        return sorted(self.open_ports, key=lambda x: x['port'])
