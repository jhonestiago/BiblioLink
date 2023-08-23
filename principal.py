import sys

from gui_principal import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QTableWidgetItem
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt

from entidades.livro import Livro
from entidades.autor import Autor
from entidades.artigo import Artigo
from entidades.tese import Tese
from controle.livro_control import LivroControl
from controle.artigo_control import ArtigoControl
from controle.tese_control import TeseControl

class Principal(Ui_MainWindow, QMainWindow):

    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.init_components()
        self.controle_livro = LivroControl()
        self.controle_artigo = ArtigoControl()
        self.controle_tese = TeseControl()
        self.cor_sucesso = 'background-color: rgb(101, 184, 145)'
        self.cor_erro = 'background-color: rgb(204, 41, 54); color: rgb(255, 255, 255)'

    def init_components(self) -> None:
        #Componentes da tela de Login
        self.frame_login_msg.hide()
        self.pushButton_login_entrar.clicked.connect(self.realizar_login)
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
        self.pushButton_livro_home.clicked.connect(self.acessar_home)
        self.pushButton_livro_lista.clicked.connect(self.acessar_lista)
        self.pushButton_livro_salvar.clicked.connect(self.salvar_livro)
        self.pushButton_livro_limpar_referencia.setIcon(QIcon('img/icon_limpar.png'))
        self.pushButton_livro_limpar_referencia.clicked.connect(lambda: self.label_livro_referencia.setText('Referência'))
        self.pushButton_livro_fechar_msg.clicked.connect(lambda: self.frame_livro_msg.hide())

        #Componentes da tela: Artigo
        self.frame_artigo_msg.hide()
        self.label_icon_artigo.setPixmap(QPixmap('img/icon_artigo.png'))
        self.pushButton_artigo_home.clicked.connect(self.acessar_home)
        self.pushButton_artigo_lista.clicked.connect(self.acessar_lista)
        self.pushButton_artigo_salvar.clicked.connect(self.salvar_artigo)
        self.pushButton_artigo_limpar_referencia.setIcon(QIcon('img/icon_limpar.png'))
        self.pushButton_artigo_limpar_referencia.clicked.connect(lambda: self.label_artigo_referencia.setText('Referência'))
        self.pushButton_artigo_fechar_msg.clicked.connect(lambda: self.frame_artigo_msg.hide())

        #Componentes da tela: Trabalhos Acadêmicos / Tese
        self.frame_tese_msg.hide()
        self.label_icon_tese.setPixmap(QPixmap('img/icon_tese.png'))
        self.pushButton_tese_home.clicked.connect(self.acessar_home)
        self.pushButton_tese_lista.clicked.connect(self.acessar_lista)
        self.pushButton_tese_salvar.clicked.connect(self.salvar_tese)
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
        self.pushButton_lista_livros_excluir.clicked.connect(self.excluir_livro)
        self.pushButton_lista_livros_novo.clicked.connect(self.acessar_livro)
        self.pushButton_lista_livros_home.clicked.connect(self.acessar_home)
        
        #Componentes da tela: Lista(Artigos)
        self.pushButton_lista_artigos_exibir.clicked.connect(self.exibir_referencia_artigo)
        self.pushButton_lista_artigos_excluir.clicked.connect(self.excluir_artigo)
        self.pushButton_lista_artigos_novo.clicked.connect(self.acessar_artigo)
        self.pushButton_lista_artigos_home.clicked.connect(self.acessar_home)

        #Componentes da tela: Lista(Teses)
        self.pushButton_lista_teses_exibir.clicked.connect(self.exibir_referencia_tese)
        self.pushButton_lista_teses_excluir.clicked.connect(self.excluir_tese)
        self.pushButton_lista_teses_novo.clicked.connect(self.acessar_tese)
        self.pushButton_lista_teses_home.clicked.connect(self.acessar_home)
    
    def realizar_login(self) -> None:
        user = self.lineEdit_login_usuario.text()
        senha = self.lineEdit_login_senha.text()
        if user == 'admin' and senha == '12345':
            self.lineEdit_login_usuario.setText('')
            self.lineEdit_login_senha.setText('')
            self.frame_login_msg.hide()
            self.stackedWidget_sistema.setCurrentWidget(self.page_sistema_home)
            print('Login realizado com sucesso')
        else:
            self.label_login_msg.setText('Usuário ou senha incorretos!!!')
            self.label_login_msg.setStyleSheet(self.cor_erro)
            self.frame_login_msg.show()
    
    # Métodos (Livro)

    def salvar_livro(self) -> None:
        livro = Livro()
        livro.add_autor(Autor())
        livro.autores[0].sobrenome = self.lineEdit_livro_sobrenome_p_autor.text()
        livro.autores[0].nome = self.lineEdit_livro_nome_p_autor.text()
        if self.lineEdit_livro_sobrenome_s_autor.text() != '':
            livro.add_autor(Autor())
            livro.autores[1].sobrenome = self.lineEdit_livro_sobrenome_s_autor.text()
            livro.autores[1].nome = self.lineEdit_livro_nome_s_autor.text()
        if self.lineEdit_livro_sobrenome_t_autor.text() != '':
            livro.add_autor(Autor())
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
            msg = self.controle_livro.add_livro(livro)
            self.label_livro_msg.setText(msg)
            self.label_livro_msg.setStyleSheet(self.cor_sucesso)
            self.frame_livro_msg.show()
            self.label_livro_referencia.setText(livro.gerar_referencia_html())
            self.listar_livros_tabela()

    def listar_livros_tabela(self) -> None:
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
            self.tableWidget_lista_livros.setItem(cont_linhas, 19, QTableWidgetItem(livro.gerar_referencia_html()))
            cont_linhas += 1

    def excluir_livro(self) -> None:
        indice = self.tableWidget_lista_livros.currentRow()
        if indice >= 0:
            msg = self.controle_livro.excluir_livro(indice)
            self.tableWidget_lista_livros.removeRow(indice)
            self.label_lista_msg.setText(msg)
            self.label_lista_msg.setStyleSheet(self.cor_sucesso)
            self.frame_lista_msg.show()
        else:
            msg = 'Por favor, selecione a linha do livro que deseja excluir'
            self.label_lista_msg.setText(msg)
            self.label_lista_msg.setStyleSheet(self.cor_erro)
            self.frame_lista_msg.show()
    
    def exibir_referencia_livro(self) -> None:
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
        artigo = Artigo()
        artigo.add_autor(Autor())
        artigo.autores[0].sobrenome = self.lineEdit_artigo_sobrenome_p_autor.text()
        artigo.autores[0].nome = self.lineEdit_artigo_nome_p_autor.text()
        if self.lineEdit_artigo_sobrenome_s_autor.text() != '':
            artigo.add_autor(Autor())
            artigo.autores[1].sobrenome = self.lineEdit_artigo_sobrenome_s_autor.text()
            artigo.autores[1].nome = self.lineEdit_artigo_nome_s_autor.text()
        if self.lineEdit_artigo_sobrenome_t_autor.text() != '':
            artigo.add_autor(Autor())
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
            msg = self.controle_artigo.add_artigo(artigo)
            self.label_artigo_msg.setText(msg)
            self.label_artigo_msg.setStyleSheet(self.cor_sucesso)
            self.frame_artigo_msg.show()
            self.label_artigo_referencia.setText(artigo.gerar_referencia_html())
            self.listar_artigos_tabela()

    def listar_artigos_tabela(self) -> None:
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
            self.tableWidget_lista_artigos.setItem(cont_linhas, 22, QTableWidgetItem(artigo.gerar_referencia_html()))
            cont_linhas += 1

    def excluir_artigo(self) -> None:
        indice = self.tableWidget_lista_artigos.currentRow()
        if indice >= 0:
            msg = self.controle_artigo.excluir_artigo(indice)
            self.tableWidget_lista_artigos.removeRow(indice)
            self.label_lista_msg.setText(msg)
            self.label_lista_msg.setStyleSheet(self.cor_sucesso)
            self.frame_lista_msg.show()
        else:
            msg = 'Por favor, selecione a linha do artigo que deseja excluir'
            self.label_lista_msg.setText(msg)
            self.label_lista_msg.setStyleSheet(self.cor_erro)
            self.frame_lista_msg.show()

    def exibir_referencia_artigo(self) -> None:
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
        tese = Tese()
        tese.add_autor(Autor())
        tese.autores[0].sobrenome = self.lineEdit_tese_sobrenome_p_autor.text()
        tese.autores[0].nome = self.lineEdit_tese_nome_p_autor.text()
        if self.lineEdit_tese_sobrenome_s_autor.text() !=  '':
            tese.add_autor(Autor())
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
            msg = self.controle_tese.add_tese(tese)
            self.label_tese_msg.setText(msg)
            self.label_tese_msg.setStyleSheet(self.cor_sucesso)
            self.frame_tese_msg.show()
            self.label_tese_referencia.setText(tese.gerar_referencia_html())
            self.listar_teses_tabela()

    def listar_teses_tabela(self) -> None:
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
            self.tableWidget_lista_teses.setItem(cont_linhas, 16, QTableWidgetItem(tese.gerar_referencia_html()))
            cont_linhas += 1
    
    def excluir_tese(self) -> None:
        indice = self.tableWidget_lista_teses.currentRow()
        if indice >= 0:
            msg = self.controle_tese.excluir_tese(indice)
            self.tableWidget_lista_teses.removeRow(indice)
            self.label_lista_msg.setText(msg)
            self.label_lista_msg.setStyleSheet(self.cor_sucesso)
            self.frame_lista_msg.show()
        else:
            msg = 'Por favor, selecione a linha do trabalho que deseja excluir'
            self.label_lista_msg.setText(msg)
            self.label_lista_msg.setStyleSheet(self.cor_erro)
            self.frame_lista_msg.show()

    def exibir_referencia_tese(self) -> None:
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
    
    # Métodos Gerais

    def acessar_livro(self) -> None:
        self.stackedWidget_sistema.setCurrentWidget(self.page_sistema_livro)
    
    def acessar_artigo(self) -> None:
        self.stackedWidget_sistema.setCurrentWidget(self.page_sistema_artigo)
    
    def acessar_tese(self) -> None:
        self.stackedWidget_sistema.setCurrentWidget(self.page_sistema_tese)
    
    def acessar_home(self) -> None:
        self.stackedWidget_sistema.setCurrentWidget(self.page_sistema_home)

    def acessar_lista(self) -> None:
        self.stackedWidget_sistema.setCurrentWidget(self.page_sistema_lista)
    
    def sair_sistema(self) -> None:
        self.stackedWidget_sistema.setCurrentWidget(self.page_sistema_login)
    
    #def set_label_img(self, label:QLabel, end_img:str) -> None:
        #img = QPixmap(end_img)
        #img = img.scaled(label.width(), label.height(), Qt.AspectRatioMode.KeepAspectRatio)
        #label.setPixmap(img)

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    principal = Principal()
    principal.show()
    qt.exec()