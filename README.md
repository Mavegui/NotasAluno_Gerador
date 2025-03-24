# **MediaAluno**

Um script em Python para calcular e gerenciar notas finais de disciplinas com base no sistema de notas da **Anhanguera Educacional**, conforme disponível no portal do aluno **Colaborar - AVA**.

## **Objetivo**

Este projeto foi desenvolvido como uma atividade prática da faculdade, adaptada para o dia a dia do aluno. Com este sistema, é possível calcular rapidamente a nota final de cada disciplina, sem precisar aguardar o final do semestre para obter a média final diretamente no portal do aluno.

---

## **Funcionalidades**

- Adicionar disciplinas e respectivas notas:
  - Verifica se a disciplina tem portfólio. Se tiver, a nota do portfólio será requisitada; caso contrário, a nota da avaliação virtual será de (0 a 5000)
  - Portfólio (0 a 2000)
  - Prova presencial (0 a 5000)
  - Avaliação virtual (0 a 3000)
  - Engajamento AVA (0 a 2000)
- Calcular automaticamente a **nota final** (máximo 10.0).
- Excluir disciplinas.
- Exibir disciplinas cadastradas e suas respectivas notas.
- Salvar dados de alunos e disciplinas em arquivos `.txt`.

---

## **Como o Sistema Funciona**

O cálculo segue o padrão do portal **Colaborar - AVA**, onde as notas das diferentes atividades são somadas e transformadas em uma escala de 0 a 10. Este script permite que você insira as notas parciais e obtenha instantaneamente a nota final de cada disciplina.

---

## **Pré-requisitos**

Antes de executar o projeto, certifique-se de ter instalado:

- **Python 3.6+**

---

### **Clonar o Repositório**

Para clonar o repositório, use o seguinte comando:

  ```bash
  git clone https://github.com/Mavegui/NotasAluno_Gerador.git
  ```
---

## **Como Executar com Docker**  

Para rodar sem precisar construir a imagem localmente, basta usar:  
  
  ```bash
  docker run --rm -it mavegui/notasaluno_gerador
  ```

Se preferir construir a imagem manualmente:
  
  ```bash
  docker build -t notasaluno_gerador .
  docker run --rm -it notasaluno_gerador
  ```

---

## **Executar o Script**

  Certifique-se de que está na pasta onde está o script MediaAluno.py.
  
  Execute o seguinte comando:
  
  ```bash 
  python3 MediaAluno.py
  ```

---

## **Interação com o Menu**

Ao executar, o script apresentará um menu com as seguintes opções:

 1. Adicionar/Alterar Disciplina: Digite o nome da disciplina e as notas correspondentes.
 2. Excluir Disciplina: Informe o nome da disciplina a ser excluída.
 3. Exibir Dados do Aluno: Mostra as disciplinas cadastradas, as notas e a média final.
 4. Salvar Dados em TXT: Salva os dados do aluno em um arquivo .txt no formato Nome_Aluno.txt.
 5. Sair: Encerra o programa.

# **Exemplo de Uso**
## **Entrada de Dados**

Ao adicionar uma disciplina, você verá o seguinte:

  ```plaintext
  Digite o nome completo do aluno: João Silva
  Menu:
  1. Adicionar/Alterar Disciplina
  2. Excluir Disciplina
  3. Exibir Dados do Aluno
  4. Salvar Dados em TXT
  5. Sair
  Escolha uma opção: 1

  Informe os dados da disciplina:
  Digite o nome da disciplina: Matemática
  Sua disciplina tem portfólio? (S/N)
  Digite a nota do portfólio (0 a 2000): 1500
  Digite a nota da prova presencial (0 a 5000): 4500
  Digite a nota da avaliação virtual final (0 a 3000): 2800
  Digite a nota final do engajamento AVA (0 a 2000): 1800
  ```

## **Saída no Terminal**
  ```bash
  Disciplina 'Matemática' adicionada/atualizada com sucesso!
  ```
---

## **Arquivo TXT Gerado**

Arquivo: João_Silva.txt

Aluno: João Silva

Disciplinas e Notas:
Disciplina: Matemática
  - Portfólio: 1500
  - Prova Presencial: 4500
  - Avaliação Virtual: 2800
  - Engajamento AVA: 1800
  - Nota Final: 10.00

---

## **Estrutura do Projeto**
  ```bash
  media_aluno/
  ├── MediaAluno.py      # Script principal
  ├── README.md          # Documentação do projeto
  ```
---

## **Contribuição**

Este projeto foi criado com fins educacionais e práticos, mas contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## **Licença**

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](./LICENSE) para mais detalhes.
