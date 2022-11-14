from tkinter import Tk, Frame, Entry, Label, Button
from ttkbootstrap import * 
from conexao import banco
from login import Login
from ttkthemes import ThemedTk
class Menu:
    def __init__(self) -> None:
        #Configuração da tela tkinter
        self.tela = Tk()
        self.tela.title("Menu ")
        self.tela.geometry("260x260")
        
        #Crição dos Frames
        self.frameUsu = Frame(self.tela)
        self.frameUsu.pack()
        self.frameSen = Frame(self.tela)
        self.frameSen.pack()
        self.frameBu = Frame(self.tela)
        self.frameBu.pack()

        #Criação dos botões
        self.LabelUsu = Label(self.frameUsu,text="Crie seu usuario: ")
        self.LabelUsu.pack(side="top",pady=8)
        self._EntryUsu = Entry(self.frameUsu,width=30)
        self._EntryUsu.pack(side="left",pady=8)

        self.LabelSen = Label(self.frameSen,text="Crie sua senha: ")
        self.LabelSen.pack(side="top",pady=8)
        self._EntrySen = Entry(self.frameSen,width=30)
        self._EntrySen.pack(side="left",pady=8)  
        
        self.ButtonLogar = Button(self.frameBu,text="Já tem conta? Entrar na sua conta",command=lambda:self.Login())
        self.ButtonLogar.pack(side="bottom",pady=8)  

        self.ButtonCriar = Button(self.frameBu,text="Criar sua conta",command=lambda:self.CriarConta())
        self.ButtonCriar.pack(side="bottom",pady=8)

       
        self.tela.mainloop()
  
    def CriarConta(self):
        self._Usuario = self._EntryUsu.get()
        self._Senha = self._EntrySen.get()
        if self._Usuario == "" or self._Senha == "":
            self.Erro()
        else:
          # banco.execute(f"insert into conta values ('{self._Usuario}','{self._Senha}');")
          # banco.execute("commit;")
           self.Login()
           
    
    def Erro(self):
        self.TelaErro = Toplevel()
        self.Mensagem = Label(self.TelaErro,text="Erro").pack(side="bottom")
        self.TelaErro.mainloop()
    
    def Login(self):
        self.tela.destroy()
        login = Login()
menu = Menu()