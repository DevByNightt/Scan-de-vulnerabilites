import socket
import sys

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 8888))
    s.listen(1)
    print("Serveur factice en écoute sur le port 8888...")
    
    # On accepte une seule connexion puis on ferme
    conn, addr = s.accept()
    # On envoie une bannière d'une version vulnérable connue dans notre JSON
    conn.send(b"220 (vsFTPd 2.3.4)\r\n")
    conn.close()
    s.close()
    print("Connexion terminee, fermeture du serveur factice.")

if __name__ == "__main__":
    start_server()
