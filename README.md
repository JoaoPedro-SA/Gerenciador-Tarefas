# 🗂️ Gerenciador de Tarefas — API Flask (Back-end)

## Grupo 

- Joao Pedro Silva Antunes
- Fernanda Aparecida Figueiredo da Silva
- Alan Araújo da Silveira
- Ana Cláudia Monteiro Misquita

## 💡 Ideia geral da aplicação
Esta aplicação é uma **API de Gerenciamento de Tarefas**, desenvolvida com **Flask**, com o objetivo de permitir que cada usuário **crie, liste, edite e exclua** suas próprias tarefas.  
O sistema visa **organizar e acompanhar atividades diárias**, servindo como base para uma futura integração com o front-end.  

O projeto segue a arquitetura **MVC (Model-View-Controller)** e foi desenvolvido para fins acadêmicos, como parte da **Avaliação AP1 da disciplina FFS**.

---

## ⚙️ Tecnologias utilizadas
- **Python 3.12+**
- **Flask** (framework web)
- **Flask-SQLAlchemy** (ORM para persistência de dados)
- **SQLite** (banco de dados)
- **Flask-Swagger-UI** (documentação da API)
- **Docker** (para conteinerização)
- **Git/GitHub** (para controle de versão)

---

## 🧩 Estrutura do projeto (MVC)

```
📁 Gerenciador-Tarefas/
│
├── controller/ # Controladores e regras de negócio
│ ├── Gerenciador-Tarefas/
│ │ ├── app.py
│ │ ├── README.md
│ │ └── Requisitos.docx
│ └── script/
│ └── appRecuperarSenha.py
│
├── models/ # Modelos e conexão com o banco de dados
│ ├── agenda.py
│ ├── bancoSQL.py
│ └── usuario.py
│
├── swagger/ # Configuração da documentação Swagger
│ ├── namespace/
│ │ ├── agendanamespace.py
│ │ └── usuarionamespace.py
│ ├── swaggerconfig.py
│ └── swaggerinit.py
│
├── app.py # Ponto de entrada da aplicação Flask
├── dockerfile # Configuração Docker
├── requirements.txt # Dependências do projeto
├── meubanco.db # Banco de dados SQLite
└── README.md # Relatório do projeto
```

 ## Diagrama ER

![Logo do projeto](Imagem%20do%20WhatsApp%20de%202025-10-07%20%C3%A0(s)%2010.14.37_7a471e5f.jpg)


 ## Como rodar API

 Para rodar a api tem que 

 Primeiro fazer o git clone do repositorio. 

 ``` git clone https://github.com/fernanda2003/Gerenciador-Tarefas.git ```

 Logo em seguida acessa o terminal e baixa os requirements. 

 ``` pip install -r requirements.txt ```

Por ultimo só execulte o app.py para ter acesso da api.

1- acesse a pasta do projeto pelo terminal

```
cd Gerenciador-Tarefas 
```

2- execute o app.py pelo terminal

```
python app.py
```
