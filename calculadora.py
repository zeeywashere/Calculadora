from tkinter import *
from tkinter import ttk

def adicionar_numero(numero):
    entrada_atual = caixa_entrada.get()
    nova_entrada = entrada_atual + str(numero)
    caixa_entrada.delete(0, END)
    caixa_entrada.insert(0, nova_entrada)

def adicionar_operacao(operacao):
    entrada_atual = caixa_entrada.get()
    ultima_caracter = entrada_atual[-1:]  

    if ultima_caracter.isdigit() or ultima_caracter == ".":
        nova_entrada = entrada_atual + operacao
        caixa_entrada.delete(0, END)
        caixa_entrada.insert(0, nova_entrada)

def calcular():
    expressao = caixa_entrada.get()
    try:
        resultado = eval(expressao)
        caixa_entrada.delete(0, END)
        caixa_entrada.insert(0, str(resultado))
    except Exception as e:
        caixa_entrada.delete(0, END)
        caixa_entrada.insert(0, "Erro")

janela = Tk()
janela.title("Calculadora")

######################## Cor de Fundo ########################
janela.configure(bg="#F0F0F0")

######################## Caixa de entrada ########################
caixa_entrada = Entry(janela, font=("Arial", 16), justify="right", bd=10)
caixa_entrada.grid(row=0, column=0, columnspan=4)

######################## Botoes do numeros ########################
botoes_numeros = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2),
    ("0", 4, 1)
]

for (texto, linha, coluna) in botoes_numeros:
    Button(janela, text=texto, font=("Arial", 16), padx=20, pady=20, command=lambda t=texto: adicionar_numero(t)).grid(row=linha, column=coluna)

######################## Botoes das operaçãoes ########################
botoes_operacoes = [
    (".", 4, 0), ("+", 1, 3), ("-", 2, 3),
    ("*", 3, 3), ("/", 4, 3), ("=", 4, 2)
]

for (texto, linha, coluna) in botoes_operacoes:
    Button(janela, text=texto, font=("Arial", 16), padx=20, pady=20, command=lambda t=texto: adicionar_operacao(t)).grid(row=linha, column=coluna)

######################## Botão de calcular ########################
Button(janela, text="=", font=("Arial", 16), padx=20, pady=20, command=calcular).grid(row=4, column=2)

janela.geometry("400x500+300+150")
janela.mainloop()

