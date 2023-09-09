import numpy as np
from entidades.referencia_bibliografica import ReferenciaBibliografica

class Artigo(ReferenciaBibliografica):
    '''
    Cria o objeto Artigo
    '''

    def __init__(self) -> None:
        super().__init__()
        self.__titulo_periodico:str = ''
        self.__subtitulo_periodico:str = ''
        self.__ano_periodico:str = ''
        self.__volume:str = ''
        self.__numero:str = ''
        self.__tomo:str = ''
        self.__paginas:str = ''
        self.__periodo:str = ''
        self.__issn:str = ''
        self.__doi:str = ''
        self.__referencia:str = ''
    
    def gerar_referencia_html(self) -> str:
        '''
        Retorna a referencia em formato html
        '''
        vetor_referencia = np.zeros(28, dtype=object)
        vetor_referencia.fill('')
        vetor_referencia[0] = '<html><body><p style="text-align : left;">'
        for i, autor in enumerate(self.autores):
            if autor.sobrenome != '':
                vetor_referencia[2 * i + 1] = f'{autor.sobrenome},'
                vetor_referencia[2 * i + 2] = f' {autor.inicial}. '
        vetor_referencia[7] = f'<i>{self.quant_autores}</i>.' if self.quant_autores == 'et al' else ''
        vetor_referencia[8] = f' {self.titulo_publicacao}'
        vetor_referencia[9] = f': {self.subtitulo_publicacao}' if self.subtitulo_publicacao != '' else ''
        vetor_referencia[10] = f'. <b>{self.titulo_periodico}</b>'
        vetor_referencia[11] = f': {self.subtitulo_periodico}' if self.subtitulo_periodico != '' else ''
        vetor_referencia[12] = f', {self.local_publicacao}' if self.local_publicacao != '' else ', [<i>S. l.</i>]'
        vetor_referencia[13] = f', ano {self.ano_periodico}' if self.ano_periodico != '' else ''
        vetor_referencia[14] = f', v. {self.volume}' if self.volume != '' else ''
        vetor_referencia[15] = f', {self.numero}' if self.numero != '' else ''
        vetor_referencia[16] = f', ed. {self.edicao}' if self.numero != '' else ''
        vetor_referencia[18] = f', t. {self.tomo}' if self.tomo != '' else ''
        vetor_referencia[19] = f', p. {self.paginas},'
        vetor_referencia[20] = f' {self.periodo}.' if self.periodo != '' else ''
        vetor_referencia[21] = f' {self.ano_publicacao}.'
        vetor_referencia[22] = f' ISSN {self.issn}.' if self.issn != '' else ''
        vetor_referencia[23] = ' versao <i>online</i>.' if self.issn == 'Online' else ''
        vetor_referencia[24] = f' DOI: {self.doi}' if self.doi != '' else ''
        vetor_referencia[25] = f' Disponível em: <a href="{self.site}">{self.site}</a>.' if self.site != '' else ''
        vetor_referencia[26] = f' Acesso em: {self.acesso}.' if self.acesso != '' else ''
        vetor_referencia[27] = '</p></body></html>'
        
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
    def titulo_periodico(self) -> str:
        '''
        Retorna a propriedade "Título" (Periódico)
        '''
        return self.__titulo_periodico
    
    @titulo_periodico.setter
    def titulo_periodico(self, titulo_periodico:str) -> None:
        if len(titulo_periodico) != 0:
            self.__titulo_periodico = titulo_periodico
        else:
            self.msg_validacao = 'O campo "Título" (Periódico) é obrigatório'

    @property
    def subtitulo_periodico(self) -> str:
        '''
        Retorna a propriedade "Subtítulo" (Periódico)
        '''
        return self.__subtitulo_periodico
    
    @subtitulo_periodico.setter
    def subtitulo_periodico(self, subtitulo_periodico:str) -> None:
        if len(subtitulo_periodico) != 0:
            self.__subtitulo_periodico = subtitulo_periodico
        
    @property
    def ano_periodico(self) -> str:
        '''
        Retorna a propriedade "Ano" (Periódico)
        '''
        return self.__ano_periodico
    
    @ano_periodico.setter
    def ano_periodico(self, ano_periodico:str) -> None:
        if len(ano_periodico) != 0:
            self.__ano_periodico = ano_periodico
        else:
            self.msg_validacao = 'O campo "Ano" (Periódico) é obrigatório'

    @property
    def volume(self) -> str:
        '''
        Retorna a propriedade "Volume" (Periódico)
        '''
        return self.__volume
    
    @volume.setter
    def volume(self, volume:str) -> None:
        if len(volume) != 0:
            self.__volume = volume

    @property
    def numero(self) -> str:
        '''
        Retorna a propriedade "Número" (Periódico)
        '''
        return self.__numero
    
    @numero.setter
    def numero(self, numero:str) -> None:
        if len(numero) != 0:
            self.__numero = numero

    @property
    def tomo(self) -> str:
        '''
        Retorna a propriedade "Tomo" (Periódico)
        '''
        return self.__tomo
    
    @tomo.setter
    def tomo(self, tomo:str) -> None:
        if len(tomo) != 0:
            self.__tomo = tomo
    
    @property
    def paginas(self) -> str:
        '''
        Retorna a propriedade "Páginas"
        '''
        return self.__paginas
    
    @paginas.setter
    def paginas(self, paginas:str) -> None:
        if len(paginas) != 0:
            self.__paginas = paginas
        else:
            self.msg_validacao = 'O campo "Páginas" é obrigatório'
    
    @property
    def periodo(self) -> str:
        '''
        Retorna a propriedade "Período"
        '''
        return self.__periodo
    
    @periodo.setter
    def periodo(self, periodo:str) -> None:
        if len(periodo) != 0:
            self.__periodo = periodo
    
    @property
    def issn(self) -> str:
        '''
        Retorna a propriedade "ISSN"
        '''
        return self.__issn
    
    @issn.setter
    def issn(self, issn:str) -> None:
        if len(issn) != 0:
            self.__issn = issn    

    @property
    def doi(self) -> str:
        '''
        Retorna a propriedade "DOI"
        '''
        return self.__doi
    
    @doi.setter
    def doi(self, doi:str) -> None:
        if len(doi) != 0:
            self.__doi = doi
    
    @property
    def referencia(self):
        return self.__referencia
    
    @referencia.setter
    def referencia(self, referencia):
        pass