from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from Dados import *

######Cores#######
co0= "#444466" #Preto
co1= "#feffff" #Branca
co2= "#6f9fbd" #Azul
co3= "#38576b" #valor
co4= "#403d3d" #letra
co5= "#ef5350" #vermelha

#criação janela

janela= Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

#criando frame
frame_digimon = Frame(janela, width=550, height=290, relief='flat')
frame_digimon.grid(row=1, column=0)

def trocar_dig(i):
    global imagem_digimon, dig_img

    frame_digimon['bg']= digimon[i]['categoria'][3]

    #categoria
    dig_nome['text'] = i
    dig_nome['bg'] =digimon[i]['categoria'][3]
    dig_tipo['text'] = digimon[i]['categoria'][0]
    dig_tipo['bg'] = digimon[i]['categoria'][3]
    dig_at['text'] = digimon[i]['categoria'][1]
    dig_at['bg'] = digimon[i]['categoria'][3]

    imagem_digimon = digimon[i]['categoria'][2]

    imagem_digimon = Image.open(imagem_digimon)
    imagem_digimon = imagem_digimon.resize((238, 238))
    imagem_digimon = ImageTk.PhotoImage(imagem_digimon)

    dig_img = Label(frame_digimon, image=imagem_digimon, relief='flat', bg=digimon[i]['categoria'][3], fg=co1)
    dig_img.place(x=60, y=50)
    dig_tipo.lift()
    dig_at.lift()

    #status digimon
    dig_Hp['text']= digimon[i]['status'][0]
    dig_Sp['text']= digimon[i]['status'][1]
    dig_Atk['text']= digimon[i]['status'][2]
    dig_INT['text']= digimon[i]['status'][3]
    dig_DEF['text']= digimon[i]['status'][4]
    dig_SPD['text']= digimon[i]['status'][5]
    dig_total['text']= digimon[i]['status'][6]
    #digimon habilidades
    dig_hab1['text']=digimon[i]['habilidades'][0]
    dig_hab2['text']=digimon[i]['habilidades'][1]
    dig_hab3['text'] = digimon[i]['habilidades'][2]




#nome
dig_nome = Label(frame_digimon, text='', relief='flat', anchor=CENTER, font=('Fixedsys 20'),bg= co1, fg=co1)
dig_nome.place(x=12, y=15)

#categoria
dig_tipo = Label(frame_digimon, text='', relief='flat', anchor=CENTER, font=('Ivy 10 bold'),bg= co1, fg=co1)
dig_tipo.place(x=12, y=50)

#atributo
dig_at = Label(frame_digimon, text='', relief='flat', anchor=CENTER, font=('Ivy 10 bold'),bg= co1, fg=co1)
dig_at.place(x=12, y=70)

#imagem do digimon


#Status
dig_status = Label(janela, text='Status lv.50', relief='flat', anchor=CENTER, font=('Verdana 15'),bg= co1, fg=co0)
dig_status.place(x=15, y=330)

#hp
dig_Hp = Label(janela, text='Hp: 940', relief='flat', anchor=CENTER, font=('Verdana 10'),bg= co1, fg=co4)
dig_Hp.place(x=15, y=360)

#sp
dig_Sp = Label(janela, text='Sp: 94', relief='flat', anchor=CENTER, font=('Verdana 10'),bg= co1, fg=co4)
dig_Sp.place(x=15, y=380)

#Atk
dig_Atk = Label(janela, text='Atk: 128', relief='flat', anchor=CENTER, font=('Verdana 10'),bg= co1, fg=co4)
dig_Atk.place(x=15, y=400)

#INT
dig_INT = Label(janela, text='Int: 128', relief='flat', anchor=CENTER, font=('Verdana 10'),bg= co1, fg=co4)
dig_INT.place(x=15, y=420)

#DEF
dig_DEF = Label(janela, text='Def: 89', relief='flat', anchor=CENTER, font=('Verdana 10'),bg= co1, fg=co4)
dig_DEF.place(x=15, y=440)

#SPD
dig_SPD = Label(janela, text='Spd: 99', relief='flat', anchor=CENTER, font=('Verdana 10'),bg= co1, fg=co4)
dig_SPD.place(x=15, y=460)

#Total
dig_total = Label(janela, text='Total: 1478', relief='flat', anchor=CENTER, font=('Verdana 10'),bg= co1, fg=co4)
dig_total.place(x=15, y=480)

#Habilidades
dig_hab = Label(janela, text='Habilidades', relief='flat', anchor=CENTER, font=('Verdana 20'),bg= co1, fg=co0)
dig_hab.place(x=180, y=310)

#hab1
dig_hab1 = Label(janela, text="Heaven's Knucle", relief='flat', anchor=CENTER, font=('Verdana 10'),bg= co1, fg=co4)
dig_hab1.place(x=195, y=360)

#hab2
dig_hab2 = Label(janela, text='Holy Light II', relief='flat', anchor=CENTER, font=('Verdana 10'),bg= co1, fg=co4)
dig_hab2.place(x=195, y=385)

#hab3
dig_hab3 = Label(janela, text='X-Heal', relief='flat', anchor=CENTER, font=('Verdana 10'),bg= co1, fg=co4)
dig_hab3.place(x=195, y=410)

#criando botões para digimons
#botao1
imagem_dig_head1= Image.open('Images/77-angemon-head.png')
imagem_dig_head1= imagem_dig_head1.resize((40, 40))
imagem_dig_head1= ImageTk.PhotoImage(imagem_dig_head1)

b_dig_1 = Button(janela,command=lambda:trocar_dig('Angemon'),image= imagem_dig_head1,text='Angemon',width=150, relief='raised',overrelief= RIDGE ,compound=LEFT,anchor= NW,padx=5,font=('Verdana 12'),bg= co1, fg=co0)
b_dig_1.place(x=375, y=10)

#botao2
imagem_dig_head2= Image.open('Images/223-imperialdramon-fm-head.png')
imagem_dig_head2= imagem_dig_head2.resize((40, 40))
imagem_dig_head2= ImageTk.PhotoImage(imagem_dig_head2)

b_dig_1 = Button(janela,command=lambda:trocar_dig('Imperialdramon'),image= imagem_dig_head2,text='Imperialdramon',width=150, relief='raised',overrelief= RIDGE ,compound=LEFT,anchor= NW,padx=5,font=('Verdana 12'),bg= co1, fg=co0)
b_dig_1.place(x=375, y=65)

#botao3
imagem_dig_head3= Image.open('Images/kyubimon-head.png')
imagem_dig_head3= imagem_dig_head3.resize((40, 40))
imagem_dig_head3= ImageTk.PhotoImage(imagem_dig_head3)

b_dig_1 = Button(janela,command=lambda:trocar_dig('Kyubimon'),image= imagem_dig_head3,text='Kyubimon',width=150, relief='raised',overrelief= RIDGE ,compound=LEFT,anchor= NW,padx=5,font=('Verdana 12'),bg= co1, fg=co0)
b_dig_1.place(x=375, y=120)

#botao4
imagem_dig_head4= Image.open('Images/89-kurisarimon-head.png')
imagem_dig_head4= imagem_dig_head4.resize((40, 40))
imagem_dig_head4= ImageTk.PhotoImage(imagem_dig_head4)

b_dig_1 = Button(janela,command=lambda:trocar_dig('Kurisarimon'),image= imagem_dig_head4,text='Kurisarimon',width=150, relief='raised',overrelief= RIDGE ,compound=LEFT,anchor= NW,padx=5,font=('Verdana 12'),bg= co1, fg=co0)
b_dig_1.place(x=375, y=175)

#botao5
imagem_dig_head5= Image.open('Images/25-gaomon-head.png')
imagem_dig_head5= imagem_dig_head5.resize((40, 40))
imagem_dig_head5= ImageTk.PhotoImage(imagem_dig_head5)

b_dig_1 = Button(janela,command=lambda:trocar_dig('Gaomon'),image= imagem_dig_head5,text='Gaomon',width=150, relief='raised',overrelief= RIDGE ,compound=LEFT,anchor= NW,padx=5,font=('Verdana 12'),bg= co1, fg=co0)
b_dig_1.place(x=375, y=230)


#tela inicial, digimon aleatorio quando abre o programa
import random
Lista_digimons=['Angemon','Imperialdramon','Kyubimon','Kurisarimon','Gaomon']

digimon_escohido= random.sample(Lista_digimons, 1)

trocar_dig(digimon_escohido[0])


janela.mainloop()
