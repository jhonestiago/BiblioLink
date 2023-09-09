class Usuario:
    '''
    Cria a classe Usuario
    '''

    def __init__(self):
        self.__nome:str = ''
        self.__sobrenome:str = ''
        self.__user:str = ''
        self.__senha:str = ''
        self.__senha_conf:str = ''
        self.msg_validacao:str = ''

    @property
    def nome(self) -> str:
        '''
        Retorna a propriedade nome
        '''
        return self.__nome

    @nome.setter
    def nome(self, nome:str) -> None:
        if nome != '':
            self.__nome = nome
            self.msg_validacao = ''
        else:
            self.msg_validacao = 'O campo "Nome" é obrigatório'

    @property
    def sobrenome(self) -> str:
        '''
        Retorna a propriedade sobrenome
        '''
        return self.__sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome:str) -> None:
        if sobrenome != '':
            self.__sobrenome = sobrenome
            self.msg_validacao = ''
        else:
            self.msg_validacao = 'O campo "Sobrenome" é obrigatório'

    @property
    def user(self) -> str:
        '''
        Retorna a propriedade user
        '''
        return self.__user

    @user.setter
    def user(self, user:str) -> None:
        if user != '':
            self.__user  = user
            self.msg_validacao = ''
        else:
            self.msg_validacao = 'O campo "user" é obrigatório'

    @property
    def senha(self) -> str:
        '''
        Retorna a propriedade senha
        '''
        return self.__senha

    @senha.setter
    def senha(self, senha:str) -> None:
        if senha != '':
            if len(senha) >= 5 and len(senha) <= 8:
                self.__senha = senha
                self.msg_validacao = ''
            else:
                self.msg_validacao = 'A senha deve possuir entre 5 a 8 caracteres'
        else:
            self.msg_validacao = 'O campo "senha" é obrigatório'

    @property
    def senha_conf(self) -> str:
        '''
        Retorna a propriedade senha_conf
        '''
        return self.__senha_conf

    @senha_conf.setter
    def senha_conf(self, senha_conf:str) -> None:
        if senha_conf != '':
            if senha_conf == self.senha:
                self.__senha_conf = senha_conf
            else:
                self.msg_validacao = 'As senhas fornecidas não são iguais'
        else:
            self.msg_validacao = 'É obrigatório a confirmação da senha'
