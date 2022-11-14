from tkinter import Tk, Frame, Entry, Label, Button, StringVar
from conexao import banco
from login import TelaLogin
from ttkbootstrap import *
class TelaCadastro:
    def __init__(self) -> None:
        #Configuração da tela tkinter
        self.tela = Tk()
        self.tela.title("Cadastro ")
        self.tela.geometry("280x280")
        self.tela.minsize(280, 280) 
        self.tela.maxsize(280, 280)

        #Crição dos Frames
        self.frameUsu = Frame(self.tela)
        self.frameUsu.pack()
        self.frameSen = Frame(self.tela)
        self.frameSen.pack()
        self.frameBu = Frame(self.tela)
        self.frameBu.pack()
        self.frameEr = Frame(self.tela)
        self.frameEr.pack()


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
        Dados = banco.execute(f"select * from conta where Usuario = '{self._Usuario}';")
        if self._Usuario == "" or self._Senha == "":
            self.Erro("Vazio")
        elif Dados == 1:
            self.Erro("Usu")
        else:
          # banco.execute(f"insert into conta values ('{self._Usuario}','{self._Senha}');")
          # banco.execute("commit;")
           self.Login()
           
    
    def Erro(self,e):
        self.StrMensagem = StringVar()
        for i in self.frameEr.winfo_children():
            i.destroy()        
        if e == "Vazio":
            self.StrMensagem.set("Erro, Campo Vazio")
            self.Mensagem = Label(self.frameEr, textvariable=self.StrMensagem).pack()
        elif e == "Usu":
            self.StrMensagem.set("Erro, Usuario já existe") 
            self.Mensagem = Label(self.frameEr, textvariable=self.StrMensagem).pack()        
    
        
       
    def Login(self):
        self.tela.destroy()
        login1 = TelaLogin()

if __name__ == "__main__":
    menu = TelaCadastro()