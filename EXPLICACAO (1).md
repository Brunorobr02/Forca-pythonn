# Explicação da Solução e Reflexão

## 1. Lógica geral

O programa funciona como uma **sequência de instruções que modifica o estado dos dados** passo a passo, que é a ideia central do paradigma imperativo.

O estado de cada partida é guardado em variáveis dentro de `jogar_partida()`:

- `palavra`: a palavra secreta sorteada.
- `letras_certas`: lista das letras já descobertas.
- `letras_tentadas`: lista de todas as letras já chutadas (certas e erradas).
- `erros`: contador de erros, de 0 a 6.

Fora da partida, `main()` guarda o placar em `vitorias` e `derrotas`.

O fluxo é: sortear a palavra, repetir as rodadas (mostrar o estado, ler uma letra, atualizar o estado) até a palavra ser descoberta ou os erros chegarem a 6, mostrar o resultado e perguntar se o jogador quer jogar de novo.

## 2. Elementos do paradigma imperativo no código

### 2.1 Sequência de instruções
Dentro do laço de `jogar_partida()`, cada rodada executa em ordem: exibir o estado, ler a letra, registrá-la como tentada e depois verificar se está na palavra. A ordem importa: a letra só pode ser classificada como acerto ou erro depois de lida e validada.

### 2.2 Variáveis e atribuições (alteração de estado)
O estado muda por atribuições explícitas:

| Instrução | O que muda no estado |
|-----------|----------------------|
| `letras_tentadas.append(letra)` | A letra é registrada como já usada |
| `letras_certas.append(letra)` | Uma letra da palavra é descoberta |
| `erros += 1` | O contador de erros aumenta e a forca avança |
| `vitorias += 1` / `derrotas += 1` | O placar é atualizado |
| `resultado += letra + " "` | A palavra oculta é montada letra a letra |

Exemplo do estado ao longo de uma partida com a palavra "python":

1. Início: `letras_certas = []`, `letras_tentadas = []`, `erros = 0`
2. Jogador digita `p` (acerto): `letras_certas = ['p']`, `letras_tentadas = ['p']`, `erros = 0`
3. Jogador digita `z` (erro): `letras_certas = ['p']`, `letras_tentadas = ['p', 'z']`, `erros = 1`
4. A palavra oculta passa a ser exibida como `p _ _ _ _ _`

### 2.3 Estruturas de decisão
- **`ler_letra()`**: cadeia `if / elif / else` que recusa entradas com mais de um caractere ou não alfabéticas, recusa letras repetidas e aceita as demais.
- **`jogar_partida()`**: `if letra in palavra` decide entre acerto e erro; no final, `if erros >= MAX_ERROS` decide entre vitória e derrota.
- **`montar_palavra_oculta()`**: para cada letra, decide se mostra a letra ou o traço `_`.
- **`palavra_descoberta()`**: retorna `False` assim que encontra uma letra ainda não descoberta.

### 2.4 Estruturas de repetição
- **`while erros < MAX_ERROS and not palavra_descoberta(...)`**: o laço principal da partida, que repete enquanto o jogo não terminou.
- **`while True` (em `ler_letra`)**: repete a leitura até receber uma letra válida e inédita.
- **`while continuar == "s"` (em `main`)**: permite várias partidas seguidas.
- **`for letra in palavra`**: percorre a palavra em `montar_palavra_oculta()` e `palavra_descoberta()`.

### 2.5 Funções (procedimentos)
O código foi dividido em funções com responsabilidade única:

- `sortear_palavra`: escolhe a palavra secreta.
- `montar_palavra_oculta`: gera o texto com letras descobertas e traços.
- `ler_letra`: lê e valida a entrada do jogador.
- `exibir_estado`: mostra a forca, a palavra, as letras tentadas e os erros.
- `palavra_descoberta`: verifica se o jogador venceu.
- `jogar_partida`: controla uma partida completa e devolve se foi vitória ou derrota.
- `main`: controla o placar e as repetições de partidas.

Isso deixa o código mais legível e fácil de testar e manter.

## 3. Reflexão sobre o desenvolvimento

### Principais decisões
- **Tema**: escolhi o jogo da forca porque a regra é conhecida, o estado muda a cada jogada e isso fica bem visível no vídeo.
- **Estruturas de dados**: usei listas para as letras e uma lista de strings para os desenhos da forca, indexada pelo número de erros. Assim, `FORCA[erros]` mostra o desenho certo sem precisar de vários `if`.
- **Validação de entrada**: letras repetidas ou entradas inválidas não contam como erro, para não punir o jogador injustamente.
- **Divisão em funções**: separei a lógica de uma partida do controle do placar, para organizar melhor o código.

### Dificuldades encontradas
- *(Edite com a sua experiência real. Exemplos:)*
- Fazer a palavra oculta ser atualizada corretamente quando a mesma letra aparece em várias posições.
- Evitar que letras repetidas ou entradas inválidas fossem contadas como erro.
- Escrever o desenho da forca corretamente, já que a barra invertida `\` precisa ser escrita como `\\` dentro de strings em Python.

### Possíveis melhorias
- Ler as palavras de um arquivo de texto, com categorias e dicas.
- Adicionar níveis de dificuldade (palavras curtas e longas).
- Aceitar palavras com acento.
- Permitir que o jogador tente adivinhar a palavra inteira.
- Modo para dois jogadores, em que um digita a palavra e o outro adivinha.

## 4. Contribuição dos integrantes

- **Integrante 1**: Artur Zavarise Deprá
- **Integrante 2**: Bruno Brunoro dos Santos
- **Integrante 3**: Davi Resplandes de Sousa Marques
