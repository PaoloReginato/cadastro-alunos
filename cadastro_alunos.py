import tkinter as tk
from tkinter import ttk
import datetime as dt

lista_sexo = ['Masculino', 'Feminino']
lista_cod = []

janela = tk.Tk()
janela.title('Cadastro Alunos')
janela.geometry("250x300")


def gerar_cod():
    nome = entry_nome.get()
    sobrenome = entry_sobrenome.get()
    cpf = entry_cpf.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    sexo = combobox_selecionar_sexo.get()
    data_criacao = dt.datetime.now()
    data_criacao = data_criacao.strftime('%d/%m/%y %H:%M')
    codigo = len(lista_cod) + 1
    codigo_str = 'COD-{}'.format(codigo)
    lista_cod.append((codigo_str, nome, sobrenome, cpf, email, telefone, sexo, data_criacao))


label_nome = tk.Label(text='Nome')
label_nome.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)
entry_nome = tk.Entry()
entry_nome.grid(row=1, column=1, padx=10, pady=10, sticky='nswe', columnspan=2)

label_sobrenome = tk.Label(text='Sobrenome')
label_sobrenome.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)
entry_sobrenome = tk.Entry()
entry_sobrenome.grid(row=2, column=1, padx=10, pady=10, sticky='nswe', columnspan=2)

label_cpf = tk.Label(text='CPF')
label_cpf.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)
entry_cpf = tk.Entry()
entry_cpf.grid(row=3, column=1, padx=10, pady=10, sticky='nswe', columnspan=2)

label_email = tk.Label(text='E-mail')
label_email.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)
entry_email = tk.Entry()
entry_email.grid(row=4, column=1, padx=10, pady=10, sticky='nswe', columnspan=2)

label_telefone = tk.Label(text='Telefone')
label_telefone.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)
entry_telefone = tk.Entry()
entry_telefone.grid(row=5, column=1, padx=10, pady=10, sticky='nswe', columnspan=2)

label_sexo = tk.Label(text='Sexo')
label_sexo.grid(row=6, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)
combobox_selecionar_sexo = ttk.Combobox(values=lista_sexo)
combobox_selecionar_sexo.grid(row=6, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)

botao_cadastrar = tk.Button(text='Cadastrar / Gerar código do aluno', command=gerar_cod)
botao_cadastrar.grid(row=7, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

janela.mainloop()

print(lista_cod)
