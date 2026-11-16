import socket
import datetime

HOST = "127.0.0.1"
PORT = 8000
LOG_FILE = "port_check.log"

def check_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    result = s.connect_ex((host, port))
    s.close()
    return result == 0

def write_log(message):
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")

def main():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    is_open = check_port(HOST, PORT)
    status = "OPEN" if is_open else "CLOSED"
    message = f"{now} | {HOST}:{PORT} | {status}"
    print(message)
    write_log(message)

if __name__ == "__main__":
    main()