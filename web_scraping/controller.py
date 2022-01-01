from tkinter.messagebox import showerror

class controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def save(self, url):
        """
        s'il y a un url lancer le thread sinon afficher un message d'erreur
        :param url:
        :return:
        """
        if url:
            self.view.button_url["state"] = "disabled"
            self.view.html_scrolledtext.delete(1.0, "end")

            th = self.model.Html(url)
            th.start()
            th.run()
            if th.erreur:
                showerror("Erreur", """Merci d'insérer un URL valide \nN'oubliez pas d'ajouter "http://" ou "https://" au début de l'URL""")
                self.view.button_url["state"] = "normal"
                th.erreur = False


            self.monitor(th)
        else:
            showerror("Erreur", "merci d'insérer un URL")

    def monitor(self, thread):
        """
        attendre le téléchargement du fichier html
        mettre le fichier html télécharger dans le champ scrolledtext
        :param thread:
        :return:
        """
        if thread.is_alive():
            self.view.after(100, lambda: self.monitor(thread))
        else:
            self.view.html_scrolledtext["state"] = "normal"
            self.view.html_scrolledtext.insert(1.0, thread.html)
            self.view.html_scrolledtext["state"] = "disabled"
            self.view.button_url["state"] = "normal"

    def chercher(self, balise=None, attribut=None, text=None):
        html = self.view.html_scrolledtext.get(1.0, "end")
        #chercher par balise
        if not attribut and not text and balise:
            result1 = self.model.Html.recherche_balise(html, balise)
            if result1:
                self.succes()
            else:
                self.echec()
        # chercher par balise et attribut
        elif attribut and not text and balise:
            result2 = self.model.Html.recherche_balise_attribut(html, balise, attribut)
            if result2:
                self.succes()
            else:
                self.echec()
        # chercher par attribut
        elif attribut and not text and not balise:
            result3 = self.model.Html.recherche_attribut(html, attribut)
            if result3:
                self.succes()
            else:
                self.echec()
        # chercher par texte
        elif not attribut and text and not balise:
            result4 = self.model.Html.recherche_texte(html, text)
            if result4:
                self.succes()
            else:
                self.echec()
        # chercher par texte, balise et attribut
        elif attribut and text and balise:
            result5 = self.model.Html.recherche_balise_attribut_texte(html, balise, attribut, text)
            if result5:
                self.succes()
            else:
                self.echec()
        # chercher par texte et attribut
        elif attribut and text and not balise:
            result6 = self.model.Html.recherche_attribut_texte(html, attribut, text)
            if result6:
                self.succes()
            else:
                self.echec()
        # chercher par balise et par texte
        elif not attribut and text and balise:
            result7 = self.model.Html.recherche_balise_texte(html, balise, text)
            if result7:
                self.succes()
            else:
                self.echec()
    def succes(self):
        """
        recherche effecuée avec succes
        :return:
        """
        self.view.message_label_var.set("""La recherche a été efféctué avec succés \nMerci de cliquer sur "Consulter la recherche" pour voir le résultat """)
        self.view.message_label["foreground"] = "green"
        self.view.button_consulter["state"] = "normal"
        self.view.button_nouvelle_recherche["state"] = "normal"
        self.view.message_label.after(5000, lambda: self.view.message_label_var.set(" "))

    def echec(self):
        """
        erreur survenu lors de la recherche
        :return:
        """
        self.view.message_label_var.set("Une erreur a été survenu")
        self.view.message_label.after(5000, lambda: self.view.message_label_var.set(" "))
        self.view.message_label["foreground"] = "red"
        self.view.button_consulter["state"] = "disabled"
        self.view.button_nouvelle_recherche["state"] = "disabled"

    def open(self):
        self.model.Html.open_file()
