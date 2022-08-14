from flask import Flask
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User
import re 

password_errors = []
class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=12)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

    def validate_password(self, password):
        digit_error = re.search(r"\d", password.data) is None
        uppercase_error = re.search(r"[A-Z]", password.data) is None
        lowercase_error = re.search(r"[a-z]", password.data) is None
        symbol_error = re.search(r"[~!@#$%^&*()_+]", password.data) is None

        if digit_error:
            password_errors.append("At least 1 digit")
        if uppercase_error:
            password_errors.append('At least 1 uppercase')
        if lowercase_error:
            password_errors.append('At least 1 lowercase')
        if symbol_error:
            password_errors.append('At least 1 special character of the following ~!@#$%^&*()_+')

        if digit_error or uppercase_error or lowercase_error or symbol_error:
            raise ValidationError('Weak Password')
        


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class MfaForm(FlaskForm):
    otp = StringField('Enter OTP', validators=[DataRequired()])
    submit = SubmitField('Verify')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')


class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(), Length(min=12)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')


    def validate_password(self, password):
        digit_error = re.search(r"\d", password.data) is None
        uppercase_error = re.search(r"[A-Z]", password.data) is None
        lowercase_error = re.search(r"[a-z]", password.data) is None
        symbol_error = re.search(r"[~!@#$%^&*()_+]", password.data) is None

        if digit_error:
            password_errors.append("At least 1 digit")
        if uppercase_error:
            password_errors.append('At least 1 uppercase')
        if lowercase_error:
            password_errors.append('At least 1 lowercase')
        if symbol_error:
            password_errors.append('At least 1 special character of the following ~!@#$%^&*()_+')

        if digit_error or uppercase_error or lowercase_error or symbol_error:
            raise ValidationError('Weak Password')
