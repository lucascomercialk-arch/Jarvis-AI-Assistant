from flask import Flask, jsonify 

@app.route('/status')
def status():
    return jsonify({"status": "ok", "msg": "Jarvis funcionando"})


app =  Flask(__name__)

@app.route('/')
def home():
    return "Jarvis está online"

if __name__ == '_main_':
    app.run(debug=True)