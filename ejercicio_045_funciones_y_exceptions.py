#Back / Servidor
def validar_email(email):
    #Si la longitud del email es <6 el email se produce un error
    if len(email)<6:
        raise ValueError("La longitud del email no es correcta")
    return "@" in email

def validar_password(password):
    #Si la password contiene un 5 se produce un error
    return len(password)>6

def validar_usuario(email, password):
    try:
        usuario_correcto = validar_email(email) and validar_password(password)
    except ValueError as ve:
        print("LOG DEL SISTEMA: se ha producido un ValueError")
        raise ve
    return usuario_correcto
    
#Front / Cliente
if __name__=="__main__":
    email = "fe@gm"
    password = "pepinillo12@"
    try:
        if validar_usuario(email, password):
            print("Todo correcto")
        else:
            print("Incorrecto")
    except ValueError:
        print("El email no es correcto")