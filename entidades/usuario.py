class Usuario:

    def __init__(self):
        self.__nome:str = ''
        self.__sobrenome:str = ''
        self.__user:str = ''
        self.__senha:str = ''
        self.__senha_conf:str = ''
        self.msg_validacao:str = ''
    
    @property
    def nome(self):
        '''
        Retorna a propriedade "nome"
        '''
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if nome != '':
            self.__nome = nome
        else:
            self.msg_validacao = 'O campo "Nome" é obrigatório'
    
    @property
    def sobrenome(self):
        '''
        Retorna a propriedade "sobrenome"
        '''
        return self.__sobrenome
    
    @sobrenome.setter
    def sobrenome(self, sobrenome):
        if sobrenome != '':
            self.__sobrenome = sobrenome
        else:
            self.msg_validacao = 'O campo "Sobrenome" é obrigatório'
    
    @property
    def user(self):
        '''
        Retorna a propriedade "user"
        '''
        return self.__user
    
    @user.setter
    def user(self, user):
        if user != '':
            self.__user  = user
        else:
            self.msg_validacao = 'O campo "user" é obrigatório'
    
    @property
    def senha(self):
        '''
        Retorna a propriedade "senha"
        '''
        return self.__senha
    
    @senha.setter
    def senha(self, senha):
        if senha != '':
            if len(senha) >= 5 and len(senha) <= 8:
                self.__senha = senha
            else:
                self.msg_validacao = 'A senha deve possuir entre 5 a 8 caractéres'
        else:
            self.msg_validacao = 'O campo "senha" é obrigatório'
    
    @property
    def senha_conf(self):
        '''
        Retorna a propriedade "senha_conf"
        '''
        return self.__senha_conf
    
    @senha_conf.setter
    def senha_conf(self, senha_conf):
        if senha_conf != '':
            if senha_conf == self.senha:
                self.__senha_conf = senha_conf
            else:
                self.msg_validacao = 'As senhas fornecidas não são iguais'
        else:
            self.msg_validacao = 'É obrigatório a confirmação da senha'