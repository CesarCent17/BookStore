from tkinter import *
from centrar import *
from views.formulario import *
from controllers.crud import *
from tkinter import messagebox
from views.menu_ventas import *


class Iniciar:
    def __init__(self):
        self.obj_crud = Crud()
        self.obj_centrar = Centro()
        self.getVentana()
        canvas = Canvas(self.ventana_login,bg="#ffffff",height=600,width=1000,bd=0,highlightthickness=0,relief="ridge")
        canvas.place(x=0, y=0)

        background_img = PhotoImage(file=f"C:/Users/PC/PycharmProjects/BookStore/multimedia/Iniciar/background.png")
        background = canvas.create_image(500.0, 300.0,image=background_img)

        entry0_img = PhotoImage(file=f"C:/Users/PC/PycharmProjects/BookStore/multimedia/Iniciar/img_textBox0.png")
        entry0_bg = canvas.create_image(500.0, 323.5,image=entry0_img)
        self.contrasena = Entry(self.ventana_login,bd=0,bg="#393e46",highlightthickness=0,
                             font=("Arial", 14), fg="white",show="*")
        self.contrasena.place(x=387, y=301,width=226,height=43)

        entry1_img = PhotoImage(file=f"C:/Users/PC/PycharmProjects/BookStore/multimedia/Iniciar/img_textBox1.png")
        entry1_bg = canvas.create_image(500.0, 237.5,image=entry1_img)
        self.usuario = Entry(self.ventana_login,bd=0,bg="#393e46",highlightthickness=0,
                                font=("Arial", 14),fg="white", )
        self.usuario.place(x=387, y=215,width=226,height=43)

        #Button ENTRAR
        img0 = PhotoImage(file=f"C:/Users/PC/PycharmProjects/BookStore/multimedia/Iniciar/img0.png")
        self.entrar = Button(self.ventana_login,image=img0,borderwidth=0,
                             highlightthickness=0,relief="flat", command= self.accionLogin)
        self.entrar.place(x=433, y=393,width=133,height=37)
        #Button REGISTRARTE
        img1 = PhotoImage(file=f"C:/Users/PC/PycharmProjects/BookStore/multimedia/Iniciar/img1.png")
        self.registrarte = Button(self.ventana_login,image=img1, borderwidth=0,
                                  highlightthickness=0,relief="flat", command=self.getFormulario)
        self.registrarte.place(x=837, y=509, width=141, height=42)
        self.ventana_login.mainloop()

    def getVentana(self):
        self.ventana_login = Tk()
        self.ventana_login.title("Book Store")
        self.obj_centrar.centrar_ventana(self.ventana_login, 600, 1000)
        # self.ventana_formulario.geometry("1000x600")
        self.ventana_login.configure(bg="#ffffff")
        self.ventana_login.resizable(0, 0)

    def getFormulario(self):
        obj = Formulario()
    def accionLogin(self):
        obj_usuario = self.obj_crud.autentificacionLogin(self.usuario.get(), self.contrasena.get())
        if obj_usuario != None:
            self.ventana_login.wm_state('withdrawn')
            obj_menu = MenuP(obj_usuario)
        elif obj_usuario == None:
            messagebox.showinfo("Error", "Usuario no existe")


execute = Iniciar()