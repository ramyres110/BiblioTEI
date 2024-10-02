

def mostrar_menu():
    print("+--------------------+")
    print("|      BiblioTEI     |")
    print("+--------------------+")
    while True:
        print("1 - Cadastrar Livro")
        print("2 - Realizar empréstimo")
        print("3 - Realizar devolução")
        print("4 - Consultar livro")
        print("5 - Relatórios")
        print("0 - Sair")
        opcao = input("Informe a opção: ")
        if opcao == "0":
            break    


mostrar_menu()