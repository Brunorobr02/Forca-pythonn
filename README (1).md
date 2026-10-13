# Jogo da Forca em Python

Atividade Avaliativa AV1 – **Paradigmas de Programação**
Universidade da Amazônia (UNAMA) – Ciência da Computação
Professor: Rodrigo Medeiros Costa

## Integrantes

| Nome | GitHub | Contribuição |
|------|--------|--------------|
| Artur Deprá | @slipperyking | Vídeo |
| Bruno Brunoro | @Brunorobr02 | Código |
| Davi Resplandes | @daviresplandes | README |

## Descrição do problema

O jogo da forca é um jogo de adivinhação de palavras. O computador escolhe uma palavra secreta e o jogador tenta descobri-la chutando uma letra por vez. Cada letra errada aproxima o jogador da derrota, representada pelo desenho de um boneco na forca.

Este projeto implementa o jogo em **terminal**, usando o paradigma imperativo: o estado do jogo (letras descobertas, letras tentadas e número de erros) é modificado a cada jogada por uma sequência de instruções.

### Entradas
- Uma letra por rodada (texto de um caractere)
- Resposta "s" ou "n" para jogar novamente

### Regras principais
- O programa sorteia uma palavra de uma lista pré-definida.
- A palavra aparece oculta, com um traço `_` para cada letra ainda não descoberta.
- O jogador digita uma letra por vez:
  - Se a letra está na palavra, ela é revelada em todas as posições.
  - Se não está, o número de erros aumenta e o desenho da forca avança.
- O jogador pode errar no máximo **6 vezes**.
- Letras repetidas, números, símbolos ou mais de um caractere são recusados sem penalizar o jogador.
- A partida termina quando a palavra é descoberta (vitória) ou quando os 6 erros são atingidos (derrota).
- O programa mantém um placar de vitórias e derrotas entre as partidas.

### Resultados esperados
- Desenho da forca atualizado a cada erro
- Palavra parcialmente revelada e lista de letras já tentadas
- Mensagem de vitória ou derrota, revelando a palavra secreta
- Placar acumulado e opção de jogar novamente

## Requisitos

- Python 3.8 ou superior (usa apenas o módulo `random`, que já vem com o Python; não precisa instalar nada)

## Como executar

1. Clone o repositório:
   ```bash
   git clone LINK-DO-SEU-REPOSITORIO
   cd NOME-DA-PASTA
   ```
2. Execute o programa:
   ```bash
   python forca.py
   ```
   (em alguns sistemas, use `python3 forca.py`)
3. Digite uma letra por vez e pressione Enter.

## Exemplo de uso

```
===== NOVA PARTIDA =====
A palavra tem 6 letras.

   +---+
   |   |
       |
       |
       |
       |
=========

Palavra: _ _ _ _ _ _
Letras tentadas:
Erros: 0/6
Digite uma letra: p

Boa! A letra 'p' está na palavra.
```

## Vídeo de demonstração

[Assistir ao vídeo](https://drive.google.com/file/d/1G7dRfZAmPoaIlpC2cZJJeqy12WwBi8vY/view?usp=sharing)

## Explicação da solução

A explicação detalhada dos elementos do paradigma imperativo, junto com a reflexão sobre o desenvolvimento, está no arquivo [EXPLICACAO.md](EXPLICACAO.md).

## Estrutura do repositório

```
.
├── forca.py        # código-fonte
├── README.md       # este arquivo
└── EXPLICACAO.md   # explicação da solução e reflexão
```
