from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BoleanField, DataRequired, Length, Email, EqualTo, DateTimeField

class FormPacient(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    birthday = DateTimeField('Data de Nascimento', validators=[DataRequired()])
    genre = StringField('Gênero', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    confirm_password = PasswordField('Repete Senha', validators[DataRequired(), EqualTo('password')])