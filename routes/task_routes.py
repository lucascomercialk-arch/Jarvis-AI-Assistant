from flask import Blueprint, jsonify, request
from services.task_service import adicionar_tarefa, listar_tarefas

task_bp = Blueprint('tasks',__name__)

@task_bp.route('/tarefas',methods=['GET'])
def get_tarefa():
    return jsonify(listar_tarefas())

@task_bp.route('/tarefas', methods=['POST'])
def criar_tarefa():
    dados = request.get_json()
    texto = dados.get('texto', '').strip()

    if not texto:
        return jsonify({"erro": "Texto da tarefa vazio"}), 400
    
    tarefa = adicionar_tarefa(texto)
    return jsonify(tarefa), 201