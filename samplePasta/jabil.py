import os
import time
import platform
import subprocess

# Lista de alvos internos que respondem ping
TARGETS = [
    "10.56.17.95",
    "10.56.17.92"
]

INTERVAL = 300  # segundos entre pings (300 = 5 minutos)

def ping_once(host: str, timeout_sec: int = 2) -> bool:
    sys = platform.system().lower()
    count_flag = "-n" if sys == "windows" else "-c"
    to_flag = "-w" if sys == "windows" else "-W"
    try:
        subprocess.check_call(
            ["ping", count_flag, "1", to_flag, str(timeout_sec), host],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return True
    except subprocess.CalledProcessError:
        return False
    except FileNotFoundError:
        return False

def main():
    target_index = 0
    while True:
        host = TARGETS[target_index]
        if not ping_once(host):
            # Se um alvo falhar, tenta o próximo
            target_index = (target_index + 1) % len(TARGETS)
        time.sleep(INTERVAL)


print('Sou o seu import')
if __name__ == "__main__":
    main()
