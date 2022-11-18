from tkinter import Tk, Frame, Entry, Label, Button, StringVar, Listbox, END, Toplevel, messagebox
from conexao import banco
from tkcalendar import DateEntry
class Tarefas:
    def __init__(self,Usu,listaTarefas=[]) -> None:
        self.listaTarefas = listaTarefas
        self.__Usu = Usu

    
    def TelaTk(self):
        #Configurações da Tela
        self.TelaTarefas = Tk()
        self.TelaTarefas.title("Tarefas")
        self.TelaTarefas.geometry("520x480")
        self.TelaTarefas.minsize(520, 480) 
        self.TelaTarefas.maxsize(520, 480)       
        
        #Criação dos Frames
        self.Frame_Cima = Frame(self.TelaTarefas)
        self.Frame_Cima.pack()
                
        self.BoxCenter = Listbox(self.TelaTarefas,font="Arial 12",xscrollcommand="yes")
        self.BoxCenter.pack(fill="both", expand="yes")
        self.Tudo = Frame(self.BoxCenter)
        self.Tudo.pack()

        self.Frame_Baixo = Frame(self.TelaTarefas)
        self.Frame_Baixo.pack()
       
        #Butões/Labels
        titulo = Label(self.Frame_Cima, text="Minhas Tarefas",font=("Elephant 35"))
        titulo.grid(row=0, column=0, pady=1,)
        
        self.ButtonAdicionar = Button(self.Frame_Baixo,text="Adiconar", width=15,command=lambda:self.Acao("Adiconar"))
        self.ButtonAdicionar.pack(side="left",padx=8,pady=8)  
        self.ButtonAtualizar = Button(self.Frame_Baixo,text="Alterar", width=15,command=lambda:self.Acao("Alterar"))
        self.ButtonAtualizar.pack(side="left",padx=8,pady=8)  
        self.ButtonRemover = Button(self.Frame_Baixo,text="Remover", width=15,command=lambda:self.Remover())
        self.ButtonRemover.pack(side="left",padx=8,pady=8)  
       
    

       #Tarefas No Banco de Dados
        global Dados
        banco.execute(f"select * from tarefas where Conta_Usuario = '{self.__Usu}';")
        Dados = banco.fetchall()
        print(Dados)
        for i in Dados:
            #print(i)
            self.listaTarefas.append(f'{i[2]}'+' '*len(i[2]) +f'Data de Entrega: {i[3]}')

        
        for Tarefa in self.listaTarefas:
            self.BoxCenter.insert(END,Tarefa)

       
        self.TelaTarefas.mainloop()       



    def AdicionarTarefas(self,txt,data):
        self._NovaTarefa = txt
        self.listaTarefas.append(f'{self._NovaTarefa}'+' '*len(txt) +f'Data de Entrega: {data}')
        banco.execute(f'insert into tarefas(Conta_Usuario,tarefas,data) values("{self.__Usu}", "{self._NovaTarefa}","{data}");')
        banco.execute("commit;")
        self.BoxCenter.insert(END,f'{self._NovaTarefa}'+' '*len(txt) +f'Data de Entrega: {data}')
        self.Tela.destroy()
        return self.listaTarefas

    def Remover(self):
        self.Item = list(self.BoxCenter.curselection())
        if self.Item == []:
            self.Erro("Sele")
        else:
            Num = int(self.Item[0])
            self.BoxCenter.delete(Num)
            del self.listaTarefas[Num]
            teste = list(Dados)[Num][1]
            print(teste)
            banco.execute(f'delete from tarefas where Id = "{teste}"; ')
            banco.execute("commit")

    def Atualizar(self):
        pass

    def Acao(self,condi):
        self.Tela = Toplevel()
        self.Tela.geometry("240x150")
        self.Frame = Frame(self.Tela)
        self.Frame.pack()
        self.FrameCal = Frame(self.Tela)
        self.FrameCal.pack()
        self.FrameB = Frame(self.Tela)
        self.FrameB.pack()
        if condi == "Adiconar":
            self.LabelTarefa = Label(self.Frame,text="Digite a tarefa que deseja adicionar: ")
            self.LabelTarefa.pack()
            self._EntryTarefa = Entry(self.Frame,width=30)
            self._EntryTarefa.pack(side="right",pady=8)

            self.LabelTarefa = Label(self.FrameCal,text="Coloque a Data de Entrega: ")
            self.LabelTarefa.pack()           
            self.LabelData=Entry(self.FrameCal)
            self.LabelData.pack()
          
            
            self.ButonOK = Button(self.FrameB, text="OK", command=lambda:self.AdicionarTarefas(self._EntryTarefa.get(), self.LabelData.get()))
            self.ButonOK.pack(side="bottom",pady=12)  

        elif condi == "Alterar":
            self.Item = int(list(self.BoxCenter.curselection())[0])
            #teste = list(Dados)[self.Item]
            print(self.Item)
            self.LabelTarefa = Label(self.Frame,text="Alterar o nome do trabalho: ")
            self.LabelTarefa.pack()

            self._EntryTarefa = Entry(self.Frame,width=30,textvariable=self.Item)
            self._EntryTarefa.insert(0,"Sei la")
            self._EntryTarefa.pack(side="right",pady=8)            


        self.Tela.mainloop()
    def Erro(self,e):
        if e == "Vazio":
            messagebox.showwarning(title="Erro", message="Campo Vazio")
        if e == "Sele":
            messagebox.showwarning(title="Erro", message="Nenhum Item foi selecionado")
if __name__ == "__main__":
    obj = Tarefas("Lulu")
    obj.TelaTk()