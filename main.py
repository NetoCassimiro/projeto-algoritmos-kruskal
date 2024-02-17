# Importando bibliotecas necessárias
import matplotlib.pyplot as plt
from tkinter import *
from src.script.read_database import get_nodes_and_edges

# Obtendo informações dos nós e arestas da base de dados
infos = get_nodes_and_edges()
nodes, edges = infos[0], infos[1]

# Criando a interface gráfica usando Tkinter
window = Tk()
window.title("Projeto de algoritmos e estrutura de dados")
window.geometry("1000x687")
window.resizable(0, 0)

# Criando a figura do grafo usando Matplotlib
plt.figure(1)

# Adicionando uma imagem de fundo
bg = PhotoImage(file="src/assets/images/bg.png")

# Criando um canvas para exibir a imagem
canvas = Canvas(window, width=1000, height=687)
canvas.pack(fill="both", expand=True)

# Exibindo a imagem de fundo no canvas
canvas.create_image(0, 0, image=bg, anchor="nw")

# Botão para exibir a Árvore Geradora Mínima (MST)
btn_show_mst = Button(window, 
                      text="Exibir a árvore geradora mínima (MST)", 
                      command="", 
                      font=('Times New Roman CE', 16, 'bold'), 
                      bg="white", 
                      foreground="black", 
                      activebackground="#001F48", 
                      activeforeground="white")

# Botão para exibir o Grafo completo
btn_show_full_grafo = Button(window,
                             text="Exibir o Grafo completo", 
                             command="", 
                             font=('Times New Roman CE', 16, 'bold'), 
                             bg="white", 
                             foreground="black", 
                             activebackground="#001F48", 
                             activeforeground="white")

# Texto explicativo sobre a rede neural
text = "Rede Neural Caenorhabditis Elegans é uma rede direcionada e ponderada que representa a rede neural do Caenorhabditis elegans ou C. Elegans, um verme nematódeo que foi de extrema importância no estudo de exploração das doenças humanas. Os dados com informações da rede neural do C. Elegans foram retirados do site do Prof. Duncan Watts na Universidade de Columbia, http://cdg.columbia.edu/cdg/datasets e foram compilados por Duncan Watts e Steven Strogatz dos dados experimentais originais por White et al. e disponibilizados na Internet. Dados experimentais originais obtidos de J. G. White, E. Southgate, J. N. Thompson, e S. Brenner, Phil. Trans. R. Soc. London 314, 1-340 (1986)."

# Renderizando elementos no canvas
canvas.create_text(510, 60, text="Projeto Algoritmo e estrutura de dados", fill='white', font=('Times New Roman CE', 28, 'bold'))
canvas.create_text(500, 105, text="Algoritmo de Kruskal - Rede Neural Caenorhabditis Elegans", fill='white', font=('', 16, 'bold'))
canvas.create_text(500, 280, text=text, fill='white', font=('', 14, 'bold'), width=850, justify='center')

# Colocando os botões no canvas
btn_show_full_grafo_canva = canvas.create_window(150, 450, anchor="nw", window=btn_show_full_grafo)
btn_show_mst_canva = canvas.create_window(450, 450, anchor="nw", window=btn_show_mst)

# Texto de copyright
canvas.create_text(520, 660, text="Copyright © 2024 - Eraldo Cassimiro", fill='white', font=('', 14, 'bold', 'italic'))

# Mantendo a interface aberta
window.mainloop()