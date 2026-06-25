from flask import Flask, request, jsonify
app = Flask(__name__) #registra rotas e incia o servidor

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///escola.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#cria o banco de dados
from database import db
db.init_app(app)

# cria tabela do banco
with app.app_context():
    db.create_all()

app.run(debug=True)

