from tkinter import *
import mysql.connector

# FUNÇÕES PARA INSERÇÃO DOS DADOS

def inserir_pessoa():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    sql = "INSERT INTO Pessoas (CPF, Nome) VALUES (%s, %s)"
    values = (cpf, nome)
    cursor.execute(sql, values)
    db.commit()
    listar_registros()

def inserir_numero_telefone():
    numero = entry_numero.get()
    cpf_pessoa = entry_cpf_pessoa.get()
    sql = "INSERT INTO NumerosTelefone (Numero, CPF_pessoa) VALUES (%s, %s)"
    values = (numero, cpf_pessoa)
    cursor.execute(sql, values)
    db.commit()
    listar_registros()

def listar_registros():
    sql = "SELECT p.Nome, p.CPF, nt.ID, nt.Numero FROM Pessoas p INNER JOIN NumerosTelefone nt ON p.CPF = nt.CPF_pessoa"
    cursor.execute(sql)
    registros = cursor.fetchall()
    
    text_registros.delete(1.0, END)
    for registro in registros:
        nome = registro[0]
        cpf = registro[1]
        id_numero = registro[2]
        numero = registro[3]
        text_registros.insert(END, f"Nome: {nome}\nCPF: {cpf}\nID do Número: {id_numero}\nNúmero de telefone: {numero}\n---------------------------\n")

def atualizar_pessoa():
    cpf = entry_cpf_atualizar.get()
    novo_nome = entry_novo_nome.get()
    sql = "UPDATE Pessoas SET Nome = %s WHERE CPF = %s"
    values = (novo_nome, cpf)
    cursor.execute(sql, values)
    db.commit()
    listar_registros()

def atualizar_numero_telefone():
    id_numero = entry_id_numero_atualizar.get()
    novo_numero = entry_novo_numero.get()
    sql = "UPDATE NumerosTelefone SET Numero = %s WHERE ID = %s"
    values = (novo_numero, id_numero)
    cursor.execute(sql, values)
    db.commit()
    listar_registros()

def deletar_pessoa():
    cpf = entry_cpf_deletar.get()
    sql = "DELETE FROM Pessoas WHERE CPF = %s"
    value = (cpf,)
    cursor.execute(sql, value)
    db.commit()
    listar_registros()

def deletar_numero_telefone():
    id_numero = entry_id_numero_deletar.get()
    sql = "DELETE FROM NumerosTelefone WHERE ID = %s"
    value = (id_numero,)
    cursor.execute(sql, value)
    db.commit()
    listar_registros()

# INTERFACE CRUD

root = Tk()
root.title("Cadastro de Pessoas")

# Conexão com o banco de dados
db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="crud"
)
cursor = db.cursor()


label_nome = Label(root, text="Nome:")
label_nome.grid(row=0, column=0, padx=5, pady=5)
entry_nome = Entry(root)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

label_cpf = Label(root, text="CPF:")
label_cpf.grid(row=1, column=0, padx=5, pady=5)
entry_cpf = Entry(root)
entry_cpf.grid(row=1, column=1, padx=5, pady=5)

button_inserir_pessoa = Button(root, text="Inserir Pessoa", command=inserir_pessoa)
button_inserir_pessoa.grid(row=2, column=0, padx=5, pady=5)

label_numero = Label(root, text="Número de Telefone:")
label_numero.grid(row=3, column=0, padx=5, pady=5)
entry_numero = Entry(root)
entry_numero.grid(row=3, column=1, padx=5, pady=5)

label_cpf_pessoa = Label(root, text="CPF da Pessoa:")
label_cpf_pessoa.grid(row=4, column=0, padx=5, pady=5)
entry_cpf_pessoa = Entry(root)
entry_cpf_pessoa.grid(row=4, column=1, padx=5, pady=5)

button_inserir_numero_telefone = Button(root, text="Inserir Número de Telefone", command=inserir_numero_telefone)
button_inserir_numero_telefone.grid(row=5, column=0, padx=5, pady=5)

button_listar = Button(root, text="Listar Registros", command=listar_registros)
button_listar.grid(row=6, column=0, padx=5, pady=5)

text_registros = Text(root, width=50, height=10)
text_registros.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

label_cpf_atualizar = Label(root, text="CPF da Pessoa:")
label_cpf_atualizar.grid(row=8, column=0, padx=5, pady=5)
entry_cpf_atualizar = Entry(root)
entry_cpf_atualizar.grid(row=8, column=1, padx=5, pady=5)

label_novo_nome = Label(root, text="Novo Nome:")
label_novo_nome.grid(row=9, column=0, padx=5, pady=5)
entry_novo_nome = Entry(root)
entry_novo_nome.grid(row=9, column=1, padx=5, pady=5)

button_atualizar_pessoa = Button(root, text="Atualizar Pessoa", command=atualizar_pessoa)
button_atualizar_pessoa.grid(row=10, column=0, padx=5, pady=5)

label_id_numero_atualizar = Label(root, text="ID do Número:")
label_id_numero_atualizar.grid(row=11, column=0, padx=5, pady=5)
entry_id_numero_atualizar = Entry(root)
entry_id_numero_atualizar.grid(row=11, column=1, padx=5, pady=5)

label_novo_numero = Label(root, text="Novo Número:")
label_novo_numero.grid(row=12, column=0, padx=5, pady=5)
entry_novo_numero = Entry(root)
entry_novo_numero.grid(row=12, column=1, padx=5, pady=5)

button_atualizar_numero_telefone = Button(root, text="Atualizar Número de Telefone", command=atualizar_numero_telefone)
button_atualizar_numero_telefone.grid(row=13, column=0, padx=5, pady=5)

label_cpf_deletar = Label(root, text="CPF da Pessoa:")
label_cpf_deletar.grid(row=14, column=0, padx=5, pady=5)
entry_cpf_deletar = Entry(root)
entry_cpf_deletar.grid(row=14, column=1, padx=5, pady=5)

button_deletar_pessoa = Button(root, text="Deletar Pessoa", command=deletar_pessoa)
button_deletar_pessoa.grid(row=15, column=0, padx=5, pady=5)

label_id_numero_deletar = Label(root, text="ID do Número:")
label_id_numero_deletar.grid(row=16, column=0, padx=5, pady=5)
entry_id_numero_deletar = Entry(root)
entry_id_numero_deletar.grid(row=16, column=1, padx=5, pady=5)

button_deletar_numero_telefone = Button(root, text="Deletar Número de Telefone", command=deletar_numero_telefone)
button_deletar_numero_telefone.grid(row=17, column=0, padx=5, pady=5)

root.mainloop()
