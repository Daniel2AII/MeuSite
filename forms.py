from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BoleanField
from wtforms import DataRequired, Length, Email, EqualTo

class FormDoctor(FlaskForm):
    usernameD = StringField('Usuário', validators=[DataRequired(), Length(min=2, max=20)])
    nameD = StringField('Nome', validators=[DataRequired(), Length(min=2, max=100)])
    emailD = StringField('E-mail', validators=[DataRequired(), Email()])
    passwordD = PasswordField('Senha', validators=[DataRequired()])
    confirm_passwordD = PasswordField('Repete Senha', validators[DataRequired(), EqualTo('password')])

class FormPacient(FlaskForm):
    usernameP = StringField('Usuário', validators=[DataRequired(), Length(min=2, max=20)])
    nameP = StringField('Nome', validators=[DataRequired(), Length(min=2, max=100)])
    emailP = StringField('E-mail', validators=[DataRequired(), Email()])
    passwordP = PasswordField('Senha', validators=[DataRequired()])
    confirm_passwordP = PasswordField('Repete Senha', validators[DataRequired(), EqualTo('password')])