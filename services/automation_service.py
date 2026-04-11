import webbrowser
import os



def modo_clinica():
    webbrowser.open("https://calendar.google.com")
    webbrowser.open("https://web.whatsapp.com")
    return "Modo Clinica Ativado"


def modo_faculdade():
    webbrowser.open("https://www.google.co")
    return  "Modo Faculdade Ativado"


def modo_projeto():
    os.startfile("C:\\Users\\Pichau\\Documents\\Projetos")
    webbrowser.open("https://github.com")
    return "Modo Projeto Ativado"


def modo_vendas():
    webbrowser.open("https://documento.google")
    return "Modo Vendas Ativado"