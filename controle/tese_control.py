from typing import List
from entidades.tese import Tese

class TeseControl:
    '''
    Cria o objeto TeseControl
    '''

    def __init__(self):
        self.__lista_teses: List[Tese] = []
    
    def add_tese(self, tese: Tese) -> str:
        '''
        Adiciona um objeto Tese em lista_teses
        '''
        self.__lista_teses.append(tese)
        return 'Tese salva com sucesso'
    
    def consultar_tese(self, indice:int):
        '''
        Retorna uma tesa da lista_teses
        '''
        tese = self.__lista_teses[indice]
        return tese
    
    def alterar_tese(self, indice:int, tese:Tese):
        '''
        Altera uma tese da lista_teses
        '''
        self.__lista_teses[indice] = tese
        return 'Tese alterada com sucesso'
    
    def excluir_tese(self, indice: int) -> str:
        '''
        Exclui um objeto Tese em lista_teses
        '''
        del self.__lista_teses[indice]
        return 'Tese excluída com sucesso'
    
    @property
    def lista_teses(self) -> List[Tese]:
        '''
        Retorna a propriedade "Lista de Teses"
        '''
        return self.__lista_teses
    
    @lista_teses.setter
    def lista_teses(self, lista):
        pass