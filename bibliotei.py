
livros = [
    {
        "id": 1,
        "titulo": "A Morte e a Morte de Quincas Berro d'Água",
        "autor": "Jorge Amado",
        "isbn": "1234567890",
        "editora": "Companhia das Letras",
        "status": "disponivel"
    },
    {
        "id": 2,
        "titulo": "Grande Sertão: Veredas",
        "autor": "João Guimarães Rosa",
        "isbn": "1234567890",
        "editora": "Nova Fronteira",
        "status": "disponivel"
    }
]


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
        "status": "disponivel"
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
        match opcao:
            case "0": 
                break
            case "1": 
                cadastrar_livro()
            case "4": 
                consultar_livros()    


mostrar_menu()