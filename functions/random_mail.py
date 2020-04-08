import random
import string
import webbrowser


def random_mail():
    dominio = "gmail.com"
    lunghezza = int(12)
    lettere = string.ascii_letters[:12]
    
    email = (''.join(random.choice(lettere) for i in range(lunghezza))) + '@' + dominio
    return email


def random_password():
    lunghezza = int(12)
    insieme_alfanum = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz'
    password = (''.join(random.choice(insieme_alfanum) for i in range(lunghezza)))
    return password


def accedi_random():
    webbrowser.open("https://accounts.google.com/signup/v2/webcreateaccount?hl=en-GB&flowName=GlifWebSignIn&flowEntry=SignUp")


