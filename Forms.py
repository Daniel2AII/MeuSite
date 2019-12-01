from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateTimeField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class FormPacient(FlaskForm):
    username = StringField('USUÁRIO', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('E-MAIL', validators=[DataRequired(), Email()])
    age = DateTimeField('IDADE', validators=[DataRequired()])
    genre = StringField('GÊNERO', validators=[DataRequired()])
    password = PasswordField('SENHA', validators=[DataRequired()])
    confirm_password = PasswordField('COMFIRMAR SENHA', validators=[DataRequired(), EqualTo('password')])

class Respostas(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired(), Length(min=5, max=50)])
    resp1 = BooleanField('Resposta 1', validators=[DataRequired()])
    resp2 = BooleanField('Resposta 2', validators=[DataRequired()])
    resp3 = BooleanField('Resposta 3', validators=[DataRequired()])
    resp4 = BooleanField('Resposta 4', validators=[DataRequired()])
    resp5 = BooleanField('Resposta 5', validators=[DataRequired()])
    resp6 = BooleanField('Resposta 6', validators=[DataRequired()])
    resp7 = BooleanField('Resposta 7', validators=[DataRequired()])
    resp8 = BooleanField('Resposta 8', validators=[DataRequired()])
    resp_consulta = BooleanField('Consultado', validators=[DataRequired()])
    Q_tempo = DateTimeField('Quantidade de tempo', validators=[DataRequired()])