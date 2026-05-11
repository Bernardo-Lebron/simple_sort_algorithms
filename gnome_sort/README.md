# 📊 Gnome Sort - Análise de Performance

## O que foi feito

Testei o algoritmo Gnome Sort em 5 linguagens: C, C++, Rust, JavaScript e Python. Rodei para N = 100, 1000, 10000 e 100000 elementos, nos três cenários: melhor caso (já ordenado), caso médio (aleatório) e pior caso (decrescente).

Fiz 5 execuções por cenário, descartei o maior e o menor tempo, e tirei a média dos 3 do meio. Isso pra evitar qualquer ruído do processador.

## Resultados (N = 100.000)

| Linguagem | Melhor Caso | Caso Médio | Pior Caso |
|-----------|-------------|------------|-----------|
| Rust | 0,05 ms | 3,95 s | 8,28 s |
| C++ | 0,16 ms | 13,97 s | 28,26 s |
| JavaScript | 1,77 ms | 13,91 s | 27,45 s |
| C | 0,18 ms | 15,19 s | 28,91 s |
| Python | 18,46 ms | 257,01 s | — |

## O que deu certo

**Rust foi o mais rápido disparado.** No caso médio com 100k elementos, Rust levou 3,95 segundos enquanto C e C++ ficaram na casa dos 14-15 segundos. Quase 4x mais rápido.

**JavaScript surpreendeu.** Node.js competiu pau a pau com C++: 13,91s contra 13,97s.

**C e C++ performaram igual.** Como esperado, ficaram muito próximos.

**Python foi triste.** 257 segundos pra rodar o caso médio com 100k elementos. Inviável pra qualquer coisa acima de 10k.

## O que não deu certo

Os testes com 1 milhão de elementos não foram concluídos. Python travou, JavaScript demorou horas. Melhor deixar pra próxima.

## Conclusão

- Se quer velocidade bruta, use **Rust**
- Se quer algo que rode no navegador, **JavaScript** atende bem
- Se está preso a **C/C++**, o desempenho é OK
- **Python foge** pra qualquer coisa com N > 10.000

## Gráficos

Os gráficos estão na pasta `graficos/` com o padrão: `gnome_sort_<linguagem>.png`
