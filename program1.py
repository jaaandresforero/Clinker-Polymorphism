import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


def upload_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    if file_path:
        img = Image.open(file_path)
        img = img.resize((300, 300))  # Removendo Image.ANTIALIAS para evitar erro
        img = ImageTk.PhotoImage(img)
        label_image.config(image=img)
        label_image.image = img  # Mantém a referência da imagem


# Criando a janela principal
root = tk.Tk()
root.title("PolymorphismPro")
root.geometry("400x450")
root.configure(bg="black")  # Definindo o fundo preto

# Adicionando um logo no canto superior direito
logo_path = "G:\Meu Drive\C5Lab\Polymorphism\logoC5lab.png"  # Substitua pelo caminho do seu logo
try:
    logo_img = Image.open(logo_path)
    logo_img = logo_img.resize((80, 70))  # Ajuste o tamanho conforme necessário
    logo_img = ImageTk.PhotoImage(logo_img)
    label_logo = tk.Label(root, image=logo_img)
    label_logo.image = logo_img
    label_logo.place(x=330, y=10)  # Posiciona no canto superior direito
except Exception as e:
    print(f"Erro ao carregar o logo: {e}")

# Botão para carregar imagem
btn_upload = tk.Button(root, text="Upload Image", command=upload_image)
btn_upload.pack(pady=20)

# Label para exibir a imagem
label_image = tk.Label(root)
label_image.pack()

# Inicia o loop principal da interface gráfica
root.mainloop()
