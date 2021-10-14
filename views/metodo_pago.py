from tkinter import *
from centrar import *
from controllers.crud import *
from views.finalizar_compra import *
from tkinter import messagebox

class Metodo:
    def __init__(self, obj, libro):
        self.obj_libro = libro
        self.obj_usuario = obj
        self.obj_crud = Crud()
        self.obj_centrar = Centro()
        self.getVentana()
        canvas = Canvas(self.ventana_metodopago, bg="#eeeeee", height=600, width=1000, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        background_img = PhotoImage(file=f"C:/Users/PC/PycharmProjects/BookStore/multimedia/Metodo de pago/background.png")
        background = canvas.create_image(500.0, 300.0, image=background_img)

        entry0_img = PhotoImage(file=f"C:/Users/PC/PycharmProjects/BookStore/multimedia/Metodo de pago/img_textBox0.png")
        entry0_bg = canvas.create_image(350.5, 206.0, image=entry0_img)
        self.tarjeta = Entry(self.ventana_metodopago,bd=0, bg="#ffffff", highlightthickness=0,font=("Arial", 14))
        self.tarjeta.place(x=150, y=187, width=401, height=36)

        entry1_img = PhotoImage(file=f"C:/Users/PC/PycharmProjects/BookStore/multimedia/Metodo de pago/img_textBox1.png")
        entry1_bg = canvas.create_image(350.5, 313.5, image=entry1_img)
        self.emailactual = StringVar()
        self.emailactual.set(f"{self.obj_usuario.email}")
        self.destinatario = Entry(self.ventana_metodopago,bd=0, bg="#ffffff",
                                  highlightthickness=0, textvariable=self.emailactual,font=("Arial", 14))
        self.destinatario.place(x=150, y=294, width=401, height=37)

        entry2_img = PhotoImage(file=f"C:/Users/PC/PycharmProjects/BookStore/multimedia/Metodo de pago/img_textBox2.png")
        entry2_bg = canvas.create_image(230.5, 431.5, image=entry2_img)
        self.cantidad = Entry(self.ventana_metodopago,bd=0, bg="#ffffff", highlightthickness=0,font=("Arial", 14))
        self.cantidad.place(x=150, y=412, width=161, height=37)

        img0 = PhotoImage(file=f"C:/Users/PC/PycharmProjects/BookStore/multimedia/Metodo de pago/img0.png")
        self.siguiente = Button(self.ventana_metodopago,image=img0, borderwidth=0,
                                highlightthickness=0, relief="flat", command=self.getFinalizar)
        self.siguiente.place(x=423, y=503, width=154, height=39)
        self.ventana_metodopago.mainloop()


    def getVentana(self):
        self.ventana_metodopago = Toplevel()
        self.ventana_metodopago.title("Metodo de pago")
        self.obj_centrar.centrar_ventana(self.ventana_metodopago, 600, 1000)
        self.ventana_metodopago.configure(bg="#ffffff")
        self.ventana_metodopago.resizable(0, 0)

    def getFinalizar(self):
        if ((self.cantidad.get().isdecimal() == True) and (self.tarjeta.get().isdecimal() == True)) and (len(self.tarjeta.get())>0):
            obj = Finalizar(self.obj_libro, self.obj_usuario, self.cantidad.get())
        elif (self.cantidad.get().isdecimal() == False) or (self.tarjeta.get().isdecimal() == False):
            messagebox.showinfo("Error", "Debe ingresar numeros enteros")



