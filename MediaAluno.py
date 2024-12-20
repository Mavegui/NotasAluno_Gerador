import os  # Importa o módulo que permite manipular txt
import re  # Importa a biblioteca para usar somente letras e espaços no nome aluno

class Aluno:
    
    # Inicializa aluno e dictionary
    def __init__(self, nome):
        """
        Inicializa o aluno com o nome e um dicionário para armazenar disciplinas e notas.
        """
        self.nome = nome
        self.disciplinas = {}

    # Add disciplinas
    def adicionar_disciplina(self, disciplina, portfolio, prova_Presencial, av_Virtual, engajamento_AVA):
        total = portfolio + prova_Presencial + av_Virtual + engajamento_AVA
        nota_final = min(total / 1000, 10)
        self.disciplinas[disciplina] = {
            "portfolio": portfolio,
            "prova_Presencial": prova_Presencial,
            "av_Virtual": av_Virtual,
            "engajamento_AVA": engajamento_AVA,
            "nota_Final": nota_final
        }
    # Excluir disciplina
    def excluir_disciplina(self, disciplina):
        if disciplina in self.disciplinas:
            del self.disciplinas[disciplina]
            return True
        return False
    
    # Exibir dados cadastrados no dictionary
    def exibir_dados(self):
        
        # Nada cadastrado
        print(f"\nAluno: {self.nome}")
        if not self.disciplinas:
            print("Nenhuma disciplina cadastrada.")
            return
        
        # Com dados cadastrados
        print("\nDisciplinas e Notas:")
        for disciplina, dados in self.disciplinas.items():
            print(f"\nDisciplina: {disciplina}")
            print(f"  - Portfólio: {dados['portfolio']:.0f}")
            print(f"  - Prova Presencial: {dados['prova_Presencial']:.0f}")
            print(f"  - Avaliação Virtual: {dados['av_Virtual']:.0f}")
            print(f"  - Engajamento AVA: {dados['engajamento_AVA']:.0f}")
            print(f"  - Nota Final: {dados['nota_Final']:.2f}")
    
    # Salva os dados em .txt
    def salvar_em_txt(self):
        nome_arquivo = f"{self.nome.replace(' ', '_')}.txt"
        
        # Se deseja adicionar algo novo, usa o modo "a = append" 
        if os.path.exists(nome_arquivo):
            modo_abertura = "a"
            cabecalho = "\nDisciplinas e Notas Adicionadas:\n"
        
        # Se não cria ou sobrescreve o arquivo, usa o modo "w = write"
        else:
            modo_abertura = "w"
            cabecalho = f"Aluno: {self.nome}\n\nDisciplinas e Notas:\n"
        
        # Implementa esses dados na criação, seguindo esse padrão formatado.
        with open(nome_arquivo, modo_abertura) as arquivo:
            arquivo.write(cabecalho)
            for disciplina, dados in self.disciplinas.items():
                arquivo.write(f"\nDisciplina: {disciplina}\n")
                arquivo.write(f"  - Portfólio: {dados['portfolio']:.0f}\n")
                arquivo.write(f"  - Prova Presencial: {dados['prova_Presencial']:.0f}\n")
                arquivo.write(f"  - Avaliação Virtual: {dados['av_Virtual']:.0f}\n")
                arquivo.write(f"  - Engajamento AVA: {dados['engajamento_AVA']:.0f}\n")
                arquivo.write(f"  - Nota Final: {dados['nota_Final']:.2f}\n")

        print(f"Novas disciplinas salvas no arquivo '{nome_arquivo}' com sucesso!")

def main():
    """
    Função principal para gerenciar a entrada de dados e exibição de resultados.
    """
    try:
        # Validação do nome do aluno
        while True:
            nome = input("Digite o nome completo do aluno: ")
            if re.match(r'^[A-Za-zÀ-ÿ\s]+$', nome):  # Permite apenas letras com acentos e espaços
                break
            else:
                print("Erro: O nome deve conter apenas letras e espaços. Tente novamente!")

        aluno = Aluno(nome)
        
        # Estrutura contendo um menu simples
        while True:
            print("\nMenu:")
            print("1. Adicionar/Alterar Disciplina")
            print("2. Excluir Disciplina")
            print("3. Exibir Dados do Aluno")
            print("4. Salvar Dados em TXT")
            print("5. Sair")
            opcao = input("Escolha uma opção: ")
            
            # 1 - Add disciplinas ou Alterar
            if opcao == "1":
                print("\nInforme os dados da disciplina:")
                disciplina = input("Digite o nome da disciplina: ")
                portfolio = float(input("Digite a nota do portfólio (0 a 2000): "))
                prova_Presencial = float(input("Digite a nota da prova presencial (0 a 5000): "))
                av_Virtual = float(input("Digite a nota da avaliação virtual final (0 a 3000): "))
                engajamento_AVA = float(input("Digite a nota final do engajamento AVA (0 a 2000): "))
                
                # Validação das notas
                if not (0 <= portfolio <= 2000 and 0 <= prova_Presencial <= 5000 and 
                        0 <= av_Virtual <= 3000 and 0 <= engajamento_AVA <= 2000):
                    print("Notas fora do intervalo permitido. Tente novamente.")
                    continue
                
                # Salva disciplina e notas
                aluno.adicionar_disciplina(disciplina, portfolio, prova_Presencial, av_Virtual, engajamento_AVA)
                print(f"\nDisciplina '{disciplina}' adicionada/atualizada com sucesso!")
            
            # 2 - Exclusão da disciplina
            elif opcao == "2":
                disciplina = input("Digite o nome da disciplina a ser excluída: ")
                if aluno.excluir_disciplina(disciplina):
                    print(f"\nDisciplina '{disciplina}' excluída com sucesso!")
                else:
                    print(f"\nDisciplina '{disciplina}' não encontrada!")
            
            # 3 - Mostra disciplinas
            elif opcao == "3":
                aluno.exibir_dados()
            
            # 4 - Salva em txt
            elif opcao == "4":
                aluno.salvar_em_txt()
            
            # 5 - Finaliza execução
            elif opcao == "5":
                print("Saindo...")
                break
            
            # Caso seja valor errado. 
            else:
                print("Opção inválida. Tente novamente.")

    except ValueError:
        print("Por favor, insira valores válidos para as notas!")

# Executa  o main apenas quando o Python for executado diretamente.
if __name__ == "__main__":
    main()