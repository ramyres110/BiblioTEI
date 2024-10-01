# BiblioTEI
App de Biblioteca


## História
****
Um bibliotecário precisa de um sistema para gerenciar o acervo de livros de uma pequena biblioteca. Ele deseja cadastrar novos livros, realizar empréstimos e devoluções, consultar a disponibilidade de livros e gerar relatórios simples.

## Requisitos

### Cadastro de Livros:

* Cada livro deve ter um código único, título, autor, ISBN, editora e status (disponível ou emprestado).
* Ao cadastrar um novo livro, o status deve ser automaticamente definido como "disponível".
 
### Empréstimo de Livros:

Um livro só pode ser emprestado se estiver disponível.
Ao realizar um empréstimo, o sistema deve registrar o nome do usuário que realizou o empréstimo.
O status do livro deve ser alterado para "emprestado".

### Devolução de Livros:

Ao devolver um livro, o sistema deve verificar se o livro foi emprestado para aquele usuário.
O status do livro deve ser alterado para "disponível".

### Consulta de Livros:

O bibliotecário deve poder consultar a disponibilidade de um livro por título, autor ou ISBN.
O sistema deve exibir informações detalhadas sobre o livro, como título, autor, editora e status.

### Relatórios:

O sistema deve gerar relatórios simples, como a lista de todos os livros, os livros emprestados e os livros disponíveis.
