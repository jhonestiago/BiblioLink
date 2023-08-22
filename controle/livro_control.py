from typing import List
from entidades.livro import Livro

class LivroControl:
    '''
    Cria o objeto Livro Control
    '''

    def __init__(self):
        self.__lista_livros:List[Livro] = []
    
    def add_livro(self, livro:Livro) -> str:
        '''
        Adiciona um objeto Livro em lista_livro
        '''
        self.__lista_livros.append(livro)
        return 'Livro salvo com sucesso'
    
    def excluir_livro(self, indice:int) -> str:
        '''
        Exclui um objeto Livro em lista_livro
        '''
        del self.__lista_livros[indice]
        return 'Livro excluído com sucesso'
    
    @property
    def lista_livros(self) -> List[Livro]:
        '''
        Retorna a propriedade "Lista de Livros"
        '''
        return self.__lista_livros
    
    @lista_livros.setter
    def lista_livros(self, lista):
        pass