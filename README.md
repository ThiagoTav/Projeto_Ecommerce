# Lista de Tarefas

## Escopo do Projeto

### 1. Introdução
O projeto será uma Lista de Tarefas, com o objetivo de ajudar as pessoas a se organizarem diariamente. Este sistema visa evitar que os usuários esqueçam de realizar suas tarefas, proporcionando uma maneira eficiente de gerenciar suas atividades diárias.

### 2. Visão Geral do Sistema
#### Descrição do Sistema
O sistema permitirá aos usuários adicionar, finalizar e deletar tarefas. Haverá uma página principal onde as tarefas podem ser gerenciadas, e uma página de histórico que mostrará todas as atividades concluídas. As tarefas terão um status que indicará se estão prestes a atingir a data de finalização ou se estão atrasadas.

#### Público-alvo
Todas as pessoas que desejam uma ferramenta para melhorar sua organização pessoal e não esquecer de suas tarefas diárias.

### 3. Arquitetura do Sistema
#### Explicação da Arquitetura MVT (Model-View-Template)
O sistema será desenvolvido seguindo o padrão de arquitetura MVT do Django, que é similar ao MVC (Model-View-Controller).

#### Papel de Cada Componente
- **Model:** Representa a estrutura dos dados e contém a lógica de negócios. No nosso caso, será substituído pelo uso direto do MongoDB com `pymongo`.
- **View:** Lida com a lógica de apresentação. Recebe as solicitações do usuário, interage com o modelo e retorna as respostas adequadas.
- **Template:** Responsável pela renderização da interface do usuário com dados dinâmicos.

### 4. Requisitos Funcionais
- **Adicionar Tarefa:** Usuários podem adicionar novas tarefas.
- **Finalizar Tarefa:** Usuários podem marcar tarefas como concluídas.
- **Deletar Tarefa:** Usuários podem deletar tarefas.
- **Visualizar Histórico:** Usuários podem ver o histórico de todas as tarefas concluídas.
- **Status da Tarefa:** Exibir o status das tarefas indicando se estão próximas da data de finalização ou atrasadas.
- **Autenticação e Autorização:** Usuários devem se autenticar para acessar o sistema.

#### Casos de Uso Principais
- **Cadastrar Usuário:** Novo usuário se registra no sistema.
- **Login:** Usuário existente faz login no sistema.
- **Gerenciar Tarefas:** Usuário adiciona, finaliza ou deleta tarefas.
- **Visualizar Histórico:** Usuário visualiza o histórico de tarefas concluídas.

#### Fluxos de Trabalho do Usuário
1. **Registro/Login:**
   - Usuário acessa a tela de login e se autentica.
2. **Gerenciamento de Tarefas:**
   - Usuário adiciona, edita e deleta tarefas na página principal.
3. **Visualização de Histórico:**
   - Usuário acessa a página de histórico para visualizar tarefas concluídas.

### 5. Requisitos Não Funcionais
- **Desempenho:** O sistema deve responder rapidamente às interações do usuário, com tempo de resposta inferior a 2 segundos para operações comuns.
- **Autenticação JWT:** Implementação de autenticação JWT para segurança e controle de sessões.
- **Escalabilidade:** O sistema deve ser escalável para suportar um grande número de usuários e tarefas.
- **Manutenibilidade:** O código deve ser bem documentado e modular para facilitar a manutenção futura.

### 6. Tecnologias Utilizadas
- **Linguagens de Programação:** Python, HTML, CSS, JavaScript
- **Frameworks:** Django, Django REST Framework, SimpleJWT, Bootstrap
- **Banco de Dados:** MongoDB (usando `pymongo` para acesso direto)
- **Ferramentas de Desenvolvimento:** Git, GitHub

### 7. Modelo de Dados
#### Estrutura do Banco de Dados
- **Usuário:** Campos para nome de usuário, email e senha.
- **Tarefa:** Campos para título, descrição, data de criação, data de conclusão, status, e ID do usuário.

#### Relacionamentos entre Entidades
- **Usuário -> Tarefa:** Um usuário pode ter várias tarefas.

#### Esquema de Armazenamento
Os dados serão armazenados no MongoDB, organizados em coleções (`users` e `tasks`).

### 8. Interfaces do Usuário
#### Layout e Design das Interfaces
- **Tela de Login:** Formulário para entrada de credenciais do usuário.
- **Página Principal (Home):** Exibe as tarefas com opções para adicionar, editar e deletar.
- **Página de Histórico:** Lista de tarefas concluídas com detalhes.

#### Fluxos de Interação do Usuário
1. **Login:** Usuário insere credenciais e autentica-se.
2. **Adicionar Tarefa:** Usuário insere detalhes da tarefa e salva.
3. **Gerenciar Tarefas:** Usuário visualiza, edita ou deleta tarefas.
4. **Visualizar Histórico:** Usuário acessa a página de histórico para ver tarefas concluídas.

### 9. Arquitetura de Implementação
#### Organização do Código-Fonte
- **Estrutura do Projeto:**
  - `myproject/`
    - `users/`
      - `models.py`
      - `views.py`
      - `serializers.py`
      - `repositories.py`
      - `urls.py`
    - `templates/`
    - `static/`

#### Divisão em Módulos e Componentes
- **Autenticação:** Gerenciamento de login e registro.
- **CRUD de Tarefas:** Funcionalidades de adicionar, editar e deletar tarefas.
- **Histórico:** Visualização das tarefas concluídas.

#### Dependências entre os Componentes
- **Views** dependem de **Repositories** para acesso aos dados.
- **Repositories** interagem diretamente com o MongoDB.

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
- **Branching Model:** Uso de branches `main`, `development`, e `feature`.
- **Commits:** Commits frequentes com mensagens claras e descritivas.

#### Uso de Ferramentas de Controle de Versão
- **Git:** Controle de versão distribuído.
- **GitHub:** Repositório remoto para colaboração e gestão do código.

### 12. Gestão de Projetos
#### Cronograma de Desenvolvimento
- **Semana 1:** Desenvolvimento da tela de login com autenticação JWT.
- **Semana 2:** Implementação da página principal (CRUD de tarefas).
- **Semana 3:** Desenvolvimento da página de histórico de tarefas.
- **Semana 4:** Testes finais e ajustes.

#### Monitoramento do Projeto
- **GitHub:** Utilização do histórico de commits para monitorar o progresso e colaboração.

### 13. Considerações de Segurança
#### Mecanismos de Autenticação e Autorização
- **Django JWT:** Implementação de autenticação segura com tokens JWT.
- **Proteção Contra Vulnerabilidades:** Uso das melhores práticas de segurança das bibliotecas e frameworks utilizados.

### 14. Considerações de Manutenção
#### Suporte Pós-Lançamento
- **Versionamento:** Continuidade do desenvolvimento e manutenção via Git para gerenciar versões e correções de bugs.
- **Documentação:** Manutenção de documentação clara e atualizada para facilitar a manutenção futura.