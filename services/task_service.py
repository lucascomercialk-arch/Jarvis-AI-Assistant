tarefas = []

def adicionar_tarefa(texto):
    nova_tarefa = {
        "texto": texto,
        "concluida": False
    }
    tarefas.append(nova_tarefa)
    return nova_tarefa

def listar_tarefas():
    return tarefas