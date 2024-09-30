# Impordanto Customtkinter
from customtkinter import *
import customtkinter as ctk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

# Impordando tkcalendar
from tkcalendar import Calendar, DateEntry

# Importanto Views
from view import *

# Executando Primeiro o Banco de Dados
import banco


################# cores ###############
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue
co10 = "#4c2a12"  # dark

################# Criando APP ###############

# Centralizando a Iniciação da Janela


def centralizar_janela(app):
    # Obter largura e altura da tela
    largura_tela = app.winfo_screenwidth()
    altura_tela = app.winfo_screenheight()

    # Dimensões da janela
    largura_janela = 1200
    altura_janela = 600

    # Calcular a posição x e y
    pos_x = (largura_tela // 2) - (largura_janela // 2)
    pos_y = (altura_tela // 2) - (altura_janela // 2)

    # Definir a posição da janela
    app.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")


app = ctk.CTk()
app.title("Cadastro de Clientes")
centralizar_janela(app)
app.iconbitmap('D:/python_emanuel/Projeto1/icon_projeto1.ico')
app.configure(background=co10)
app.resizable(width=FALSE, height=FALSE)

# app.geometry('1043x453')

################# Criando APP ###############


################# Dividindo FRAMES ###############
# frame cima
frame_cima = ctk.CTkFrame(app, fg_color="#038cfc",
                          border_color="white", border_width=0)
frame_cima.grid(row=0, column=0, sticky="nsew",)

# frame baixo
frame_baixo = ctk.CTkFrame(app, fg_color="white",
                           border_color="white", border_width=2)
frame_baixo.grid(row=1, column=0, sticky="nsew")

# frame direita
frame_direita = ctk.CTkFrame(
    app, fg_color="white", border_color="white", border_width=2)
frame_direita.grid(row=0, column=1, rowspan=2, sticky="nsew")

################# Configurando Labels ###############

app.grid_columnconfigure(0, weight=1)  # Coluna para frames da esquerda
app.grid_columnconfigure(1, weight=4)  # Coluna para o frame da direita
app.grid_rowconfigure(1, weight=1)  # Segunda linha (frame inferior esquerdo)

# Variavel tree global
global tree

# Atualizar Treeview


def atualizar_treeview():
    # Limpa o Treeview
    for item in tree.get_children():
        tree.delete(item)

    # Recarrega os dados do banco de dados
    con = lite.connect('dados.db')
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM formulario")
        rows = cur.fetchall()
        for row in rows:
            tree.insert("", "end", values=row)  # Insere cada linha no Treeview
    con.close()  # Fecha a conexão


# Função Inserir


def inserir():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    data = entry_dia_em.get()
    observacoes = entry_observacoes.get("1.0", "end-1c")

    lista = [nome, cpf, email, telefone, data, observacoes]

    if nome == '':
        messagebox.showerror('Erro', 'Preenchar todos os campos!')
    else:
        inserir_info(lista)
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!')

        entry_nome.delete(0, 'end')
        entry_cpf.delete(0, 'end')
        entry_email.delete(0, 'end')
        entry_telefone.delete(0, 'end')
        entry_dia_em.delete(0, 'end')
        entry_observacoes.delete("1.0", "end")

    for widget in frame_direita.winfo_children():
        widget.destroy()

    mostrar()

# Função Atualizar


def atualizar():
    try:
        treeview_dados = tree.focus()
        treeview_dicionario = tree.item(treeview_dados)
        tree_lista = treeview_dicionario['values']

        valor_id = tree_lista[0]

        entry_nome.delete(0, 'end')
        entry_cpf.delete(0, 'end')
        entry_email.delete(0, 'end')
        entry_telefone.delete(0, 'end')
        entry_dia_em.delete(0, 'end')
        entry_observacoes.delete("1.0", "end")

        entry_nome.insert(0, tree_lista[1])
        entry_cpf.insert(0, tree_lista[2])
        entry_email.insert(0, tree_lista[3])
        entry_telefone.insert(0, tree_lista[4])
        entry_dia_em.insert(0, tree_lista[5])
        entry_observacoes.insert("1.0", tree_lista[6])

        # Funcção Inserir
        def update():
            nome = entry_nome.get()
            cpf = entry_cpf.get()
            email = entry_email.get()
            telefone = entry_telefone.get()
            data = entry_dia_em.get()
            observacoes = entry_observacoes.get("1.0", "end-1c")

            lista = [nome, cpf, email, telefone, data, observacoes, valor_id]

            if nome == '':
                messagebox.showerror('Erro', 'Preenchar os todos os campos')
            else:
                try:
                    atualizar_info(lista)
                    messagebox.showinfo(
                        'Sucesso', 'Os dados foram atualizados com sucesso!')

                    entry_nome.delete(0, 'end')
                    entry_cpf.delete(0, 'end')
                    entry_email.delete(0, 'end')
                    entry_telefone.delete(0, 'end')
                    entry_dia_em.delete(0, 'end')
                    entry_observacoes.delete("1.0", "end")

                    atualizar_treeview()

                except Exception as e:
                    messagebox.showerror('Erro', str(e))

            for widget in frame_direita.winfo_children():
                widget.destroy()

                mostrar()

        botao_confirmar = ctk.CTkButton(frame_baixo, command=update, text="Confirmar",
                                        width=100, height=30,  # Ajuste de tamanho
                                        # Fonte um pouco maior
                                        font=("Calibri", 10, "bold"),
                                        fg_color="#038cfc",          # Cor de fundo
                                        text_color="white",    # Cor do texto
                                        hover_color="grey",  # Cor ao passar o mouse
                                        corner_radius=10).grid(row=5, column=1, padx=(10), pady=5, sticky="nsew")

    except IndexError():
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')

# Função Deletar


def deletar():
    try:
        # Obter todos os itens selecionados no Treeview
        tree_dados = tree.selection()

        if not tree_dados:
            messagebox.showwarning("Aviso", "Nenhum cliente selecionado!")
            return

        # Confirmação de deleção
        confirmacao = messagebox.askyesno(
            "Confirmação", "Você realmente deseja deletar os clientes selecionados?")

        if confirmacao:
            valores_ids = []
            for item in tree_dados:
                treeview_dicionario = tree.item(item)
                tree_lista = treeview_dicionario['values']
                valor_id = tree_lista[0]
                valores_ids.append(valor_id)

            # Chama a função de deletar passando a lista de IDs
            deletar_info(valores_ids)  # Agora deve funcionar corretamente

            # Remove do Treeview os itens selecionados
            for item in tree_dados:
                tree.delete(item)

            messagebox.showinfo("Sucesso", "Clientes deletados com sucesso!")
        else:
            print("Deleção cancelada.")

    except Exception as e:
        print(f"Erro ao deletar: {e}")
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

# Função Visualizar


def item_selecionado(event):
    for item in tree.selection():
        # Captura os valores da linha selecionada
        item_text = tree.item(item, 'values')
        # Exibe no console os dados da linha (ID, Nome, CPF, etc.)
        print(item_text)

        # Preenche os campos da interface com os dados da linha selecionada
        entry_nome.delete(0, 'end')
        entry_nome.insert(0, item_text[1])  # Nome

        entry_cpf.delete(0, 'end')
        entry_cpf.insert(0, item_text[2])  # CPF

        entry_email.delete(0, 'end')
        entry_email.insert(0, item_text[3])  # Email

        entry_telefone.delete(0, 'end')
        entry_telefone.insert(0, item_text[4])  # Telefone

        entry_dia_em.delete(0, 'end')
        entry_dia_em.insert(0, item_text[5])  # Data de vencimento

        entry_observacoes.delete('1.0', 'end')
        entry_observacoes.insert('1.0', item_text[6])  # Observações

# Funçaõ Limpar


def limpar_campos():
    entry_nome.delete(0, 'end')
    entry_cpf.delete(0, 'end')
    entry_email.delete(0, 'end')
    entry_telefone.delete(0, 'end')
    entry_dia_em.delete(0, 'end')
    entry_observacoes.delete('1.0', 'end')  # Para o campo de texto

# Limita o CPF a 11 números


def limitar_cpf(event):
    if event.keysym in ("BackSpace", "Delete", "Tab"):
        return None

    if len(entry_cpf.get()) >= 14:
        return "break"  # Impede a entrada se já houver 11 caracteres
    return None


# Permite APENAS NÚMEROS no CPF e DATE
def permitir_digitos(event):
    # Permite apenas dígitos, /, ., e as teclas de controle, incluindo Tab
    if event.char.isdigit() or event.char in ("/", ".") or event.keysym in ("BackSpace", "Delete", "Tab"):
        return None

    return "break"

# Formatar CPF para que ele fique 000.000.000-00


def formatar_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

    # Formata o CPF
    if len(cpf) <= 3:
        return cpf
    elif len(cpf) <= 6:
        return f"{cpf[:3]}.{cpf[3:]}"
    elif len(cpf) <= 9:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:]}"
    elif len(cpf) == 11:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return cpf


def atualizar_cpf(event):
    # Obtém o texto atual no campo de entrada
    texto_atual = entry_cpf.get()

    # Formata o texto
    texto_formatado = formatar_cpf(texto_atual)

    # Atualiza o campo de entrada com o texto formatado
    entry_cpf.delete(0, ctk.END)
    entry_cpf.insert(0, texto_formatado)

# Limitar o TELEFONE a 11 números


def limitar_telefone(event):
    if event.keysym in ("BackSpace", "Delete", "Tab"):
        return None

    if len(entry_telefone.get()) >= 14:
        return "break"  # Impede a entrada se já houver 11 caracteres
    return None

# Permitir APENAS NÚMEROS no TELEFONE


def permitir_digitos_telefone(event):
    # Permite apenas dígitos, (, ), -, e as teclas de controle, incluindo Tab
    if event.char.isdigit() or event.char in ("(", ")", "-") or event.keysym in ("BackSpace", "Delete", "Tab"):
        return None
    return "break"

# Formatar TELEFONE para que ele fique no formato de (00)00000-0000


def formatar_telefone(telefone):
    # Remove todos os caracteres não numéricos
    telefone = ''.join(filter(str.isdigit, telefone))

    # Formata o telefone
    if len(telefone) <= 2:
        return f"({telefone}"
    elif len(telefone) <= 7:
        return f"({telefone[:2]}){telefone[2:]}"
    elif len(telefone) <= 11:
        return f"({telefone[:2]}){telefone[2:7]}-{telefone[7:]}"
    else:
        return f"({telefone[:2]}){telefone[2:7]}-{telefone[7:11]}"


def atualizar_telefone(event):
    # Obtém o texto atual no campo de entrada
    texto_atual = entry_telefone.get()

    # Formata o texto
    texto_formatado = formatar_telefone(texto_atual)

    # Atualiza o campo de entrada com o texto formatado
    entry_telefone.delete(0, ctk.END)
    entry_telefone.insert(0, texto_formatado)


# Limitar números PARA DATE
def limitar_dia_em(event):
    if event.keysym in ("BackSpace", "Delete", "Tab"):
        return None

    if len(entry_dia_em.get()) >= 8:
        return "break"  # Impede a entrada se já houver 11 caracteres
    return None

#


# Label CIMA
label_cima = ctk.CTkLabel(
    frame_cima, text="Cadastro de Clientes", font=("Calibri", 20, "bold"))
label_cima.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Label BAIXO NOME
label_nome = ctk.CTkLabel(
    frame_baixo, text="Nome:*", text_color="black", font=("Calibri", 13, "bold"), width=10, height=10)
label_nome.grid(row=0, column=0, padx=10, pady=10, sticky="w")
# Entry BAIXO NOME
entry_nome = ctk.CTkEntry(
    frame_baixo, fg_color="black", border_width=2,  width=200)
entry_nome.grid(row=1, column=0, padx=10, pady=0, sticky="w")
entry_nome.configure(font=("Calibri", 13, "bold"))

# Label BAIXO CPF
label_cpf = ctk.CTkLabel(
    frame_baixo, text="CPF:*", text_color="black", font=("Calibri", 13, "bold"))
label_cpf.grid(row=2, column=0, padx=10, pady=5, sticky="w")

# Entry para CPF
entry_cpf = ctk.CTkEntry(
    frame_baixo, fg_color="black", border_width=2, width=200)
entry_cpf.grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_cpf.bind("<Key>", limitar_cpf)
entry_cpf.bind("<KeyPress>", permitir_digitos)
entry_cpf.bind("<KeyRelease>", atualizar_cpf)
entry_cpf.configure(font=("Calibri", 13, "bold"))

# Label BAIXO EMAIL
label_email = ctk.CTkLabel(
    frame_baixo, text="Email:*", text_color="black", font=("Calibri", 13, "bold"), width=10, height=10)
label_email.grid(row=4, column=0, padx=10, pady=10, sticky="w")

# Entry para EMAIL
entry_email = ctk.CTkEntry(
    frame_baixo, fg_color="black", border_width=2, width=200)
entry_email.grid(row=5, column=0, padx=10, pady=5, sticky="w")
entry_email.configure(font=("Calibri", 13, "bold"))

# Label BAIXO TELEFONE
label_telefone = ctk.CTkLabel(
    frame_baixo, text="Telefone:*", text_color="black", font=("Calibri", 13, "bold"), width=10, height=10)
label_telefone.grid(row=6, column=0, padx=10, pady=10, sticky="w")

# Entry para TELEFONE
entry_telefone = ctk.CTkEntry(
    frame_baixo, fg_color="black", border_width=2, width=200)
entry_telefone.grid(row=7, column=0, padx=10, pady=5, sticky="w")
entry_telefone.bind("<Key>", limitar_telefone)
entry_telefone.bind("<Key>", permitir_digitos_telefone)
entry_telefone.bind("<KeyRelease>", atualizar_telefone)
entry_telefone.configure(font=("Calibri", 13, "bold"))

# Label BAIXO DATA DE VENCIMENTO
label_data = ctk.CTkLabel(
    frame_baixo, text="Data de vencimento:*", text_color="black", font=("Calibri", 13, "bold"), width=10, height=10)
label_data.grid(row=8, column=0, padx=10, pady=10, sticky="w")

# Entry para DATA DE VENCIMENTO
entry_dia_em = DateEntry(
    frame_baixo, font=("Calibri", 13, "bold"), width=12, background='darkblue', foreground='white',
    borderwidth=2, date_pattern='dd/mm/yyyy',
    headersbackground='lightblue', headersforeground='black',
    selectbackground='lightgreen', selectforeground='black')
entry_dia_em.grid(row=9, column=0, padx=10, pady=5, sticky="w")
entry_dia_em.bind("<Key>", limitar_dia_em)
entry_dia_em.bind("<Key>", permitir_digitos)

# Label BAIXO OBESERVAÇÕES
label_observacoes = ctk.CTkLabel(
    frame_baixo, text="Observações:*", text_color="black", font=("Comic Sans MS", 13, "bold"), width=10, height=10)
label_observacoes.grid(row=10, column=0, padx=10, pady=10, sticky="w")

# Entry para OBSERVAÇÕES
entry_observacoes = ctk.CTkTextbox(
    frame_baixo, width=400, height=80)
entry_observacoes.grid(row=11, column=0, columnspan=2,
                       padx=10, pady=5, sticky="w")
entry_observacoes.configure(font=("Calibri", 13, "bold"))

################### BOTÕES ########################
# Botão INSERIR
botao = ctk.CTkButton(frame_baixo, command=inserir, text="Inserir",
                      width=130, height=40,  # Ajuste de tamanho
                      # Fonte um pouco maior
                      font=("Calibri", 15, "bold"),
                      fg_color="#038cfc",          # Cor de fundo
                      text_color="white",    # Cor do texto
                      hover_color="grey",  # Cor ao passar o mouse
                      corner_radius=10).grid(row=1, column=1, padx=(10), pady=5, sticky="nsew")

# Botão ATUALIZAR
botao = ctk.CTkButton(frame_baixo, command=atualizar, text="Atualizar",
                      width=130, height=40,  # Ajuste de tamanho
                      # Fonte um pouco maior
                      font=("Calibri", 15, "bold"),
                      fg_color="#4fa882",          # Cor de fundo
                      text_color="white",    # Cor do texto
                      hover_color="grey",  # Cor ao passar o mouse
                      corner_radius=10).grid(row=3, column=1, padx=(10), pady=5, sticky="nsew")

# Botao DELETAR
botao = ctk.CTkButton(frame_baixo, command=deletar, text="Deletar",
                      width=130, height=40,  # Ajuste de tamanho
                      # Fonte um pouco maior
                      font=("Calibri", 15, "bold"),
                      fg_color="#ef5350",          # Cor de fundo
                      text_color="white",    # Cor do texto
                      hover_color="grey",  # Cor ao passar o mouse
                      corner_radius=10).grid(row=7, column=1, padx=(10), pady=5, sticky="nsew")

# Botão LIMPAR
botao = ctk.CTkButton(frame_baixo, command=limpar_campos, text="Limpar",
                      width=130, height=40,  # Ajuste de tamanho
                      # Fonte um pouco maior
                      font=("Calibri", 15, "bold"),
                      fg_color="#ffdb58",          # Cor de fundo
                      text_color="white",    # Cor do texto
                      hover_color="grey",  # Cor ao passar o mouse
                      corner_radius=10).grid(row=8, column=1, padx=(10), pady=5, sticky="nsew")


# Label DIREITA

# Criando Função Mostrar
def mostrar():

    global tree

    style = ttk.Style()
    # Alterando a fonte
    style.configure("Treeview", font=("Calibri", 9, "bold"))
    style.configure("Treeview.Heading", font=("Calibri", 11, "bold"))

    lista = mostrar_info()

    # Tabela para cabeçalho
    tabela_header = ['ID', 'Nome', 'CPF', 'Email',
                     'Telefone', 'Data', 'Observações']

    # Criando o Treeview
    tree = ttk.Treeview(frame_direita, selectmode="extended",
                        columns=tabela_header, show="headings")

    # Configurando as colunas e largura
    for col in tabela_header:
        tree.heading(col, text=col)
        tree.column(col, minwidth=0, width=100)

    # Inserindo dados na Treeview
    for item in lista:
        tree.insert('', 'end', values=item)

    # Configurando Scrollbars
    # Scroll Vertical
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)
    # Scroll Horizantal
    hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    # Posicionando a Treeview e Scrollbars
    tree.grid(row=0, column=0, sticky="nsew")
    vsb.grid(row=0, column=1, sticky="ns")
    hsb.grid(row=1, column=0, sticky="ew")

    hd = ["nw", "nw", "nw", "nw", "nw", "center", "center"]
    h = [10, 130, 100, 140, 80, 60, 100]
    n = 0

    for col in tabela_header:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n], anchor=hd[n])

        n += 1

    tree.bind('<<TreeviewSelect>>', item_selecionado)

    # Ajustando tamanho do frame_direita
    frame_direita.grid_rowconfigure(0, weight=1)
    frame_direita.grid_columnconfigure(0, weight=1)

    label_direita = ctk.CTkLabel(frame_direita, text="")
    label_direita.grid(row=0, column=1, rowspan=2,
                       sticky="nsew", padx=10, pady=10)


# Chamando Função Mostrar
mostrar()


app.mainloop()
