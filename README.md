<img width="1200" height="300" alt="image" src="https://github.com/user-attachments/assets/919963f1-5b07-4d12-8862-191073dde33c" />


# Comparativo de Desempenho: Algoritmos de Ordenação Simples

Este repositório contém um ambiente de benchmarking experimental para analisar e comparar o desempenho de quatro algoritmos de ordenação simples: **Selection Sort**, **Insertion Sort**, **Gnome Sort** e **Bubble Sort**.

Os algoritmos são implementados em múltiplas linguagens de programação e avaliados sob diferentes tamanhos de entrada e cenários de ordenação, com o objetivo de verificar empiricamente as previsões teóricas de complexidade computacional.

Trabalho prático da disciplina de **Algoritmos e Estruturas de Dados I**
**CEFET-MG — Campus V, Divinópolis**

&nbsp;

## 📋 Sumário

1. [O que são Métodos de Ordenação?](#1-o-que-são-métodos-de-ordenação)
2. [Contextualização dos Algoritmos Simples](#2-contextualização-dos-algoritmos-simples)
3. [Objetivos](#3-objetivos)
4. [Estrutura do Projeto](#4-estrutura-do-projeto)
5. [Algoritmos Analisados](#5-algoritmos-analisados)
   - 5.1. [Selection Sort](#51-selection-sort)
   - 5.2. [Insertion Sort](#52-insertion-sort)
   - 5.3. [Gnome Sort](#53-gnome-sort)
   - 5.4. [Bubble Sort](#54-bubble-sort)
6. [Metodologia Experimental](#6-metodologia-experimental)
7. [Equipe e Colaboradores](#7-equipe-e-colaboradores)

&nbsp;

---

## 1. O que são Métodos de Ordenação?

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

---

## 2. Contextualização dos Algoritmos Simples

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

---

## 3. Objetivos

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

---

## 4. Estrutura do Projeto

O projeto está organizado de forma que cada algoritmo possua sua respectiva pasta independente, viabilizando o desenvolvimento paralelo pela equipe via Git.

```text
.
├── selection_sort/       # 📂 Selection Sort
│   ├── c/
│   ├── cpp/
│   ├── rust/
│   ├── js/
│   ├── python/
│   └── makefile
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

---

## 5. Algoritmos Analisados

### 5.1. Selection Sort

> 🚧 Seção a ser preenchida pelo(a) responsável.

&nbsp;

---

### 5.2. Insertion Sort

> 🚧 Seção a ser preenchida pelo(a) responsável.

&nbsp;

---

### 5.3. Gnome Sort

> 🚧 Seção a ser preenchida pelo(a) responsável.

&nbsp;

---

### 5.4. Bubble Sort

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
| Interpretador Python | CPython 3.x |

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

---

## 6. Metodologia Experimental

Os experimentos foram conduzidos de forma padronizada para todos os algoritmos, garantindo comparações consistentes entre implementações.

**Tamanhos de entrada testados:**
```
N ∈ { 10², 10³, 10⁴, 10⁵ }
```

**Cenários de entrada:** crescente (melhor caso), aleatório (caso médio) e decrescente (pior caso).

**Repetições:** cada configuração foi executada 5 vezes; os valores reportados são a média aritmética das execuções.

**Medição:** apenas o tempo de ordenação é medido — o tempo de leitura de arquivo é descartado.

&nbsp;

---

## 7. Equipe e Colaboradores

| Algoritmo | Responsável |
|---|---|
| Selection Sort | *a preencher* |
| Insertion Sort | *a preencher* |
| Gnome Sort | *a preencher* |
| Bubble Sort | Bernardo Lebron |

Projeto desenvolvido para a disciplina de **Algoritmos e Estruturas de Dados I**
**CEFET-MG — Campus V, Divinópolis** · Prof. Michel Pires
