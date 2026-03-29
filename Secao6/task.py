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

# Exemplo de uso
if __name__=='__main__':
    teste_passou = False
    if teste_passou:
        mostrar_imagem_centrada(pass_path)
    else:
        mostrar_imagem_centrada(fail_path)
