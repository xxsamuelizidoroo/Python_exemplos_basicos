import customtkinter as ctk
from random import randint
from PIL import Image, ImageTk
import os
import sys

# Função para obter o caminho correto de arquivos, como imagens e ícones, tanto no desenvolvimento quanto no executável
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # Caminho temporário onde o PyInstaller coloca os arquivos
    except Exception:
        base_path = os.path.abspath(".")  # Caminho atual para desenvolvimento
    return os.path.join(base_path, relative_path)

# Configuração da aparência da interface (modo claro, escuro ou sistema)
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Janela principal
root = ctk.CTk()
root.geometry("520x350")
root.title("Gerador de senha")

# Tentativa de carregar o ícone da aplicação
try:
    icon_path = resource_path("senha1.ico")
    icon_image = Image.open(icon_path)
    icon_photo = ImageTk.PhotoImage(icon_image)
    root.iconphoto(False, icon_photo)
except Exception as e:
    print(f"Não foi possível carregar o ícone: {e}")

# Função para gerar uma nova senha aleatória
def new_rand():
    pw_entry.delete(0, ctk.END)
    pw_length = int(my_entry.get()) if my_entry.get() else 0  # Verifica se o valor é um número válido
    my_password = ''.join(chr(randint(33, 126)) for _ in range(pw_length))  # Gera senha com caracteres ASCII visíveis
    pw_entry.insert(0, my_password)
    pw_entry.configure(justify='center')  # Centraliza o texto da senha gerada

# Função para copiar a senha gerada para a área de transferência
def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())

# Função para limpar as entradas
def clear_entry():
    my_entry.delete(0, ctk.END)
    pw_entry.delete(0, ctk.END)

# Validação para garantir que o comprimento da senha seja numérico e não ultrapasse 32 caracteres
def validate_length(input):
    if input.isdigit() and len(input) <= 32:
        return True
    elif input == "":
        return True
    else:
        return False

# Registro da função de validação
validate_command = root.register(validate_length)

# Frame para entrada do comprimento da senha
lf = ctk.CTkFrame(root)
lf.pack(pady=20)

# Rótulo para o comprimento da senha
ctk.CTkLabel(lf, text="Quantos caracteres (Máximo 32)?", font=("Helvetica", 16)).pack(pady=10)

# Entrada para o comprimento da senha
my_entry = ctk.CTkEntry(lf, font=("Helvetica", 24), validate="key", validatecommand=(validate_command, '%P'), width=80, justify='center')
my_entry.pack(pady=10)

# Entrada para exibir a senha gerada
pw_entry = ctk.CTkEntry(root, font=("Helvetica", 24), justify='center', width=500)
pw_entry.pack(pady=20)

# Frame para os botões
my_frame = ctk.CTkFrame(root)
my_frame.pack(pady=20)

# Tentativa de carregar imagens para os botões
try:
    create_image = ctk.CTkImage(light_image=Image.open(resource_path("create.png")), size=(20, 20))
    copy_image = ctk.CTkImage(light_image=Image.open(resource_path("copy.png")), size=(20, 20))
    clean_image = ctk.CTkImage(light_image=Image.open(resource_path("clean.png")), size=(20, 20))
except Exception as e:
    print(f"Não foi possível carregar uma ou mais imagens: {e}")
    create_image = copy_image = clean_image = None  # Se não carregar as imagens, os botões ainda funcionarão sem ícones

# Botão para gerar senha forte (verde)
my_button = ctk.CTkButton(my_frame, text="Gerar senha forte", command=new_rand, image=create_image, compound="left", 
                          font=("Helvetica", 16), fg_color="#4CAF50", hover_color="#45a049")
my_button.grid(row=0, column=0, padx=10)

# Botão para copiar a senha gerada
clip_button = ctk.CTkButton(my_frame, text="Copiar", command=clipper, image=copy_image, compound="left", 
                            font=("Helvetica", 16))
clip_button.grid(row=0, column=1, padx=10)

# Botão para limpar os campos (laranja)
clear_button = ctk.CTkButton(my_frame, text="Limpar", command=clear_entry, image=clean_image, compound="left", 
                             font=("Helvetica", 16), fg_color="#FF9800", hover_color="#F57C00")
clear_button.grid(row=0, column=2, padx=10)

# Inicia o loop da interface gráfica
root.mainloop()
