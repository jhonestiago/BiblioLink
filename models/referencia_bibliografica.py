from typing import List
from models.autor import Autor

class ReferenciaBibliografica:
    '''
    Cria o objeto ReferenciaBibliográfica
    '''

    def __init__(self) -> None:
        '''
        Método inicializador da classe ReferenciaBibliografica
        '''
        self._autores:List[Autor] = []
        self._quant_autores:str = ''
        self._titulo_publicacao:str = ''
        self._subtitulo_publicacao:str = ''
        self._edicao:str = ''
        self._local_publicacao:str = ''
        self._ano_publicacao:str = ''
        self._versao:str = ''
        self._site:str = ''
        self._acesso:str = ''
        self.msg_validacao:str = ''

    def add_autor(self, autor) -> None:
        '''
        Adiciona um item do tipo "Autor" a lista "autores"
        autor: Autor
        '''
        if isinstance(autor, Autor):
            self._autores.append(autor)

    @property
    def autores(self) -> List[Autor]:
        '''
        Retorna a propriedade "Autores"
        '''
        return self._autores

    @autores.setter
    def autores(self, lista) -> None:
        pass

    @property
    def quant_autores(self) -> str:
        '''
        Retorna a propriedade "Quant. Autores"
        '''
        return self._quant_autores

    @quant_autores.setter
    def quant_autores(self, quantidade:str) -> None:
        if len(quantidade) != 0:
            if quantidade == '1 a 3 autores':
                self._quant_autores = quantidade
            elif quantidade == '> 3 autores':
                self._quant_autores = 'et al'
            self.msg_validacao = ''
        else:
            self.msg_validacao = 'O campo "Quant. Autores" é obrigatório'

    @property
    def titulo_publicacao(self) -> str:
        '''
        Retorna a propriedade "Título (Publicação)"
        '''
        return self._titulo_publicacao

    @titulo_publicacao.setter
    def titulo_publicacao(self, titulo:str) -> None:
        if len(titulo) != 0:
            self._titulo_publicacao = titulo
            self.msg_validacao = ''
        else:
            self.msg_validacao = 'O campo "Título" é obrigatório'

    @property
    def subtitulo_publicacao(self) -> str:
        '''
        Retorna a propriedade "Subtitulo (Publicação)"
        '''
        return self._subtitulo_publicacao

    @subtitulo_publicacao.setter
    def subtitulo_publicacao(self, subtitulo:str) -> None:
        if len(subtitulo) != 0:
            self._subtitulo_publicacao = subtitulo

    @property
    def edicao(self) -> str:
        '''
        Retorna a propriedade "Edição"
        '''
        return self._edicao

    @edicao.setter
    def edicao(self, edicao:str) -> None:
        if len(edicao) != 0:
            self._edicao = edicao

    @property
    def local_publicacao(self) -> str:
        '''
        Retorna a propriedade "Local (Publicação)"
        '''
        return self._local_publicacao

    @local_publicacao.setter
    def local_publicacao(self, local:str) -> None:
        if len(local) != 0:
            self._local_publicacao = local

    @property
    def ano_publicacao(self) -> str:
        '''
        Retorna a propriedade "Ano (Publicação)"
        '''
        return self._ano_publicacao

    @ano_publicacao.setter
    def ano_publicacao(self, ano:str) -> None:
        if len(ano) != 0:
            self._ano_publicacao = ano
            self.msg_validacao = ''
        else:
            self.msg_validacao = 'O campo ano é obrigatório'

    @property
    def versao(self) -> str:
        '''
        Retorna a propriedade "Versão"
        '''
        return self._versao

    @versao.setter
    def versao(self, versao:str) -> None:
        if len(versao) != 0:
            self._versao = versao

    @property
    def site(self) -> str:
        '''
        Retorna a propriedade "Site"
        '''
        return self._site

    @site.setter
    def site(self, site:str) -> None:
        if len(site) != 0:
            self._site = site

    @property
    def acesso(self) -> str:
        '''
        Retorna a propriedade "Acesso" (Data)
        '''
        return self._acesso

    @acesso.setter
    def acesso(self, acesso:str) -> None:
        if len(acesso) != 0:
            self._acesso = acesso
