from Control.conexao import Conexao

conectarBanco = Conexao("ClickMed", "localhost", "5432", "postgres", "postgres")

class User():

    def __init__(self, usuario = None, email = None, senha = None, nome = None, tipoSangue = None, altura = None, peso = None, idade = None, endereço = None, fone = None):

        self._usuario = usuario
        self._email = email
        self._senha = senha
        self._nome = nome
        self._tipoSangue = tipoSangue
        self._peso = peso
        self._idade = idade
        self._endereço = endereço
        self._fone = fone

    def criarUsuario(self, usuario, email, senha):

        self._usuario = usuario
        self._email = email
        self._senha = senha

        criarUsuario = conectarBanco.manipularBanco(f'''
        Insert into "Cliente"
        Values (default, {self._usuario}, {self._email}, {self._senha})
        ''')

        if criarUsuario:

            return True
        
        else:
            
            return False