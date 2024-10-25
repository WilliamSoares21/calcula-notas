# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 16:54:32 2020
"""

import tkinter as tk
from tkinter import ttk
import pandas as pd
import os  # Importa a biblioteca os para manipulação de arquivos / verifica se o arquivo existe

class PrincipalRAD:
    def __init__(self, win):
        # Componentes
        self.lblNome = tk.Label(win, text='Nome do Aluno:')
        self.lblNota1 = tk.Label(win, text='Nota 1')
        self.lblNota2 = tk.Label(win, text='Nota 2')
        self.lblMedia = tk.Label(win, text='Média')
        self.txtNome = tk.Entry(bd=3)
        self.txtNota1 = tk.Entry()
        self.txtNota2 = tk.Entry()
        self.selected_item = None

        # Botões
        self.btnCalcular = tk.Button(win, text='Calcular Média', command=self.fCalcularMedia)
        self.btnAlterar = tk.Button(win, text="Alterar Dados", command=self.fAlterar)
        self.btnExcluir = tk.Button(win, text="Excluir Dados", command=self.fExcluir)

        # Posicionamento dos botões
        self.btnCalcular.place(x=100, y=200)
        self.btnAlterar.place(x=200, y=200)  
        self.btnExcluir.place(x=300, y=200)

        # ----- Componente TreeView --------------------------------------------
        self.dadosColunas = ("Aluno", "Nota1", "Nota2", "Média", "Situação")

        self.treeMedias = ttk.Treeview(win,
                                       columns=self.dadosColunas,
                                       selectmode='browse')

        self.verscrlbar = ttk.Scrollbar(win,
                                        orient="vertical",
                                        command=self.treeMedias.yview)

        self.verscrlbar.pack(side='right', fill='x')
        self.treeMedias.configure(yscrollcommand=self.verscrlbar.set)

        self.treeMedias.heading("Aluno", text="Aluno")
        self.treeMedias.heading("Nota1", text="Nota 1")
        self.treeMedias.heading("Nota2", text="Nota 2")
        self.treeMedias.heading("Média", text="Média")
        self.treeMedias.heading("Situação", text="Situação")

        self.treeMedias.column("Aluno", minwidth=0, width=100)
        self.treeMedias.column("Nota1", minwidth=0, width=100)
        self.treeMedias.column("Nota2", minwidth=0, width=100)
        self.treeMedias.column("Média", minwidth=0, width=100)
        self.treeMedias.column("Situação", minwidth=0, width=100)

        self.treeMedias.pack(padx=10, pady=10)

        # ---------------------------------------------------------------------
        # Posicionamento dos componentes na janela
        # ---------------------------------------------------------------------
        self.lblNome.place(x=100, y=50)
        self.txtNome.place(x=200, y=50)

        self.lblNota1.place(x=100, y=100)
        self.txtNota1.place(x=200, y=100)

        self.lblNota2.place(x=100, y=150)
        self.txtNota2.place(x=200, y=150)

        self.treeMedias.place(x=100, y=300)
        self.verscrlbar.place(x=805, y=300, height=225)

        self.id = 0
        self.iid = 0

        self.carregarDadosIniciais()

    # -----------------------------------------------------------------------------
    def carregarDadosIniciais(self):
        fsave = 'C:/Users/Daft/OneDrive/Área de Trabalho/PYTHON ESTACIO/PlanilhaAlunos.csv'
        if not os.path.exists(fsave):         
            print('Arquivo não encontrado')
            return  
        try:
            dados = pd.read_csv(fsave)
            print("************ dados disponíveis ***********")
            print(dados)

            u = dados.count()
            print('u:' + str(u))
            nn = len(dados['Aluno'])
            for i in range(nn):
                nome = dados['Aluno'][i]
                nota1 = str(dados['Nota1'][i])
                nota2 = str(dados['Nota2'][i])
                media = str(dados['Média'][i])
                situacao = dados['Situação'][i]

                self.treeMedias.insert('', 'end',
                                    iid=self.iid,
                                    values=(nome,
                                            nota1,
                                            nota2,
                                            media,
                                            situacao))

                self.iid += 1
                self.id += 1
        except Exception as e:  
            print(f'Erro ao carregar os dados: {e}')

    # -----------------------------------------------------------------------------
    def fSalvarDados(self):
        try:
            fsave = 'C:/Users/Daft/OneDrive/Área de Trabalho/PYTHON ESTACIO/PlanilhaAlunos.csv'
            dados = []

            for line in self.treeMedias.get_children():
                lstDados = []
                for value in self.treeMedias.item(line)['values']:
                    lstDados.append(value)

                dados.append(lstDados)

            df = pd.DataFrame(data=dados, columns=self.dadosColunas)
            df.to_csv(fsave, index=False)  # Salva o DataFrame em um arquivo CSV
            print("Dados Salvos")

        except Exception as e:
            print(f'Não foi possível salvar os dados {e}')

    # -----------------------------------------------------------------------------
    def fVerificarSituacao(self, nota1, nota2):
        media = (nota1 + nota2) / 2
        if media >= 7.0:
            situacao = 'Aprovado'
        elif media >= 5.0:
            situacao = 'Em Recuperação'
        else:
            situacao = 'Reprovado'
        return media, situacao

    # -----------------------------------------------------------------------------
    def fCalcularMedia(self):
        try:
            nome = self.txtNome.get()
            nota1 = float(self.txtNota1.get())
            nota2 = float(self.txtNota2.get())
            media, situacao = self.fVerificarSituacao(nota1, nota2)

            if self.selected_item:
                #Atualiza os dados do item selecionado
                self.treeMedias.item(self.selected_item,
                                     values=(nome,
                                             str(nota1),
                                             str(nota2),
                                             str(media),
                                             situacao))
                self.selected_item = None # Reseta o item selecionado
            else:
                self.treeMedias.insert('', 'end',
                                    iid=self.iid,
                                    values=(nome,
                                            str(nota1),
                                            str(nota2),
                                            str(media),
                                            situacao))

            self.iid += 1
            self.id += 1

            self.fSalvarDados()
        except ValueError:
            print('Entre com valores válidos')
        finally:
            self.txtNome.delete(0, 'end')
            self.txtNota1.delete(0, 'end')
            self.txtNota2.delete(0, 'end')

    # -----------------------------------------------------------------------------
    def fAlterar(self):
        try:
            self.selected_item = self.treeMedias.selection()[0] #Armazena o item selecionado
            values = self.treeMedias.item(self.selected_item)['values']
            self.txtNome.delete(0, 'end')
            self.txtNome.insert(0, values[0])
            self.txtNota1.delete(0, 'end')
            self.txtNota1.insert(0, values[1])
            self.txtNota2.delete(0, 'end')
            self.txtNota2.insert(0, values[2])
            # Lógica para atualizar os dados após alteração
            #self.fSalvarDados()

        except IndexError:
            print("Nenhum aluno selecionado.")

    def fExcluir(self):
        try:
            selected_item = self.treeMedias.selection()[0]
            self.treeMedias.delete(selected_item)
            self.fSalvarDados()
        except IndexError:
            print("Nenhum aluno selecionado.")

# ----------------------------------------------------------------------------- 
# Programa Principal
# ----------------------------------------------------------------------------- 
janela = tk.Tk()
principal = PrincipalRAD(janela)
janela.title('Bem Vindo ao RAD')
janela.geometry("820x600+10+10")
janela.mainloop()
