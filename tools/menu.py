
def menu_show(title, items):
    """Menu generico"""
    flag=True
    print("********** "+title+" **********")
    for i in range(len(items)):
        print(str(i+1)+". "+items[i])
    print("0. Salir")
    print("**************************")
    while flag:
        res =  input("Elija una opcion: ")
        if res == "0":
            flag = False
        elif int(res) in range(1,len(items)+1):
            flag = False
        else:
            print("Opcion no valida")
    return items[int(res)-1]