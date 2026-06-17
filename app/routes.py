from flask import Blueprint, render_template, request
from app.models import User
from app.extensions import db
import hashlib

routes_bp = Blueprint('routes', __name__, template_folder='./templates')

def hash(txt):
  hash_obj = hashlib.sha3_256(txt.encode('utf-8'))
  return hash_obj.hexdigest()

@routes_bp.route('/')
def home():
  return 'StudyFlow funcionando !'


@routes_bp.route('/register', methods=['GET', 'POST'])
def registrar():
  if request.method == 'GET':
    return render_template('registrar.html')
  elif request.method == 'POST':
    nome = request.form.get('nomeForm')
    email = request.form.get('emailForm')
    senha = request.form.get('senhaForm')
    conf_senha = request.form.get('confSenhaForm')
    msg = ''

    if len(senha) < 8:
      msg = 'Senha precisa ter mais de 8 caracteres'

    elif senha != conf_senha:
      msg = 'Senhas não conferem'

    if msg:
        return render_template('registrar.html', alerta=msg)
    

    existing_user = db.session.query(User).filter_by(email=email).first()
    if existing_user:
      msg = 'Email já cadastro'
      return render_template('registrar.html', alerta=msg)

    new_user = User(username=nome, email=email, password=hash(senha))
    db.session.add(new_user)
    db.session.commit()
    return('Usuario criado')