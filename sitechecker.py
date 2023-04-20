# Importação dos módulos e bibliotecas
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import font
import requests

lista_final = [] # 

# Definição das funções utilizadas para os botões interativos
def apagar_texto():
    """ Essa função irá apagar o item (nome do site) que estiver selecionado dentro da janela interativa que contém a lista de sites 
    que foram adicionados ou manualmente ou por meio de arquivos .txt """
    selecao = lista_sites.curselection() 
    if selecao: 
        item_selecionado = selecao[0]  
        lista_sites.delete(item_selecionado) 

def testar_conexao():
    """ Essa função irá testar a conexão do site que estiver selecionado dentro da janela interativa e funciona da seguinte maneira
    1 - Pega o texto (site) que estiver selecionado na janela interativa
    2 - Verifica se a seleção não está vazia
    3 - Tenta realizar a conexão
    4 - Mostra na tela o resultado (online ou offline) logo abaixo do botão, caso estaja online a janela da mensagem fica verde, caso contrário fica vermelha
    5 - Apaga da janela interativa o site após ser testado
    6 - Salva o resultado na lista_final, caso ainda não tenha sido salvo anteriormente (evitar que seja salvo sites repetidos), 
    possibilitando salvar tudo num arquivo .txt """
    selecao = lista_sites.curselection()
    if selecao:
        indice = selecao[0]
        item_selecionado = lista_sites.get(tk.ACTIVE)
        try:
            response = requests.get(item_selecionado)
            response.raise_for_status()
            lista_sites.delete(indice)
            resultado = str("O site: " + item_selecionado + " está online")
            status_conexao.config(text= resultado, bg="green" )
            if resultado not in lista_final:
                lista_final.append(resultado)
            return True
        except:
            resultado = str("O site: " + item_selecionado + " está offline")
            lista_sites.delete(indice)
            status_conexao.config(text= resultado, bg="red" )
            if resultado not in lista_final:
                lista_final.append(resultado)
            return False

def adicionar_site():
    """ Botão para adicionar o site digitado à janela interativa que contém a lista de sites """
    site = entrada_site.get()
    if site != "":
        lista_sites.insert(tk.END, site)
        entrada_site.delete(0, tk.END)

def salvar_e_fechar():
    """ Caso tenha sites que não foram testados usando o botão testar conexão, irá testar as conexões para cada site que restou dentro da janela
    e acrescentar na lista_final que contém todos os sites testados diretamente ou não. 
    Em seguida irá salvar todos os resultados num arquivo chamado final.txt """
    urls = list(lista_sites.get(0, tk.END))
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()
            resultado = str("O site: " + url + " está online")
            if resultado not in lista_final:
                lista_final.append(resultado)
        except:
            resultado = str("O site: " + url + " está offline")
            if resultado not in lista_final:
                lista_final.append(resultado)
                
    with open("final.txt", "w") as arquivo_final:
        for elemento in lista_final:
            arquivo_final.write(elemento + "\n")
    messagebox.showinfo("Salvar", "Itens salvos com sucesso!")
    janela.destroy() 

def abrir_arquivo():
    """ Essa função permite ao usuário abrir arquivos .txt do computador, onde cada linha deve ser um site para ser testado. """
    arquivo = filedialog.askopenfilename(filetypes= [("Arquivos de Texto", "*.txt")]) 
    if arquivo:
        with open(arquivo, "r") as arquivo_txt:
            for linha in arquivo_txt:
                lista_sites.insert(tk.END, linha.strip())

# Cração da janela de interação
janela = tk.Tk() 
janela.title("Teste de conectividade de Urls")
janela.geometry("500x500")

# Criação de uma caixa, no topo da janela com comprimento ocupando todo o espaço e alterando tamanho e formato da fonte para destacar uma descrição do projeto  
label_topo = tk.Label(janela, text= "Digite as urls e pressione adicionar na lista ou abra um arquivo .txt do seu computador (OBS: digitar urls completas com 'https://...')", wraplength= 500, bg= "black", fg= "white")  
label_topo.pack(side= tk.TOP, pady= 10)
nova_fonte = font.nametofont("TkDefaultFont").copy()
nova_fonte.configure(size= 14, weight= "bold") 
label_topo.configure(font= nova_fonte)

# Criando o botão para abrir arquivo de texto no computador
botao_abrir = tk.Button(janela, text= "Abrir arquivo de texto", command= abrir_arquivo)  
botao_abrir.pack(fill= tk.X, expand= True, padx= 5)

# Cria um quadro dentro da janela, logo abaixo do botão definido anteriormente para agrupar os próximos 3 elementos na mesma linha
frame = tk.Frame(janela)
frame.pack(pady= 5, fill= tk.X, expand= True)

# Cria uma caixa dentro do quadro criado anteriormente e alinha ela à esquerda
label = tk.Label(frame, text= "Digite o site:")
label.pack(side= tk.LEFT)

# Cria uma caixa de entrada dentro do quadro criado anteriormente, que permite ao usuário digitar o site
entrada_site = tk.Entry(frame)
entrada_site.pack(side= tk.LEFT, padx= 5, fill= tk.X, expand= True)

# Cria um botão logo a direita da caixa de entrada para que o usuário pressione quando desejar adicionar o que foi digitado na lista de sites
botao_adicionar = tk.Button(frame, text= "Adicionar na lista de sites", command= adicionar_site)
botao_adicionar.pack(side= tk.RIGHT)

# Cria uma caixa de texto ocupando a tela inteira (abaixo dos que foram criados anteriormente) para mostrar os sites que foram adicionados
lista_sites = tk.Listbox(janela)
lista_sites.pack(fill= tk.BOTH, expand= True, padx= 5, pady= 5)

# Cria um botão logo abaixo da caixa de texto que permite testar a conexão do site que estiver selecionado dentro da caixa de texto
botao_testar_conexao = tk.Button(janela, text= "Testar conexão", command= testar_conexao)
botao_testar_conexao.pack(fill= tk.X, expand= True, padx= 5, pady= 5)

# Cria uma caixa logo abaixo do botão anterior que permite mostrar a mensagem se o site está ou não online
status_conexao = tk.Label(janela, text= "")
status_conexao.pack(fill= tk.BOTH, expand= True, padx= 5, pady= 5)

#Cria um botão abaixo do anterior para apagar a linha de texto selecionada dentro da caixa de texto que contém todos os que foram adicionados
botao_apagar_texto = tk.Button(janela, text= "Apagar texto", command= apagar_texto)
botao_apagar_texto.pack(fill= tk.X, expand= True, padx= 5, pady= 5)

""" Cria um botão abaixo do anterior que irá testar todos os sites que ainda não foram testados usando o botão de testar, mas ainda estão na caixa de texto,
salvar todos os resultados que foram testados durante o uso da aplicação em um arquivo chamado final.txt e fechar a janela de interação """
botao_salvar_e_fechar = tk.Button(janela, text= "Testar tudo, salvar e Fechar", command= salvar_e_fechar)
botao_salvar_e_fechar.pack(fill= tk.X, expand= True, padx= 5)

janela.mainloop()



