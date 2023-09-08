import numpy as np
from entidades.referencia_bibliografica import ReferenciaBibliografica

class Livro(ReferenciaBibliografica):
    '''
    Cria o objeto Livro
    '''

    def __init__(self) -> None:
        super().__init__()
        self.__tradutores:str = ''
        self.__editora:str = ''
        self.__total_paginas:str = ''
        self.__titulo_original:str = ''
        self.__colecao:str = ''
        self.__volume:str = ''
        self.__isbn:str = ''
        self.__referencia:str = ''
    
    def gerar_referencia_html(self):
        '''
        Retorna a referência em formato html
        '''
        vetor_referencia = np.zeros(24, dtype=object)
        vetor_referencia.fill('')
        vetor_referencia[0] = '<html><body><p style="text-align : left;">'
        for i, autor in enumerate(self.autores):
            if autor.sobrenome != '':
                vetor_referencia[2 * i + 1] = f'{autor.sobrenome},'
                vetor_referencia[2 * i + 2] = f' {autor.inicial}.'
        vetor_referencia[7] = f' <i>{self.quant_autores}</i>.' if self.quant_autores == 'et al' else ''
        vetor_referencia[8] = f' <b>{self.titulo_publicacao}</b>'
        vetor_referencia[9] = f': {self.subtitulo_publicacao}' if self.subtitulo_publicacao != '' else ''
        vetor_referencia[10] = f'. {self.edicao}. ed.' if self.edicao != '' else ''
        vetor_referencia[11] = f' Tradução de {self.tradutores}.' if self.tradutores != '' else ''
        vetor_referencia[12] = f' {self.local_publicacao}:' if self.local_publicacao != '' else ' [<i>S. l.</i>]:'
        vetor_referencia[13] = f' {self.editora},'
        vetor_referencia[14] = f' {self.ano_publicacao}.'
        vetor_referencia[15] = f' {self.total_paginas} p.' if self.total_paginas != '' else ''
        vetor_referencia[16] = f' Titulo original: {self.titulo_original}.' if self.titulo_original != '' else ''
        vetor_referencia[17] = f' ({self.colecao},' if self.colecao != '' else ''
        vetor_referencia[18] = f' v. {self.volume}).' if self.volume != '' else ''
        vetor_referencia[19] = f' <i>{self.versao}</i>.' if self.versao == 'E-book' else ''
        vetor_referencia[20] = f' ISBN: {self.isbn}.' if self.isbn != '' else ''
        vetor_referencia[21] = f' Disponível em: <a href="{self.site}">{self.site}</a>.' if  self.site != '' else ''
        vetor_referencia[22] = f' Acesso em: {self.acesso}.' if self.acesso != '' else ''
        vetor_referencia[23] = '</p></body></html>'
        
        if vetor_referencia[7] != '':
            for i in range(3, 7):
                vetor_referencia[i] = ''

        html_referencia = ''
        for dado in vetor_referencia:
            if dado == '':
                continue
            html_referencia += dado
        self.__referencia = html_referencia
        return html_referencia

    @property
    def tradutores(self) -> str:
        '''
        Retorna a propriedade "Tradutores"
        '''
        return self.__tradutores
    
    @tradutores.setter
    def tradutores(self, tradutores:str) -> None:
        if len(tradutores) != 0:
            self.__tradutores = tradutores
        
    @property
    def editora(self) -> str:
        '''
        Retorna a propriedade "Editora"
        '''
        return self.__editora
    
    @editora.setter
    def editora(self, editora:str) -> None:
        if len(editora) != 0:
            self.__editora = editora
        else:
            self.msg_validacao = 'O campo "Editora" é obrigatório'
    
    @property
    def total_paginas(self) -> str:
        '''
        Retorna a propriedade "Total Páginas"
        '''
        return self.__total_paginas
    
    @total_paginas.setter
    def total_paginas(self, total_paginas:str) -> None:
        if len(total_paginas) != 0:
            self.__total_paginas = total_paginas
    
    @property
    def titulo_original(self) -> str:
        '''
        Retorna a propriedade "Titulo original"
        '''
        return self.__titulo_original
    
    @titulo_original.setter
    def titulo_original(self, titulo_original:str) -> None:
        if len(titulo_original) != 0:
            self.__titulo_original = titulo_original

    @property
    def isbn(self) -> str:
        '''
        Retorna a propriedade "ISBN"
        '''
        return self.__isbn
    
    @isbn.setter
    def isbn(self, isbn:str) -> None:
        if len(isbn) != 0:
            self.__isbn = isbn
    
    @property
    def colecao(self) -> str:
        '''
        Retorna a propriedade "Coleção"
        '''
        return self.__colecao

    @colecao.setter
    def colecao(self, colecao:str) -> None:
        if len(colecao) != 0:
            self.__colecao = colecao

    @property
    def volume(self) -> str:
        '''
        Retorna a propriedade "Volume" (Coleção)
        '''
        return self.__volume

    @volume.setter
    def volume(self, volume:str) -> None:
        if len(volume) != 0:
            self.__volume = volume
    
    @property
    def referencia(self):
        '''
        Retorna a propriedade referencia
        '''
        return self.__referencia
    
    @referencia.setter
    def referencia(self, referencia:str):
        if referencia != '':
            self.__referencia = referencia
        else:
            self.msg_validacao = 'O campo "Referência" será mantido'