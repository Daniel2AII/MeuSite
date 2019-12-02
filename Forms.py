from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateTimeField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class FormPacient(FlaskForm):
    username = StringField('USUÁRIO', validators=[DataRequired(), Length(min=2, max=20)])
    age = StringField('IDADE', validators=[DataRequired()])
    genre = StringField('GÊNERO', validators=[DataRequired()])
    email = StringField('E-MAIL', validators=[DataRequired(), Email()]) 
    password = PasswordField('SENHA', validators=[DataRequired()])
    confirm_password = PasswordField('COMFIRMAR SENHA', validators=[DataRequired(), EqualTo('password')])
    button = SubmitField('Cadastrar')