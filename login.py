from tkinter import Tk, Frame, Entry, Label, Button, StringVar
from conexao import banco
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from main import Tarefas
class TelaLogin:
    def __init__(self) -> None:
        #Configurações da tela de login
        self.TelaLogin = Tk()
        self.TelaLogin.title("Login")
        self.TelaLogin.geometry("280x280")
        self.TelaLogin.minsize(280, 280) 
        self.TelaLogin.maxsize(280, 280)
        #Crição dos Frames
        self.frameUsu = Frame(self.TelaLogin)
        self.frameUsu.pack()
        self.frameSen = Frame(self.TelaLogin)
        self.frameSen.pack()
        self.frameBu = Frame(self.TelaLogin)
        self.frameBu.pack()
        self.frameEr = Frame(self.TelaLogin)
        self.frameEr.pack()

        #Criação dos botões
        self.LabelUsu = Label(self.frameUsu,text="Digite seu usuario: ")
        self.LabelUsu.pack(side="top",pady=8)
        self._EntryUsu = Entry(self.frameUsu,width=30)
        self._EntryUsu.pack(side="left",pady=8)
    
        self.LabelSen = Label(self.frameSen,text="Digite sua senha: ")
        self.LabelSen.pack(side="top",pady=8)
        self._EntrySen = Entry(self.frameSen,width=30,show="*")
        self._EntrySen.pack(side="left",pady=8)  
        
        self.ButtonLogar = Button(self.frameBu,text="Entrar", command=lambda:self.Verifi())
        self.ButtonLogar.pack(side="bottom",pady=8)  


        self.TelaLogin.mainloop()    

    def Verifi(self):
        self._Usuario = self._EntryUsu.get()
        self._Senha = self._EntrySen.get()
        Dados = banco.execute(f"select * from conta where Usuario = '{self._Usuario}' and Senha = '{self._Senha}'")
        if self._Usuario == "" or self._Senha == "":
            self.Erro("Vazio")        
        elif Dados != 1:            
              self.Erro("Errado")
        else:
            self.TelaLogin.destroy()
            Obj = Tarefas(self._Usuario)
            Obj.TelaTk()
    def Erro(self,e):
        self.StrMensagem = StringVar()
        for i in self.frameEr.winfo_children():
            i.destroy()
        if e == "Vazio":
            self.StrMensagem.set("Erro, Campo Vazio")
            self.Mensagem = Label(self.frameEr, textvariable=self.StrMensagem).pack()
        elif e == "Errado":
            self.StrMensagem.set("Erro, Usuario ou senha errado") 
            self.Mensagem = Label(self.frameEr, textvariable=self.StrMensagem).pack(side="left")  

if __name__== "__main__":
    login = TelaLogin()