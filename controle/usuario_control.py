from typing import List
from entidades.usuario import Usuario

class UsuarioControl:

    def __init__(self):
        self.__lista_usuarios:List[Usuario] = []

    def add_usuario(self, usuario:Usuario) -> str:
        '''
        Adiciona um usuário a lista_usuarios
        '''
        self.__lista_usuarios.append(usuario)
        return 'Usuário adicionado com sucesso'
        
    def consultar_usuario(self, user:str, senha:str) -> bool:
        '''
        Consulta um usuário na lista_usuario
        '''
        acesso = None
        for usuario in self.__lista_usuarios:
            if usuario.user == user and usuario.senha == senha:
                acesso = True
                break
            else:
                acesso = False
        return acesso


    def alterar_usuario(self, indice:int, usuario:Usuario) -> str:
        '''
        Altera um usuario da lista_usuarios
        '''
        self.__lista_usuarios[indice] = usuario
        return 'Usuário alterado com sucesso'
    
    def excluir_usuario(self, indice:int) -> str:
        '''
        Exclui um usuario da lista_usuarios
        '''
        del self.__lista_usuarios[indice]
        return 'Usuário excluído com sucesso'
    
    @property
    def lista_usuarios(self) -> List[Usuario]:
        '''
        Retorna  a propriedade lista_usuarios
        '''
        return self.__lista_usuarios
    
    @lista_usuarios.setter
    def lista_usuarios(self, usuario):
        pass