
## Grupo 

- Joao Pedro Silva Antunes
- Fernanda Aparecida Figueiredo da Silva
- Alan Araújo da Silveira
- Ana Cláudia Monteiro Misquita

# 🗂️ Gerenciador de Tarefas — Visão Geral do Projeto

O Gerenciador de Tarefas é uma solução completa para organização de atividades diárias, permitindo que cada usuário cadastre, visualize, edite e exclua suas próprias tarefas. O projeto foi desenvolvido com foco acadêmico, utilizando arquitetura MVC e tecnologias modernas para garantir escalabilidade e fácil integração.

## Objetivo
Oferecer uma plataforma onde usuários possam gerenciar suas tarefas de forma simples, eficiente e segura, servindo tanto para uso pessoal quanto como base para estudos e futuras expansões.

## Componentes do Projeto
- **Back-end:** API desenvolvida em Flask, responsável por toda a lógica de negócio, persistência de dados e exposição de endpoints para o front-end.
- **Front-end:** Interface gráfica (UI) planejada para consumir a API, permitindo interação amigável com o usuário (pode ser implementada em qualquer framework moderno, como React, Angular ou Vue).
- **Banco de Dados:** Utiliza SQLite para armazenar informações de usuários e tarefas, garantindo persistência e integridade dos dados.
- **Documentação:** Swagger UI integrado para facilitar testes e integração com outros sistemas.
- **Docker:** Possibilidade de conteinerização para facilitar o deploy e padronizar o ambiente de execução.

## Fluxo Geral de Uso
1. O usuário acessa a interface (front-end) e realiza login ou cadastro.
2. Após autenticado, pode criar, visualizar, editar e excluir tarefas.
3. Todas as operações são enviadas para a API, que processa e armazena as informações no banco de dados.
4. A documentação Swagger permite que desenvolvedores testem e conheçam todos os endpoints disponíveis.

## Diferenciais
- Estrutura modular e organizada (MVC), facilitando manutenção e expansão.
- Pronto para integração com diferentes interfaces de usuário.
- Documentação automática e interativa.
- Possibilidade de rodar localmente ou em containers Docker.

## Como executar
1. Clone o repositório.
2. Instale as dependências do back-end e execute a API.
3. (Opcional) Implemente ou utilize um front-end para consumir a API.
4. Utilize a documentação Swagger para explorar os endpoints.
