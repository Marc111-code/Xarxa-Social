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

def searchUser(b):
    '''
    cat
    '''
    dni = 0
    while dni not in list(b.keys()):
        print("=====================================")
        print("Searching user in Social Network")
        print("=====================================")
        dni = int(input("Posa el dni: "))
        print(list(b.keys()))
        if dni in list(b.keys()):
            print("Usuari Trobat! Buscant informació")
            print("Nom i Cognom: " + str((b[dni])[0]) + str((b[dni])[1]))
            print("Ciutat: " + str((b[dni])[2]))
            print("Centre: " +  str((b[dni])[3]))
            print("Hobbies: " + str((b[dni])[4]))
            print("Email: " + str((b[dni])[5]))
        else:
            print("No s'ha trobat cap usuari")


def listUsers(b):
    print("=====================================")
    print("Llista usuaris")
    print("=====================================")

    if len(b) == 0:
        print("O usuaris trobats")
    else:
        for i in b.values():
            print("Nom i Cognom: " + i[0] +" "+ i[1])
            print("Ciutat: " + i[2])
            print("Centre: " + i[3])
            print("Hobbies: " + i[4])
            print("Email: " + i[5])
            print("=====================================")
        print(str(len(b)) + " usuaris trobats")


def acceptUser(b):
    amics1 = []
    m = 1        
    print("=====================================")
    print("Fer amics")
    print("=====================================")
    while m == 1:
        dni1 = int(input("Enter dni1: "))
        if int(dni1) in b.keys():
            dni2 = int(input("Enter dni2: "))
            if int(dni2) in b.keys():
                print("El dni1 i el dni2 son usuaris de la xarxa")
                print("Amics de " + str(dni1) + ":")
                b[dni1] = b[dni1] + [[dni2]]
                b[dni2] = b[dni2] + [[dni1]]
                print(b)
                print("=====================================")
                print("Fer amics")
                print("=====================================")
                resposta = input("Vols fer més amics? (s / n)")
                if resposta == "s" or resposta == "S":
                    m = 1
                else:
                    m = 0
            
        else:
            print("El dni:" + str(dni1) + " no és usuari de la xarxa")
            resposta = input("Vols fer més amics? (s / n)")
            if resposta == "s" or resposta == "S":
                m = 1
            else:
                m = 0 
acceptUser({4:["marc"],2:["marc2"],6:["marc3"]})
