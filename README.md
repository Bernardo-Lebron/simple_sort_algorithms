<img width="1200" height="300" alt="image" src="https://github.com/user-attachments/assets/919963f1-5b07-4d12-8862-191073dde33c" />


# Comparativo de Desempenho: Algoritmos de Ordenação Simples

Este repositório contém um ambiente de benchmarking experimental para analisar e comparar o desempenho de quatro algoritmos de ordenação simples: **Selection Sort**, **Insertion Sort**, **Gnome Sort** e **Bubble Sort**.

Os algoritmos são implementados em múltiplas linguagens de programação e avaliados sob diferentes tamanhos de entrada e cenários de ordenação, com o objetivo de verificar empiricamente as previsões teóricas de complexidade computacional.

Trabalho prático da disciplina de **Algoritmos e Estruturas de Dados I**
**CEFET-MG — Campus V, Divinópolis**

&nbsp;

## 📋 Sumário

1. O que são Métodos de Ordenação?
2. Contextualização dos Algoritmos Simples
3. Objetivos
4. Estrutura do Projeto
5. Algoritmos Analisados
   - 5.1. Selection Sort
   - 5.2. Insertion Sort
   - 5.3. Gnome Sort
   - 5.4. Bubble Sort
6. Metodologia Experimental
7. Equipe e Colaboradores

&nbsp;


## 🤔 1. O que são Métodos de Ordenação?

Métodos de ordenação são algoritmos computacionais utilizados para reorganizar os elementos de uma estrutura de dados segundo uma ordem determinada — normalmente crescente ou decrescente. Formalmente, dado um vetor `A = [a₁, a₂, ..., aₙ]`, o objetivo é produzir uma permutação `A' = [a'₁, a'₂, ..., a'ₙ]` tal que:

```
a'₁ ≤ a'₂ ≤ ... ≤ a'ₙ
```

A ordenação é um dos problemas mais fundamentais e estudados da Ciência da Computação. Está presente de forma ubíqua em aplicações que envolvem busca binária, indexação em bancos de dados, compressão de dados e pré-processamento para algoritmos mais complexos. Dados previamente ordenados permitem operações de busca em tempo **O(log n)**, em contraste com a busca linear **O(n)** necessária em conjuntos desordenados.

Os algoritmos de ordenação podem ser classificados segundo diversas propriedades:

| Propriedade | Descrição |
|---|---|
| **Estabilidade** | Preserva a ordem relativa de elementos com valores iguais |
| **In-place** | Opera diretamente na estrutura original, sem memória auxiliar proporcional à entrada |
| **Adaptatividade** | Aproveita ordenação prévia parcial para reduzir o número de operações |
| **Complexidade** | Custo assintótico de tempo e espaço em função do tamanho da entrada |

&nbsp;


## 📌 2. Contextualização dos Algoritmos Simples

Os algoritmos de ordenação simples — também chamados de algoritmos elementares ou quadráticos — constituem a classe mais básica de métodos de ordenação baseados em comparação. Pertencem à categoria **O(n²)** no caso médio e pior caso, o que os torna inadequados para grandes volumes de dados, mas valiosos sob outras perspectivas.

**Por que estudá-los?**

- **Didática:** a lógica de funcionamento é direta e facilmente compreensível, sendo ideal para introduzir conceitos de análise de algoritmos, invariantes de laço e complexidade assintótica.
- **Eficiência em entradas pequenas:** para `N` pequeno (tipicamente `N ≤ 50`), o overhead reduzido desses algoritmos pode torná-los competitivos ou até superiores a métodos mais sofisticados.
- **Adaptatividade:** alguns algoritmos simples, como Insertion Sort e Bubble Sort com parada antecipada, degradam para **O(n)** em entradas já ordenadas ou quase ordenadas — o que é explorado por algoritmos híbridos modernos como o **TimSort**.
- **Base de comparação:** compreender o comportamento dos algoritmos simples é pré-requisito para avaliar criticamente o ganho obtido por algoritmos mais eficientes.

Os algoritmos analisados neste projeto compartilham as seguintes características gerais:

| Característica | Valor típico |
|---|---|
| Complexidade de tempo (médio/pior) | O(n²) |
| Complexidade de espaço | O(1) — in-place |
| Estabilidade | Varia por algoritmo |
| Paradigma | Ordenação por comparação iterativa |

&nbsp;


## 🎯 3. Objetivos

O objetivo central deste projeto é realizar uma **análise empírica e comparativa** dos algoritmos de ordenação simples, verificando na prática as previsões teóricas de complexidade computacional e quantificando o impacto de diferentes linguagens de programação sobre o tempo de execução.

De forma específica, o projeto busca:

- Implementar cada algoritmo em múltiplas linguagens, mantendo a **mesma lógica algorítmica** em todas elas, de modo que as diferenças de desempenho sejam atribuídas ao ambiente de execução e não a variações de implementação;
- Comparar o comportamento dos algoritmos nos três cenários clássicos: **melhor caso**, **caso médio** e **pior caso**;
- Avaliar o impacto dos níveis de otimização de compilador (`-O0` e `-O3`) sobre linguagens compiladas;
- Analisar criticamente os resultados, identificando comportamentos esperados e anomalias.

Os experimentos foram conduzidos com três cenários de entrada para cada tamanho `N`:

| Cenário | Descrição | Caso do algoritmo |
|---|---|---|
| Crescente | Vetor já ordenado | Melhor caso — O(n) ou O(n²) |
| Aleatório | Vetor embaralhado | Caso médio — O(n²) |
| Decrescente | Vetor invertido | Pior caso — O(n²) |

&nbsp;


## 📂 4. Estrutura do Projeto

O projeto está organizado de forma que cada algoritmo possua sua respectiva pasta independente, viabilizando o desenvolvimento paralelo pela equipe via Git.

```text
.
selection_sort/
├── c/
│   └── selection.c
├── cpp/
│   └── selection.cpp
├── dados/
│   ├── aleatorio.txt
│   ├── crescente.txt
│   └── decrescente.txt
├── javascript/
│   └── selection.js
├── python/
│   └── selection.py
├── rust/
│   └── selection.rs
└── makefile
├── insertion_sort/       # 📂 Insertion Sort
│   ├── ...
├── gnome_sort/           # 📂 Gnome Sort
│   ├── ...
├── bubble_sort/          # 📂 Bubble Sort (Algoritmo Adicional)
│   ├── c/
│   │   └── bubble_sort.c
│   ├── cpp/
│   │   └── bubble_sort.cpp
│   ├── rust/
│   │   └── bubble_sort.rs
│   ├── js/
│   │   └── bubble_sort.js
│   ├── python/
│   │   └── bubble_sort.py
│   └── makefile
├── data/                 # 📂 Arquivos de entrada
│   ├── crescente.txt
│   ├── aleatorio.txt
│   └── decrescente.txt
└── README.md
```

&nbsp;


## 5. Algoritmos Analisados

### 📊 5.1. Selection Sort

O Selection Sort é um algoritmo de ordenação por comparação que opera sob o paradigma de **seleção do mínimo**: a cada iteração `i`, o algoritmo percorre o subarray não ordenado `A[i..n-1]`, identifica o índice do menor elemento e o posiciona definitivamente na posição `i` por meio de uma única troca. Esse processo se repete por `n-1` iterações até que todo o array esteja ordenado.

A principal característica que diferencia o Selection Sort dos demais algoritmos simples é o uso exclusivo de **swapping** (troca direta de posições), em oposição ao **shifting** (deslocamento encadeado de elementos). Isso garante no máximo `O(n)` trocas no total, independentemente da distribuição dos dados — propriedade vantajosa quando a operação de escrita em memória tem custo elevado, como em memórias flash e dispositivos embarcados.

#### Pseudocódigo

```
FUNCAO SELECTION_SORT
  ENTRADA: VETOR de tamanho N
  SAIDA  : VETOR ordenado em ordem crescente

  PARA i DE 0 ATE N - 2 FACA
    MIN_IDX <- i

    PARA j DE i + 1 ATE N - 1 FACA
      SE VETOR[j] < VETOR[MIN_IDX] ENTAO
        MIN_IDX <- j
      FIM SE
    FIM PARA

    SE MIN_IDX != i ENTAO
      AUXILIAR        <- VETOR[i]
      VETOR[i]        <- VETOR[MIN_IDX]
      VETOR[MIN_IDX]  <- AUXILIAR
    FIM SE
  FIM PARA

  RETORNE VETOR
FIM FUNCAO
```

#### Complexidade

O número de comparações realizadas é fixo e independente da distribuição dos dados, calculado pelo somatório:

```
C(n) = Σ (n - i - 1) para i de 0 até n-2  =  n(n-1)/2
```

Por isso, o Selection Sort apresenta complexidade **Θ(n²)** em todos os casos — não existe melhor caso em número de comparações.

| Caso | Comparações | Trocas | Complexidade |
|---|---:|---:|---:|
| Melhor caso | n(n−1)/2 | 0 | Θ(n²) |
| Caso médio | n(n−1)/2 | O(n) | Θ(n²) |
| Pior caso | n(n−1)/2 | n − 1 | Θ(n²) |

**Complexidade espacial:** O(1) — ordenação in-place, sem memória auxiliar proporcional à entrada.

#### Propriedades

| Propriedade | Valor | Justificativa |
|---|---|---|
| **Estável** | ❌ Não | A troca do mínimo com `A[i]` pode inverter a ordem relativa de elementos iguais |
| **In-place** | ✅ Sim | Usa apenas variáveis auxiliares temporárias (índice do mínimo e variável de troca) |
| **Adaptativo** | ❌ Não | O laço interno sempre percorre `A[i..n-1]` por completo, mesmo que o array já esteja ordenado |

> **Nota sobre não-adaptatividade:** diferente do Insertion Sort — que degrada para O(n) em entradas já ordenadas — o Selection Sort realiza exatamente `n(n-1)/2` comparações em qualquer cenário. Essa característica é confirmada empiricamente nos resultados: os tempos dos cenários crescente e aleatório são praticamente idênticos.

#### Linguagens e Estruturas de Dados

Todas as implementações seguem a mesma lógica algorítmica, garantindo que as diferenças de desempenho sejam atribuídas exclusivamente ao ambiente de execução.

| Linguagem | Estrutura interna | Tipo do elemento | Modelo de execução |
|---|---|---|---|
| C | `double[]` alocado com `malloc` | `double` (64 bits) | Compilada — gcc |
| C++ | `std::vector<double>` | `double` (64 bits) | Compilada — g++ |
| Rust | `Vec<f64>` | `f64` (64 bits) | Compilada — rustc (LLVM) |
| JavaScript | `Array` (SMI/float64 otimizado pelo V8) | Number (float64) | JIT — Node.js / V8 |
| Python | `list` (referências a objetos PyObject) | `float` | Interpretada — CPython |

> A estrutura `list` do Python armazena **referências a objetos genéricos**, adicionando uma camada de indireção em cada acesso e comparação — principal fator do desempenho inferior dessa linguagem nos benchmarks. O Rust utiliza o método nativo `.swap()` de `Vec`, que o compilador otimiza para instruções de swap em registrador, sem acesso à memória intermediária.

#### Ambiente Experimental

| Componente | Especificação |
|---|---|
| Processador | Intel Core i3-1315U (1.20 GHz) |
| Memória RAM | 8 GB |
| Sistema Operacional | Windowns 11 - WSL |
| Compilador C | GCC — flags `-O0` (sem otimização) e `-O3` (máxima otimização) |
| Compilador C++ | G++ — flags `-O0` e `-O3` |
| Compilador Rust | rustc — `opt-level=0` e `opt-level=3` |
| Runtime JavaScript | Node.js (motor V8 com JIT) |
| Interpretador Python | CPython 3.12.11 |

**Medição de tempo por linguagem:**

| Linguagem | Função utilizada | Precisão |
|---|---|---|
| C | `clock()` / `CLOCKS_PER_SEC` | Microssegundos |
| C++ | `std::chrono::high_resolution_clock` | Nanossegundos |
| Rust | `std::time::Instant::now()` / `.elapsed()` | Nanossegundos |
| JavaScript | `process.hrtime.bigint()` | Nanossegundos |
| Python | `time.time()` | Microssegundos |

#### Dataset

Os experimentos utilizam arquivos de entrada gerados previamente, localizados em `dados/`:

| Arquivo | Conteúdo | Cenário |
|---|---|---|
| `crescente.txt` | Inteiros ordenados de forma crescente | Melhor caso em trocas |
| `aleatorio.txt` | Inteiros em ordem aleatória (0 a 999.999) | Caso médio |
| `decrescente.txt` | Inteiros ordenados de forma decrescente | Pior caso em trocas |

Cada arquivo contém **1.000.000 de linhas** (um inteiro por linha). Os experimentos utilizam as primeiras `N` linhas do arquivo, controlado pelo parâmetro `N` do Makefile.

#### Resultados

**N = 10² e N = 10³ (tempos em segundos)**

| Linguagem | Otimiz. | Crescente | Aleatório | Decrescente |
|---|---|---:|---:|---:|
| **N = 10²** | | | | |
| C | -O0 | 0.000000 | 0.000004 | 0.000004 |
| C | -O3 | 0.000000 | 0.000002 | 0.000002 |
| C++ | -O0 | 0.000000 | 0.000012 | 0.000010 |
| C++ | -O3 | 0.000000 | 0.000002 | 0.000002 |
| Rust | sem | 0.000000 | 0.000025 | 0.000027 |
| Rust | com | 0.000000 | 0.000003 | 0.000002 |
| JavaScript | V8 JIT | 0.000300 | 0.000300 | 0.000600 |
| Python | N/A | 0.000100 | 0.000100 | 0.000100 |
| **N = 10³** | | | | |
| C | -O0 | 0.000400 | 0.000400 | 0.000400 |
| C | -O3 | 0.000200 | 0.000200 | 0.000200 |
| C++ | -O0 | 0.001000 | 0.001200 | 0.001000 |
| C++ | -O3 | 0.000200 | 0.000200 | 0.000200 |
| Rust | sem | 0.002400 | 0.002500 | 0.002700 |
| Rust | com | 0.000200 | 0.000300 | 0.000200 |
| JavaScript | V8 JIT | 0.009300 | 0.002200 | 0.002200 |
| Python | N/A | 0.009600 | 0.008900 | 0.008900 |

**N = 10⁴ e N = 10⁵ (tempos em segundos)**

| Linguagem | Otimiz. | Crescente | Aleatório | Decrescente |
|---|---|---:|---:|---:|
| **N = 10⁴** | | | | |
| C | -O0 | 0.0377 | 0.0692 | 0.0420 |
| C | -O3 | 0.0167 | 0.0053 | 0.0207 |
| C++ | -O0 | 0.1225 | 0.1074 | 0.1070 |
| C++ | -O3 | 0.0213 | 0.0404 | 0.0198 |
| Rust | sem | 0.2882 | 0.2543 | 0.2544 |
| Rust | com | 0.0245 | 0.0432 | 0.0263 |
| JavaScript | V8 JIT | 0.0415 | 0.0793 | 0.0530 |
| Python | N/A | 0.8565 | 1.6155 | 0.9334 |
| **N = 10⁵** | | | | |
| C | -O0 | 3.9520 | 4.1242 | 4.1141 |
| C | -O3 | 2.0500 | 3.5188 | 1.9618 |
| C++ | -O0 | 10.2689 | 10.3148 | 10.3462 |
| C++ | -O3 | 2.1247 | 3.5188 | 1.9089 |
| Rust | sem | 24.498 | 25.153 | 24.694 |
| Rust | com | 2.3265 | 4.2560 | 2.1320 |
| JavaScript | V8 JIT | 3.5835 | 6.6564 | 3.5851 |
| Python | N/A | 93.164 | 164.890 | 98.378 |

> `N = 10⁶` foi executado apenas para linguagens compiladas com `-O3`. Python foi descartado por tempo estimado superior a 10 horas.

**N = 10⁶ — apenas linguagens compiladas com otimização**

| Linguagem | Crescente | Aleatório | Decrescente |
|---|---:|---:|---:|
| C (-O3) | 201.24 | 208.13 | 213.05 |
| C++ (-O3) | 201.54 | 237.43 | 217.39 |
| Rust (com) | 251.39 | 271.34 | 256.24 |
| JavaScript | 365.82 | 388.34 | 366.47 |

#### Análise dos Resultados

**Não-adaptatividade confirmada empiricamente:**
Os tempos dos cenários crescente e aleatório são praticamente idênticos para todas as linguagens compiladas. Em C com `-O3` para N = 10⁵, o cenário crescente levou 2.0500 s e o aleatório 3.5188 s — a diferença decorre da ausência de trocas no cenário crescente, não da redução de comparações. Isso confirma que o número de comparações é sempre `n(n-1)/2`, independentemente da entrada.

**Impacto da otimização de compilador:**
A flag `-O3` reduziu o tempo em C de 4.1242 s para 3.5188 s para N = 10⁵ no cenário aleatório — ganho de ~15%. No Rust, o impacto foi mais expressivo: de 25.153 s para 4.256 s (speedup de ~6×), pois em `opt-level=0` o compilador mantém verificações de *bounds checking* que são eliminadas com otimização.

**Hierarquia de desempenho:**
`C -O3 ≈ C++ -O3 < Rust (com) < JavaScript < Python`

O JavaScript (V8 JIT) se manteve competitivo até N = 10⁵, superando o Rust sem otimização. O Python foi inviável para N ≥ 10⁵ em cenário prático.

#### Gráficos

Os gráficos abaixo mostram o tempo de execução por linguagem nos três cenários:

| Melhor Caso (Crescente) | Caso Médio (Aleatório) | Pior Caso (Decrescente) |
|:---:|:---:|:---:|
| ![Melhor caso](Graficos%20SelectionSort/Melhor%20caso.png) | ![Caso médio](Graficos%20SelectionSort/Caso%20m%C3%A9dio.png) | ![Pior caso](Graficos%20SelectionSort/Pior%20Caso.png) |

#### Compilação e Execução

> **Requisito:** Linux com `gcc`, `g++`, `rustc`, `node` e `python3` instalados.

```bash
cd selection_sort

make clean          # Remove binários anteriores
make                # Compila C, C++ e Rust (sem otimização por padrão)
make run N=10000    # Executa o benchmark para N = 10.000 elementos
```

Para executar **com otimização máxima**, edite o `Makefile` e altere as flags:

```makefile
CFLAGS    = -O3
CXXFLAGS  = -O3
RUSTFLAGS = -C opt-level=3
```

| Comando | Função |
|---|---|
| `make clean` | Remove os binários gerados |
| `make` | Compila C, C++ e Rust |
| `make run N=<valor>` | Executa o benchmark completo para `N` elementos |

&nbsp;



### 🃏 5.2. Insertion Sort

O Insertion Sort é um algoritmo de ordenação por comparação baseado no paradigma de **inserção incremental**. A cada iteração, o algoritmo assume que a porção esquerda do vetor já está ordenada e insere o próximo elemento na posição correta, deslocando os elementos maiores uma posição para frente.

Seu funcionamento é inspirado na forma como cartas são organizadas manualmente em um baralho: cada nova carta é inserida na posição adequada entre as cartas já ordenadas.

A principal característica do Insertion Sort é sua natureza **adaptativa**. Diferentemente de algoritmos quadráticos como o Selection Sort, ele consegue aproveitar entradas já parcialmente ordenadas, reduzindo significativamente a quantidade de operações realizadas.

Além disso, o algoritmo utiliza principalmente operações de **shifting** (deslocamento de elementos), ao invés de trocas diretas sucessivas.

---

### Pseudocódigo

```text
FUNCAO INSERTION_SORT
  ENTRADA: VETOR de tamanho N
  SAIDA  : VETOR ordenado em ordem crescente

  PARA i DE 1 ATE N - 1 FACA

    CHAVE <- VETOR[i]
    j <- i - 1

    ENQUANTO j >= 0 E VETOR[j] > CHAVE FACA
      VETOR[j + 1] <- VETOR[j]
      j <- j - 1
    FIM ENQUANTO

    VETOR[j + 1] <- CHAVE

  FIM PARA

  RETORNE VETOR
FIM FUNCAO
```

### Complexidade

O desempenho do Insertion Sort depende diretamente da organização prévia dos dados.

| Caso        | Comparações | Movimentações | Complexidade |
| ----------- | ----------: | ------------: | -----------: |
| Melhor caso |        O(n) |          O(1) |         Θ(n) |
| Caso médio  |       O(n²) |         O(n²) |        Θ(n²) |
| Pior caso   |       O(n²) |         O(n²) |        Θ(n²) |

**Complexidade espacial:** O(1) — algoritmo in-place, sem memória auxiliar proporcional à entrada.

---

### Propriedades

| Propriedade    | Valor | Justificativa                                             |
| -------------- | ----- | --------------------------------------------------------- |
| **Estável**    | ✅ Sim | Elementos iguais mantêm a ordem relativa original         |
| **In-place**   | ✅ Sim | Utiliza apenas variáveis auxiliares simples               |
| **Adaptativo** | ✅ Sim | Aproveita entradas já ordenadas ou parcialmente ordenadas |

> **Nota sobre adaptatividade:** diferente do Selection Sort, o Insertion Sort reduz significativamente sua quantidade de operações quando os dados já estão ordenados. Isso foi confirmado experimentalmente pelos tempos extremamente baixos obtidos no cenário crescente.

---

### Linguagens e Estruturas de Dados

Todas as implementações seguem exatamente a mesma lógica algorítmica, garantindo que as diferenças observadas estejam relacionadas principalmente ao ambiente de execução, compilador e otimizações aplicadas.

| Linguagem  | Estrutura interna | Tipo do elemento | Modelo de execução       |
| ---------- | ----------------- | ---------------- | ------------------------ |
| C          | `int[]` estático  | `int` (32 bits)  | Compilada — gcc          |
| C++        | `int[]` estático  | `int` (32 bits)  | Compilada — g++          |
| Rust       | `Vec<i32>`        | `i32` (32 bits)  | Compilada — rustc (LLVM) |
| JavaScript | `Array`           | `Number`         | JIT — Node.js / V8       |
| Python     | `list`            | `int`            | Interpretada — CPython   |

> O Python apresentou desempenho inferior devido ao overhead da máquina virtual e ao armazenamento de objetos dinâmicos. Já C e C++ obtiveram os melhores resultados após a aplicação de otimizações agressivas de compilação (`-O3`).

---

### Ambiente Experimental

| Componente           | Especificação                                                  |
| -------------------- | -------------------------------------------------------------- |
| Sistema Operacional  | Windows 11                                                     |
| Processador          | Intel Core i5 — 12ª geração                                    |
| Memória RAM          | 16 GB                                                          |
| Armazenamento        | SSD 512 GB                                                     |
| Placa de vídeo       | NVIDIA GeForce RTX 3050                                        |
| Compilador C         | GCC — flags `-O0` (sem otimização) e `-O3` (máxima otimização) |
| Compilador C++       | G++ — flags `-O0` e `-O3`                                      |
| Compilador Rust      | rustc — `opt-level=0` e `opt-level=3`                          |
| Runtime JavaScript   | Node.js (motor V8 com JIT)                                     |
| Interpretador Python | CPython                                                        |

---

### Medição de Tempo

| Linguagem  | Função utilizada                           | Precisão       |
| ---------- | ------------------------------------------ | -------------- |
| C          | `gettimeofday()`                           | Microssegundos |
| C++        | `std::chrono::high_resolution_clock`       | Nanossegundos  |
| Rust       | `std::time::Instant::now()` / `.elapsed()` | Nanossegundos  |
| JavaScript | `process.hrtime.bigint()`                  | Nanossegundos  |
| Python     | `time.perf_counter()`                      | Alta precisão  |

---

### Dataset

Os experimentos utilizam arquivos de entrada gerados previamente:

| Arquivo           | Conteúdo                          | Cenário     |
| ----------------- | --------------------------------- | ----------- |
| `crescente.txt`   | Inteiros ordenados crescentemente | Melhor caso |
| `aleatorio.txt`   | Inteiros aleatórios               | Caso médio  |
| `decrescente.txt` | Inteiros em ordem decrescente     | Pior caso   |

Cada arquivo contém até **1.000.000 de números inteiros**, sendo utilizados subconjuntos de tamanho:

```text
10², 10³, 10⁴, 10⁵ e 10⁶
```

---

## 📊 Resultados Experimentais

### N = 10² e N = 10³ (tempos em segundos)

| Linguagem   | Otimiz. |  Crescente | Aleatório | Decrescente |
| ----------- | ------- | ---------: | --------: | ----------: |
| **N = 10²** |         |            |           |             |
| C           | -O0     |   0.000001 |  0.000004 |    0.000010 |
| C           | -O3     |  0.0000001 |  0.000002 |    0.000003 |
| C++         | -O0     |  0.0000015 |  0.000021 |    0.000040 |
| C++         | -O3     |  0.0000002 | 0.0000021 |   0.0000031 |
| Rust        | sem     |   0.000001 |  0.000015 |    0.000024 |
| Rust        | com     |   0.000000 |  0.000002 |    0.000004 |
| JavaScript  | V8 JIT  |   0.000042 |  0.000219 |    0.000340 |
| Python      | N/A     |   0.000011 |  0.000117 |    0.000196 |
| **N = 10³** |         |            |           |             |
| C           | -O0     |   0.000001 |  0.000271 |    0.000545 |
| C           | -O3     |   0.000001 |  0.000102 |    0.000129 |
| C++         | -O0     | 0.00010072 |  0.002454 |   0.0050692 |
| C++         | -O3     |  0.0000002 | 0.0000664 |   0.0001221 |
| Rust        | sem     |   0.000011 |  0.001176 |    0.003093 |
| Rust        | com     |   0.000001 |  0.000095 |    0.000181 |
| JavaScript  | V8 JIT  |   0.000191 |  0.000993 |    0.001215 |
| Python      | N/A     |   0.000107 |  0.010413 |     0.02094 |

---

### N = 10⁴ e N = 10⁵ (tempos em segundos)

| Linguagem   | Otimiz. | Crescente | Aleatório | Decrescente |
| ----------- | ------- | --------: | --------: | ----------: |
| **N = 10⁴** |         |           |           |             |
| C           | -O0     |  0.000014 |  0.025653 |    0.059135 |
| C           | -O3     |  0.000007 |  0.006070 |    0.011672 |
| C++         | -O0     | 0.0000093 |  0.193293 |    0.389041 |
| C++         | -O3     | 0.0000065 | 0.0059649 |   0.0120779 |
| Rust        | sem     |  0.000124 |  0.011176 |    0.223538 |
| Rust        | com     |  0.000008 |  0.008847 |    0.020271 |
| JavaScript  | V8 JIT  |  0.000514 |  0.016374 |    0.032820 |
| Python      | N/A     |  0.000591 |  1.239607 |     2.25077 |
| **N = 10⁵** |         |           |           |             |
| C           | -O0     |  0.000142 |  2.591586 |     5.02298 |
| C           | -O3     |  0.000055 |  0.615683 |    1.188966 |
| C++         | -O0     | 0.0010404 |     18.86 |       37.81 |
| C++         | -O3     | 0.0000634 |  0.587483 |       1.183 |
| Rust        | sem     |  0.001099 |  11.69859 |     23.3430 |
| Rust        | com     |  0.000079 |  0.897895 |    1.774292 |
| JavaScript  | V8 JIT  |  0.000809 |  1.525250 |    3.033301 |
| Python      | N/A     |  0.005321 |   136.295 |     226.560 |

---

> `N = 10⁶` apresentou crescimento extremamente elevado devido à complexidade quadrática `O(n²)` do algoritmo. Em alguns cenários, especialmente sem otimização, os tempos ultrapassaram dezenas de minutos.

### N = 10⁶ (tempos em segundos)

| Linguagem  | Crescente | Aleatório | Decrescente |
| ---------- | --------: | --------: | ----------: |
| C (-O0)    |  0.001413 |   262.592 |      543.40 |
| C (-O3)    |  0.000587 |  60.79153 |      118.26 |
| C++ (-O0)  |  0.009488 |   1832.96 |     3670.49 |
| C++ (-O3)  |  0.000622 |   60.1009 |     119.147 |
| Rust (sem) |  0.011581 |   1123.52 |           — |
| Rust (com) |  0.000861 |  90.24779 |    182.6751 |
| JavaScript |  0.000809 |    152.74 |     312.910 |
| Python     |   0.05369 |         — |           — |

---

## 📈 Análise dos Resultados

### Adaptatividade confirmada empiricamente

Os resultados mostraram claramente a principal característica do Insertion Sort: sua capacidade de aproveitar entradas previamente ordenadas.

Nos cenários crescentes, mesmo para `10⁶` elementos, os tempos permaneceram extremamente baixos, confirmando experimentalmente o melhor caso:

```text id="8vnh5y"
T(n) = O(n)
```

Isso ocorreu porque praticamente não houve deslocamentos internos no vetor.

Já nos cenários aleatórios e decrescentes, o crescimento quadrático tornou-se evidente.

---

### Impacto da otimização de compilador

As otimizações tiveram impacto extremamente significativo em C, C++ e Rust.

O caso mais impressionante ocorreu no C++ utilizando entrada decrescente com `10⁶` elementos:

* Sem otimização (`-O0`): aproximadamente **3670 segundos**
* Com otimização (`-O3`): aproximadamente **119 segundos**

A redução foi superior a **30 vezes**, demonstrando a eficiência das otimizações modernas de compiladores como GCC e LLVM.

Em C, o mesmo cenário caiu de aproximadamente **543 segundos** para **118 segundos**.

---

### Comparação entre linguagens

A hierarquia geral de desempenho observada foi:

```text id="p81i4p"
C (-O3) ≈ C++ (-O3) < Rust (O3) < JavaScript < Python
```

As linguagens compiladas com otimização máxima apresentaram desempenho extremamente próximo.

O JavaScript apresentou resultados surpreendentemente competitivos devido ao motor V8 com compilação JIT.

Já o Python apresentou os maiores tempos de execução devido ao overhead do interpretador e do modelo dinâmico de objetos.

---

### Crescimento quadrático

O crescimento dos tempos tornou-se extremamente elevado entre `10⁵` e `10⁶` elementos nos cenários aleatório e decrescente.

Esse comportamento confirmou experimentalmente a complexidade:

```text id="l0xixm"
T(n) = O(n^2)
```

Por esse motivo, o Insertion Sort torna-se inviável para grandes volumes de dados quando comparado a algoritmos mais eficientes como Merge Sort ou Quick Sort.

---

### Sensibilidade à ordenação prévia

O contraste entre os cenários crescente e decrescente demonstrou claramente a sensibilidade do Insertion Sort à distribuição inicial dos dados.

Enquanto o cenário crescente executou em poucos microssegundos mesmo com `10⁶` elementos, o cenário decrescente exigiu centenas ou até milhares de segundos nas versões sem otimização.

Essa característica explica o uso do Insertion Sort em algoritmos híbridos modernos, principalmente para pequenos subconjuntos parcialmente ordenados.


#### Hierarquia de desempenho

```text
C (-O3) ≈ C++ (-O3) < Rust (O3) < JavaScript < Python
```

As linguagens compiladas com otimização máxima apresentaram desempenho muito próximo entre si.

O JavaScript surpreendeu positivamente devido às otimizações JIT do motor V8, enquanto o Python apresentou os maiores tempos devido ao overhead interpretado.

---

### Gráficos

Os gráficos abaixo mostram o comportamento do algoritmo nos três cenários:

|               Melhor Caso               |               Caso Médio              |              Pior Caso              |
| :-------------------------------------: | :-----------------------------------: | :---------------------------------: |
| ![Melhor Caso](Graficos/MelhorCaso.png) | ![Caso Médio](Graficos/CasoMedio.png) | ![Pior Caso](Graficos/PiorCaso.png) |

---

#### Compilação e Execução

> **Requisito:** Linux com `gcc`, `g++`, `rustc`, `node` e `python3` instalados.

```bash
cd insertion_sort

make clean       # Remove binários anteriores
make             # Compila C, C++ e Rust (com -O3 por padrão)
make run N=100000  # Executa o benchmark completo para N elementos
```

| Comando | Função |
|---|---|
| `make clean` | Remove os binários gerados |
| `make` | Compila C, C++ e Rust |
| `make run N=<valor>` | Executa o benchmark completo para N elementos |


&nbsp;


### 5.3. Gnome Sort

> 🚧 Seção a ser preenchida pelo(a) responsável.

&nbsp;


### 🫧 5.4. Bubble Sort

O Bubble Sort é um algoritmo de ordenação por comparação que opera realizando passagens sucessivas sobre o vetor, comparando pares de elementos adjacentes e efetuando trocas sempre que a condição de desordem é satisfeita (`aᵢ > aᵢ₊₁`). A cada iteração completa, o maior elemento ainda não posicionado é deslocado para sua posição definitiva ao final do subvetor não ordenado — comportamento que origina o nome do algoritmo, em referência ao movimento de "bolhas" ascendentes.

A implementação utiliza **parada antecipada**: uma variável `swapped` detecta a ausência de trocas ao longo de uma passagem completa, encerrando o algoritmo imediatamente caso o vetor já esteja ordenado. Esse mecanismo reduz o melhor caso de O(n²) para **O(n)**.

#### Pseudocódigo

```
FUNCAO BUBBLE_SORT
  ENTRADA: VETOR de tamanho N
  SAIDA  : VETOR ordenado em ordem crescente

  PARA i DE 0 ATE N - 1 FACA
    SWAPPED <- FALSO

    PARA j DE 0 ATE N - i - 2 FACA
      SE VETOR[j] > VETOR[j + 1] ENTAO
        AUXILIAR   <- VETOR[j]
        VETOR[j]   <- VETOR[j + 1]
        VETOR[j+1] <- AUXILIAR
        SWAPPED    <- VERDADEIRO
      FIM SE
    FIM PARA

    SE SWAPPED = FALSO ENTAO
      RETORNE VETOR   // Encerramento antecipado
    FIM SE
  FIM PARA

  RETORNE VETOR
FIM FUNCAO
```

#### Complexidade

| Caso | Comparações | Complexidade |
|---|---|---|
| Melhor caso | n − 1 | O(n) |
| Caso médio | n(n−1)/4 | O(n²) |
| Pior caso | n(n−1)/2 | O(n²) |

**Complexidade espacial:** O(1) — ordenação in-place, sem memória auxiliar proporcional à entrada.

#### Propriedades

| Propriedade | Valor |
|---|---|
| Estável | ✅ Sim — trocas só ocorrem quando `aᵢ > aᵢ₊₁`, nunca entre iguais |
| In-place | ✅ Sim — apenas variáveis auxiliares temporárias |
| Adaptativo | ✅ Sim — com parada antecipada, degrada para O(n) em entradas ordenadas |

#### Linguagens e Estruturas de Dados

| Linguagem | Estrutura interna | Modelo de execução |
|---|---|---|
| C | `int[]` alocado com `malloc` | Compilada — gcc |
| C++ | `std::vector<int>` | Compilada — g++ |
| Rust | `Vec<i32>` | Compilada — LLVM |
| JavaScript | `Array` (SMI otimizado pelo V8) | JIT — Node.js / V8 |
| Python | `list` (referências a objetos) | Interpretada — CPython |

> A estrutura `list` do Python armazena **referências a objetos genéricos**, adicionando uma camada de indireção em cada acesso e comparação — principal fator do desempenho inferior dessa linguagem nos benchmarks.

#### Ambiente Experimental

| Componente | Especificação |
|---|---|
| Processador | Intel Core Ultra 7 155H (até 4,80 GHz) |
| Memória RAM | 16 GB |
| Armazenamento | SSD 512 GB |
| Sistema Operacional | Zorin OS (Linux) |
| Compilador C/C++ | GCC 13.3.0 / G++ 13.3.0 |
| Compilador Rust | rustc (LLVM backend) |
| Runtime JavaScript | Node.js (motor V8) |
| Interpretador Python | CPython 3.12.3 |

As linguagens compiladas (C, C++, Rust) foram testadas em dois níveis de otimização:
- **`-O0`** — sem otimização
- **`-O3`** — otimização máxima

Cada configuração foi executada **5 vezes**; os valores reportados são a **média aritmética** das execuções. O valor `N = 10⁶` foi descartado: o tempo estimado em Python ultrapassaria 10 horas, inviabilizando a coleta estatística.

#### Resultados — Otimização -O3

**N = 10² e N = 10³ (tempos em segundos)**

| Linguagem | Crescente | Aleatório | Decrescente |
|---|---:|---:|---:|
| **N = 10²** | | | |
| C | 0,000000 | 0,000024 | 0,000033 |
| C++ | 0,000000 | 0,000022 | 0,000031 |
| Rust | 0,000000 | 0,000015 | 0,000011 |
| JavaScript | 0,000208 | 0,000232 | 0,001566 |
| Python | 0,000004 | 0,000184 | 0,000242 |
| **N = 10³** | | | |
| C | 0,000001 | 0,001997 | 0,002683 |
| C++ | 0,000001 | 0,001824 | 0,003205 |
| Rust | 0,000002 | 0,000918 | 0,001506 |
| JavaScript | 0,000207 | 0,002347 | 0,002040 |
| Python | 0,000030 | 0,027045 | 0,041739 |

**N = 10⁴ e N = 10⁵ (tempos em segundos)**

| Linguagem | Crescente | Aleatório | Decrescente |
|---|---:|---:|---:|
| **N = 10⁴** | | | |
| C | 0,000006 | 0,137051 | 0,235662 |
| C++ | 0,000008 | 0,162150 | 0,239835 |
| Rust | 0,000009 | 0,053641 | 0,090389 |
| JavaScript | 0,000433 | 0,062382 | 0,067006 |
| Python | 0,000305 | 2,932210 | 3,755458 |
| **N = 10⁵** | | | |
| C | 0,000042 | 20,489569 | 23,568626 |
| C++ | 0,000045 | 21,165759 | 23,919268 |
| Rust | 0,000051 | 13,513529 | 9,231813 |
| JavaScript | 0,001753 | 15,012168 | 6,905683 |
| Python | 0,003504 | 312,509064 | 403,412438 |

#### Impacto das Otimizações de Compilador

**Speedup de -O3 em relação a -O0 (caso médio — entrada aleatória)**

| Linguagem | N = 10² | N = 10³ | N = 10⁴ | N = 10⁵ |
|---|---:|---:|---:|---:|
| C | 1,28× | 0,90× | 0,95× | 1,13× |
| C++ | 2,01× | 2,88× | 2,73× | 2,08× |
| Rust | 13,55× | 16,51× | 23,19× | 9,10× |
| JavaScript | 1,08× | 1,04× | 1,05× | 0,98× |
| Python | 1,08× | 1,16× | 1,05× | 1,01× |

**Destaques da análise:**

- **Rust** foi a linguagem que mais se beneficiou da otimização — speedup de até **23×** em N = 10⁴. Em `-O0`, o compilador mantém verificações de segurança (*bounds checks*) eliminadas com `-O3`. Sem otimização, Rust chegou a 122,9 s no caso médio para N = 10⁵.
- **C++** obteve ganho consistente de **~2–3×**, graças a inlining de funções e eliminação de código morto aplicados pelo `g++` com `-O3`.
- **C** apresentou comportamento atípico: o speedup ficou próximo de 1×, indicando que o `gcc` já gera código eficiente para o padrão simples de acesso do Bubble Sort, e que otimizações agressivas como *loop unrolling* podem introduzir overhead maior que o ganho.
- **JavaScript superou C e C++ no pior caso (N = 10⁵):** JS registrou 6,9 s contra ~23 s das linguagens compiladas. O motor V8 identificou o padrão repetitivo de trocas e gerou código de máquina altamente especializado via JIT.
- **Python inviável para N ≥ 10⁵:** 403 s no pior caso — a indireção por referência da `list` e o interpretador CPython impõem overhead proporcional ao O(n²) de operações.

#### Compilação e Execução

> **Requisito:** Linux com `gcc`, `g++`, `rustc`, `node` e `python3` instalados.

```bash
cd bubble_sort

make clean       # Remove binários anteriores
make             # Compila C, C++ e Rust (com -O3 por padrão)
make run N=100000  # Executa o benchmark completo para N elementos
```

| Comando | Função |
|---|---|
| `make clean` | Remove os binários gerados |
| `make` | Compila C, C++ e Rust |
| `make run N=<valor>` | Executa o benchmark completo para N elementos |

&nbsp;


## ⚙️ 6. Metodologia Experimental

Os experimentos foram conduzidos de forma padronizada para todos os algoritmos, garantindo comparações consistentes entre implementações.

**Tamanhos de entrada testados:**
```
N ∈ { 10², 10³, 10⁴, 10⁵ }
```

**Cenários de entrada:** crescente (melhor caso), aleatório (caso médio) e decrescente (pior caso).

**Repetições:** cada configuração foi executada 5 vezes; os valores reportados são a média aritmética das execuções.

**Medição:** apenas o tempo de ordenação é medido — o tempo de leitura de arquivo é descartado.

&nbsp;


## 👤 7. Equipe e Colaboradores

| Algoritmo | Responsável |
|---|---|
| Selection Sort | *a preencher* |
| Insertion Sort | *a preencher* |
| Gnome Sort | *a preencher* |
| Bubble Sort | Bernardo Lebron |

Projeto desenvolvido para a disciplina de **Algoritmos e Estruturas de Dados I**
**CEFET-MG — Campus V, Divinópolis** · Prof. Michel Pires
