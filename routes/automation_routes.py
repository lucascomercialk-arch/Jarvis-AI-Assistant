from flask import Blueprint, jsonify
from services.automation_service import(
    abrir_modo_clinica,
    abrir_modo_faculdade,
    abrir_modo_projeto,
    abrir_modo_vendas
)

automation_bp = Blueprint('automation',__name__)

@automation_bp.route('/status')
def status():
    return jsonify({"status": "ok", "msg": "Jarvis funcionando"})

@automation_bp.route('/comando/ola')
def ola():
    return jsonify({"msg":"Olá chefe"})

@automation_bp.route('/abrir')
def abrir():
    return jsonify({"msg":"Comando Executado"})

@automation_bp.route('/modo/clinica')
def modo_clinica():
    msg = abrir_modo_clinica()
    return jsonify({"msg": msg})

@automation_bp.route('/modo/faculdae')
def modo_faculdade():
    msg = abrir_modo_faculdade()
    return jsonify({"msg": msg})

@automation_bp.route('/modo/projeto')
def modo_projeto():
    msg = abrir_modo_projeto()
    return jsonify({"msg": msg})

@automation_bp.route('/modo/vendas')
def modo_vendas():
    msg = abrir_modo_vendas()
    return jsonify({"msg": msg})
