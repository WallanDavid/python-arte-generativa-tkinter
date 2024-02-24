import turtle
import random
from colorsys import hsv_to_rgb
import tkinter as tk
from tkinter import ttk

# Configuração inicial
turtle.speed(0)
turtle.bgcolor("black")
turtle.pensize(2)

# Função para converter valores HSV para RGB
def hsv_to_rgb_color(h, s, v):
    r, g, b = hsv_to_rgb(h, s, v)
    return r, g, b

# Função para desenhar uma forma com o número especificado de lados
def desenhar_forma(num_lados, tamanho, cor_base):
    turtle.fillcolor(cor_base)
    turtle.begin_fill()

    for _ in range(num_lados):
        turtle.color(cor_base)
        turtle.forward(tamanho)
        turtle.right(360 / num_lados)

    turtle.end_fill()

# Função chamada quando o botão é pressionado
def desenhar_com_forma():
    forma_selecionada = formas_menu.get()
    num_lados = formas_validas[forma_selecionada]
    tamanho = int(tamanho_var.get())
    cor_base = hsv_to_rgb_color(random.random(), 1, 1)

    turtle.penup()
    turtle.goto(random.randint(-300, 300), random.randint(-300, 300))
    turtle.pendown()

    turtle.setheading(random.randint(0, 360))
    desenhar_forma(num_lados, tamanho, cor_base)

# Criação da interface gráfica
root = tk.Tk()
root.title("Generative Art Menu")

# Variáveis para armazenar os valores do menu
tamanho_var = tk.StringVar(value="100")

# Lista de formas válidas e seus respectivos números de lados
formas_validas = {"Quadrilátero": 4, "Pentágono": 5, "Hexágono": 6, "Heptágono": 7, "Octágono": 8, "Eneágono": 9, "Decágono": 10}

# Criação dos widgets
label_tamanho = ttk.Label(root, text="Tamanho:")
entry_tamanho = ttk.Entry(root, textvariable=tamanho_var)

# Menu suspenso para seleção de forma
formas_menu = ttk.Combobox(root, values=list(formas_validas.keys()))

button_desenhar = ttk.Button(root, text="Desenhar", command=desenhar_com_forma)

# Posicionamento dos widgets
label_tamanho.grid(row=0, column=0, padx=5, pady=5)
entry_tamanho.grid(row=0, column=1, padx=5, pady=5)
formas_menu.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
button_desenhar.grid(row=2, column=0, columnspan=2, pady=10)

# Mantém a interface gráfica aberta
root.mainloop()
