from tkinter import *
from centrar import *
from views.metodo_pago import *

class Descripcion:
    def __init__(self, obj, libro):
        self.obj_libro = libro
        self.obj_usuario = obj
        # self.obj_crud = Crud()
        self.obj_centrar = Centro()
        self.getVentana()
        canvas = Canvas(self.ventana_descripcion, bg="#eeeeee", height=600, width=1000, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        background_img = PhotoImage(file=f"C:/Users/PC/PycharmProjects/BookStore/multimedia/Descripcion/background.png")
        background = canvas.create_image(500.0, 350.5, image=background_img)
        #Ir a pagar
        img0 = PhotoImage(file=f"C:/Users/PC/PycharmProjects/BookStore/multimedia/Descripcion/img0.png")
        self.ir_a_pagar = Button(self.ventana_descripcion,image=img0, borderwidth=0,
                                 highlightthickness=0, relief="flat", command=self.metodoPago)
        self.ir_a_pagar.place(x=619, y=367, width=154, height=39)
        self.ventana_descripcion.mainloop()

    def getVentana(self):
        self.ventana_descripcion = Toplevel()
        self.ventana_descripcion.title("Madame Bovary")
        self.obj_centrar.centrar_ventana(self.ventana_descripcion, 600, 1000)
        self.ventana_descripcion.configure(bg="#ffffff")
        self.ventana_descripcion.resizable(0, 0)

    def metodoPago(self):
        obj = Metodo(self.obj_usuario, self.obj_libro)
