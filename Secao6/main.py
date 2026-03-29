# main.py
from screen import criar_tela
import cv2
import ctypes

nome_janela = "RESULTADO:"

win_w = 800
win_h = 480

# Pega resolução da tela (Windows)
user32 = ctypes.windll.user32
screen_w = user32.GetSystemMetrics(0)
screen_h = user32.GetSystemMetrics(1)

# Calcula posição para centralizar
pos_x = (screen_w - win_w) // 2
pos_y = (screen_h - win_h) // 2

cv2.namedWindow(nome_janela, cv2.WINDOW_NORMAL)
cv2.resizeWindow(nome_janela, win_w, win_h)

pass_path = 'Secao6\\pass_screen.png'
fail_path = 'Secao6\\fail_screen.png'
time_image = 2000

def mostrar_imagem_centrada(caminho_imagem:str):
    img = cv2.imread(caminho_imagem)
    if img is None:
        raise FileNotFoundError(f"Não consegui carregar a imagem em: {caminho_imagem}")

    # Mostra imagem
    cv2.imshow(nome_janela, img)

    # Move a janela para o centro (depois do imshow)
    cv2.moveWindow(nome_janela, pos_x, pos_y)

    cv2.waitKey(time_image)
    cv2.destroyAllWindows()


def rodar_teste(serial: str):
    """
    Aqui entra a sua lógica real de teste.
    Por enquanto vou só fazer um exemplo tosco:
    - Se o serial começa com 'P' -> PASS
    - Senão -> FAIL
    """
    print(f"[MAIN] Rodando teste para serial: {serial}")
    return serial



serial = criar_tela(rodar_teste)

if serial.startswith('T'):
    mostrar_imagem_centrada(pass_path)