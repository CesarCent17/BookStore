from tkinter import *
from centrar import *
from controllers.crud import *
from tkinter import messagebox
import webbrowser as wb
import sys

class Finalizar:
    def __init__(self, libro,usuario,cantidad):
        self.obj_crud = Crud()
        self.obj_libro = libro
        obj = Crud()
        self.tupla = (f"{usuario.nombre} {usuario.apellido}", "Libro", f"{self.obj_libro.precio}", f"{cantidad}", "0", "0", "0", "0")
        self.tupla = self.obj_crud.resultProcedimiento("factura", self.tupla)
        print(self.tupla)
        self.obj_centrar = Centro()
        self.getVentana()
        canvas = Canvas(self.ventana_finalizar,bg="#ffffff",height=600,width=1000,bd=0,highlightthickness=0,relief="ridge")
        canvas.place(x=0, y=0)

        background_img = PhotoImage(file=f"C:/Users/PC/PycharmProjects/BookStore/multimedia/Finalizar/background.png")
        background = canvas.create_image(500.0, 300.0,image=background_img)

        entry0_img = PhotoImage(file=f"C:/Users/PC/PycharmProjects/BookStore/multimedia/Finalizar/img_textBox0.png")
        entry0_bg = canvas.create_image(575.0, 328.0,image=entry0_img)
        #Total
        self.totalpagarBD = StringVar()
        self.totalpagarBD.set(f"{self.tupla[6]}")
        self.totalpagar = Entry(self.ventana_finalizar,bd=0,bg="#ffffff",
                              highlightthickness=0,font=("Arial", 14),textvariable=self.totalpagarBD)
        self.totalpagar.place(x=508, y=309,width=134,height=36)

        #Subtotal
        entry1_img = PhotoImage(file=f"C:/Users/PC/PycharmProjects/BookStore/multimedia/Finalizar/img_textBox1.png")
        entry1_bg = canvas.create_image(575.0, 180.0,image=entry1_img)
        self.subtotalBD = StringVar()
        self.subtotalBD.set(f"{self.tupla[4]}")
        self.subtotal = Entry(self.ventana_finalizar,bd=0,bg="#ffffff",
                         highlightthickness=0,font=("Arial", 14), textvariable=self.subtotalBD)
        self.subtotal.place(x=508, y=161,width=134,height=36)

        #Iva
        entry2_img = PhotoImage(file=f"C:/Users/PC/PycharmProjects/BookStore/multimedia/Finalizar/img_textBox2.png")
        entry2_bg = canvas.create_image(575.0, 249.0,image=entry2_img)
        self.ivaBD = StringVar()
        self.ivaBD.set(f"{self.tupla[5]:.2f}")
        self.iva= Entry(self.ventana_finalizar,bd=0,bg="#ffffff",
                                highlightthickness=0,font=("Arial", 14), textvariable=self.ivaBD)
        self.iva.place(x=508, y=230,width=134,height=36)

        img0 = PhotoImage(file=f"C:/Users/PC/PycharmProjects/BookStore/multimedia/Finalizar/img0.png")
        self.finalizar_compra = Button(self.ventana_finalizar,image=img0,borderwidth=0,highlightthickness=0,relief="flat", command = self.getFinal)
        self.finalizar_compra.place(x=417, y=427,width=215,height=39)
        self.ventana_finalizar.mainloop()

    def getVentana(self):
        self.ventana_finalizar = Toplevel()
        self.ventana_finalizar.title("Factura")
        self.obj_centrar.centrar_ventana(self.ventana_finalizar, 600, 1000)
        self.ventana_finalizar.configure(bg="#ffffff")
        self.ventana_finalizar.resizable(0, 0)
    def getFinal(self):
        messagebox.showinfo("Estado", f"{self.tupla[7]}")
        self.enviarlibro1()
        self.cerrarSesion()
    def enviarlibro1(self):
        wb.open_new(r"C:/Users/PC/PycharmProjects/BookStore/multimedia/Gustave Flaubert Madame Bovary.pdf")

    def cerrarSesion(self):
        self.ventana_finalizar.destroy()
        sys.exit()
