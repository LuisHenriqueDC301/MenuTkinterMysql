import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from conexao import banco
from login import TelaLogin
class TelaCadastro:
    def __init__(self) -> None:
        #Configuração da tela tkinter
        self.tela = ttk.Window(themename="journal")
        self.tela.title("Cadastro ")
        self.tela.geometry("280x280")
        self.tela.minsize(280, 280) 
        self.tela.maxsize(280, 280)

        #Crição dos Frames
        self.frameUsu = ttk.Frame(self.tela)
        self.frameUsu.pack()
        self.frameSen = ttk.Frame(self.tela)
        self.frameSen.pack()
        self.frameBu = ttk.Frame(self.tela)
        self.frameBu.pack()
        self.frameEr = ttk.Frame(self.tela)
        self.frameEr.pack()


        #Criação dos botões
        self.LabelUsu = ttk.Label(self.frameUsu,text="Crie seu usuario: ")
        self.LabelUsu.pack(side="top",pady=8)
        self._EntryUsu = ttk.Entry(self.frameUsu,width=30)
        self._EntryUsu.pack(side="left",pady=8)

        self.LabelSen = ttk.Label(self.frameSen,text="Crie sua senha: ")
        self.LabelSen.pack(side="top",pady=8)
        self._EntrySen = ttk.Entry(self.frameSen,width=30,show="*")
        self._EntrySen.pack(side="left",pady=8)  
        
        self.ButtonLogar = ttk.Button(self.frameBu,text="     Fazer Login      ",command=lambda:self.Login())
        self.ButtonLogar.pack(side="bottom",pady=8)  

        self.ButtonCriar = ttk.Button(self.frameBu,text="Criar Conta",command=lambda:self.CriarConta())
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
           banco.execute(f"insert into conta values ('{self._Usuario}','{self._Senha}');")
           banco.execute("commit;")
           self.Login()
           
    
    def Erro(self,e):
        self.StrMensagem = ttk.StringVar()
        for i in self.frameEr.winfo_children():
            i.destroy()        
        if e == "Vazio":
            self.StrMensagem.set("Erro, Campo Vazio")
            self.Mensagem = ttk.Label(self.frameEr, textvariable=self.StrMensagem).pack()
        elif e == "Usu":
            self.StrMensagem.set("Erro, Usuario já existe") 
            self.Mensagem = ttk.Label(self.frameEr, textvariable=self.StrMensagem).pack()        
    
        
       
    def Login(self):
        self.tela.destroy()
        login1 = TelaLogin()

    
if __name__ == "__main__":
    menu = TelaCadastro()