from threading import Thread
import os
import re

import requests
from bs4 import BeautifulSoup

class Html(Thread):
    def __init__(self, url):
        Thread.__init__(self)
        self.url = url
        self.html = ""

        self.erreur = False

    def run(self):
        try:
            self.erreur = False
            r = requests.get(self.url)
            self.html = r.text
        except:
            self.erreur = True


    def set_erreur(self):
        return self.erreur

    # chercher par balise
    @staticmethod
    def recherche_balise(html, balise):
        """
        recherche ce qui correspond à la balise demandée
        insérer le résultat dans le fichier "rechercher.txt"
        :param html:
        :param balise:
        :return:
        """
        soup = BeautifulSoup(html, 'html.parser')
        try:
            with open("recherche.txt", "w", encoding="utf_8") as fichier:
                for element in soup.find_all(balise):
                    fichier.write(f"{element} \n")
        except:
            return False
        else:
            return True

    # chercher par texte
    @staticmethod
    def recherche_texte(html, text):
        """
        recherche ce qui correspond au texte demandée
        insérer le résultat dans le fichier "rechercher.txt"
        :param html:
        :param text:
        :return:
        """
        soup = BeautifulSoup(html, 'html.parser')
        try:
            with open("recherche.txt", "w", encoding="utf_8") as fichier:
                if isinstance(text, dict):
                    for element in soup.find_all(string=re.compile(text["commencer"])):
                        if re.search(text["terminer"], element) is not None:
                            fichier.write(f"{element} \n")
                else:
                    for element in soup.find_all(string=re.compile(text)):
                        fichier.write(f"{element} \n")
        except:
            return False
        else:
            return True

    # chercher par balise et par texte
    @staticmethod
    def recherche_balise_texte(html,balise, text):
        """
        recherche ce qui correspond à la balise et au texte demandés
        insérer le résultat dans le fichier "rechercher.txt"
        :param html:
        :param balise:
        :param text:
        :return:
        """
        soup = BeautifulSoup(html, 'html.parser')
        try:
            with open("recherche.txt", "w", encoding="utf_8") as fichier:
                if isinstance(text, dict):
                    for element in soup.find_all(balise, string=re.compile(text["commencer"])):
                        if re.search(text["terminer"], element) is not None:
                            fichier.write(f"{element} \n")
                else:
                    for element in soup.find_all(balise, string=re.compile(text)):
                        fichier.write(f"{element} \n")
        except:
            return False
        else:
            return True

    @staticmethod
    def recherche_attribut(html, attribut):
        """
        recherche ce qui correspond à l'attribut demandé
        insérer le résultat dans le fichier "rechercher.txt"
        :param html:
        :param attribut:
        :return:
        """
        soup = BeautifulSoup(html, 'html.parser')
        try:
            with open("recherche.txt", "w", encoding="utf_8") as fichier:
                for key in attribut.keys():
                    if key == "class":
                        elements = soup.find_all(class_=attribut["class"])
                    elif key == "id":
                        elements = soup.find_all(id=attribut["id"])
                    elif key == "choisir un attribut":
                        elements = soup.find_all(attrs=attribut["choisir un attribut"])
                for element in elements:
                    fichier.write(f"{element} \n")
        except:
            return False
        else:
            return True

    @staticmethod
    def recherche_balise_attribut(html, balise, attribut):
        """
        recherche ce qui correspond à la balise et l'attribut demandés
        insérer le résultat dans le fichier "rechercher.txt"
        :param html:
        :param balise:
        :param attribut:
        :return:
        """
        soup = BeautifulSoup(html, 'html.parser')
        try:
            with open("recherche.txt", "w", encoding="utf_8") as fichier:
                for key in attribut.keys():
                    if key == "class":
                        elements = soup.find_all(balise, class_=attribut["class"])
                    elif key == "id":
                        elements = soup.find_all(balise, id=attribut["id"])
                    elif key == "choisir un attribut":
                        elements = soup.find_all(balise, attribut["choisir un attribut"])
                for element in elements:
                    fichier.write(f"{element} \n")
        except:
            return False
        else:
            return True

    @staticmethod
    def recherche_balise_attribut_texte(html, balise, attribut, text):
        """
        recherche ce qui correspond à la balise, l'attribut et le texte demandés
        insérer le résultat dans le fichier "rechercher.txt"
        :param html:
        :param balise:
        :param attribut:
        :param text:
        :return:
        """
        soup = BeautifulSoup(html, 'html.parser')
        try:
            with open("recherche.txt", "w", encoding="utf_8") as fichier:
                for key in attribut.keys():
                    if key == "id":
                        if isinstance(text, dict):
                            for element in soup.find_all(balise, id=attribut["class"], string=re.compile(text["commencer"])):
                                if re.search(text["terminer"], element) is not None:
                                    fichier.write(f"{element} \n")
                        else:
                            for element in soup.find_all(balise, id=attribut["class"], string=re.compile(text)):
                                fichier.write(f"{element} \n")

                    elif key == "class":
                        if isinstance(text, dict):
                            for element in soup.find_all(balise, class_=attribut["class"], string=re.compile(text["commencer"])):
                                if re.search(text["terminer"], element) is not None:
                                    fichier.write(f"{element} \n")
                        else:
                            for element in soup.find_all(balise, class_=attribut["class"], string=re.compile(text)):
                                fichier.write(f"{element} \n")
                    elif key == "choisir un attribut":
                        if isinstance(text, dict):
                            for element in soup.find_all(balise, attribut["choisir un attribut"], string=re.compile(text["commencer"])):
                                if re.search(text["terminer"], element) is not None:
                                    fichier.write(f"{element} \n")
                        else:
                            for element in soup.find_all(balise, attribut["choisir un attribut"], string=re.compile(text)):
                                fichier.write(f"{element} \n")

        except:
            return False
        else:
            return True

    @staticmethod
    def recherche_attribut_texte(html, attribut, text):
        """
        recherche ce qui correspond à l'attribut et le texte demandés
        insérer le résultat dans le fichier "rechercher.txt"
        :param html:
        :param attribut:
        :param text:
        :return:
        """
        soup = BeautifulSoup(html, 'html.parser')
        try:
            with open("recherche.txt", "w", encoding="utf_8") as fichier:
                for key in attribut.keys():
                    if key == "id":
                        if isinstance(text, dict):
                            for element in soup.find_all(id=attribut["class"], string=re.compile(text["commencer"])):
                                if re.search(text["terminer"], element) is not None:
                                    fichier.write(f"{element} \n")
                        else:
                            for element in soup.find_all(id=attribut["class"], string=re.compile(text)):
                                fichier.write(f"{element} \n")

                    elif key == "class":
                        if isinstance(text, dict):
                            for element in soup.find_all(class_=attribut["class"], string=re.compile(text["commencer"])):
                                if re.search(text["terminer"], element) is not None:
                                    fichier.write(f"{element} \n")
                        else:
                            for element in soup.find_all(class_=attribut["class"], string=re.compile(text)):
                                fichier.write(f"{element} \n")
                    elif key == "choisir un attribut":
                        if isinstance(text, dict):
                            for element in soup.find_all(attribut["choisir un attribut"], string=re.compile(text["commencer"])):
                                if re.search(text["terminer"], element) is not None:
                                    fichier.write(f"{element} \n")
                        else:
                            for element in soup.find_all(attribut["choisir un attribut"], string=re.compile(text)):
                                fichier.write(f"{element} \n")

        except:
            return False
        else:
            return True


    @staticmethod
    def open_file():
        os.system("start recherche.txt")