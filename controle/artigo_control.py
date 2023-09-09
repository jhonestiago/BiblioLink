from typing import List
from entidades.artigo import Artigo

class ArtigoControl:
    '''
    Cria o objeto ArtigoControl
    '''

    def __init__(self):
        self.__lista_artigos: List[Artigo] = []
    
    def add_artigo(self, artigo: Artigo) -> str:
        '''
        Adiciona um objeto Artigo em lista_artigos
        '''
        self.__lista_artigos.append(artigo)
        return 'Artigo salvo com sucesso'
    
    def consultar_artigo(self, indice:int):
        '''
        Retorna um artigo da lista_artigos
        '''
        artigo = self.__lista_artigos[indice]
        return artigo
    
    def alterar_artigo(self, indice:int, artigo:Artigo):
        '''
        Altera um artigo da lista_artigos
        '''
        self.__lista_artigos[indice] = artigo
        return 'Artigo exlcuído com sucesso'
    
    def excluir_artigo(self, indice: int) -> str:
        '''
        Exclui um objeto Artigo em lista_artigos
        '''
        del self.__lista_artigos[indice]
        return 'Artigo excluído com sucesso'
    
    @property
    def lista_artigos(self) -> List[Artigo]:
        '''
        Retorna a propriedade "Lista de Artigos"
        '''
        return self.__lista_artigos
    
    @lista_artigos.setter
    def lista_artigos(self, lista):
        pass