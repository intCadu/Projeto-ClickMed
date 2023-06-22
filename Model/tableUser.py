from Control.conexao import Conexao

def createTable():

    listSql = ['''
    Create table "Cliente"(
    "ID" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Usuário" varchar(255) NOT NULL,
    "E-mail" varchar(255) NOT NULL,
    "Senha" varchar(255) NOT NULL,
    "Nome" varchar(255),
    "Tipo_Sangue" varchar(2),
    "Peso" numeric(2),
    "Ïdade" int,
    "Endereço" varchar(255), 
    "Contato" varchar(11)
    )
    ''']

    for sql in listSql:

        if connectionBank.manipularBanco(sql):

            print("Table created!")

        else:

            print("Something goes wrong...")

connectionBank = Conexao("ClickMed", "localhost", "5432", "postgres", "postgres")

createTable()