from flask import Flask, jsonify, render_template
from routes.automation_routes import automation_bp

app =  Flask(__name__)

app.register_blueprint(automation_bp)

@app.route('/')
def home():
    return render_template('dashboard.html')


# Modos Jarvis

if __name__ == '__main__':
    app.run(debug=True)