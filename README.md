# Comparativo de Desempenho: Algoritmos de Ordenação Quadráticos

Este repositório contém um ambiente de benchmarking experimental para analisar e comparar o desempenho de quatro algoritmos de ordenação simples: **Selection Sort**, **Insertion Sort**, **Gnome Sort** e **Bubble Sort**. 

Cada algoritmo é implementado em cinco linguagens de programação — **C, C++, Rust, JavaScript e Python** — avaliado sob múltiplos tamanhos de entrada e diferentes níveis de otimização de compilador.

Trabalho prático da disciplina de **Algoritmos e Estruturas de Dados I** **CEFET-MG — Campus V, Divinópolis**

&nbsp;

## 📋 Sumário

1. Contextualização e Objetivo
2. Estrutura do Projeto
3. Metodologia Experimental
4. Algoritmos Analisados
 - 4.1. Selection Sort
 - 4.2. Insertion Sort
 - 4.3. Gnome Sort
 - 4.4. Bubble Sort
5. Equipe e Colaboradores

&nbsp;

## 📖 Sobre o Projeto
 
O objetivo deste projeto é realizar uma **análise empírica e comparativa** dos algoritmos de ordenação simples, verificando na prática as previsões teóricas de complexidade computacional e quantificando o impacto de diferentes linguagens de programação e níveis de otimização de compilador sobre o tempo de execução.
 
Cada linguagem implementa a **mesma lógica algorítmica** garantindo que as diferenças de desempenho sejam atribuídas ao ambiente de execução e não a variações de implementação.
 
Os experimentos foram conduzidos com três cenários de entrada para cada tamanho `N`:
 
| Cenário | Descrição | Caso do algoritmo |
|---|---|---|
| Crescente | Vetor já ordenado | Melhor caso — O(n) |
| Aleatório | Vetor embaralhado | Caso médio — O(n²) |
| Decrescente | Vetor invertido | Pior caso — O(n²) |

&nbsp;

## 2. Estrutura do Projeto

Para viabilizar a colaboração via Git, o projeto está organizado de forma que cada algoritmo possua sua respectiva pasta independente. A estrutura final mapeada para o repositório é:

```text
.
├── selection_sort/       # 📂 Espaço reservado para o Selection Sort
│   ├── c/
│   ├── cpp/
│   ├── rust/
│   ├── js/
│   ├── python/
│   └── makefile
├── insertion_sort/       # 📂 Espaço reservado para o Insertion Sort
│   ├── ...
├── gnome_sort/           # 📂 Espaço reservado para o Gnome Sort
│   ├── ...
├── bubble_sort/          # 📂 Implementação do Bubble Sort (Concluído)
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
├── data/                 # 📂 Geradores/Arquivos de entrada
│   ├── crescente.txt
│   ├── aleatorio.txt
│   └── decrescente.txt
└── README.md

```

&nbsp;

# 🫧 Algoritmo Bubble Sort
 
O Bubble Sort opera por passagens sucessivas sobre o vetor, comparando pares adjacentes e realizando trocas quando necessário. A implementação utiliza **parada antecipada**: uma variável `swapped` detecta a ausência de trocas, encerrando o algoritmo imediatamente caso o vetor já esteja ordenado.
 
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
 
### Complexidade
 
| Caso | Comparações | Complexidade |
|---|---|---|
| Melhor caso | n − 1 | O(n) |
| Caso médio | n(n−1)/4 | O(n²) |
| Pior caso | n(n−1)/2 | O(n²) |
 
Complexidade espacial: **O(1)** — ordenação in-place, sem memória auxiliar proporcional à entrada.

&nbsp;

## 💻 Linguagens e Estruturas de Dados
 
| Linguagem | Estrutura interna | Modelo de execução |
|---|---|---|
| C | `int[]` alocado com `malloc` | Compilada — gcc |
| C++ | `std::vector<int>` | Compilada — g++ |
| Rust | `Vec<i32>` | Compilada — LLVM |
| JavaScript | `Array` (SMI otimizado pelo V8) | JIT — Node.js / V8 |
| Python | `list` (referências a objetos) | Interpretada — CPython |
 
A estrutura `list` do Python armazena **referências a objetos genéricos**, adicionando uma camada de indireção em cada acesso e comparação — o principal fator do desempenho inferior dessa linguagem nos benchmarks.
 
&nbsp;
 
## 🧪 Metodologia Experimental
 
### Ambiente
 
| Componente | Especificação |
|---|---|
| Processador | Intel Core Ultra 7 155H (até 4,80 GHz) |
| Memória RAM | 16 GB |
| Armazenamento | SSD 512 GB |
| Sistema Operacional | Zorin OS (Linux) |
 
### Configurações de compilação
 
As linguagens compiladas (C, C++, Rust) foram testadas em dois níveis de otimização:
 
- **`-O0`** — sem otimização (Nível 0)
- **`-O3`** — otimização máxima (Nível 3)
JavaScript e Python não são afetadas por flags de compilação nativa — seus resultados refletem exclusivamente o comportamento do motor V8 e do interpretador CPython.
 
### Tamanhos de entrada
 
```
N ∈ { 10², 10³, 10⁴, 10⁵ }
```
 
> O valor N = 10⁶ foi descartado: o tempo estimado em Python ultrapassaria 10 horas, inviabilizando a coleta estatística.
 
Cada configuração foi executada **5 vezes**. Os valores reportados são a **média aritmética** das cinco execuções.
 
&nbsp;
 
## 📊 Resultados
 
### Otimização -O3 — N = 10² e N = 10³ (tempos em segundos)
 
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
 
### Otimização -O3 — N = 10⁴ e N = 10⁵ (tempos em segundos)
 
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
 
### Destaques
 
- **Confirmação da complexidade O(n²):** aumentar N de 10⁴ para 10⁵ resultou em crescimento ~100× no tempo dos casos médio e pior caso, exatamente o esperado para complexidade quadrática.
- **Parada antecipada:** para N = 10⁵, o melhor caso em C completou em ~0,000042 s enquanto o pior caso levou ~23,6 s — razão de 5,6 × 10⁵.
- **JavaScript superou C e C++ no pior caso (N = 10⁵):** JS registrou 6,9 s contra ~23 s das linguagens compiladas. O motor V8 identificou o padrão repetitivo de trocas e gerou código de máquina altamente especializado via JIT.
- **Python inviável para N ≥ 10⁵:** 403 s no pior caso — a estrutura `list` com indireção por referência e o interpretador CPython impõem overhead proporcional ao O(n²) de operações.

&nbsp;
 
## ⚙️ Impacto das Otimizações de Compilador
 
### Speedup de -O3 em relação a -O0 (caso médio: entrada aleatória)
 
| Linguagem | N = 10² | N = 10³ | N = 10⁴ | N = 10⁵ |
|---|---:|---:|---:|---:|
| C | 1,28× | 0,90× | 0,95× | 1,13× |
| C++ | 2,01× | 2,88× | 2,73× | 2,08× |
| Rust | 13,55× | 16,51× | 23,19× | 9,10× |
| JavaScript | 1,08× | 1,04× | 1,05× | 0,98× |
| Python | 1,08× | 1,16× | 1,05× | 1,01× |
 
### Análise
 
**Rust** foi a linguagem que mais se beneficiou da otimização — speedup de até **23×** em N = 10⁴. Em modo `-O0`, o compilador mantém verificações de segurança (bounds checks) que são eliminadas com `-O3`. Sem otimização, Rust chegou a 122,9 s no caso médio para N = 10⁵, tornando-se a mais lenta entre as compiladas.
 
**C++** obteve ganho consistente de **~2–3×** em todos os tamanhos, graças a inlining de funções e eliminação de código morto aplicados pelo `g++` com `-O3`.
 
**C** apresentou comportamento atípico: o speedup ficou próximo de 1× e em alguns casos `-O3` foi marginalmente mais lento que `-O0`. Isso indica que o `gcc` já gera código eficiente para o padrão simples de acesso do Bubble Sort, e que otimizações agressivas como loop unrolling podem introduzir overhead de controle maior que o ganho.
 
**JavaScript e Python** são imunes à flag de compilação nativa. Os valores ~1× confirmam que seus tempos dependem exclusivamente de seus próprios runtimes.
 
&nbsp;
 
## 🔧 Compilação e Execução
 
> **Requisito:** Linux (Ubuntu ou Zorin OS) com `gcc`, `g++`, `rustc`, `node` e `python3` instalados.
 
```bash
# Entrar no diretório
cd bubble_sort
 
# Limpar compilações anteriores
make clean
 
# Compilar todas as linguagens
make
 
# Executar benchmark com N elementos
make run N=100000
```
 
| Comando | Função |
|---|---|
| `make clean` | Remove os binários gerados |
| `make` | Compila C, C++ e Rust (com -O3 por padrão) |
| `make run N=<valor>` | Compila e executa o benchmark completo para N elementos |
 
&nbsp;
 
## 💻 Ambiente de Desenvolvimento
 
- **Sistema Operacional:** Zorin OS (Linux)
- **Compilador C/C++:** GCC 13.3.0 / G++ 13.3.0
- **Compilador Rust:** rustc (LLVM backend)
- **Runtime JavaScript:** Node.js (motor V8)
- **Interpretador Python:** CPython 3.x
- **Hardware:** Intel Core Ultra 7 155H @ 4,80 GHz · 16 GB RAM · SSD 512 GB · Intel Arc Graphics integrada (Samsung Galaxy Book4 Pro)

&nbsp;
 
## 👤 Autor
 
Projeto desenvolvido por **Bernardo Lebron**
Estudante de **Engenharia de Computação — CEFET-MG, Campus V, Divinópolis**
Disciplina: Algoritmos e Estruturas de Dados I · Prof. Michel Pires
 
