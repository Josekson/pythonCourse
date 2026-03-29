import tkinter as tk
from tkinter import scrolledtext

# ----------------- FUNÇÕES -----------------
def criar_tela(rodar_teste_callback):
    def on_ok():
        serial = entry_serial.get().strip()
        if not serial:
            clear_console()
            add_console("Nenhum serial informado.\n")
        else:
            clear_console()
            add_console(f"Serial recebido: {serial}\n")
            rodar_teste_callback(serial)
            # aqui você pode chamar sua função de teste com o serial
            # ex: rodar_teste(serial)

    def add_console(texto: str):
        console.configure(state="normal")
        console.insert(tk.END, texto)
        console.see(tk.END)
        console.configure(state="disabled")


    def clear_console():
        console.configure(state="normal")
        console.delete("1.0", tk.END)  # apaga tudo
        console.configure(state="disabled")



    # ----------------- JANELA PRINCIPAL -----------------
    root = tk.Tk()
    root.title("Teste de Serial")

    # Tamanho da janela
    LARGURA = 800
    ALTURA = 480

    # Centralizar na tela
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()
    pos_x = (largura_tela - LARGURA) // 2
    pos_y = (altura_tela - ALTURA) // 2
    root.geometry(f"{LARGURA}x{ALTURA}+{pos_x}+{pos_y}")

    # Cor de fundo azul
    root.configure(bg="#3b6fb3")  # azul parecido com o da imagem

    # ----------------- LAYOUT -----------------
    # Usando .place() pra posicionar mais “livre”, parecido com mockup

    # Label "Serial:"
    label_serial = tk.Label(
        root,
        text="Serial:",
        bg="#3b6fb3",
        fg="black",
        font=("Arial", 20, "bold")
    )
    label_serial.place(relx=0.5, rely=0.15, anchor="center")

    # Entrada de texto (serial)
    entry_serial = tk.Entry(
        root,
        font=("Arial", 15),
        width=25,
        justify="left"
    )
    entry_serial.place(relx=0.5, rely=0.23, anchor="center")

    # Botão OK
    button_ok = tk.Button(
        root,
        text="OK",
        font=("Arial", 20, "bold"),
        bg="#4CAF50",      # verde
        fg="black",
        activebackground="#45a049",
        width=6,
        command=on_ok
    )
    button_ok.bind("<Return>", lambda event: on_ok())
    button_ok.place(relx=0.5, rely=0.33, anchor="center")

    # Label "Console:"
    label_console = tk.Label(
        root,
        text="Console:",
        bg="#3b6fb3",
        fg="black",
        font=("Arial", 20, "bold")
    )
    label_console.place(relx=0.5, rely=0.48, anchor="center")

    # Caixa grande para console
    console = scrolledtext.ScrolledText(
        root,
        font=("Consolas", 14),
        width=50,
        height=8.5,
        state="disabled"   # começa desabilitado (somente leitura)
    )
    console.place(relx=0.5, rely=0.73, anchor="center")

    # Focar a entrada ao abrir
    entry_serial.focus_set()

    # Loop principal
    root.mainloop()