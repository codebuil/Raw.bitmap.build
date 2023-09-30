import tkinter as tk
from tkinter import filedialog
from PIL import Image
values = []
# Função para abrir uma imagem
def abrir_imagem():
    global imagem_original
    global imagem_convertida

    file_path = filedialog.askopenfilename(filetypes=[("Imagens", "*.bmp;*.jpg;*.png;*.gif")])
    if file_path:
        values = []
        imagem_original = Image.open(file_path)
        imagem_convertida = converter_imagem(imagem_original)
        imagem_original.show()

# Função para converter a imagem
def converter_imagem(imagem):
    largura, altura = imagem.size
    imagem_converted = Image.new("P", (largura, altura))

    for x in range(largura):
        for y in range(altura):
            r, g, b, _ = imagem.getpixel((x, y))

            # Calcular o valor da cor com base nas regras
            cor = 0
            if b > 63:
                cor |= 1
            if b > 63 and g > 63:
                cor |= 2
            if b > 63 and g > 63 and r > 63:
                cor |= 4
            if r > 128 or g > 128 or b > 128:
                cor |= 8

            values.append(cor)

    

# Função para salvar a imagem convertida como .raw
def salvar_imagem_raw():
   # Salve os valores em um arquivo RAW
   with open('output.raw', 'wb') as file:
       file.write(bytearray(values))

# Criar a janela principal
janela = tk.Tk()
janela.title("Conversor de Imagem")
janela.geometry("400x400")
janela.configure(bg="blue")

# Caixa de texto
caixa_texto = tk.Entry(janela)
caixa_texto.pack(pady=20)

# Botão para abrir uma imagem
botao_abrir = tk.Button(janela, text="Abrir Imagem", command=abrir_imagem)
botao_abrir.pack()

# Botão para salvar a imagem convertida como .raw
botao_salvar = tk.Button(janela, text="Salvar como .raw", command=salvar_imagem_raw)
botao_salvar.pack()

# Variáveis globais para as imagens
imagem_original = None
imagem_convertida = None

janela.mainloop()

