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
    buscarAmics = True
    while buscarAmics == True:
        print("=====================================")
        print("Searching user in Social Network")
        print("=====================================")
        dni = int(input("Posa el dni: "))
        if dni in list(b.keys()):
            print("Usuari Trobat! Buscant informació")
            print("Nom i Cognom: " + str((b[dni])[0]) + " " + str((b[dni])[1]))
            print("Ciutat: " + str((b[dni])[2]))
            print("Centre: " +  str((b[dni])[3]))
            print("Hobbies: " + str((b[dni])[4]))
            print("Email: " + str((b[dni])[5]))
            print("Amics:" + str((b[dni])[6]))
            
        else:
            print("No s'ha trobat cap usuari") 
        buscarAmics = input("Vols buscar els amics de més persones?(s/n)")
        if buscarAmics == "S" or buscarAmics == "s":
            buscarAmics = True
        else:
            buscarAmics = False
'''
b = acceptUser({4:["marc","Soler","Codelearn", "Barcelona", "Basquet", "email"],2:["marc2","Soler","Codelearn", "Barcelona", "Basquet", "email"],6:["marc3","Soler","Codelearn", "Barcelona", "Basquet", "email"]})
searchUser(b)
'''
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
            if len(i) > 6:
                print("Amics:" + str(i[6]))            
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
                print(b[dni1])
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



def saveFile(b):
    resposta = input("Enter Option: ")
    if resposta == "exit":
        resposta1 = input("Are you sure you want to logout? ( y / n )")
        if resposta1 == "y" or resposta1 =="Y":
            print("Thanks for using Social Network")
            with open("data.csv", "a") as f:
                f.write("Nom i Cognom, Ciutat, Centre, Hobbies, Email, Contrasenya, Amics")
                f.write("\n")
                for i in b.values():

                    f.write(i[0] +" "+ i[1] + ", ")
                    f.write(i[2] + ", ")
                    f.write(i[3] + ", ")
                    f.write(i[4] + ", ")
                    f.write(i[5] + ", ")
                    if len(i) > 6:
                        f.write(str(i[6]) + ", ")
                    f.write("\n")

b = {4:["marc","Soler","Codelearn", "Barcelona", "Basquet", "email",[]],2:["marc2","Soler","Codelearn", "Barcelona", "Basquet", "email",[]],6:["marc3","Soler","Codelearn", "Barcelona", "Basquet", "email",[]]}            
def readFile():
    '''
    load
    '''
    fit = ""
    with open("data.csv", "a") as f:
        for i in b.values():
            fit = fit + str(i[0]) + " "
            fit = fit + str(i[1]) + " "
            fit = fit + str(i[2]) + " "
            fit = fit + str(i[3]) + " "
            fit = fit + str(i[4]) + " "
            fit = fit + str(i[5]) + " "
            if len(i) > 6:
                fit = fit + str(i[6]) + " "  
            fit = fit + "\n"
    print(fit)
    return fit

def game(b):
    resposta2 = menu()
    if resposta2 == "new":
        b=newUser(b)
        print(b)
    if resposta2 == "cat":
        print(searchUser(b))
    if resposta2 == "ls":
        listUsers(b)
    if resposta2 == "add":
        acceptUser(b)
    if resposta2 == "load":
        readFile()

        
game(b)
