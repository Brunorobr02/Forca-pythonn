
import random


PALAVRAS = [
    "python", "variavel", "funcao", "repeticao", "compilador",
    "algoritmo", "teclado", "memoria", "programa", "estrutura",
    "decisao", "atribuicao", "terminal", "arquivo", "processador",
]
MAX_ERROS = 6

FORCA = [
    """
   +---+
   |   |
       |
       |
       |
       |
=========""",
    """
   +---+
   |   |
   O   |
       |
       |
       |
=========""",
    """
   +---+
   |   |
   O   |
   |   |
       |
       |
=========""",
    """
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========""",
    """
   +---+
   |   |
   O   |
  /|\\  |
       |
       |
=========""",
    """
   +---+
   |   |
   O   |
  /|\\  |
  /    |
       |
=========""",
    """
   +---+
   |   |
   O   |
  /|\\  |
  / \\  |
       |
=========""",
]



def sortear_palavra():
   
    return random.choice(PALAVRAS)


def montar_palavra_oculta(palavra, letras_certas):

    resultado = ""
    for letra in palavra:
        if letra in letras_certas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado.strip()


def ler_letra(letras_tentadas):
  
    while True:
        entrada = input("Digite uma letra: ").strip().lower()

        if len(entrada) != 1 or not entrada.isalpha():
            print("Entrada inválida. Digite apenas UMA letra.")
        elif entrada in letras_tentadas:
            print("Você já tentou essa letra. Escolha outra.")
        else:
            return entrada


def exibir_estado(palavra, letras_certas, letras_tentadas, erros):
   
    print(FORCA[erros])
    print("\nPalavra:", montar_palavra_oculta(palavra, letras_certas))
    print("Letras tentadas:", " ".join(sorted(letras_tentadas)))
    print(f"Erros: {erros}/{MAX_ERROS}")


def palavra_descoberta(palavra, letras_certas):
    
    for letra in palavra:
        if letra not in letras_certas:
            return False
    return True


# ---------------------------------------------------------------
# UMA PARTIDA COMPLETA
# ---------------------------------------------------------------
def jogar_partida():
    palavra = sortear_palavra()
    letras_certas = []
    letras_tentadas = []
    erros = 0

    print("\n===== NOVA PARTIDA =====")
    print(f"A palavra tem {len(palavra)} letras.")

    while erros < MAX_ERROS and not palavra_descoberta(palavra, letras_certas):
        exibir_estado(palavra, letras_certas, letras_tentadas, erros)
        letra = ler_letra(letras_tentadas)
        letras_tentadas.append(letra)         

        if letra in palavra:
            letras_certas.append(letra)      
            print(f"\nBoa! A letra '{letra}' está na palavra.")
        else:
            erros += 1                       
            print(f"\nErrou! A letra '{letra}' não está na palavra.")

   
    exibir_estado(palavra, letras_certas, letras_tentadas, erros)

    if erros >= MAX_ERROS:
        print(f"\nVocê perdeu! A palavra era: {palavra}")
        return False
    else:
        print(f"\nParabéns, você venceu! A palavra era: {palavra}")
        return True


def main():
    vitorias = 0
    derrotas = 0
    continuar = "s"

    print("===== JOGO DA FORCA =====")

    while continuar == "s":
        if jogar_partida():
            vitorias += 1                   
        else:
            derrotas += 1

        print(f"\nPlacar -> Vitórias: {vitorias} | Derrotas: {derrotas}")
        continuar = input("Jogar novamente? (s/n): ").strip().lower()

    print("\nObrigado por jogar! Até a próxima.")


if __name__ == "__main__":
    main()