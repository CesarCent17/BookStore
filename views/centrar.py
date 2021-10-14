class Centro:
    def centrar_ventana(self, obj, altura, ancho):
        x = int((obj.winfo_screenwidth() / 2) - (ancho / 2))
        y = int((obj.winfo_screenheight() / 2) - (altura / 2))
        obj.geometry(f"{ancho}x{altura}+{x}+{y}")
