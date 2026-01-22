def menu():
    print("=====================================")
    print("Welcome to Social Network")
    print("=====================================")
    print("new --> Create new user")
    print("cat --> Show user information")
    print("ls ---> List users")
    print("add --> Add friends to an user")
    print("se ---> Search user by pattern")
    print("mv ---> Modify user information")
    print("save -> Save users to disk")
    print("load -> Load users from disk")
    print("exit -> Logout")
    print("=====================================")
    respostam = input("Enter option: ")
    return respostam

def newUser(b):
    '''
    mira si el dni que introdueix l'usuari ja ha sigut utlitzat,
   i si no li demana tota la informació
    '''
    dni = input("Posa el DNI: ")
    if dni in list(b.keys()):
        return "Aquest usuari ja ha sigut introduit, inicia sessió."
    else:        
        info=[]
        nom = input("Posa el teu Nom: ")
        cognom = input("Posa el Cognom: ")
        ciutat = input("Posa la teva Ciutat: ")
        network = input("Network: ")
        hobbies = input("Posa els teus Hobbies: ")
        email = input("Posa el teu Email: ")
        contra = input("Posa la teva Contrasenya: ")
        info = info + [nom]
        info = info + [cognom]
        info = info + [ciutat]
        info = info + [network]
        info = info + [hobbies]
        info = info + [email]
        info = info + [contra]
        b[dni]=info
    return b

resposta = input("Vols crear un nou usuari (s/n)")
while resposta=="s": 
    print(newUser({}))
    resposta = input("Vols crear un nou usuari (s/n)")
