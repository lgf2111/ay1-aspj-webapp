# Local imports
import datetime

# External imports
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, SelectField
from wtforms.validators import DataRequired, Length


class PaymentForm(FlaskForm):
    """Flask Payment Form"""

    # Field types followed by label and data validators
    CreditCardNumber = StringField(
            'Credit Card Number',
            [
                DataRequired(),
                Length(min=13, max=16, message="Invalid Credit Card Number")
            ]
        )
    CardHolder = StringField(
            'Credit Card Holder',
            [
            DataRequired(),
            Length(min=5,max=49, message="Invalid Length")
            ]
        )
    ExpirationDateMM = SelectField('Month', [DataRequired(),], choices=[('01', 'January'),
                                                                        ('02', 'Febuary'),
                                                                        ('03', 'March'),
                                                                        ('04', 'April'),
                                                                        ('05', 'May'),
                                                                        ('06', 'June'),
                                                                        ('07', 'July'),
                                                                        ('08', 'August'),
                                                                        ('09', 'September'),
                                                                        ('10', 'October'),
                                                                        ('11', 'November'),
                                                                        ('12', 'December')],
        )

    ExpirationDateYY = SelectField('Year', [DataRequired(),], choices= [('22', '2022'),
                                                                        ('23', '2023'),
                                                                        ('24', '2024'),
                                                                        ('25', '2025'),
                                                                        ('26', '2026')],
        )



    SecurityCode = StringField('Security Code',
            [
            DataRequired(),
            Length(min=3, max=3, message="Length should be 3 digits")
            ]
        )

    Amount = DecimalField( 'Amount',
            [
            DataRequired()
            ],
            places=2
        )

    submit = SubmitField('Pay')