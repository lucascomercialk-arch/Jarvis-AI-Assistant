import json
from datetime import datetime

ARQUIVO = 'tarefas.json'

def tarefas_do_dia():
    tarefas = carregar_tarefas()
    hoje = datetime.now().strftime("%d/%m/%Y")

    return [
        t for t in tarefas
        if t["data_criacao"].startswith(hoje) and not t["concluida"]
    ]

def tarefas_atrasadas():
    tarefas = carregar_tarefas()
    hoje = datetime.now().strftime("%d/%m/%Y")

    return [
        t for t in tarefas
        if t["prazo"] and t["prazo"] < hoje and not t["concluida"]
    ]

def carregar_tarefas():
    try:
        with open(ARQUIVO, 'r') as f:
            return json.load(f)
    except:
        return []


def salvar_tarefas(tarefas):
    with open(ARQUIVO, 'w') as f:
        json.dump(tarefas, f, indent=4)


def gerar_id(tarefas):
    if not tarefas:
        return 1
    return max(t['id'] for t in tarefas) + 1


def detectar_categoria(texto):
    texto = texto.lower()

    if "estudar" in texto or "prova" in texto:
        return "faculdade"
    elif "cliente" in texto or "vender" in texto:
        return "vendas"
    elif "jarvis" in texto or "codigo" in texto:
        return "projeto"
    elif "clinica" in texto or "exame" in texto:
        return "clinica"
    else:
        return "geral"


def adicionar_tarefa(texto, prioridade="media"):
    tarefas = carregar_tarefas()

    nova = {
        "id": gerar_id(tarefas),
        "texto": texto,
        "concluida": False,
        "categoria": detectar_categoria(texto),
        "prioridade": prioridade,
        "data_criacao": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "prazo": None
    }

    tarefas.append(nova)
    salvar_tarefas(tarefas)

    return nova


def listar_tarefas():
    return carregar_tarefas()


def concluir_tarefa(id):
    tarefas = carregar_tarefas()

    for t in tarefas:
        if t['id'] == id:
            t['concluida'] = True
            salvar_tarefas(tarefas)
            return t

    return None


def remover_tarefa(id):
    tarefas = carregar_tarefas()

    novas = [t for t in tarefas if t['id'] != id]

    if len(novas) == len(tarefas):
        return False

    salvar_tarefas(novas)
    return True