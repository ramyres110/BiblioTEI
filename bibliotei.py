from json import loads, dumps

livros = []

# Cada livro deve ter um código único, título, autor, ISBN, editora e status (disponível ou emprestado).
# Ao cadastrar um novo livro, o status deve ser automaticamente definido como "disponível"
def cadastrar_livro():
    titulo = input("Titulo:")
    autor = input("Autor:")
    isbn = input("ISBN:")
    editora = input("Editora:")
    livro = {
        "id": len(livros) + 1,
        "titulo": titulo,
        "autor": autor,
        "isbn": isbn,
        "editora": editora,
        "status": "disponível"
    }
    livros.append(livro)

# O bibliotecário deve poder consultar a disponibilidade de um livro por título, autor ou ISBN.
# O sistema deve exibir informações detalhadas sobre o livro, como título, autor, editora e status.
def consultar_livros():
    pesquisa = input("Pesquisar: ")
    resultado = []
    for livro in livros:
        chave = livro["titulo"]+livro["autor"]+livro["isbn"]
        if chave.find(pesquisa) >= 0:
            resultado.append(livro)
    if not resultado:
        print("Nenhum resultado.")
        return
    print("|id \t| titulo \t| autor \t| isbn \t| editora \t| status")
    for livro in resultado:
        print("|{} \t| {} \t| {} \t| {} \t| {} \t| {} |".format(livro["id"],livro["titulo"],livro["autor"],livro["isbn"],livro["editora"],livro["status"]))


# Um livro só pode ser emprestado se estiver disponível.
# Ao realizar um empréstimo, o sistema deve registrar o nome do usuário que realizou o empréstimo.
# O status do livro deve ser alterado para "emprestado".
def emprestar_livro():
    id_livro = input("Informe o Id do livro: ")
    if not id_livro:
        print("Informe um id válido.")
        return

    livro = None
    indice = -1
    for index, livro_pesquisa in enumerate(livros):
        if str(livro_pesquisa["id"]) == id_livro:
            indice = index
            livro = livro_pesquisa
            
    if not livro:
        print("Livro não encontrado.")
        return

    if livro["status"] != "disponível":
        print("Livro não está disponível.")
        return

    usuario = input("Informe o nome do usuário: ")
    if not usuario:
        print("Informe um nome de usuário válido.")
        return

    livro["usuario"] = usuario
    livro["status"] = "emprestado"
    livros[indice] = livro
    print("Livro {} emprestado para {}.".format(livro["titulo"], usuario))


# Ao devolver um livro, o sistema deve verificar se o livro foi emprestado para aquele usuário.
# O status do livro deve ser alterado para "disponível"
def devolver_livro():    
    id_livro = input("Informe o Id do livro: ")
    livro = None
    indice = -1
    for index, livro_pesquisa in enumerate(livros):
        if str(livro_pesquisa["id"]) == id_livro:
            indice = index
            livro = livro_pesquisa
    if not livro:
        print("Livro não encontrado.")
        return

    if livro["status"] == "disponível":
        print("Livro não está emprestado.")
        return
    
    usuario = input("Informe o nome do usuário: ")
    if not usuario:
        print("Informe um nome de usuário válido.")
        return

    if livro["usuario"] != usuario:
        print("Livro foi emprestado por outro usuário.")
        return

    livro.pop("usuario")
    livro["status"] = "diponível"
    livros[indice] = livro
    print("Livro {} devolvido.".format(livro["titulo"]))


def mostrar_relatorios():
    print("1 - Listar todos")
    print("2 - Listar disponíveis")
    print("3 - Listar emprestados")
    opcao_relatorio = input("Informe o relatório: ")
    if opcao_relatorio == "1":
        if not livros:
            print("Nenhum livro cadastrado.")
            return
        
        print("|id \t| titulo \t| autor \t| isbn \t| editora \t| status")
        for livro in livros:
            print("|{} \t| {} \t| {} \t| {} \t| {} \t| {} |".format(livro["id"],livro["titulo"],livro["autor"],livro["isbn"],livro["editora"],livro["status"]))

    elif opcao_relatorio == "2":
        livros_disponiveis = [livro for livro in livros if livro["status"] == "disponível"]
        if not livros_disponiveis:
            print("Nenhum livro disponível.")
            return
        
        print("|id \t| titulo \t| autor \t| isbn \t| editora \t| status")
        for livro in livros_disponiveis:
            print("|{} \t| {} \t| {} \t| {} \t| {} \t| {} |".format(livro["id"],livro["titulo"],livro["autor"],livro["isbn"],livro["editora"],livro["status"]))

    elif opcao_relatorio == "3":
        livros_emprestados = [livro for livro in livros if livro["status"] == "emprestado"]
        if not livros_emprestados:
            print("Nenhum livro emprestado.")
            return
        
        print("|id \t| titulo \t| autor \t| isbn \t| editora \t| status \t| usuario")
        for livro in livros_emprestados:
            print("|{} \t| {} \t| {} \t| {} \t| {} \t| {} \t| {}".format(livro["id"],livro["titulo"],livro["autor"],livro["isbn"],livro["editora"],livro["status"],livro["usuario"]))

    else:
        print("Opção de relatório inválido.")


def ler_livros_arquivo():
    try:
        with open("livros.json","r") as arquivo_livros_json:
            texto = arquivo_livros_json.read()
            if texto:
                livros_salvos = loads(texto)
                livros.extend(livros_salvos)
            arquivo_livros_json.close()
    except:
        return

def salvar_livros_arquivo():
    with open("livros.json","w") as arquivo_livros_json:
        texto = dumps(livros)    
        arquivo_livros_json.write(texto)
        arquivo_livros_json.close()

def mostrar_menu():
    ler_livros_arquivo()

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
        match opcao:
            case "0": 
                salvar_livros_arquivo()
                break
            case "1": 
                cadastrar_livro()
            case "2": 
                emprestar_livro()
            case "3": 
                devolver_livro()
            case "4": 
                consultar_livros()    
            case "5": 
                mostrar_relatorios()    


mostrar_menu()