'''
Módulo principal do aplicativo BiblioLink.

Este módulo contém a lógica principal do aplicativo BiblioLink, 
incluindo a inicialização e execução da interface gráfica do usuário.
'''

import sys
from gui_principal import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication 
from PyQt6.QtWidgets import QTableWidgetItem, QLineEdit, QRadioButton, QComboBox
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt

from models.livro import Livro
from models.autor import Autor
from models.artigo import Artigo
from models.tese import Tese
from models.usuario import Usuario

from controllers.livro_control import LivroControl
from controllers.artigo_control import ArtigoControl
from controllers.tese_control import TeseControl
from controllers.usuario_control import UsuarioControl

class Principal(Ui_MainWindow, QMainWindow):
    '''
    Cria a classe Principal
    '''

    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.init_components()
        self.controle_livro = LivroControl()
        self.controle_artigo = ArtigoControl()
        self.controle_tese = TeseControl()
        self.controle_usuario = UsuarioControl()
        self.init_usuarios()
        self.cor_sucesso = 'background-color: rgb(101, 184, 145)'
        self.cor_erro = 'background-color: rgb(204, 41, 54); color: rgb(255, 255, 255)'

    def init_components(self) -> None:
        '''
        Inicializa os componentes das páginas:
        Login, Home, Livro, Artigo, Tese,
        Lista e Cadastro
        '''
        #Componentes da tela de Login
        self.frame_login_msg.hide()
        self.label_login_icone.setPixmap(QPixmap('img/icon_user'))
        self.pushButton_login_entrar.clicked.connect(self.realizar_login)
        self.pushButton_login_cadastrar.clicked.connect(self.acessar_cadastro)
        self.pushButton_login_fechar_msg.clicked.connect(lambda: self.frame_login_msg.hide())

        #Componentes da tela: Home
        self.label_home_logo.setPixmap(QPixmap('img/logo.png'))
        self.label_home_icon_livro.setPixmap(QPixmap('img/icon_livro.png'))
        self.label_home_icon_artigo.setPixmap(QPixmap('img/icon_artigo.png'))
        self.label_home_icon_tese.setPixmap(QPixmap('img/icon_tese.png'))
        self.label_home_icon_lista.setPixmap(QPixmap('img/icon_lista.png'))
        self.pushButton_home_livro.clicked.connect(self.acessar_livro)
        self.pushButton_home_artigo.clicked.connect(self.acessar_artigo)
        self.pushButton_home_tese.clicked.connect(self.acessar_tese)
        self.pushButton_home_lista.clicked.connect(self.acessar_lista)
        self.pushButton_home_sair.setIcon(QIcon('img/icon_sair.png'))
        self.pushButton_home_sair.clicked.connect(self.sair_sistema)

        #Componentes da tela: Livro
        self.frame_livro_msg.hide()
        self.label_icon_livro.setPixmap(QPixmap('img/icon_livro.png'))
        self.pushButton_livro_salvar.clicked.connect(self.salvar_livro)
        self.pushButton_livro_lista.clicked.connect(self.acessar_lista)
        self.pushButton_livro_home.clicked.connect(self.acessar_home)
        self.pushButton_livro_limpar_referencia.setIcon(QIcon('img/icon_limpar.png'))
        self.pushButton_livro_limpar_referencia.clicked.connect(lambda: self.label_livro_referencia.setText('Referência'))
        self.pushButton_livro_fechar_msg.clicked.connect(lambda: self.frame_livro_msg.hide())

        #Componentes da tela: Artigo
        self.frame_artigo_msg.hide()
        self.label_icon_artigo.setPixmap(QPixmap('img/icon_artigo.png'))
        self.pushButton_artigo_salvar.clicked.connect(self.salvar_artigo)
        self.pushButton_artigo_lista.clicked.connect(self.acessar_lista)
        self.pushButton_artigo_home.clicked.connect(self.acessar_home)
        self.pushButton_artigo_limpar_referencia.setIcon(QIcon('img/icon_limpar.png'))
        self.pushButton_artigo_limpar_referencia.clicked.connect(lambda: self.label_artigo_referencia.setText('Referência'))
        self.pushButton_artigo_fechar_msg.clicked.connect(lambda: self.frame_artigo_msg.hide())

        #Componentes da tela: Trabalhos Acadêmicos / Tese
        self.frame_tese_msg.hide()
        self.label_icon_tese.setPixmap(QPixmap('img/icon_tese.png'))
        self.pushButton_tese_salvar.clicked.connect(self.salvar_tese)
        self.pushButton_tese_lista.clicked.connect(self.acessar_lista)
        self.pushButton_tese_home.clicked.connect(self.acessar_home)
        self.pushButton_tese_limpar_referencia.setIcon(QIcon('img/icon_limpar.png'))
        self.pushButton_tese_limpar_referencia.clicked.connect(lambda : self.label_tese_referencia.setText('Referência'))
        self.pushButton_tese_fechar_msg.clicked.connect(lambda: self.frame_tese_msg.hide())

        #Componentes da tela: Lista(Geral)
        self.frame_lista_msg.hide()
        self.label_icon_lista.setPixmap(QPixmap('img/icon_lista.png'))
        self.pushButton_lista_fechar_msg.clicked.connect(lambda: self.frame_lista_msg.hide())
        self.pushButton_lista_limpar_referencia.setIcon(QIcon('img/icon_limpar.png'))
        self.pushButton_lista_limpar_referencia.clicked.connect(lambda: self.label_lista_referencia.setText('Referência'))

        #Componentes da tela: Lista(Livros)
        self.pushButton_lista_livros_exibir.clicked.connect(self.exibir_referencia_livro)
        self.pushButton_lista_livros_alterar.clicked.connect(self.alterar_dados_livro)
        self.pushButton_lista_livros_excluir.clicked.connect(self.excluir_livro)
        self.pushButton_lista_livros_novo.clicked.connect(self.acessar_livro)
        self.pushButton_lista_livros_home.clicked.connect(self.acessar_home)

        #Componentes da tela: Lista(Artigos)
        self.pushButton_lista_artigos_exibir.clicked.connect(self.exibir_referencia_artigo)
        self.pushButton_lista_artigos_alterar.clicked.connect(self.alterar_dados_artigo)
        self.pushButton_lista_artigos_excluir.clicked.connect(self.excluir_artigo)
        self.pushButton_lista_artigos_novo.clicked.connect(self.acessar_artigo)
        self.pushButton_lista_artigos_home.clicked.connect(self.acessar_home)

        #Componentes da tela: Lista(Teses)
        self.pushButton_lista_teses_exibir.clicked.connect(self.exibir_referencia_tese)
        self.pushButton_lista_teses_alterar.clicked.connect(self.alterar_dados_tese)
        self.pushButton_lista_teses_excluir.clicked.connect(self.excluir_tese)
        self.pushButton_lista_teses_novo.clicked.connect(self.acessar_tese)
        self.pushButton_lista_teses_home.clicked.connect(self.acessar_home)

        #Componentes da tela: Cadastro de usuário
        self.frame_cadastro_msg.hide()
        self.label_icon_cadastro.setPixmap(QPixmap('img/icon_user'))
        self.pushButton_cadastro_cadastrar.clicked.connect(self.cadastrar_usuario)
        self.pushButton_cadastro_sair.clicked.connect(self.sair_sistema)
        self.pushButton_cadastro_fechar_msg.clicked.connect(lambda: self.frame_cadastro_msg.hide())

        #Componentes da tela: Usuários
        self.frame_usuarios_msg.hide()
        self.label_icon_usuarios.setPixmap(QPixmap('img/icon_user'))
        self.pushButton_usuarios_alterar.clicked.connect(self.alterar_dados_usuario)
        self.pushButton_usuarios_excluir.clicked.connect(self.excluir_usuario)
        self.pushButton_usuarios_cadastrar.clicked.connect(self.acessar_cadastro)
        self.pushButton_usuarios_sair.clicked.connect(self.sair_sistema)
        self.pushButton_usuarios_fechar_msg.clicked.connect(lambda: self.frame_usuarios_msg.hide())

    def init_usuarios(self) -> None:
        '''
        Inicializa o user "admin" e "controle"
        '''
        usuario_1 = Usuario()
        usuario_1.nome = 'ADMIN'
        usuario_1.user = 'admin'
        usuario_1.senha = '12345'
        usuario_1.senha_conf = '12345'
        self.controle_usuario.add_usuario(usuario_1)
        usuario_2 = Usuario()
        usuario_2.nome = 'CONTROLE'
        usuario_2.user = 'controle'
        usuario_2.senha = '54321'
        usuario_2.senha_conf = '54321'
        self.controle_usuario.add_usuario(usuario_2)

    def realizar_login(self) -> None:
        '''
        Acessa a plataforma BiblioLink
        e faz a validação de usuário
        '''
        user = self.lineEdit_login_usuario.text()
        senha = self.lineEdit_login_senha.text()
        if self.controle_usuario.consultar_usuario(user, senha):
            if user == 'controle':
                self.lineEdit_login_usuario.clear()
                self.lineEdit_login_senha.clear()
                self.frame_login_msg.hide()
                self.acessar_usuarios()
            else:
                self.lineEdit_login_usuario.clear()
                self.lineEdit_login_senha.clear()
                self.frame_login_msg.hide()
                self.stackedWidget_sistema.setCurrentWidget(self.page_sistema_home)
                print('Login realizado com sucesso')
        else:
            self.label_login_msg.setText('Usuário ou senha incorretos!!!')
            self.label_login_msg.setStyleSheet(self.cor_erro)
            self.frame_login_msg.show()

    # Métodos (Livro)

    def salvar_livro(self) -> None:
        '''
        Salva as informações da referência livro
        '''
        indice = self.tableWidget_lista_livros.currentRow()
        livro = Livro()
        livro.add_autor(Autor())
        livro.autores[0].sobrenome = self.lineEdit_livro_sobrenome_p_autor.text()
        livro.autores[0].nome = self.lineEdit_livro_nome_p_autor.text()
        livro.add_autor(Autor())
        if self.lineEdit_livro_sobrenome_s_autor.text() != '':
            livro.autores[1].sobrenome = self.lineEdit_livro_sobrenome_s_autor.text()
            livro.autores[1].nome = self.lineEdit_livro_nome_s_autor.text()
        livro.add_autor(Autor())
        if self.lineEdit_livro_sobrenome_t_autor.text() != '':
            livro.autores[2].sobrenome = self.lineEdit_livro_sobrenome_t_autor.text()
            livro.autores[2].nome = self.lineEdit_livro_nome_t_autor.text()
        if self.radioButton_livro_quant_autores_1.isChecked():
            livro.quant_autores = '1 a 3 autores'
        elif self.radioButton_livro_quant_autores_2.isChecked():
            livro.quant_autores = '> 3 autores'
        livro.titulo_publicacao = self.lineEdit_livro_titulo.text()
        livro.subtitulo_publicacao = self.lineEdit_livro_subtitulo.text()
        livro.edicao = self.lineEdit_livro_edicao.text()
        livro.tradutores = self.lineEdit_livro_tradutores.text()
        livro.local_publicacao = self.lineEdit_livro_local.text()
        livro.editora = self.lineEdit_livro_editora.text()
        livro.ano_publicacao = self.lineEdit_livro_ano.text()
        livro.total_paginas = self.lineEdit_livro_total_paginas.text()
        livro.titulo_original = self.lineEdit_livro_titulo_original.text()
        livro.colecao = self.lineEdit_livro_colecao.text()
        livro.volume = self.lineEdit_livro_colecao_volume.text()
        livro.versao = self.comboBox_livro_versao.currentText()
        livro.isbn = self.lineEdit_livro_isbn.text()
        livro.site = self.lineEdit_livro_site.text()
        livro.acesso = self.lineEdit_livro_acesso.text()
        if len(livro.msg_validacao) != 0:
            self.label_livro_msg.setText(livro.msg_validacao)
            self.label_livro_msg.setStyleSheet(self.cor_erro)
            self.frame_livro_msg.show()
        else:
            if indice >= 0:
                msg = self.controle_livro.alterar_livro(indice, livro)
                self.label_livro_msg.setText(msg)
                self.label_livro_msg.setStyleSheet(self.cor_sucesso)
                self.frame_livro_msg.show()
                self.label_livro_referencia.setText(livro.gerar_referencia_html())
                self.tabelar_livros()
                self.limpar_livro()
                self.tableWidget_lista_livros.clearSelection()
            else:
                msg = self.controle_livro.add_livro(livro)
                self.label_livro_msg.setText(msg)
                self.label_livro_msg.setStyleSheet(self.cor_sucesso)
                self.frame_livro_msg.show()
                self.label_livro_referencia.setText(livro.gerar_referencia_html())
                self.tabelar_livros()
                self.limpar_livro()

    def tabelar_livros(self) -> None:
        '''
        Atualiza as infomações da tabela de livros
        '''
        cont_linhas = 0
        self.tableWidget_lista_livros.clearContents()
        self.tableWidget_lista_livros.setRowCount(len(self.controle_livro.lista_livros))
        for livro in self.controle_livro.lista_livros:
            self.tableWidget_lista_livros.setItem(cont_linhas, 0, QTableWidgetItem(livro.autores[0].sobrenome))
            autor_sec = livro.autores[1].sobrenome if len(livro.autores) >= 2 else ''
            autor_ter = livro.autores[2].sobrenome if len(livro.autores) == 3 else ''
            self.tableWidget_lista_livros.setItem(cont_linhas, 1, QTableWidgetItem(autor_sec))
            self.tableWidget_lista_livros.setItem(cont_linhas, 2, QTableWidgetItem(autor_ter))
            self.tableWidget_lista_livros.setItem(cont_linhas, 3, QTableWidgetItem(livro.quant_autores))
            self.tableWidget_lista_livros.setItem(cont_linhas, 4, QTableWidgetItem(livro.titulo_publicacao))
            self.tableWidget_lista_livros.setItem(cont_linhas, 5, QTableWidgetItem(livro.subtitulo_publicacao))
            self.tableWidget_lista_livros.setItem(cont_linhas, 6, QTableWidgetItem(livro.edicao))
            self.tableWidget_lista_livros.setItem(cont_linhas, 7, QTableWidgetItem(livro.tradutores))
            self.tableWidget_lista_livros.setItem(cont_linhas, 8, QTableWidgetItem(livro.local_publicacao))
            self.tableWidget_lista_livros.setItem(cont_linhas, 9, QTableWidgetItem(livro.editora))
            self.tableWidget_lista_livros.setItem(cont_linhas, 10, QTableWidgetItem(livro.ano_publicacao))
            self.tableWidget_lista_livros.setItem(cont_linhas, 11, QTableWidgetItem(livro.total_paginas))
            self.tableWidget_lista_livros.setItem(cont_linhas, 12, QTableWidgetItem(livro.titulo_original))
            self.tableWidget_lista_livros.setItem(cont_linhas, 13, QTableWidgetItem(livro.colecao))
            self.tableWidget_lista_livros.setItem(cont_linhas, 14, QTableWidgetItem(livro.volume))
            self.tableWidget_lista_livros.setItem(cont_linhas, 15, QTableWidgetItem(livro.versao))
            self.tableWidget_lista_livros.setItem(cont_linhas, 16, QTableWidgetItem(livro.isbn))
            self.tableWidget_lista_livros.setItem(cont_linhas, 17, QTableWidgetItem(livro.site))
            self.tableWidget_lista_livros.setItem(cont_linhas, 18, QTableWidgetItem(livro.acesso))
            self.tableWidget_lista_livros.setItem(cont_linhas, 19, QTableWidgetItem(livro.referencia))
            cont_linhas += 1

    def alterar_dados_livro(self) -> None:
        '''
        Acessa as informações de um livro cadastrado,
        possibilando a edição de seus dados
        '''
        indice = self.tableWidget_lista_livros.currentRow()
        if indice >= 0:
            livro = self.controle_livro.consultar_livro(indice)
            self.lineEdit_livro_sobrenome_p_autor.setText(livro.autores[0].sobrenome)
            self.lineEdit_livro_nome_p_autor.setText(livro.autores[0].nome)
            self.lineEdit_livro_sobrenome_s_autor.setText(livro.autores[1].sobrenome)
            self.lineEdit_livro_nome_s_autor.setText(livro.autores[1].nome)
            self.lineEdit_livro_sobrenome_t_autor.setText(livro.autores[2].sobrenome)
            self.lineEdit_livro_nome_t_autor.setText(livro.autores[2].nome)
            if livro.quant_autores == '1 a 3 autores':
                self.radioButton_livro_quant_autores_1.setAutoExclusive(False)
                self.radioButton_livro_quant_autores_1.setChecked(True)
                self.radioButton_livro_quant_autores_1.setAutoExclusive(True)
            else:
                self.radioButton_livro_quant_autores_2.setAutoExclusive(False)
                self.radioButton_livro_quant_autores_2.setChecked(True)
                self.radioButton_livro_quant_autores_2.setAutoExclusive(True)    
            self.lineEdit_livro_titulo.setText(livro.titulo_publicacao)
            self.lineEdit_livro_subtitulo.setText(livro.subtitulo_publicacao)
            self.lineEdit_livro_edicao.setText(livro.edicao)
            self.lineEdit_livro_tradutores.setText(livro.tradutores)
            self.lineEdit_livro_local.setText(livro.local_publicacao)
            self.lineEdit_livro_editora.setText(livro.editora)
            self.lineEdit_livro_ano.setText(livro.ano_publicacao)
            self.lineEdit_livro_total_paginas.setText(livro.total_paginas)
            self.lineEdit_livro_titulo_original.setText(livro.titulo_original)
            self.lineEdit_livro_colecao.setText(livro.colecao)
            self.lineEdit_livro_colecao_volume.setText(livro.volume)
            if livro.versao == 'Físico':
                i = 1
            elif livro.versao == 'E-book':
                i = 2
            else:
                i = 0
            self.comboBox_livro_versao.setCurrentIndex(i)
            self.lineEdit_livro_isbn.setText(livro.isbn)
            self.lineEdit_livro_site.setText(livro.site)
            self.lineEdit_livro_acesso.setText(livro.acesso)
            self.acessar_livro()
        else:
            msg = 'Por favor, selecione a linha do livro que deseja alterar'
            self.label_lista_msg.setText(msg)
            self.label_lista_msg.setStyleSheet(self.cor_erro)
            self.frame_lista_msg.show()

    def excluir_livro(self) -> None:
        '''
        Exclui um livro cadastrado
        '''
        indice = self.tableWidget_lista_livros.currentRow()
        if indice >= 0:
            msg = self.controle_livro.excluir_livro(indice)
            self.label_lista_msg.setText(msg)
            self.label_lista_msg.setStyleSheet(self.cor_sucesso)
            self.frame_lista_msg.show()
            self.tabelar_livros()
            self.tableWidget_lista_livros.clearSelection()
        else:
            msg = 'Por favor, selecione a linha do livro que deseja excluir'
            self.label_lista_msg.setText(msg)
            self.label_lista_msg.setStyleSheet(self.cor_erro)
            self.frame_lista_msg.show()

    def limpar_livro(self) -> None:
        '''
        Limpa os campos do formulário livro
        '''
        componentes = [
            self.lineEdit_livro_sobrenome_p_autor,
            self.lineEdit_livro_nome_p_autor,
            self.lineEdit_livro_sobrenome_s_autor,
            self.lineEdit_livro_nome_s_autor,
            self.lineEdit_livro_sobrenome_t_autor,
            self.lineEdit_livro_nome_t_autor,
            self.radioButton_livro_quant_autores_1,
            self.radioButton_livro_quant_autores_2,
            self.lineEdit_livro_titulo,
            self.lineEdit_livro_subtitulo,
            self.lineEdit_livro_edicao,
            self.lineEdit_livro_tradutores,
            self.lineEdit_livro_local,
            self.lineEdit_livro_editora,
            self.lineEdit_livro_ano,
            self.lineEdit_livro_total_paginas,
            self.lineEdit_livro_titulo_original,
            self.lineEdit_livro_colecao,
            self.lineEdit_livro_colecao_volume,
            self.comboBox_livro_versao,
            self.lineEdit_livro_isbn,
            self.lineEdit_livro_site,
            self.lineEdit_livro_acesso
        ]
        self.frame_livro_msg.hide()
        self.__limpar_componentes(componentes)

    def exibir_referencia_livro(self) -> None:
        '''
        Exibe a referencia de livro (html)
        na tela listar
        '''
        linha = self.tableWidget_lista_livros.currentRow()
        if linha >= 0:
            coluna = 19
            referencia = self.tableWidget_lista_livros.item(linha, coluna).text()
            self.label_lista_referencia.setText(referencia)
        else:
            msg = 'Por favor, selecione a linha da qual deseja exibir a referência'
            self.label_lista_msg.setText(msg)
            self.label_lista_msg.setStyleSheet(self.cor_erro)
            self.frame_lista_msg.show()

    # Métodos (Artigo)

    def salvar_artigo(self) -> None:
        '''
        Salva as informações da referência artigo
        '''
        indice = self.tableWidget_lista_artigos.currentRow()
        artigo = Artigo()
        artigo.add_autor(Autor())
        artigo.autores[0].sobrenome = self.lineEdit_artigo_sobrenome_p_autor.text()
        artigo.autores[0].nome = self.lineEdit_artigo_nome_p_autor.text()
        artigo.add_autor(Autor())
        if self.lineEdit_artigo_sobrenome_s_autor.text() != '':
            artigo.autores[1].sobrenome = self.lineEdit_artigo_sobrenome_s_autor.text()
            artigo.autores[1].nome = self.lineEdit_artigo_nome_s_autor.text()
        artigo.add_autor(Autor())
        if self.lineEdit_artigo_sobrenome_t_autor.text() != '':
            artigo.autores[2].sobrenome = self.lineEdit_artigo_sobrenome_t_autor.text()
            artigo.autores[2].nome = self.lineEdit_artigo_nome_t_autor.text()
        if self.radioButton_artigo_quant_autores_1.isChecked():
            artigo.quant_autores = '1 a 3 autores'
        elif self.radioButton_artigo_quant_autores_2.isChecked():
            artigo.quant_autores = '> 3 autores'
        artigo.titulo_publicacao = self.lineEdit_artigo_titulo.text()
        artigo.subtitulo_publicacao = self.lineEdit_artigo_subtitulo.text()
        artigo.titulo_periodico = self.lineEdit_artigo_periodico_titulo.text()
        artigo.subtitulo_periodico = self.lineEdit_artigo_periodico_subtitulo.text()
        artigo.local_publicacao = self.lineEdit_artigo_local.text()
        artigo.ano_periodico = self.lineEdit_artigo_num_ano.text()
        artigo.volume = self.lineEdit_artigo_volume.text()
        artigo.numero = self.lineEdit_artigo_numero.text()
        artigo.edicao = self.lineEdit_artigo_edicao.text()
        artigo.tomo = self.lineEdit_artigo_tomo.text()
        artigo.paginas = self.lineEdit_artigo_paginas.text()
        artigo.periodo = self.lineEdit_artigo_periodo.text()
        artigo.ano_publicacao = self.lineEdit_artigo_ano.text()
        artigo.issn = self.lineEdit_artigo_issn.text()
        artigo.versao = self.comboBox_artigo_versao.currentText()
        artigo.doi = self.lineEdit_artigo_doi.text()
        artigo.site = self.lineEdit_artigo_site.text()
        artigo.acesso = self.lineEdit_artigo_acesso.text()
        if len(artigo.msg_validacao) != 0:
            self.label_artigo_msg.setText(artigo.msg_validacao)
            self.label_artigo_msg.setStyleSheet(self.cor_erro)
            self.frame_artigo_msg.show()
        else:
            if indice >= 0:
                msg = self.controle_artigo.alterar_artigo(indice, artigo)
                self.label_artigo_msg.setText(msg)
                self.label_artigo_msg.setStyleSheet(self.cor_sucesso)
                self.frame_artigo_msg.show()
                self.label_artigo_referencia.setText(artigo.gerar_referencia_html())
                self.tabelar_artigos()
                self.limpar_artigo()
                self.tableWidget_lista_artigos.clearSelection()
            else:
                msg = self.controle_artigo.add_artigo(artigo)
                self.label_artigo_msg.setText(msg)
                self.label_artigo_msg.setStyleSheet(self.cor_sucesso)
                self.frame_artigo_msg.show()
                self.label_artigo_referencia.setText(artigo.gerar_referencia_html())
                self.tabelar_artigos()
                self.limpar_artigo()

    def tabelar_artigos(self) -> None:
        '''
        Atualiza as infomações da tabela de artigos
        '''
        cont_linhas = 0
        self.tableWidget_lista_artigos.clearContents()
        self.tableWidget_lista_artigos.setRowCount(len(self.controle_artigo.lista_artigos))
        for artigo in self.controle_artigo.lista_artigos:
            self.tableWidget_lista_artigos.setItem(cont_linhas, 0, QTableWidgetItem(artigo.autores[0].sobrenome))
            autor_sec = artigo.autores[1].sobrenome if len(artigo.autores) >= 2 else ''
            autor_ter = artigo.autores[2].sobrenome if len(artigo.autores) == 3 else ''
            self.tableWidget_lista_artigos.setItem(cont_linhas, 1, QTableWidgetItem(autor_sec))
            self.tableWidget_lista_artigos.setItem(cont_linhas, 2, QTableWidgetItem(autor_ter))
            self.tableWidget_lista_artigos.setItem(cont_linhas, 3, QTableWidgetItem(artigo.quant_autores))
            self.tableWidget_lista_artigos.setItem(cont_linhas, 4, QTableWidgetItem(artigo.titulo_publicacao))
            self.tableWidget_lista_artigos.setItem(cont_linhas, 5, QTableWidgetItem(artigo.subtitulo_publicacao))
            self.tableWidget_lista_artigos.setItem(cont_linhas, 6, QTableWidgetItem(artigo.titulo_periodico))
            self.tableWidget_lista_artigos.setItem(cont_linhas, 7, QTableWidgetItem(artigo.subtitulo_periodico))
            self.tableWidget_lista_artigos.setItem(cont_linhas, 8, QTableWidgetItem(artigo.local_publicacao))
            self.tableWidget_lista_artigos.setItem(cont_linhas, 9, QTableWidgetItem(artigo.ano_periodico))
            self.tableWidget_lista_artigos.setItem(cont_linhas, 10, QTableWidgetItem(artigo.volume))
            self.tableWidget_lista_artigos.setItem(cont_linhas, 11, QTableWidgetItem(artigo.numero))
            self.tableWidget_lista_artigos.setItem(cont_linhas, 12, QTableWidgetItem(artigo.edicao))
            self.tableWidget_lista_artigos.setItem(cont_linhas, 13, QTableWidgetItem(artigo.tomo))
            self.tableWidget_lista_artigos.setItem(cont_linhas, 14, QTableWidgetItem(artigo.paginas))
            self.tableWidget_lista_artigos.setItem(cont_linhas, 15, QTableWidgetItem(artigo.periodo))
            self.tableWidget_lista_artigos.setItem(cont_linhas, 16, QTableWidgetItem(artigo.ano_publicacao))
            self.tableWidget_lista_artigos.setItem(cont_linhas, 17, QTableWidgetItem(artigo.issn))
            self.tableWidget_lista_artigos.setItem(cont_linhas, 18, QTableWidgetItem(artigo.versao))
            self.tableWidget_lista_artigos.setItem(cont_linhas, 19, QTableWidgetItem(artigo.doi))
            self.tableWidget_lista_artigos.setItem(cont_linhas, 20, QTableWidgetItem(artigo.site))
            self.tableWidget_lista_artigos.setItem(cont_linhas, 21, QTableWidgetItem(artigo.acesso))
            self.tableWidget_lista_artigos.setItem(cont_linhas, 22, QTableWidgetItem(artigo.referencia))
            cont_linhas += 1

    def alterar_dados_artigo(self) -> None:
        '''
        Acessa as informações de um artigo cadastrado,
        possibilando a edição de seus dados
        '''
        indice = self.tableWidget_lista_artigos.currentRow()
        if indice >= 0:
            artigo = self.controle_artigo.consultar_artigo(indice)
            self.lineEdit_artigo_sobrenome_p_autor.setText(artigo.autores[0].sobrenome)
            self.lineEdit_artigo_nome_p_autor.setText(artigo.autores[0].nome)
            self.lineEdit_artigo_sobrenome_s_autor.setText(artigo.autores[1].sobrenome)
            self.lineEdit_artigo_nome_s_autor.setText(artigo.autores[1].nome)
            self.lineEdit_artigo_sobrenome_t_autor.setText(artigo.autores[2].sobrenome)
            self.lineEdit_artigo_nome_t_autor.setText(artigo.autores[2].nome)
            if artigo.quant_autores == '1 a 3 autores':
                self.radioButton_artigo_quant_autores_1.setAutoExclusive(False)
                self.radioButton_artigo_quant_autores_1.setChecked(True)
                self.radioButton_artigo_quant_autores_1.setAutoExclusive(True)
            else:
                self.radioButton_artigo_quant_autores_2.setAutoExclusive(False)
                self.radioButton_artigo_quant_autores_2.setChecked(True)
                self.radioButton_artigo_quant_autores_2.setAutoExclusive(True)
            self.lineEdit_artigo_titulo.setText(artigo.titulo_publicacao)
            self.lineEdit_artigo_subtitulo.setText(artigo.subtitulo_publicacao)
            self.lineEdit_artigo_periodico_titulo.setText(artigo.titulo_periodico)
            self.lineEdit_artigo_periodico_subtitulo.setText(artigo.subtitulo_periodico)
            self.lineEdit_artigo_local.setText(artigo.local_publicacao)
            self.lineEdit_artigo_num_ano.setText(artigo.ano_periodico)
            self.lineEdit_artigo_volume.setText(artigo.volume)
            self.lineEdit_artigo_numero.setText(artigo.numero)
            self.lineEdit_artigo_edicao.setText(artigo.edicao)
            self.lineEdit_artigo_tomo.setText(artigo.tomo)
            self.lineEdit_artigo_paginas.setText(artigo.paginas)
            self.lineEdit_artigo_periodo.setText(artigo.periodo)
            self.lineEdit_artigo_ano.setText(artigo.ano_publicacao)
            self.lineEdit_artigo_issn.setText(artigo.issn)
            if artigo.versao == 'Físico':
                i = 1
            elif artigo.versao == 'Online':
                i = 2
            else:
                i = 0
            self.comboBox_artigo_versao.setCurrentIndex(i)
            self.lineEdit_artigo_doi.setText(artigo.doi)
            self.lineEdit_artigo_site.setText(artigo.site)
            self.lineEdit_artigo_acesso.setText(artigo.acesso)
            self.acessar_artigo()
        else:
            msg = 'Por favor, selecione a linha do artigo que deseja alterar'
            self.label_lista_msg.setText(msg)
            self.label_lista_msg.setStyleSheet(self.cor_erro)
            self.frame_lista_msg.show()

    def excluir_artigo(self) -> None:
        '''
        Exclui um artigo cadastrado
        '''
        indice = self.tableWidget_lista_artigos.currentRow()
        if indice >= 0:
            msg = self.controle_artigo.excluir_artigo(indice)
            self.label_lista_msg.setText(msg)
            self.label_lista_msg.setStyleSheet(self.cor_sucesso)
            self.frame_lista_msg.show()
            self.tabelar_artigos()
            self.tableWidget_lista_artigos.clearSelection()
        else:
            msg = 'Por favor, selecione a linha do artigo que deseja excluir'
            self.label_lista_msg.setText(msg)
            self.label_lista_msg.setStyleSheet(self.cor_erro)
            self.frame_lista_msg.show()

    def limpar_artigo(self) -> None:
        '''
        Limpa os campos do formulário artigo
        '''
        componentes = [
            self.lineEdit_artigo_sobrenome_p_autor,
            self.lineEdit_artigo_nome_p_autor,
            self.lineEdit_artigo_sobrenome_s_autor,
            self.lineEdit_artigo_nome_s_autor,
            self.lineEdit_artigo_sobrenome_t_autor,
            self.lineEdit_artigo_nome_t_autor,
            self.radioButton_artigo_quant_autores_1,
            self.radioButton_artigo_quant_autores_2,
            self.lineEdit_artigo_titulo,
            self.lineEdit_artigo_subtitulo,
            self.lineEdit_artigo_periodico_titulo,
            self.lineEdit_artigo_periodico_subtitulo,
            self.lineEdit_artigo_local,
            self.lineEdit_artigo_num_ano,
            self.lineEdit_artigo_volume,
            self.lineEdit_artigo_numero,
            self.lineEdit_artigo_edicao,
            self.lineEdit_artigo_tomo,
            self.lineEdit_artigo_paginas,
            self.lineEdit_artigo_periodo,
            self.lineEdit_artigo_ano,
            self.lineEdit_artigo_issn,
            self.comboBox_artigo_versao,
            self.lineEdit_artigo_doi,
            self.lineEdit_artigo_site,
            self.lineEdit_artigo_acesso
        ]
        self.frame_artigo_msg.hide()
        self.__limpar_componentes(componentes)

    def exibir_referencia_artigo(self) -> None:
        '''
        Exibe a referencia de artigo (html)
        na tela listar
        '''
        linha = self.tableWidget_lista_artigos.currentRow()
        if linha >= 0:
            coluna = 22
            referencia = self.tableWidget_lista_artigos.item(linha, coluna).text()
            self.label_lista_referencia.setText(referencia)
        else:
            msg = 'Por favor, selecione a linha da qual deseja exibir a referência'
            self.label_lista_msg.setText(msg)
            self.label_lista_msg.setStyleSheet(self.cor_erro)
            self.frame_lista_msg.show()

    # Métodos (Tese)

    def salvar_tese(self) -> None:
        '''
        Salva as informações da referência tese
        '''
        indice = self.tableWidget_lista_teses.currentRow()
        tese = Tese()
        tese.add_autor(Autor())
        tese.autores[0].sobrenome = self.lineEdit_tese_sobrenome_p_autor.text()
        tese.autores[0].nome = self.lineEdit_tese_nome_p_autor.text()
        tese.add_autor(Autor())
        if self.lineEdit_tese_sobrenome_s_autor.text() !=  '':
            tese.autores[1].sobrenome = self.lineEdit_tese_sobrenome_s_autor.text()
            tese.autores[1].nome = self.lineEdit_tese_nome_s_autor.text()
        tese.titulo_publicacao = self.lineEdit_tese_titulo.text()
        tese.subtitulo_publicacao = self.lineEdit_tese_subtitulo.text()
        tese.orientador = self.lineEdit_tese_orientador.text()
        tese.ano_deposito = self.lineEdit_tese_ano_deposito.text()
        tese.total_folhas = self.lineEdit_tese_total_folhas.text()
        tese.tipo_trabalho = self.comboBox_tese_tipo_trabalho.currentText()
        tese.grau_academico = self.lineEdit_tese_grau.text()
        tese.instituto = self.lineEdit_tese_instituto.text()
        tese.universidade = self.lineEdit_tese_universidade.text()
        tese.local_publicacao = self.lineEdit_tese_local_defesa.text()
        tese.ano_publicacao = self.lineEdit_tese_ano_defesa.text()
        tese.versao = self.comboBox_tese_versao.currentText()
        tese.site = self.lineEdit_tese_site.text()
        tese.acesso = self.lineEdit_tese_acesso.text()
        if len(tese.msg_validacao) != 0:
            self.label_tese_msg.setText(tese.msg_validacao)
            self.label_tese_msg.setStyleSheet(self.cor_erro)
            self.frame_tese_msg.show()
        else:
            if indice >= 0:
                msg = self.controle_tese.alterar_tese(indice, tese)
                self.label_tese_msg.setText(msg)
                self.label_tese_msg.setStyleSheet(self.cor_sucesso)
                self.frame_tese_msg.show()
                self.label_tese_referencia.setText(tese.gerar_referencia_html())
                self.tabelar_teses()
                self.limpar_tese()
                self.tableWidget_lista_teses.clearSelection()
            else:
                msg = self.controle_tese.add_tese(tese)
                self.label_tese_msg.setText(msg)
                self.label_tese_msg.setStyleSheet(self.cor_sucesso)
                self.frame_tese_msg.show()
                self.label_tese_referencia.setText(tese.gerar_referencia_html())
                self.tabelar_teses()
                self.limpar_tese()

    def tabelar_teses(self) -> None:
        '''
        Atualiza as infomações da tabela de teses
        '''
        cont_linhas = 0
        self.tableWidget_lista_teses.clearContents()
        self.tableWidget_lista_teses.setRowCount(len(self.controle_tese.lista_teses))
        for tese in self.controle_tese.lista_teses:
            self.tableWidget_lista_teses.setItem(cont_linhas, 0, QTableWidgetItem(tese.autores[0].sobrenome))
            autor_sec = tese.autores[1].sobrenome if len(tese.autores) == 2 else ''
            self.tableWidget_lista_teses.setItem(cont_linhas, 1, QTableWidgetItem(autor_sec))
            self.tableWidget_lista_teses.setItem(cont_linhas, 2, QTableWidgetItem(tese.titulo_publicacao))
            self.tableWidget_lista_teses.setItem(cont_linhas, 3, QTableWidgetItem(tese.subtitulo_publicacao))
            self.tableWidget_lista_teses.setItem(cont_linhas, 4, QTableWidgetItem(tese.orientador))
            self.tableWidget_lista_teses.setItem(cont_linhas, 5, QTableWidgetItem(tese.ano_deposito))
            self.tableWidget_lista_teses.setItem(cont_linhas, 6, QTableWidgetItem(tese.total_folhas))
            self.tableWidget_lista_teses.setItem(cont_linhas, 7, QTableWidgetItem(tese.tipo_trabalho))
            self.tableWidget_lista_teses.setItem(cont_linhas, 8, QTableWidgetItem(tese.grau_academico))
            self.tableWidget_lista_teses.setItem(cont_linhas, 9, QTableWidgetItem(tese.instituto))
            self.tableWidget_lista_teses.setItem(cont_linhas, 10, QTableWidgetItem(tese.universidade))
            self.tableWidget_lista_teses.setItem(cont_linhas, 11, QTableWidgetItem(tese.local_publicacao))
            self.tableWidget_lista_teses.setItem(cont_linhas, 12, QTableWidgetItem(tese.ano_publicacao))
            self.tableWidget_lista_teses.setItem(cont_linhas, 13, QTableWidgetItem(tese.versao))
            self.tableWidget_lista_teses.setItem(cont_linhas, 14, QTableWidgetItem(tese.site))
            self.tableWidget_lista_teses.setItem(cont_linhas, 15, QTableWidgetItem(tese.acesso))
            self.tableWidget_lista_teses.setItem(cont_linhas, 16, QTableWidgetItem(tese.referencia))
            cont_linhas += 1

    def alterar_dados_tese(self):
        '''
        Acessa as informações de uma tese cadastrada,
        possibilando a edição de seus dados
        '''
        indice = self.tableWidget_lista_teses.currentRow()
        if indice >= 0:
            tese = self.controle_tese.consultar_tese(indice)
            self.lineEdit_tese_sobrenome_p_autor.setText(tese.autores[0].sobrenome)
            self.lineEdit_tese_nome_p_autor.setText(tese.autores[0].nome)
            self.lineEdit_tese_sobrenome_s_autor.setText(tese.autores[1].sobrenome)
            self.lineEdit_tese_nome_s_autor.setText(tese.autores[1].nome)
            self.lineEdit_tese_titulo.setText(tese.titulo_publicacao)
            self.lineEdit_tese_subtitulo.setText(tese.subtitulo_publicacao)
            self.lineEdit_tese_orientador.setText(tese.orientador)
            self.lineEdit_tese_ano_deposito.setText(tese.ano_deposito)
            self.lineEdit_tese_total_folhas.setText(tese.total_folhas)
            if tese.tipo_trabalho == 'Tese':
                i = 1
            elif tese.tipo_trabalho == 'Dissetação':
                i = 2
            elif tese.tipo_trabalho == 'Trabalho de Conclusão de Curso':
                i = 3
            else:
                i = 0
            self.comboBox_tese_tipo_trabalho.setCurrentIndex(i)
            self.lineEdit_tese_grau.setText(tese.grau_academico)
            self.lineEdit_tese_instituto.setText(tese.instituto)
            self.lineEdit_tese_universidade.setText(tese.universidade)
            self.lineEdit_tese_local_defesa.setText(tese.local_publicacao)
            self.lineEdit_tese_ano_defesa.setText(tese.ano_publicacao)
            if tese.versao == 'Físico':
                j = 1
            elif tese.versao == 'Digital':
                j = 2
            else:
                j = 0
            self.comboBox_tese_versao.setCurrentIndex(j)
            self.lineEdit_tese_site.setText(tese.site)
            self.lineEdit_tese_acesso.setText(tese.acesso)
            self.acessar_tese()
        else:
            msg = 'Por favor, selecione a linha da Tese que deseja alterar'
            self.label_lista_msg.setText(msg)
            self.label_lista_msg.setStyleSheet(self.cor_erro)
            self.frame_lista_msg.show()

    def excluir_tese(self) -> None:
        '''
        Exclui uma tese cadastrada
        '''
        indice = self.tableWidget_lista_teses.currentRow()
        if indice >= 0:
            msg = self.controle_tese.excluir_tese(indice)
            self.label_lista_msg.setText(msg)
            self.label_lista_msg.setStyleSheet(self.cor_sucesso)
            self.frame_lista_msg.show()
            self.tabelar_teses()
            self.tableWidget_lista_teses.clearSelection()
        else:
            msg = 'Por favor, selecione a linha do trabalho que deseja excluir'
            self.label_lista_msg.setText(msg)
            self.label_lista_msg.setStyleSheet(self.cor_erro)
            self.frame_lista_msg.show()

    def limpar_tese(self) -> None:
        '''
        Limpa os campos do formulário tese
        '''
        componentes = [
            self.lineEdit_tese_sobrenome_p_autor,
            self.lineEdit_tese_nome_p_autor,
            self.lineEdit_tese_sobrenome_s_autor,
            self.lineEdit_tese_nome_s_autor,
            self.lineEdit_tese_titulo,
            self.lineEdit_tese_subtitulo,
            self.lineEdit_tese_orientador,
            self.lineEdit_tese_ano_deposito,
            self.lineEdit_tese_total_folhas,
            self.comboBox_tese_tipo_trabalho,
            self.lineEdit_tese_grau,
            self.lineEdit_tese_instituto,
            self.lineEdit_tese_universidade,
            self.lineEdit_tese_local_defesa,
            self.lineEdit_tese_ano_defesa,
            self.comboBox_tese_versao,
            self.lineEdit_tese_site,
            self.lineEdit_tese_acesso
        ]
        self.frame_tese_msg.hide()
        self.__limpar_componentes(componentes)

    def exibir_referencia_tese(self) -> None:
        '''
        Exibe a referencia de livro (html)
        na tela listar
        '''
        linha = self.tableWidget_lista_teses.currentRow()
        if linha >= 0:
            coluna = 16
            referencia = self.tableWidget_lista_teses.item(linha, coluna).text()
            self.label_lista_referencia.setText(referencia)
        else:
            msg = 'Por favor, selecione a linha da qual deseja exibir a referência'
            self.label_lista_msg.setText(msg)
            self.label_lista_msg.setStyleSheet(self.cor_erro)
            self.frame_lista_msg.show()

    # Método (Usuário)

    def cadastrar_usuario(self) -> None:
        '''
        Salva as informações de usuario
        '''
        indice = self.tableWidget_usuarios_usuarios.currentRow()
        usuario = Usuario()
        usuario.nome  = self.lineEdit_cadastro_nome.text()
        usuario.sobrenome = self.lineEdit_cadastro_sobrenome.text()
        usuario.user = self.lineEdit_cadastro_usuario.text()
        usuario.senha = self.lineEdit_cadastro_senha_1.text()
        usuario.senha_conf = self.lineEdit_cadastro_senha_2.text()
        if len(usuario.msg_validacao) != 0:
            self.label_cadastro_msg.setText(usuario.msg_validacao)
            self.label_cadastro_msg.setStyleSheet(self.cor_erro)
            self.frame_cadastro_msg.show()
        else:
            if indice >= 0:
                msg = self.controle_usuario.alterar_usuario(indice, usuario)
                self.label_cadastro_msg.setText(msg)
                self.label_cadastro_msg.setStyleSheet(self.cor_sucesso)
                self.frame_cadastro_msg.show()
                self.tabelar_usuarios()
                self.tableWidget_usuarios_usuarios.clearSelection()
                self.limpar_cadastrar()
            else:
                if self.controle_usuario.consultar_usuario(usuario.user, usuario.senha):
                    msg = 'Nome de usuário já utilizado'
                    self.label_cadastro_msg.setText(msg)
                    self.label_cadastro_msg.setStyleSheet(self.cor_erro)
                    self.frame_cadastro_msg.show()
                else:
                    msg = self.controle_usuario.add_usuario(usuario)
                    self.label_cadastro_msg.setText(msg)
                    self.label_cadastro_msg.setStyleSheet(self.cor_sucesso)
                    self.frame_cadastro_msg.show()
                    self.tabelar_usuarios()
                    self.limpar_cadastrar()

    def tabelar_usuarios(self) -> None:
        '''
        Atualiza as infomações da tabela de usuarios
        '''
        cont_linhas = 0
        self.tableWidget_usuarios_usuarios.clearContents()
        self.tableWidget_usuarios_usuarios.setRowCount(len(self.controle_usuario.lista_usuarios))
        for usuario in self.controle_usuario.lista_usuarios:
            self.tableWidget_usuarios_usuarios.setItem(cont_linhas, 0, QTableWidgetItem(usuario.nome))
            self.tableWidget_usuarios_usuarios.setItem(cont_linhas, 1, QTableWidgetItem(usuario.sobrenome))
            self.tableWidget_usuarios_usuarios.setItem(cont_linhas, 2, QTableWidgetItem(usuario.user))
            cont_linhas += 1

    def alterar_dados_usuario(self):
        '''
        Acessa as informações de um usuário cadastrado,
        possibilando a edição de seus dados
        '''
        indice = self.tableWidget_usuarios_usuarios.currentRow()
        if indice >= 0:
            if indice > 1:
                usuario = self.controle_usuario.acessar_usuario(indice)
                self.lineEdit_cadastro_nome.setText(usuario.nome)
                self.lineEdit_cadastro_sobrenome.setText(usuario.sobrenome)
                self.lineEdit_cadastro_usuario.setText(usuario.user)
                self.lineEdit_cadastro_senha_1.setText(usuario.senha)
                self.lineEdit_cadastro_senha_2.setText(usuario.senha_conf)
                self.acessar_cadastro()
            else:
                msg = 'Não é possível alterar o usuário'
                self.label_usuarios_msg.setText(msg)
                self.label_usuarios_msg.setStyleSheet(self.cor_erro)
                self.frame_usuarios_msg.show()
        else:
            msg = 'Por favor, selecione o Usuário que deseja alterar'
            self.label_usuarios_msg.setText(msg)
            self.label_usuarios_msg.setStyleSheet(self.cor_erro)
            self.frame_usuarios_msg.show()

    def excluir_usuario(self) -> None:
        '''
        Exclui um usuário cadastrado
        '''
        indice = self.tableWidget_usuarios_usuarios.currentRow()
        if indice >= 0:
            if indice > 1:
                msg = self.controle_usuario.excluir_usuario(indice)
                self.label_usuarios_msg.setText(msg)
                self.label_usuarios_msg.setStyleSheet(self.cor_sucesso)
                self.frame_usuarios_msg.show()
                self.tableWidget_usuarios_usuarios.clearSelection()
                self.tabelar_usuarios()
            else:
                msg = 'Não é possível excluir o usuário'
                self.label_usuarios_msg.setText(msg)
                self.label_usuarios_msg.setStyleSheet(self.cor_erro)
                self.frame_usuarios_msg.show()
        else:
            msg = 'Por favor, selecione o Usuário que deseja excluir'
            self.label_usuarios_msg.setText(msg)
            self.label_usuarios_msg.setStyleSheet(self.cor_erro)
            self.frame_usuarios_msg.show()

    def limpar_cadastrar(self) -> None:
        '''
        Limpa os campos do formulário usuário
        '''
        componentes = [
            self.lineEdit_cadastro_nome,
            self.lineEdit_cadastro_sobrenome,
            self.lineEdit_cadastro_usuario,
            self.lineEdit_cadastro_senha_1,
            self.lineEdit_cadastro_senha_2,
        ]
        self.frame_cadastro_msg.hide()
        self.__limpar_componentes(componentes)

    # Métodos Gerais

    def acessar_livro(self) -> None:
        '''
        Acessa o formulário "Livro"
        '''
        self.stackedWidget_sistema.setCurrentWidget(self.page_sistema_livro)

    def acessar_artigo(self) -> None:
        '''
        Acessa o formulário "Artigo"
        '''
        self.stackedWidget_sistema.setCurrentWidget(self.page_sistema_artigo)

    def acessar_tese(self) -> None:
        '''
        Acessa o formulário "Tese"
        '''
        self.stackedWidget_sistema.setCurrentWidget(self.page_sistema_tese)

    def acessar_home(self) -> None:
        '''
        Acessa a página "Home"
        '''
        self.stackedWidget_sistema.setCurrentWidget(self.page_sistema_home)

    def acessar_lista(self) -> None:
        '''
        Acessa a página "Lista"
        '''
        self.stackedWidget_sistema.setCurrentWidget(self.page_sistema_lista)

    def acessar_cadastro(self) -> None:
        '''
        Acessa o formulário "Cadastro de Usuário"
        '''
        self.stackedWidget_sistema.setCurrentWidget(self.page_sistama_cadastro)

    def acessar_usuarios(self) -> None:
        '''
        Acessa a página "Usuários"
        '''
        self.stackedWidget_sistema.setCurrentWidget(self.page_sistema_usuarios)

    def sair_sistema(self) -> None:
        '''
        Sai do sistema, acessando a página de "Login"
        '''
        self.stackedWidget_sistema.setCurrentWidget(self.page_sistema_login)

    def __limpar_componentes(self, componentes:list) -> None:
        '''
        Limpa os componentes da inteface gráfica
        da lista fornecida
        '''
        for componente in componentes:
            if isinstance(componente, QLineEdit):
                componente.clear()
            elif isinstance(componente, QRadioButton):
                componente.setAutoExclusive(False)
                componente.setChecked(False)
                componente.setAutoExclusive(True)
            elif isinstance(componente, QComboBox):
                componente.setCurrentIndex(0)

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    principal = Principal()
    principal.setWindowIcon(QIcon('img/logo.png'))
    principal.setWindowTitle('BiblioLink')
    principal.show()
    qt.exec()
