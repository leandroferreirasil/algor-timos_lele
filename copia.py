def __init__(self, nome, nome_usuário, senha, email, telefone, habilitação, cpf, rg):
        self._nome              = nome
        self._nome_usuário      = nome_usuário
        self._senha             = senha
        self._email             = email
        self._telefone          = telefone
        self._habilitação       = habilitação
        self._cpf               = cpf
        self._rg                = rg
    
    def get_nome(self):
        return self._nome
    
    def set_nome(self, nome):
        self._nome = nome
    
    def get_nome_usuário(self):
        return self._nome_usuário
    
    def set_nome_usuário(self, nome_usuário):
        self._nome_usuário = nome_usuário

    def get_senha(self):
        return self._senha
    
    def set_senha(self, senha):
        self._senha= senha

    def get_email(self):
        return self._email
    
    def set_email(self, email):
        self._email = email

    def get_telefone(self):
        return self._telefone
    
    def set_telefone(self, telefone):
        self._telefone = telefone

    def get_habilitação(self):
        return self._habilitação
    
    def set_habilitação(self, habilitação):
        self._habilitação = habilitação

    def get_cpf(self):
        return self._cpf
    
    def set_cpf(self, cpf):
        self._cpf = cpf

    def get_rg(self):
        return self._rg
    
    def set_rg(self, rg):
        self._rg = rg

    def imprimir_informações(self):
        print(" Novo Usuário!")
        print(f" Nome: {self._nome}\n Nome de usuário: {self._nome_usuário}\n Senha: {self._senha}\n Email: {self._email}\n Telefone: {self._telefone}\n Habilitação: {self._habilitação}\n Cpf: {self._cpf}\n Rg: {self._rg}")
        print(" --------------------------------------------------------------------")