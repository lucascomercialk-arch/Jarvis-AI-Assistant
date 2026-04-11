tarefas = []

def detectar_categoria(texto):
    texto  = texto.lower()

    if "estudar" in texto or "prova" in texto:
        return "faculdade"
    elif "cliente" in texto or "vender" in texto or "proposta" in texto:
        return "vendas"
    elif "projeto" in texto  or "codigo" in texto  or "site" in texto:
        return "projeto"
    elif "exame" in texto  or "empresa" in texto:
        return "clinica"
    else:
        return "geral"
    

def adicionar_tarefa(texto):
    categoria = detectar_categoria(texto)

    nova_tarefa = {
        "texto": texto,
        "concluida": False,
        "categoria": categoria
    }

    tarefas.append(nova_tarefa)
    return nova_tarefa

def listar_tarefas():
    return tarefas