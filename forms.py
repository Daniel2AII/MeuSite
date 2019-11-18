from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BoleanField, DataRequired, Length, Email, EqualTo, DateTimeField

class FormPacient(FlaskForm):
    usernameP = StringField('Usuário', validators=[DataRequired(), Length(min=2, max=20)])
    nameP = StringField('Nome', validators=[DataRequired(), Length(min=2, max=100)])
    emailP = StringField('E-mail', validators=[DataRequired(), Email()])
    birthday = DateTimeField('Data de Nascimento', validators=[DataRequired()])
    passwordP = PasswordField('Senha', validators=[DataRequired()])
    confirm_passwordP = PasswordField('Repete Senha', validators[DataRequired(), EqualTo('password')])