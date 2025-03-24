import os  # Manipular arquivos TXT
import re  # Validar nomes com apenas letras e espaços

class Aluno:
    
    # Inicializa aluno e dicionário de disciplinas
    def __init__(self, nome):
        self.nome = nome
        self.disciplinas = {}

    # Adiciona disciplinas com opção de portfólio
    def adicionar_disciplina(self, disciplina, tem_portfolio, portfolio, prova_Presencial, av_Virtual, engajamento_AVA):
        total = portfolio + prova_Presencial + av_Virtual + engajamento_AVA
        nota_final = min(total / 1000, 10)
        self.disciplinas[disciplina] = {
            "tem_portfolio": tem_portfolio,
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

    # Exibir dados cadastrados
    def exibir_dados(self):
        print(f"\nAluno: {self.nome}")
        if not self.disciplinas:
            print("Nenhuma disciplina cadastrada.")
        else:
            for disciplina, notas in self.disciplinas.items():
                print(f"\nDisciplina: {disciplina}")
                
                # Exibe portfólio apenas se a disciplina tiver
                if notas["tem_portfolio"]:
                    print(f"  - Portfólio: {notas['portfolio']:.0f}")
                
                print(f"  - Prova Presencial: {notas['prova_Presencial']:.0f}")
                print(f"  - Avaliação Virtual: {notas['av_Virtual']:.0f}")
                print(f"  - Engajamento AVA: {notas['engajamento_AVA']:.0f}")
                print(f"  - Nota Final: {notas['nota_Final']:.2f}")

    # Salva os dados em um arquivo .txt
    def salvar_em_txt(self):
        nome_arquivo = f"{self.nome.replace(' ', '_')}.txt"
        
        modo_abertura = "a" if os.path.exists(nome_arquivo) else "w"
        cabecalho = "\nDisciplinas e Notas Adicionadas:\n" if os.path.exists(nome_arquivo) else f"Aluno: {self.nome}\n\nDisciplinas e Notas:\n"
        
        with open(nome_arquivo, modo_abertura) as arquivo:
            arquivo.write(cabecalho)
            for disciplina, dados in self.disciplinas.items():
                arquivo.write(f"\nDisciplina: {disciplina}\n")
                
                if dados['tem_portfolio']:
                    arquivo.write(f"  - Portfólio: {dados['portfolio']:.0f}\n")
                
                arquivo.write(f"  - Prova Presencial: {dados['prova_Presencial']:.0f}\n")
                arquivo.write(f"  - Avaliação Virtual: {dados['av_Virtual']:.0f}\n")
                arquivo.write(f"  - Engajamento AVA: {dados['engajamento_AVA']:.0f}\n")
                arquivo.write(f"  - Nota Final: {dados['nota_Final']:.2f}\n")

        print(f"Novas disciplinas salvas no arquivo '{nome_arquivo}' com sucesso!")

# Menu usado para interagir com o usuário
def menu():
    print("\nMenu:")
    print("1. Adicionar/Alterar Disciplina")
    print("2. Excluir Disciplina")
    print("3. Exibir Dados do Aluno")
    print("4. Salvar Dados em TXT")
    print("5. Sair")
            
def main():
    try:
        # Validação do nome do aluno
        while True:
            nome = input("Digite o nome completo do aluno: ")
            if re.match(r'^[A-Za-zÀ-ÿ\s]+$', nome):  
                break
            else:
                print("Erro: O nome deve conter apenas letras e espaços. Tente novamente!")

        aluno = Aluno(nome)
        
        # Estrutura contendo um menu simples
        while True:
            menu()
            opcao = input("Escolha uma opção: ")
            
            # 1 - Adicionar ou Alterar disciplina
            if opcao == "1":
                print("\nInforme os dados da disciplina:")
                disciplina = input("Digite o nome da disciplina: ")
                
                print("Sua disciplina tem portfólio? (S/N)")
                port = input("Digite S ou N: ").strip().upper()
                
                tem_portfolio = port == "S"
                portfolio = 0
                
                if tem_portfolio:
                    portfolio = float(input("Digite a nota do portfólio (0 a 2000): "))
                    prova_Presencial = float(input("Digite a nota da prova presencial (0 a 5000): "))
                    av_Virtual = float(input("Digite a nota da avaliação virtual final (0 a 3000): "))
                    engajamento_AVA = float(input("Digite a nota final do engajamento AVA (0 a 2000): "))
                    
                    # Validação das notas com portfólio
                    if not (0 <= portfolio <= 2000 and 0 <= prova_Presencial <= 5000 and 
                            0 <= av_Virtual <= 3000 and 0 <= engajamento_AVA <= 2000):
                        print("****************************************************************")
                        print("Notas fora do intervalo permitido. Tente novamente.")
                        print("****************************************************************")
                        continue
                
                else:
                    prova_Presencial = float(input("Digite a nota da prova presencial (0 a 5000): "))
                    av_Virtual = float(input("Digite a nota da avaliação virtual final (0 a 5000): "))
                    engajamento_AVA = float(input("Digite a nota final do engajamento AVA (0 a 2000): "))
                    
                    # Validação das notas sem portfólio
                    if not (0 <= prova_Presencial <= 5000 and 
                            0 <= av_Virtual <= 5000 and 0 <= engajamento_AVA <= 2000):
                        print("****************************************************************")
                        print("Notas fora do intervalo permitido. Tente novamente.")
                        print("****************************************************************")
                        continue
                
                # Adiciona disciplina com a nova estrutura
                aluno.adicionar_disciplina(disciplina, tem_portfolio, portfolio, prova_Presencial, av_Virtual, engajamento_AVA)
                print(f"\nDisciplina '{disciplina}' adicionada/atualizada com sucesso!")
            
            # 2 - Excluir disciplina
            elif opcao == "2":
                disciplina = input("Digite o nome da disciplina a ser excluída: ")
                if aluno.excluir_disciplina(disciplina):
                    print(f"\nDisciplina '{disciplina}' excluída com sucesso!")
                else:
                    print(f"\nDisciplina '{disciplina}' não encontrada!")
            
            # 3 - Exibir dados do aluno
            elif opcao == "3":
                aluno.exibir_dados()
            
            # 4 - Salvar dados em TXT
            elif opcao == "4":
                aluno.salvar_em_txt()
            
            # 5 - Sair do programa
            elif opcao == "5":
                print("Saindo...")
                break
            
            else:
                print("Opção inválida. Tente novamente.")

    except ValueError:
        print("Por favor, insira valores válidos para as notas!")

# Executa o main apenas quando o script for executado diretamente
if __name__ == "__main__":
    main()