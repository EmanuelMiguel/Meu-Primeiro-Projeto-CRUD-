##Olá pessoal meu nome é Emanuel Miguel e esse é o meu primeiro Projeto Python, fiz aqui um CRUD usando CustomTkinter e integração com SQLite. 

Descrição do Projeto: Sistema de Cadastro de Clientes (CRUD):

"Bem, esse códgio é simples por mas de seja grande, fiz de tudo para que ele seja o mais legivel possível para quem irá ler!"

#####Funcionalidades Principais#####

*Cadastro de Clientes: Permite a entrada de informações como Nome, CPF, Email, Telefone, Data de Vencimento e Observações.

*Visualização de Dados: Exibe os dados cadastrados em um Treeview, permitindo fácil navegação e seleção de registros.

*Atualização de Informações: Os usuários podem atualizar os dados de clientes selecionados.

*Deleção de Registros: Possibilita a remoção de um ou mais registros de clientes.

*Formatação de Entradas: Inclui validação e formatação para os campos de CPF e Telefone, garantindo que os dados sejam inseridos corretamente.

*Interface Intuitiva: A interface foi projetada para ser amigável e responsiva, facilitando a interação do usuário.

#####Tecnologias Utilizadas#####

*Python: Linguagem de programação principal.

*customtkinter: Biblioteca para a criação de interfaces gráficas.

*tkcalendar: Biblioteca para a entrada de datas.

*SQLite: Banco de dados leve para armazenamento de dados.

#####Explicando as partes do Projeto (simplificado)#####

*O arquivo "main.py" roda a interface gráfica com algumas funções.

*O arquivo "banco.py" é aonde eu importo o SQLite crio o banco de dados e faço a conexão, além de definir o criar banco de dados caso não exista nenhum.

*O arquivo "view.py" é aonde ficam as funções que estão "vinculadas" aos botões. Funcões: (C)INSERIR // (R)MONSTRAR // (U)ATUALIZAR // (D)DELETAR (CRUD).

*O arquivo "icon_projeto1.ico" é para definir a aparência do ícone que representa o aplicativo no sistema operacional.

#####Observações/Curiosidades#####

*O banco de dados é criado sozinho caso não haja nenhum, ele cria automaticamente e deixa na pasta com o nome "dados.db".

*O código é totalmente maleável e de fácil entendimento, creio que as cores para os botões não foram uma boa escolha, mas isso é totalmente alterável.

*Adicionei também algumas funcionalides/definições de formatação. Ex: Quando vou digitar o CPF ele já formata assim 000.000.000-00, e quando é o telefone assim (00)00000-0000.

*O arquivo exe. funciona perfeitamente!

*O exe. abre em 1200x600 e não maximizar mais do que isso, além de sempre iniciar centralizado na tela!
