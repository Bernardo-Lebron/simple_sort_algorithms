use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::time::Instant;

fn selection_sort(arr: &mut Vec<f64>) {
    let n = arr.len();
    for i in 0..n {
        let mut min_idx = i;
        for j in (i + 1)..n {
            if arr[j] < arr[min_idx] {
                min_idx = j;
            }
        }
        arr.swap(i, min_idx);
    }
}

/**
 * Função para carregar dados do arquivo e medir o tempo de execução.
 */
fn rodar_teste(caminho: &str, n: usize) -> f64 {
    let file = match File::open(caminho) {
        Ok(f) => f,
        Err(_) => return -1.0,
    };

    let reader = BufReader::new(file);
    let mut v: Vec<f64> = Vec::with_capacity(n);

    for line in reader.lines().take(n) {
        if let Ok(l) = line {
            if let Ok(num) = l.trim().parse::<f64>() {
                v.push(num);
            }
        }
    }

    let start = Instant::now();
    selection_sort(&mut v);
    let duration = start.elapsed();

    duration.as_secs_f64()
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        println!("Uso: {} <n_elementos>", args[0]);
        return;
    }

    let n: usize = args[1].parse().unwrap_or(0);
    println!("--- Iniciando Benchmark Rust (N: {}) ---\n", n);

    let testes = [
        ("Crescente",   "../dados/crescente.txt",   "(Melhor caso)"),
        ("Aleatorio",   "../dados/aleatorio.txt",   "(Caso Médio)" ),
        ("Decrescente", "../dados/decrescente.txt", "(Pior caso)"  ),
    ];

    for (idx, (nome, caminho, desc)) in testes.iter().enumerate() {
        let tempo = rodar_teste(caminho, n);
        if tempo >= 0.0 {
            println!("{}. {:12}: {:.6} segundos {}", idx + 1, nome, tempo, desc);
        }
    }

    println!("\n--- Testes concluidos ---");
}