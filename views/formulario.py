from tkinter import *
from centrar import *
from controllers.crud import *
from tkinter import messagebox

class Formulario:
    def __init__(self):
        self.obj_crud = Crud()
        self.obj_centrar = Centro()
        self.getVentana()
        canvas = Canvas(self.ventana_formulario,bg="#393e46",height=600, width=1000,bd=0,highlightthickness=0,relief="ridge")
        canvas.place(x=0, y=0)

        background_img = PhotoImage(file=f"C:/Users/PC/PycharmProjects/BookStore/multimedia/Formulario/background.png")
        background = canvas.create_image(500.0, 300.0,image=background_img)

        entry0_img = PhotoImage(file=f"C:/Users/PC/PycharmProjects/BookStore/multimedia/Formulario/img_textBox0.png")
        entry0_bg = canvas.create_image(500.0, 175.5,image=entry0_img)
        self.nombre = Entry(self.ventana_formulario,bd=0, bg="#ffffff", highlightthickness=0,font=("Arial", 14))
        self.nombre.place(x=338, y=158,width=324, height=33)

        entry1_img = PhotoImage(file=f"C:/Users/PC/PycharmProjects/BookStore/multimedia/Formulario/img_textBox1.png")
        entry1_bg = canvas.create_image(500.0, 249.0,image=entry1_img)
        self.apellido = Entry(self.ventana_formulario,bd=0,bg="#ffffff",highlightthickness=0,font=("Arial", 14))
        self.apellido.place(x=338, y=231,width=324,height=34)

        entry2_img = PhotoImage(file=f"C:/Users/PC/PycharmProjects/BookStore/multimedia/Formulario/img_textBox2.png")
        entry2_bg = canvas.create_image(500.0, 322.5,image=entry2_img)
        self.email = Entry(self.ventana_formulario,bd=0,bg="#ffffff",highlightthickness=0,font=("Arial", 14))
        self.email.place(x=338, y=305,width=324,height=33)

        entry3_img = PhotoImage(file=f"C:/Users/PC/PycharmProjects/BookStore/multimedia/Formulario/img_textBox3.png")
        entry3_bg = canvas.create_image(500.0, 396.5,image=entry3_img)
        self.usuario = Entry(self.ventana_formulario,bd=0,bg="#ffffff",highlightthickness=0,font=("Arial", 14))
        self.usuario.place(x=338, y=379,width=324,height=33)

        entry4_img = PhotoImage(file=f"C:/Users/PC/PycharmProjects/BookStore/multimedia/Formulario/img_textBox4.png")
        entry4_bg = canvas.create_image(500.0, 470.5,image=entry4_img)
        self.contrasena = Entry(self.ventana_formulario,bd=0,bg="#ffffff",highlightthickness=0, show="*",font=("Arial", 14))
        self.contrasena.place(x=338, y=453,width=324,height=33)

        img0 = PhotoImage(file=f"C:/Users/PC/PycharmProjects/BookStore/multimedia/Formulario/img0.png")
        self.registrar = Button(self.ventana_formulario,image=img0,borderwidth=0,
                                highlightthickness=0,relief="flat", command=self.getEnviarFormulario)
        self.registrar.place(x=411, y=527,width=177,height=46)
        self.ventana_formulario.mainloop()

    def getVentana(self):
        self.ventana_formulario = Toplevel()
        self.ventana_formulario.title("Formulario")
        self.obj_centrar.centrar_ventana(self.ventana_formulario, 600, 1000)
        self.ventana_formulario.configure(bg="#ffffff")
        self.ventana_formulario.resizable(0, 0)

    def accionVolver(self):
        self.ventana_formulario.destroy()

    def getEnviarFormulario(self):
        tupla = (self.nombre.get(), self.apellido.get(), self.email.get(), self.usuario.get(), self.contrasena.get())
        obj = self.obj_crud.crearUsuarios(tupla)
        if obj != None:
            messagebox.showinfo("Registro de usuario", "El usuario ha sido ingresado correctamente!")
            self.accionVolver()
        elif obj == None:
            messagebox.showinfo("Error", "Lo sentimos hubo un error, por favor intentelo de nuevo")
