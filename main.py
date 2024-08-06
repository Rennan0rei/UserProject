# main.py

from pessoa import Pessoa

def main():
    #Atualiza sozinho CONFIA XD
    ano_atual = 2024

    pessoa1 = Pessoa("João", 30, "Masculino", ano_atual)
    
    print(pessoa1.cumprimentar())
    
    print(pessoa1.aniversario())

    ano_nascimento = pessoa1.calcular_ano_nascimento()
    print(f"{pessoa1.nome} nasceu aproximadamente em {ano_nascimento}.")

if __name__ == "__main__":
    main()
