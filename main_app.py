from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk

co0 = "black"
co1 = "white"             
co2 = "#e9edf5"    #grey         
co3 = "blue"             
co4= "#9B111E"  #red
co5 = "orange"
co6 = "#6B8E23"   #green
co13 = "gold"

janela = Tk()
janela.title("")
janela.geometry('250x380')
janela.configure(background=co1)
janela.resizable(width=False, height=False)

style = ttk.Style(janela)
style.theme_use('clam')

frameCima = Frame(janela, width=300, height=50, background=co1, relief= "flat")
frameCima.grid(row=0, column=0)
frameMeio = Frame(janela, width=300, height=90, background=co1, relief= "flat")
frameMeio.grid(row=1, column=0)
frameBaixo = Frame(janela, width=300, height=290, background=co2, relief= "flat")
frameBaixo.grid(row=2, column=0)

app = Label(frameCima, text="Orçamento:",compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=('Verdana 20'), bg=co1, fg=co0)
app.place(x=35, y=0)
app_img = Image.open(r"pngwing.com.png")
app_img = app_img.resize((35,35))
app_img = ImageTk.PhotoImage(app_img)
app_logo = Label(frameCima, image=app_img, compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=('Verdana 20'), bg=co1, fg=co0)
app_logo.place(x=0, y=0)

app_linha= Label(frameCima, width=295, relief=FLAT, anchor=NW,font=('Verdana 20'), bg=co6, fg=co6)
app_linha.place(x=0, y=47)

def calcular():
    renda_mensal = float(Renda_valor.get())
    essencial = (50 / 100) * renda_mensal
    lazer = (30 / 100) * renda_mensal
    economia = (20 / 100) * renda_mensal
    Valor_necessidades['text'] =(
    'R${:,.2f}'.format(essencial))
    Valor_lazer['text'] =(
    'R${:,.2f}'.format(lazer))
    Valor_economia['text'] = (
    'R${:,.2f}'.format(economia))

app_ = Label(frameMeio, text='Digite sua renda mensal : ', relief=FLAT, anchor=NW, font=('Ivy 12'), bg=co1, fg=co0)
app_.place(x=7, y=15)
Renda_valor= Entry(frameMeio, width=10,font=('Ivy 14'),justify='center', relief='solid')
Renda_valor.place(x=10, y=40)
Botao_calcular= Button(frameMeio, command=calcular,text='Calcular'.upper(), overrelief=RIDGE, anchor=NW, font='Ivy 9', bg=co1, fg=co0)
Botao_calcular.place(x=150, y=40)

app_ = Label(frameBaixo, text=' Valores recomendados:        ',relief=FLAT, anchor=NW, font=('Ivy 14'), bg=co6, fg=co1)
app_.place(x=0, y=0)

Valor_necessidades = Label(frameBaixo, text=' Necessidades: ', relief=FLAT, width=35, anchor=NW, font=('Verdana 12'), bg=co2, fg=co0)
Valor_necessidades.place(x=00, y=40)
Valor_necessidades = Label(frameBaixo, relief=FLAT, width=22, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
Valor_necessidades.place(x=10, y=70)

Valor_economia = Label(frameBaixo, text='Economia:', relief=FLAT, width=35, anchor=NW, font=('Verdana 12'), bg=co2, fg=co0)
Valor_economia.place(x=10, y=100)
Valor_economia = Label(frameBaixo, relief=FLAT, width=22, anchor=NW, font=('Verdana 12'), bg=co1, fg=co6)
Valor_economia.place(x=10,y=130)

Valor_lazer = Label(frameBaixo, text='Lazer: ', relief=FLAT, width=35, anchor=NW, font=('Verdana 12'), bg=co2, fg=co0)
Valor_lazer.place(x=10, y=160)
Valor_lazer = Label(frameBaixo, relief=FLAT, width=22, anchor=NW, font=('Verdana 12'), bg=co1, fg=co3)
Valor_lazer.place(x=10, y=190)
 
janela.mainloop()