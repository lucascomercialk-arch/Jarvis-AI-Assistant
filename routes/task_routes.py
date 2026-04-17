from flask import Blueprint, jsonify, request
from services.task_service import (
    adicionar_tarefa,
    listar_tarefas,
    concluir_tarefa,
    remover_tarefa,
    tarefas_do_dia,
    tarefas_priorizadas,
    proxima_acao
)

task_bp = Blueprint('tasks', __name__)

@task_bp.route('/proxima', methods=['GET'])
def proxima():
    return jsonify({"msg": proxima_acao()})

@task_bp.route('/tarefas/prioridade', methods=['GET'])
def get_prioridade():
    return jsonify(tarefas_priorizadas())

@task_bp.route('/tarefas/hoje', methods=['GET'])
def get_tarefas_hoje():
    return jsonify(tarefas_do_dia())

@task_bp.route('/tarefas', methods=['GET'])
def get_tarefas():
    return jsonify(listar_tarefas())

@task_bp.route('/tarefas', methods=['POST'])
def criar_tarefa():
    dados = request.get_json()
    texto = dados.get('texto', '').strip()
    prioridade = dados.get('prioridade', 'media')

    if not texto:
        return jsonify({"erro": "Texto da tarefa vazio"}), 400

    tarefa = adicionar_tarefa(texto, prioridade)
    return jsonify(tarefa), 201

@task_bp.route('/tarefas/<int:id>/concluir', methods=['PATCH'])
def concluir(id):
    tarefa = concluir_tarefa(id)
    if not tarefa:
        return jsonify({"erro": "Tarefa não encontrada"}), 404
    return jsonify(tarefa)

@task_bp.route('/tarefas/<int:id>', methods=['DELETE'])
def deletar_tarefa(id):
    removida = remover_tarefa(id)
    if not removida:
        return jsonify({"erro": "Tarefa não encontrada"}), 404
    return jsonify({"msg": "Tarefa removida com sucesso"})