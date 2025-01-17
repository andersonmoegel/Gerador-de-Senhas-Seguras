import random
import string
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk, simpledialog, filedialog

# Função para gerar senhas com base nas preferências do usuário
def gerar_senha(segura=True, comprimento=12, maiusculas=True, minusculas=True, numeros=True, simbolos=True, memorizavel=False):
    if comprimento < 4:
        raise ValueError("O comprimento da senha deve ser pelo menos 4 para ser segura.")

    # Caracteres permitidos com base nas preferências do usuário
    caracteres = ""
    if maiusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation

    if memorizavel:
        palavras = ["livro", "gato", "sol", "janela", "computador", "feliz"]
        senha = random.choice(palavras) + str(random.randint(100, 999))
    else:
        senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    
    return senha

# Função para avaliar a força da senha
def avaliar_forca_senha(senha):
    comprimento = len(senha)
    tem_maiusculas = any(c.isupper() for c in senha)
    tem_minusculas = any(c.islower() for c in senha)
    tem_numeros = any(c.isdigit() for c in senha)
    tem_simbolos = any(c in string.punctuation for c in senha)
    pontuacao = sum([comprimento >= 8, tem_maiusculas, tem_minusculas, tem_numeros, tem_simbolos])
    if pontuacao <= 2:
        return "Fraca"
    elif pontuacao == 3:
        return "Moderada"
    elif pontuacao >= 4:
        return "Forte"

# Função para copiar a senha para a área de transferência
def copiar_para_clipboard():
    senha = entry_senha.get()
    if senha:
        root.clipboard_clear()
        root.clipboard_append(senha)
        root.update()  # Atualiza o clipboard
        messagebox.showinfo("Copiado", "A senha foi copiada para a área de transferência.")
    else:
        messagebox.showwarning("Aviso", "Nenhuma senha para copiar.")

# Função para salvar a senha
def salvar_senha():
    senha = entry_senha.get()
    if senha:
        arquivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivo de Texto", "*.txt")])
        if arquivo:
            descricao = simpledialog.askstring("Descrição", "Digite uma descrição para a senha:")
            with open(arquivo, "a") as f:
                f.write(f"{descricao if descricao else 'Sem descrição'}: {senha}\n")
            messagebox.showinfo("Salvo", "Senha salva com sucesso!")
    else:
        messagebox.showwarning("Aviso", "Nenhuma senha para salvar.")

# Função para gerar a senha com base nas opções da interface
def gerar_senha_interface():
    try:
        comprimento = int(entry_comprimento.get())
        segura = var_segura.get()  # A variável 'var_segura' agora está definida
        maiusculas = var_maiusculas.get()
        minusculas = var_minusculas.get()
        numeros = var_numeros.get()
        simbolos = var_simbolos.get()
        memorizavel = var_memorizavel.get()

        senha = gerar_senha(segura=segura, comprimento=comprimento, maiusculas=maiusculas, minusculas=minusculas, 
                             numeros=numeros, simbolos=simbolos, memorizavel=memorizavel)
        entry_senha.delete(0, tk.END)
        entry_senha.insert(0, senha)
        forca = avaliar_forca_senha(senha)
        label_forca.config(text=f"Força da Senha: {forca}")

        # Adiciona a senha ao histórico
        listbox_historial.insert(tk.END, senha)

    except ValueError as e:
        messagebox.showerror("Erro", str(e))
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro inesperado: {e}")

# Função para mostrar dicas de segurança
def mostrar_dicas():
    dicas = """
    Dicas para criar senhas seguras:
    1. Use uma combinação de letras maiúsculas, minúsculas, números e símbolos.
    2. Evite usar palavras simples ou combinações óbvias.
    3. Faça sua senha ter pelo menos 8 caracteres.
    4. Não compartilhe sua senha com outras pessoas.
    5. Alterar sua senha regularmente ajuda a mantê-la segura.
    """
    messagebox.showinfo("Dicas de Segurança", dicas)

# Interface Gráfica Modernizada
root = tk.Tk()
root.title("Gerador de Senhas Seguras")
root.configure(bg="#f0f0f0")

style = ttk.Style()
style.configure("TFrame", padding=20, background="#f0f0f0")
style.configure("TLabel", font=("Helvetica", 12), background="#f0f0f0")
style.configure("TButton", font=("Helvetica", 12, "bold"), relief="flat", padding=10)
style.configure("TCheckbutton", font=("Helvetica", 12), background="#f0f0f0")

frame = ttk.Frame(root)
frame.pack(padx=20, pady=20)

label_comprimento = ttk.Label(frame, text="Comprimento da senha:")
label_comprimento.grid(row=0, column=0, sticky="w", pady=5)

entry_comprimento = ttk.Entry(frame, font=("Helvetica", 12))
entry_comprimento.grid(row=0, column=1, pady=5)
entry_comprimento.insert(0, "12")

# Definição da variável var_segura para a opção "senha segura"
var_segura = tk.BooleanVar(value=True)  # A variável foi definida novamente

# Disposição em duas colunas para os checkboxes
var_maiusculas = tk.BooleanVar(value=True)
checkbox_maiusculas = ttk.Checkbutton(frame, text="Incluir Maiúsculas", variable=var_maiusculas)
checkbox_maiusculas.grid(row=1, column=0, sticky="w", pady=5)

var_minusculas = tk.BooleanVar(value=True)
checkbox_minusculas = ttk.Checkbutton(frame, text="Incluir Minúsculas", variable=var_minusculas)
checkbox_minusculas.grid(row=2, column=0, sticky="w", pady=5)

var_numeros = tk.BooleanVar(value=True)
checkbox_numeros = ttk.Checkbutton(frame, text="Incluir Números", variable=var_numeros)
checkbox_numeros.grid(row=1, column=1, sticky="w", pady=5)

var_simbolos = tk.BooleanVar(value=True)
checkbox_simbolos = ttk.Checkbutton(frame, text="Incluir Símbolos", variable=var_simbolos)
checkbox_simbolos.grid(row=2, column=1, sticky="w", pady=5)

var_memorizavel = tk.BooleanVar(value=False)
checkbox_memorizavel = ttk.Checkbutton(frame, text="Gerar Senha Memorizável", variable=var_memorizavel)
checkbox_memorizavel.grid(row=3, columnspan=2, sticky="w", pady=5)

button_gerar = ttk.Button(frame, text="Gerar Senha", command=gerar_senha_interface)
button_gerar.grid(row=4, columnspan=2, pady=10)

label_senha = ttk.Label(frame, text="Senha Gerada:")
label_senha.grid(row=5, column=0, sticky="w", pady=5)

entry_senha = ttk.Entry(frame, width=40, font=("Helvetica", 12))
entry_senha.grid(row=5, column=1, pady=5)

label_forca = ttk.Label(frame, text="Força da Senha:")
label_forca.grid(row=6, columnspan=2, pady=5)

button_copiar = ttk.Button(frame, text="Copiar Senha", command=copiar_para_clipboard)
button_copiar.grid(row=7, column=0, pady=5)

button_salvar = ttk.Button(frame, text="Salvar Senha", command=salvar_senha)
button_salvar.grid(row=7, column=1, pady=5)

button_dicas = ttk.Button(frame, text="Dicas de Segurança", command=mostrar_dicas)
button_dicas.grid(row=8, columnspan=2, pady=10)

# Histórico de senhas
label_historial = ttk.Label(frame, text="Histórico de Senhas Geradas:")
label_historial.grid(row=9, columnspan=2, sticky="w", pady=5)

listbox_historial = tk.Listbox(frame, height=5, width=50, font=("Helvetica", 10))
listbox_historial.grid(row=10, columnspan=2, pady=5)

root.mainloop()
