use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::time::Instant;

fn gnome_sort(arr: &mut Vec<f32>) {
    let n = arr.len();
    let mut i = 0;
    while i < n {
        if i == 0 || arr[i] >= arr[i - 1] {
            i += 1;
        } else {
            arr.swap(i, i - 1);
            i -= 1;
        }
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
    let mut v: Vec<f32> = Vec::with_capacity(n);

    for line in reader.lines().take(n) {
        if let Ok(l) = line {
            if let Ok(num) = l.trim().parse::<f32>() {
                v.push(num);
            }
        }
    }

    let start = Instant::now();
    gnome_sort(&mut v);
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
        ("Crescente",   "inputs/melhor_1000000.txt", "(Melhor caso)"),
        ("Aleatorio",   "inputs/medio_1000000.txt",  "(Caso Médio)" ),
        ("Decrescente", "inputs/pior_1000000.txt",   "(Pior caso)"  ),
    ];

    for (idx, (nome, caminho, desc)) in testes.iter().enumerate() {
        let tempo = rodar_teste(caminho, n);
        if tempo >= 0.0 {
            println!("{}. {:12}: {:.6} segundos {}", idx + 1, nome, tempo, desc);
        }
    }

    println!("\n--- Testes concluidos ---");
}