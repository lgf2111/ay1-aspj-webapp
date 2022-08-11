from flask import Flask
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User
import re 


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
        
        # errors = []
        digit_error = re.search(r"\d", password.data) is None
        uppercase_error = re.search(r"[A-Z]", password.data) is None
        lowercase_error = re.search(r"[a-z]", password.data) is None
        symbol_error = re.search(r"[!@#$%^&*]", password.data) is None

        if digit_error or uppercase_error or lowercase_error or symbol_error:
            raise ValidationError('Your password should contain at least 1 digit, uppercase, lowercase and special characters of the following !@#$%^&*')
    # def uppercase_error(self, password):
    #     # errors = []
    #     uppercase_error = re.search(r"[A-Z]", password.data) is None
    #     lowercase_error = re.search(r"[a-z]", password.data) is None
    #     symbol_error = re.search(r"[!@#$%^&*]", password.data) is None

    #     if uppercase_error:
    #         raise ValidationError('At least 1 uppercase')

        # for error in [digit_error , uppercase_error, lowercase_error, symbol_error]:
        #     if error:
        #         errors.append(error)
        # if errors:
        #     raise ValidationError(errors)
        
        # if digit_error:
        #     errors.append('1 Digit')
        # if uppercase_error:
        #     errors.append('1 Uppercase')
        # if lowercase_error:
        #     errors.append('1 Lowercase')
        # if symbol_error:
        #     errors.append('1 Special Character')
        # for error in errors:
        #     raise ValidationError(error)
        


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
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')
