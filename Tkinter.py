from tkinter import *
from tkinter import ttk


def emprestimo(*args):

    if (entry_a.get() == ""):
        margem = 0
    else:
        margem = int(entry_a.get())

    fbancario = float(entry_b.get())
    valor = margem / fbancario
    resultado.config(
        text="Valor disponível:\n {:.2f} Reais".format(valor))


def altera_fator():
    entry_b.config(state="normal")


# Janela Principal
janela = Tk()
janela.title("Fk Empréstimos")
janela.geometry("300x300")

# Criação da Variavel Fixa
fator_fixo = StringVar(value="0.027")

# Criação das Entrys
label_a = Label(janela, text="Margem:")
entry_a = Entry(janela)
label_a.grid(row=0, column=0)
entry_a.grid(row=0, column=1)

label_b = Label(janela, text="Fator Bancário:")
entry_b = Entry(janela, textvariable=fator_fixo, state="disabled")
label_b.grid(row=1, column=0)
entry_b.grid(row=1, column=1)

# Criação do botão
botao_alterarfb = Button(janela, text="Alterar Fator", command=altera_fator)
botao_alterarfb.grid(row=2, column=1)

# Criação da label do resultado
resultado = Label(janela, font=12)
resultado.grid(row=3, column=1)

# Criação da Variavel para calcular em tempo real
entry_a.bind("<KeyRelease>", emprestimo)
entry_b.bind("<KeyRelease>", emprestimo)


janela.mainloop()
