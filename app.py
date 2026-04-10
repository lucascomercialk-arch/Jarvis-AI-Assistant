from flask import Flask, jsonify, render_template

app =  Flask(__name__)
@app.route('/')
def home():
    return render_template('dashboard.hyml')

@app.route('/')
def home():
    return "Jarvis está online"

@app.route('/status')
def status():
    return jsonify({"status": "ok", "msg": "Jarvis funcionando"})

if __name__ == '__main__':
    app.run(debug=True)