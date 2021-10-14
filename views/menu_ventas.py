from tkinter import *
from centrar import *
from views.descripcion import *

class MenuP:
    def __init__(self, obj):
        self.obj_usuario = obj
        self.obj_crud = Crud()
        self.obj_centrar = Centro()
        self.getVentana()
        canvas = Canvas(self.ventana_menup,bg="#eeeeee",height=600, width=1000,bd=0, highlightthickness=0,relief="ridge")
        canvas.place(x=0, y=0)

        background_img = PhotoImage(file=f"C:/Users/PC/PycharmProjects/BookStore/multimedia/MenuP/background.png")
        background = canvas.create_image( 500.0, 300.0,image=background_img)

        # Button comprar
        img2 = PhotoImage(file=f"C:/Users/PC/PycharmProjects/BookStore/multimedia/MenuP/img1.png")
        self.comprar1 = Button(self.ventana_menup,image=img2,borderwidth=0,
                               highlightthickness=0,relief="flat",command= self.getDescripcion1)
        self.comprar1.place(x=302, y=189,width=75,height=24)

        img1 = PhotoImage(file=f"C:/Users/PC/PycharmProjects/BookStore/multimedia/MenuP/img1.png")
        self.comprar2 = Button(self.ventana_menup, image=img1, borderwidth=0,
                               highlightthickness=0, relief="flat")
        self.comprar2.place(x=487, y=189, width=75, height=24)

        img3 = PhotoImage(file=f"C:/Users/PC/PycharmProjects/BookStore/multimedia/MenuP/img1.png")
        self.comprar3 = Button(self.ventana_menup,image=img3,borderwidth=0,highlightthickness=0,relief="flat")
        self.comprar3.place(x=672, y=189,width=75,height=24)
        self.ventana_menup.mainloop()

    def getVentana(self):
        self.ventana_menup = Toplevel()
        self.ventana_menup.title("Menu principal")
        self.obj_centrar.centrar_ventana(self.ventana_menup, 600, 1000)
        self.ventana_menup.configure(bg="#ffffff")
        self.ventana_menup.resizable(0, 0)
    def getDescripcion1(self):
        obj_libro = self.obj_crud.getLibro("Gustave Flaubert", "Madame Bovary")
        obj = Descripcion(self.obj_usuario, obj_libro)
