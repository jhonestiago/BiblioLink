class Autor:
    '''
    Cria o objeto Autor
    '''

    def __init__(self) -> None:
        self.__sobrenome:str = ''
        self.__nome = ''
        self.__inicial = self.__definir_inicial(self.nome) if self.__nome != '' else ''
        self.msg_validacao = ''

    def __definir_inicial(self, nome:str) -> str:
        var_inicial = nome[0].upper()
        return var_inicial

    @property
    def sobrenome(self) -> str:
        '''
        Retorna a propriedade "Sobrenome"
        '''
        return self.__sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome:str) -> None:
        if len(sobrenome) != 0:
            self.__sobrenome = sobrenome.upper()
            self.msg_validacao = ''
        else:
            self.msg_validacao = 'O campo "Sobrenome" é obrigatório'

    @property
    def nome(self) -> str:
        '''
        Retorna a propriedade "Nome"
        '''
        return self.__nome

    @nome.setter
    def nome(self, nome:str) -> None:
        if len(nome) != 0:
            self.__nome = nome
            self.inicial = nome
            self.msg_validacao = ''
        else:
            self.msg_validacao = 'O campo "Nome" é obrigatório'

    @property
    def inicial(self) -> str:
        '''
        Retorna a propriedade "Inicial".
        '''
        return self.__inicial

    @inicial.setter
    def inicial(self, nome:str) -> None:
        if nome != '':
            self.__inicial = self.__definir_inicial(nome)
