use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::time::Instant;

/**
 * Bubble Sort O(n^2)
 * Implementação in-place com otimização de parada antecipada.
 */
fn bubble_sort(nums: &mut Vec<f32>) {
    let n = nums.len();
    if n == 0 { return; }
    for i in 0..n - 1 {
        let mut swapped = false;
        for j in 0..n - i - 1 {
            if nums[j] > nums[j + 1] {
                nums.swap(j, j + 1);
                swapped = true;
            }
        }
        if !swapped {
            break; // Melhor caso: O(n)
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

    // Lê apenas as primeiras 'n' linhas
    for line in reader.lines().take(n) {
        if let Ok(l) = line {
            if let Ok(num) = l.trim().parse::<f32>() {
                v.push(num);
            }
        }
    }

    // Medição de tempo (semelhante ao Instant do C++ ou perf_counter do Python)
    let start = Instant::now();
    bubble_sort(&mut v);
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
        ("Crescente", "crescente.txt", "(Melhor caso)"),
        ("Aleatorio", "aleatorio.txt", "(Caso Médio)"),
        ("Decrescente", "decrescente.txt", "(Pior caso)"),
    ];

    for (nome, caminho, desc) in testes {
        let tempo = rodar_teste(caminho, n);
        if tempo >= 0.0 {
            println!("{}. {:12}: {:.6} segundos {}", 
                testes.iter().position(|&(n, _, _)| n == nome).unwrap() + 1,
                nome, tempo, desc);
        }
    }

    println!("\n--- Testes concluidos ---");
}