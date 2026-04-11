from flask import Flask, jsonify, render_template

app =  Flask(__name__)

@app.route('/')
def home():
    return render_template('dashboard.html')


@app.route('/status')
def status():
    return jsonify({"status": "ok", "msg": "Jarvis funcionando"})

@app.route('/abrir')
def abrir():
    return jsonify({"msg":"Comando Executado"})

if __name__ == '__main__':
    app.run(debug=True)