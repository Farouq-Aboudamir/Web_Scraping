import tkinter as tk

from View import view
from controller import controller
import Model

class App(tk.Tk):
    def __init__(self, model, view, controller):
        super().__init__()

        #configuration de l'application
        self.title("Web Scraping")
        self.geometry("445x615")
        self.resizable(False, False)

        #model
        self.model = model

        #mettre le conteneur principal
        self.view = view(self)
        self.view.grid(column=0, row=0, sticky=tk.NSEW)

        #controller
        self.controller = controller(self.view, self.model)
        self.view.set_controller(self.controller)


if __name__ == '__main__':
    app = App(Model, view, controller)
    app.mainloop()


