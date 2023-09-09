from typing import List
from models.livro import Livro

class LivroControl:
    '''
    Cria a classe LivroControl
    '''

    def __init__(self):
        self.__lista_livros:List[Livro] = []

    def add_livro(self, livro:Livro) -> str:
        '''
        Adiciona um objeto Livro em lista_livros
        '''
        self.__lista_livros.append(livro)
        return 'Livro salvo com sucesso'

    def consultar_livro(self, indice:int) -> Livro:
        '''
        Retorna um livro da lista_livros
        segundo o indice fornecido
        '''
        livro = self.__lista_livros[indice]
        return livro

    def excluir_livro(self, indice:int) -> str:
        '''
        Exclui um objeto Livro em lista_livros
        '''
        del self.__lista_livros[indice]
        return 'Livro excluído com sucesso'

    def alterar_livro(self, indice:int, livro:Livro) -> str:
        '''
        Altera um objeto Livro em lista_livros
        '''
        self.__lista_livros[indice] = livro
        return 'Livro alterado com sucesso'

    @property
    def lista_livros(self) -> List[Livro]:
        '''
        Retorna a propriedade "Lista de Livros"
        '''
        return self.__lista_livros

    @lista_livros.setter
    def lista_livros(self, lista:List[Livro]) -> None:
        pass
