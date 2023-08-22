import numpy as np
from entidades.referencia_bibliografica import ReferenciaBibliografica

class Tese(ReferenciaBibliografica):
    '''
    Cria o objeto Tese
    '''
    
    def __init__(self) -> None:
        super().__init__()
        self.__orientador:str = ''
        self.__ano_deposito:str = ''
        self.__total_folhas:str = ''
        self.__tipo_trabalho:str = ''
        self.__grau_academico:str = ''
        self.__instituto:str = ''
        self.__universidade:str = ''
        
    def gerar_referencia_html(self) -> str:
        '''
        Retorna a referência em formato html
        '''
        vetor_referencia = np.zeros(19, dtype = object)
        vetor_referencia.fill('')
        vetor_referencia[0] = '<html><body><p style="text-align : left;">'
        for i, autor in enumerate(self.autores):
            if autor.sobrenome != '':
                vetor_referencia[2 * i + 1] = f'{autor.sobrenome},'
                vetor_referencia[2 * i + 2] = f' {autor.inicial}.'
        vetor_referencia[5] = f' <b>{self.titulo_publicacao}<b>'
        vetor_referencia[6] = f': {self.subtitulo_publicacao}' if self.subtitulo_publicacao != '' else ''
        vetor_referencia[7] = f'. Orientador: {self.orientador}' if self.orientador != '' else ''
        vetor_referencia[8] = f'. {self.ano_deposito}.'
        vetor_referencia[9] = f' {self.total_folhas} f.' if self.total_folhas != '' else ''
        vetor_referencia[10] = f' {self.tipo_trabalho}'
        vetor_referencia[11] = f' ({self.grau_academico}) —'
        vetor_referencia[12] = f' {self.instituto},' if self.instituto != '' else ''
        vetor_referencia[13] = f' {self.universidade},'
        vetor_referencia[14] = f' {self.local_publicacao},'
        vetor_referencia[15] = f' {self.ano_publicacao}.'
        vetor_referencia[16] = f' Disponível em: <a href="{self.site}">{self.site}</a>.' if self.site != '' else ''
        vetor_referencia[17] = f' Acesso em: {self.acesso}.' if self.acesso != '' else ''
        vetor_referencia[18] = '</p></body></html>'

        html_referencia = ''
        for dado in vetor_referencia:
            if dado == '':
                continue
            html_referencia += dado
        return html_referencia

    @property
    def orientador(self) -> str:
        '''
        Retorna a propriedade "Orientador"
        '''
        return self.__orientador
    
    @orientador.setter
    def orientador(self, orientador:str) -> None:
        if len(orientador) != 0:
            self.__orientador = orientador
    
    @property
    def ano_deposito(self) -> str:
        '''
        Retorna a propriedade "Ano (Deposito)"
        '''
        return self.__ano_deposito
        
    @ano_deposito.setter
    def ano_deposito(self, ano_deposito:str) -> None:
        if len(ano_deposito) != 0:
            self.__ano_deposito = ano_deposito
        else:
            self.msg_validacao = 'O campo "Ano (Deposito)" é obrigatório'
    
    @property
    def total_folhas(self) -> str:
        '''
        Retorna a propriedade "Total de Folhas"
        '''
        return self.__total_folhas
    
    @total_folhas.setter
    def total_folhas(self, total_folhas:str) -> None:
        if len(total_folhas) != 0:
            self.__total_folhas = total_folhas
    
    @property
    def tipo_trabalho(self) -> str:
        '''
        Retorna a propriedade "Tipo de Trabalho"
        '''
        return self.__tipo_trabalho
    
    @tipo_trabalho.setter
    def tipo_trabalho(self, tipo_trabalho:str) -> None:
        if len(tipo_trabalho) != 0:
            self.__tipo_trabalho = tipo_trabalho
        else:
            self.msg_validacao = 'O campo "Tipo de Trabalho" é obrigatório'
    
    @property
    def grau_academico(self) -> str:
        '''
        Retorna a propriedade "Grau Acadêmico"
        '''
        return self.__grau_academico
    
    @grau_academico.setter
    def grau_academico(self, grau:str) -> None:
        if len(grau) != 0:
            self.__grau_academico = grau
        else:
            self.msg_validacao = 'O campo "Grau Acadêmico" é obrigatório'
    
    @property
    def instituto(self) -> str:
        '''
        Retorna a propriedade "Instituto"
        '''
        return self.__instituto
    
    @instituto.setter
    def instituto(self, instituto:str) -> None:
        if len(instituto) != 0:
            self.__instituto = instituto
    
    @property
    def universidade(self) -> str:
        '''
        Retorna a propriedade "Universidade"
        '''
        return self.__universidade
    
    @universidade.setter
    def universidade(self, universidade:str) -> None:
        if len(universidade) != 0:
            self.__universidade = universidade
        else:
            self.msg_validacao = 'O campo "Universidade" é obrigatório'