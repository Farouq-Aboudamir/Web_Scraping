import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import showerror
import re

class view(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # label_url
        self.label_url = ttk.Label(self, text="URL : ")
        self.label_url.grid(column=0, row=0, sticky=tk.W, padx=10, pady=10)

        # entry_url
        self.entry_url_var = tk.StringVar()
        self.entry_url = ttk.Entry(self, textvariable=self.entry_url_var, width=48)
        self.entry_url.grid(column=1, row=0, sticky=tk.EW, columnspan=5, pady=10)

        # button_url
        self.button_url = ttk.Button(self, text="Télécharger", command=self.save_url)
        self.button_url.grid(column=6, row=0, columnspan=2, sticky=tk.E, padx=10, pady=10)

        # html_scrolledtext
        self.html_scrolledtext = ScrolledText(self, height=10, width=50, state="disabled")
        self.html_scrolledtext.grid(column=0, row=1, columnspan=8, padx=10)

        # chercher_par--------------------------------
        self.chercher_par = ttk.Labelframe(self, text="chercher par")
        self.chercher_par.grid(column=0, row=2, sticky=tk.EW, columnspan=8, padx=10)

        # balise
        self.balise_var = tk.StringVar(value="inchecked")
        self.balise = ttk.Checkbutton(self.chercher_par, text="Balise", variable=self.balise_var, onvalue="balise", offvalue="inchecked", width=10, command=self.active_balise, state="disabled")
        self.balise.grid(column=0, row=0, padx=10)

        # texte
        self.texte_var = tk.StringVar(value="inchecked")
        self.texte = ttk.Checkbutton(self.chercher_par, text="Texte", variable=self.texte_var, onvalue="texte",offvalue="inchecked", width=10, command=self.active_texte, state="disabled")
        self.texte.grid(column=1, row=0, pady=10)

        # attribut
        self.attribut_var = tk.StringVar(value="inchecked")
        self.attribut = ttk.Checkbutton(self.chercher_par, text="Attribut", variable=self.attribut_var,onvalue="attribut", offvalue="inchecked", width=10, command=self.active_attribut, state="disabled")
        self.attribut.grid(column=2, row=0, padx=10)

        # configurer -----------------------------------
        self.configurer = ttk.Labelframe(self, text="configuration")
        self.configurer.grid(column=0, row=3, sticky=tk.EW, columnspan=8, padx=10, ipady=10)
        self.configurer.columnconfigure(0, weight=1)
        self.configurer.columnconfigure(1, weight=5)

        # balise_config_label
        self.balise_config_label = ttk.Label(self.configurer, text="Balise : ")
        self.balise_config_label.grid(column=0, row=0, sticky=tk.W, padx=10, pady=10)

        # balise_combobox
        self.balise_combobox_var = tk.StringVar()
        self.balise_combobox_value = ("choisir une balise", "body", "table", "span", "div", "ul", "ol", "li", "td", "p", "a")
        self.balise_combobox = ttk.Combobox(self.configurer, values=self.balise_combobox_value, textvariable=self.balise_combobox_var, state="disabled")
        self.balise_combobox.set("choisir une balise")
        self.balise_combobox.grid(column=1, row=0, sticky=tk.EW, padx=10, pady=10)

        # separator1
        self.sep1 = ttk.Separator(self.configurer, orient="horizontal")
        self.sep1.grid(column=0, row=1, padx=10, sticky=tk.EW, columnspan=2)

        # texte_config_label
        self.texte_config_label = ttk.Label(self.configurer, text="Texte : ")
        self.texte_config_label.grid(column=0, row=2, sticky=tk.W, padx=10, pady=10)

        # texte_combobox
        self.texte_combobox_var = tk.StringVar()
        self.texte_combobox_value = ("choisir une option", "Commence par", "Commence par - Termine par", "Termine par")
        self.texte_combobox = ttk.Combobox(self.configurer, values=self.texte_combobox_value,textvariable=self.texte_combobox_var, state="disabled")
        self.texte_combobox.set("choisir une option")
        self.texte_combobox.bind('<<ComboboxSelected>>', lambda _: self.active_commence_termine())
        self.texte_combobox.grid(column=1, row=2, sticky=tk.EW, padx=10, pady=10)

        # commence_par
        self.commence_par = ttk.Label(self.configurer, text="Commence par : ")
        self.commence_par.grid(column=0, row=3, sticky=tk.W, padx=10)

        # commence_par_entry
        self.commence_par_entry_var = tk.StringVar()
        self.commence_par_entry = ttk.Entry(self.configurer, textvariable=self.commence_par_entry_var, state="disabled")
        self.commence_par_entry.grid(column=1, row=3, sticky=tk.EW, padx=10)

        # termine_par
        self.termine_par = ttk.Label(self.configurer, text="Termine par : ")
        self.termine_par.grid(column=0, row=4, sticky=tk.W, padx=10, pady=10)

        # termine_par_entry
        self.termine_par_entry_var = tk.StringVar()
        self.termine_par_entry = ttk.Entry(self.configurer, textvariable=self.termine_par_entry_var, state="disabled")
        self.termine_par_entry.grid(column=1, row=4, sticky=tk.EW, padx=10, pady=10)

        # separator2
        self.sep2 = ttk.Separator(self.configurer, orient="horizontal")
        self.sep2.grid(column=0, row=5, padx=10, sticky=tk.EW, columnspan=2)

        # attribut_config_label
        self.attribut_config_label = ttk.Label(self.configurer, text="Attribut : ")
        self.attribut_config_label.grid(column=0, row=6, sticky=tk.W, padx=10, pady=10)

        # attribut_combobox
        self.attribut_combobox_var = tk.StringVar()
        self.attribut_combobox_value = ("choisir un attribut", "class", "id")
        self.attribut_combobox = ttk.Combobox(self.configurer, values=self.attribut_combobox_value,textvariable=self.attribut_combobox_var, state="disabled")
        self.attribut_combobox.set("choisir un attribut")
        self.attribut_combobox.grid(column=1, row=6, sticky=tk.EW, padx=10, pady=10)

        # attribut_valeur_label
        self.attribut_valeur_label = ttk.Label(self.configurer, text="Valeur d'attribut : ")
        self.attribut_valeur_label.grid(column=0, row=7, sticky=tk.W, padx=10)

        # attribut_valeur_entry
        self.attribut_valeur_entry_var = tk.StringVar()
        self.attribut_valeur_entry = ttk.Entry(self.configurer, textvariable=self.attribut_valeur_entry_var, state="disabled")
        self.attribut_valeur_entry.grid(column=1, row=7, sticky=tk.EW, padx=10)

        # button_chercher
        self.button_chercher = ttk.Button(self, text="Chercher", command=self.chercher, state="disabled")
        self.button_chercher.grid(column=0, row=4, columnspan=2, sticky=tk.EW, padx=10, pady=10)

        # button_consulter
        self.button_consulter = ttk.Button(self, text="Consulter la recherche", state="disabled", command=self.open_file)
        self.button_consulter.grid(column=2, row=4, columnspan=3, sticky=tk.EW, pady=10)

        # button_nouvelle_recherche
        self.button_nouvelle_recherche = ttk.Button(self, text="Nouvelle recherche", state="disabled", command=self.new_search)
        self.button_nouvelle_recherche.grid(column=5, row=4, columnspan=3, sticky=tk.EW, padx=10, pady=10)

        # message_label
        self.message_label_var = tk.StringVar()
        self.message_label = ttk.Label(self, textvariable=self.message_label_var, relief=tk.SOLID, anchor=tk.CENTER)
        self.message_label.grid(column=0, row=5, padx=10, sticky=tk.EW, ipady=10, columnspan=8)

        self.controller = None

    def set_controller(self, controller):
        """
        permet d'insérer un controller
        :param controller:
        :return:
        """
        self.controller = controller

    def save_url(self):
        """
        télecharger le fichier html
        :return:
        """
        self.html_scrolledtext.delete(1.0, "end")
        if self.controller:
            self.balise["state"] = "normal"
            self.attribut["state"] = "normal"
            self.texte["state"] = "normal"
            self.button_chercher["state"] = "normal"

            self.controller.save(self.entry_url_var.get())



    def active_balise(self):
        """
        permet d'activer la configuration du champ balise
        :return:
        """
        if self.balise_var.get() == "balise":
            self.balise_combobox["state"] = "readonly"
        else:
            self.balise_combobox["state"] = "disabled"
            self.balise_combobox.set("choisir une balise")

    def active_texte(self):
        """
        permet d'activer la configuration du champ texte
        :return:
        """
        if self.texte_var.get() == "texte":
            self.texte_combobox["state"] = "readonly"
        else:
            self.commence_par_entry_var.set("")
            self.termine_par_entry_var.set("")
            self.texte_combobox["state"] = "disabled"
            self.texte_combobox.set("choisir une option")
            self.commence_par_entry["state"] = "disabled"
            self.termine_par_entry["state"] = "disabled"

    def active_attribut(self):
        """
        permet d'activer la configuration du champ attribut
        :return:
        """
        if self.attribut_var.get() == "attribut":
            self.attribut_combobox["state"] = "readonly"
            self.attribut_valeur_entry["state"] = "normal"
        else:
            self.attribut_combobox["state"] = "disabled"
            self.attribut_combobox.set("choisir un attribut")
            self.attribut_valeur_entry["state"] = "disabled"
            self.attribut_valeur_entry_var.set("")

    def active_commence_termine(self):
        """
        permet d'activer/désactiver les champs de configuration "commence par" et "termine par"
        :return:
        """
        if self.texte_combobox_var.get() == "Commence par":
            self.commence_par_entry["state"] = "normal"
            self.termine_par_entry["state"] = "disabled"
            self.termine_par_entry_var.set("")
        elif self.texte_combobox_var.get() == "Termine par":
            self.commence_par_entry["state"] = "disabled"
            self.termine_par_entry["state"] = "normal"
            self.commence_par_entry_var.set("")
        elif self.texte_combobox_var.get() == "Commence par - Termine par":
            self.commence_par_entry["state"] = "normal"
            self.termine_par_entry["state"] = "normal"
        else:
            self.commence_par_entry["state"] = "disabled"
            self.termine_par_entry["state"] = "disabled"
            self.commence_par_entry_var.set("")
            self.termine_par_entry_var.set("")

    def controle_attribut(self):
        """
        controle de la valeur de l'attribut
        :return:
        """
        if self.attribut_combobox_var.get() == "choisir un attribut":
            if re.search("^[ ]{1,}$", self.attribut_valeur_entry_var.get()) is not None or self.attribut_valeur_entry_var.get() == "":
                showerror("Erreur", "Merci de choisir un attribut et d'insérer une valeur d'attribut")
                attribut = " "
                return True, attribut
            else:
                showerror("Erreur", "Merci de choisir un attribut")
                attribut = " "
                return True, attribut
        else:
            if re.search("^[ ]{1,}$", self.attribut_valeur_entry_var.get()) is not None or self.attribut_valeur_entry_var.get() == "":
                showerror("Erreur", "Merci d'insérer une valeur d'attribut")
                attribut = " "
                return True, attribut
            else:
                attribut = {self.attribut_combobox_var.get(): self.attribut_valeur_entry_var.get()}
                return False, attribut

    def controle_texte(self):
        """
        controle de la valeur du texte
        :return:
        """
        if self.texte_combobox_var.get() == "choisir une option":
            showerror("Erreur", "Merci de choisir une option")
            text = " "
            return True, text

        if self.texte_combobox_var.get() == "Commence par":
            if re.search("^[ ]{1,}$", self.commence_par_entry_var.get()) is not None or self.commence_par_entry_var.get() == "":
                showerror("Erreur", "Merci d'insérer une valeur dans le champ 'Commence par'")
                text = " "
                return True, text
            else:
                text = f"^{self.commence_par_entry_var.get()}"
                return False, text

        if self.texte_combobox_var.get() == "Termine par":
            if re.search("^[ ]{1,}$", self.termine_par_entry_var.get()) is not None or self.termine_par_entry_var.get() == "":
                showerror("Erreur", "Merci d'insérer une valeur dans le champ 'Termine par'")
                text = " "
                return True, text
            else:
                text = f"{self.termine_par_entry_var.get()}$"
                return False, text

        if self.texte_combobox_var.get() == "Commence par - Termine par":
            if (re.search("^[ ]{1,}$", self.commence_par_entry_var.get())  is not None or self.commence_par_entry_var.get() == "") and (re.search("^[ ]{1,}$", self.termine_par_entry_var.get()) is not None or self.termine_par_entry_var.get() == ""):
                showerror("Erreur", "Merci d'insérer une valeur dans les champs 'Commence par' et 'Termine par'")
                text = " "
                return True, text
            elif re.search("^[ ]{1,}$", self.commence_par_entry_var.get()) is not None or self.commence_par_entry_var.get() == "":
                showerror("Erreur", "Merci d'insérer une valeur dans le champ 'Commence par'")
                text = " "
                return True, text
            elif re.search("^[ ]{1,}$", self.termine_par_entry_var.get()) is not None or self.termine_par_entry_var.get()== "":
                showerror("Erreur", "Merci d'insérer une valeur dans le champ 'Termine par'")
                text = " "
                return True, text
            else:
                text = {"commencer": f"^{self.commence_par_entry_var.get()}",
                        "terminer": f"{self.termine_par_entry_var.get()}$"}
                return False, text

    def controle_balise(self):
        if self.balise_combobox_var.get() == "choisir une balise":
            showerror("Erreur", "merci de choisir une balise")
            balise = " "
            return True, balise
        else:
            balise = self.balise_combobox_var.get()
            return False, balise

    def chercher(self):
        """
        appelle la methode chercher() du controller
        :return:
        """
        if len(self.html_scrolledtext.get(0.1, "end")) != 1:
            if self.balise_var.get() == "balise":
                erreur_balise, balise = self.controle_balise()
            if self.attribut_var.get() == "attribut":
                erreur_attribut, attribut = self.controle_attribut()
            if self.texte_var.get() == "texte":
                erreur_texte, text = self.controle_texte()

            # chercher balise
            if self.balise_var.get() == "balise" and self.texte_var.get() == "inchecked" and self.attribut_var.get() == "inchecked":
                if not erreur_balise:
                    self.controller.chercher(balise=balise)
            # chercher balise et attribut
            elif self.balise_var.get() == "balise" and self.texte_var.get() == "inchecked" and self.attribut_var.get() == "attribut":
                 if not erreur_attribut and not erreur_balise:
                    self.controller.chercher(balise=balise, attribut=attribut)
            # chercher attribut
            elif self.balise_var.get() == "inchecked" and self.texte_var.get() == "inchecked" and self.attribut_var.get() == "attribut":
                if not erreur_attribut:
                    self.controller.chercher(attribut=attribut)
            # chercher texte
            elif self.balise_var.get() == "inchecked" and self.texte_var.get() == "texte" and self.attribut_var.get() == "inchecked":
                if not erreur_texte:
                        self.controller.chercher(text=text)
            # chercher par texte, balise et attribut
            elif self.balise_var.get() == "balise" and self.texte_var.get() == "texte" and self.attribut_var.get() == "attribut":
                if not erreur_texte and not erreur_attribut and not erreur_balise:
                        self.controller.chercher(balise=balise, attribut=attribut, text=text)
            # chercher par texte et attribut
            elif self.balise_var.get() == "inchecked" and self.texte_var.get() == "texte" and self.attribut_var.get() == "attribut":
                if not erreur_texte and not erreur_attribut:
                        self.controller.chercher(attribut=attribut, text=text)
            # chercher par balise et par texte
            elif self.balise_var.get() == "balise" and self.texte_var.get() == "texte" and self.attribut_var.get() == "inchecked":
                if not erreur_texte and not erreur_balise:
                        self.controller.chercher(balise=balise, text=text)
            #cas d'erreur
            elif self.balise_var.get() == "inchecked" and self.texte_var.get() == "inchecked" and self.attribut_var.get() == "inchecked":
                showerror("Erreur", "merci de choisir au moins une option de recherche : \n'Texte', 'Attribut' ou 'Balise'")
        else:
            self.message_label["foreground"] = "red"
            self.message_label_var.set("merci d'insérer un url valide")



    def new_search(self):
        # vider l' entry_url
        self.entry_url_var.set(" ")
        # vider le html_scrolledtext
        self.html_scrolledtext["state"] = "normal"
        self.html_scrolledtext.delete("1.0", "end")
        self.html_scrolledtext["state"] = "disabled"
        # desactiver les options de recherche
        self.balise["state"] = "disabled"
        self.texte["state"] = "disabled"
        self.attribut["state"] = "disabled"
        self.balise_var.set("inchecked")
        self.texte_var.set("inchecked")
        self.attribut_var.set("inchecked")
        # désactiver la balise
        self.balise_combobox["state"] = "disabled"
        self.balise_combobox.set("choisir une balise")
        # désactiver le text
        self.commence_par_entry_var.set("")
        self.termine_par_entry_var.set("")
        self.texte_combobox["state"] = "disabled"
        self.texte_combobox.set("choisir une option")
        self.commence_par_entry["state"] = "disabled"
        self.termine_par_entry["state"] = "disabled"
        self.commence_par_entry["state"] = "disabled"
        self.termine_par_entry["state"] = "disabled"
        self.commence_par_entry_var.set("")
        self.termine_par_entry_var.set("")
        # disactiver l'attribut
        self.attribut_combobox["state"] = "disabled"
        self.attribut_combobox.set("choisir un attribut")
        self.attribut_valeur_entry["state"] = "disabled"
        self.attribut_valeur_entry_var.set("")
        # disactiver le bouton consulter la recherche
        self.button_consulter["state"] = "disabled"


    def open_file(self):
        """
        appelle la methode open() du controller
        :return:
        """
        self.controller.open()