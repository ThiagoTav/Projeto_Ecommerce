# E-commerce

## Escopo do Projeto

### 1. Introdução
O projeto é um sistema de e-commerce, com o objetivo de proporcionar uma plataforma onde os usuários podem adicionar, editar, excluir e comprar produtos. Este sistema visa facilitar a compra e venda de produtos, proporcionando uma maneira eficiente de gerenciar o inventário e as transações.

### 2. Visão Geral do Sistema
#### Descrição do Sistema
O sistema permitirá aos usuários autenticados adicionar, editar, excluir e comprar produtos. Haverá uma página principal onde os produtos podem ser gerenciados, e uma funcionalidade para exibir produtos próximos da data de expiração ou com estoque baixo.

#### Público-alvo
Todas as pessoas que desejam uma plataforma para comprar e vender produtos.

### 3. Arquitetura do Sistema
#### Explicação da Arquitetura MVT (Model-View-Template)
O sistema será desenvolvido seguindo o padrão de arquitetura MVT do Django, que é similar ao MVC (Model-View-Controller).

#### Papel de Cada Componente
- **Model:** Representa a estrutura dos dados e contém a lógica de negócios.
- **View:** Lida com a lógica de apresentação. Recebe as solicitações do usuário, interage com o modelo e retorna as respostas adequadas.
- **Template:** Responsável pela renderização da interface do usuário com dados dinâmicos.

### 4. Requisitos Funcionais
- **Adicionar Produto:** Usuários podem adicionar novos produtos.
- **Editar Produto:** Usuários podem editar informações dos produtos.
- **Excluir Produto:** Usuários podem excluir produtos.
- **Comprar Produto:** Usuários podem comprar produtos.
- **Autenticação e Autorização:** Usuários devem se autenticar para acessar o sistema.

#### Casos de Uso Principais
- **Cadastrar Usuário:** Novo usuário se registra no sistema.
- **Login:** Usuário existente faz login no sistema.
- **Gerenciar Produtos:** Usuário adiciona, edita ou deleta produtos.
- **Comprar Produtos:** Usuário compra produtos disponíveis.

#### Fluxos de Trabalho do Usuário
1. **Registro/Login:**
   - Usuário acessa a tela de login e se autentica.
2. **Gerenciamento de Produtos:**
   - Usuário adiciona, edita e deleta produtos na página principal.
3. **Compra de Produtos:**
   - Usuário visualiza os produtos disponíveis e realiza a compra.

### 5. Requisitos Não Funcionais
- **Desempenho:** O sistema deve responder rapidamente às interações do usuário, com tempo de resposta inferior a 2 segundos para operações comuns.
- **Segurança:** Implementação de autenticação para segurança e controle de acesso.
- **Escalabilidade:** O sistema deve ser escalável para suportar um grande número de usuários e produtos.
- **Manutenibilidade:** O código deve ser bem documentado e modular para facilitar a manutenção futura.

### 6. Tecnologias Utilizadas
- **Linguagens de Programação:** Python, HTML, CSS, JavaScript
- **Frameworks:** Django, Django REST Framework, Bootstrap
- **Banco de Dados:** SQLite (usando ORM do Django)
- **Ferramentas de Desenvolvimento:** Git, GitHub

### 7. Modelo de Dados
#### Estrutura do Banco de Dados
- **Usuário:** Campos para nome de usuário, email e senha.
- **Produto:** Campos para nome, descrição, quantidade, preço e data de criação.

#### Relacionamentos entre Entidades
- **Usuário -> Produto:** Um usuário pode gerenciar vários produtos.

### 8. Interfaces do Usuário
#### Layout e Design das Interfaces
- **Tela de Login:** Formulário para entrada de credenciais do usuário.
- **Página Principal (Home):** Exibe os produtos com opções para adicionar, editar e deletar.
- **Página de Compra:** Lista de produtos disponíveis para compra com detalhes.

#### Fluxos de Interação do Usuário
1. **Login:** Usuário insere credenciais e autentica-se.
2. **Adicionar Produto:** Usuário insere detalhes do produto e salva.
3. **Gerenciar Produtos:** Usuário visualiza, edita ou deleta produtos.
4. **Comprar Produto:** Usuário visualiza e compra produtos disponíveis.

### 9. Arquitetura de Implementação
#### Organização do Código-Fonte
- **Estrutura do Projeto:**
  - `myproject/`
    - `products/`
      - `models.py`
      - `views.py`
      - `forms.py`
      - `urls.py`
    - `templates/`
      - `products/`
        - `card.html`
    - `static/`

#### Divisão em Módulos e Componentes
- **Autenticação:** Gerenciamento de login e registro.
- **CRUD de Produtos:** Funcionalidades de adicionar, editar e deletar produtos.
- **Compra:** Funcionalidade de compra de produtos.

#### Dependências entre os Componentes
- **Views** dependem de **Models** para acesso aos dados.
- **Forms** interagem com os **Models** para manipulação de dados.

### 10. Planejamento de Implantação
#### Ambientes de Implantação
- **Desenvolvimento:** Ambiente local para desenvolvimento e testes.
- **Teste:** Ambiente para testes integrados.
- **Produção:** Ambiente final para uso pelos usuários.

#### Procedimentos de Implantação
1. **Configuração do Ambiente:** Configuração do servidor e banco de dados.
2. **Deploy do Código:** Uso de ferramentas como Git para deploy contínuo.
3. **Testes:** Realização de testes pós-implantação para garantir estabilidade.

### 11. Gestão de Configuração e Controle de Versão
#### Políticas de Controle de Versão
- **Branching Model:** Uso de branches `main`, `develop`, e `feature`.
- **Commits:** Commits frequentes com mensagens claras e descritivas.

#### Uso de Ferramentas de Controle de Versão
- **Git:** Controle de versão distribuído.
- **GitHub:** Repositório remoto para colaboração e gestão do código.

### 12. Gestão de Projetos
#### Cronograma de Desenvolvimento
- **Semana 1:** Desenvolvimento da tela de login com autenticação.
- **Semana 2:** Implementação da página principal (CRUD de produtos).
- **Semana 3:** Desenvolvimento da funcionalidade de compra de produtos.
- **Semana 4:** Testes finais e ajustes.

#### Monitoramento do Projeto
- **GitHub:** Utilização do histórico de commits para monitorar o progresso e colaboração.

### 13. Considerações de Segurança
#### Mecanismos de Autenticação e Autorização
- **Django Auth:** Implementação de autenticação segura.
- **Proteção Contra Vulnerabilidades:** Uso das melhores práticas de segurança das bibliotecas e frameworks utilizados.

### 14. Considerações de Manutenção
#### Suporte Pós-Lançamento
- **Versionamento:** Continuidade do desenvolvimento e manutenção via Git para gerenciar versões e correções de bugs.
- **Documentação:** Manutenção de documentação clara e atualizada para facilitar a manutenção futura.

### Crie e Ative um Ambiente Virtual
- python -m venv .env 
- .\.env\Scripts\activate
- pip install -r requirements.txt
- python manage.py migrate

### Inicie o Servidor de Desenvolvimento
- python manage.py runserver
