from tkinter import *
from tkinter import messagebox 

from PIL import ImageTk, Image
import os

janela = Tk()
janela.title("CALCULADORA PYTHON")

diretorio_script = os.path.dirname(os.path.abspath(__file__))

# Obtém as dimensões da tela
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

# Calcula a posição para centralizar a janela
x_pos = largura_tela // 2 - 350 // 2  # Largura da janela é 350
y_pos = altura_tela // 2 - 360 // 2  # Altura da janela é 360

# Define a posição inicial da janela
janela.geometry(f"350x360+{x_pos}+{y_pos}")

janela.resizable(1, 0)
janela.config(bd=1)

caminho_imagem = os.path.join(diretorio_script, "calculadora.png")

#Imagem da calculadora
# Verifica se o arquivo da imagem existe
if os.path.isfile(caminho_imagem):
    # Imagem da calculadora
    imagem_calculadora = Image.open(caminho_imagem)
    nueva_imagen = imagem_calculadora.resize((75, 75))
    render = ImageTk.PhotoImage(nueva_imagen)
    label_imagem = Label(janela, image=render)
    label_imagem.image = render
    label_imagem.pack(pady=5)
else:
    messagebox.showerror("ERRO", "Arquivo de imagem não encontrado.")

def cfloat(numero):
    try:
        result=float(numero)
    except:
        messagebox.showerror("ERRO","Insira os dados novamente")
    return result

## Métodos das operações

def somar():
    resultado.set(cfloat(numero1.get())+cfloat(numero2.get()))
    mostrarResultado()
   
def subtracao():
    resultado.set(cfloat(numero1.get())-cfloat(numero2.get()))
    mostrarResultado()
    
 
def multiplicar():
    resultado.set(cfloat(numero1.get())*cfloat(numero2.get()))
    mostrarResultado()   

 
def dividir():
    resultado.set(cfloat(numero1.get())/cfloat(numero2.get()))
    mostrarResultado()   

def potencia():
    resultado.set(cfloat(numero1.get())**cfloat(numero2.get()))
    mostrarResultado()

def raiz():
    resultado.set(cfloat(numero1.get())**((1)/(cfloat(numero2.get()))))
    mostrarResultado()


def mostrarResultado():
    messagebox.showinfo("RESULTADO",f"O resultado da operação é: {resultado.get()}")

numero1=StringVar()
numero2=StringVar()
resultado = StringVar()

frame_conta = Frame(janela, width=300, heigh=200)
frame_conta.config(bd=4,
            padx=15,
            pady=15,    
            relief=SOLID)
frame_conta.pack(side=TOP,anchor=CENTER)
#Não altera o posicionamento
frame_conta.pack_propagate(False)


Label(frame_conta, text="Primeiro número:",fg="black",font=("Arial", 10,"bold")).pack()
Entry(frame_conta,textvariable=numero1,justify="center").pack()

Label(frame_conta, text="Segundo número:",fg="black",font=("Arial", 10,"bold")).pack()
Entry(frame_conta,textvariable=numero2,justify="center").pack()

Button(frame_conta,text="+",command=somar,height=1,width=4,bg="black",fg="white",font=("Arial", 9,"bold")).pack(side="left",fill=X,padx=1)
Button(frame_conta,text="-",command=subtracao,height=1,width=4,bg="black",fg="white",font=("Arial", 9,"bold")).pack(side="left",fill=X,padx=1)
Button(frame_conta,text="*",command=multiplicar,height=1,width=4,bg="black",fg="white",font=("Arial", 9,"bold")).pack(side="left",fill=X,padx=1)
Button(frame_conta,text="/",command=dividir,height=1,width=4,bg="black",fg="white",font=("Arial", 9,"bold")).pack(side="left",fill=X,padx=1)
Button(frame_conta,text="^",command=potencia,height=1,width=4,bg="black",fg="white",font=("Arial", 9,"bold")).pack(side="left",fill=X,padx=1)
Button(frame_conta,text="raiz",command=raiz,height=1,width=7,bg="black",fg="white",font=("Arial", 9,"bold")).pack(side="left",fill=X,padx=1)


Button(janela,text="Encerrar",command=janela.quit ,height=2,width=10,bg="red",fg="white",font=("Arial", 9,"bold")).pack(side=BOTTOM)

janela.mainloop()