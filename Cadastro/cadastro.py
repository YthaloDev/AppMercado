import tkinter as tk
from tkinter import ttk
import datetime as dt
from tkinter import messagebox
import sqlite3

lista_tipos = ['Galão', 'Saco', 'Caixa', 'Unidade']

janela = tk.Tk()

# Variável global para armazenar os dados
conn = sqlite3.connect('Database.db')
c = conn.cursor()

# Função que insere os dados na tabela
def inserir_codigo():
    data_criacao = dt.datetime.now()
    data_criacao = data_criacao.strftime("%d/%m/%y %H:%M")
    global data_base
    descricao = entry_descricao.get()
    tipo = combobox_selecionar_tipo.get()
    quant = entry_quant.get()
    data_criacao = dt.datetime.now()
    data_criacao = data_criacao.strftime("%d/%m/%y %H:%M")
    if (descricao and tipo and quant and data_criacao) == "":
        messagebox.showinfo("Alert", "Preencha os campos!")
    else:
        # Criação da tabela (apenas uma vez)
        c.execute('''CREATE TABLE IF NOT EXISTS materiais (
                             id INTEGER PRIMARY KEY,
                             descricao TEXT NOT NULL,
                             tipo TEXT NOT NULL,
                             quant INTEGER NOT NULL,
                             data_criacao TEXT NOT NULL
                             )''')

        # Inserção de dados na tabela
        c.execute("INSERT INTO materiais (descricao, tipo, quant, data_criacao) VALUES (?, ?, ?, ?)",
                  (descricao, tipo, quant, data_criacao))
        conn.commit()


# Função que exibe a tabela na janela
def exibir_tabela():
    c.execute("SELECT * FROM materiais")
    print(c.fetchall())

# Titulo da janela
janela.title("Ferramenta de cadastro de materiais")

# Frames
frame = ttk.Frame(janela)
frame.pack()

frame2 = ttk.Frame(frame)
frame2.pack()

frame3 = ttk.Frame(frame2)
frame3.pack()

frame4 = ttk.Frame(frame3)
frame4.pack()

frame5 = ttk.Frame(frame3)
frame5.pack()

# a criação da janela
label_descricao = tk.Label(frame4, text="Descrição do material")
label_descricao.pack(pady=10)

entry_descricao = tk.Entry(frame4, width=50)
entry_descricao.pack(pady=10)


label_unidade = tk.Label(frame3, text="Tipo da unidade do Material")
label_unidade.pack(side='left', pady=10)

combobox_selecionar_tipo = ttk.Combobox(frame3, values=lista_tipos)
combobox_selecionar_tipo.pack(side='right', pady=10)

label_quant = tk.Label(frame2, text="Quantidade na unidade de material")
label_quant.pack(side='left', pady=10)

entry_quant = tk.Entry(frame2)
entry_quant.pack(side='right', pady=10)

botao_criar_codigo = tk.Button(frame, width=20, text="Inserir dados", command=inserir_codigo)
botao_criar_codigo.pack(side='left', padx=5)

botao_mostrar_tabela = tk.Button(frame, width=20, text="Mostrar Tabela", command=exibir_tabela)
botao_mostrar_tabela.pack(side='right', padx=5)

mostra_tabela = tk.Label()
mostra_tabela.pack()

janela.mainloop()
