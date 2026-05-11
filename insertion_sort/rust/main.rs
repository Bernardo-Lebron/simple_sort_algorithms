use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::time::Instant;

fn insertion_sort(arr: &mut Vec<i32>) {
    for i in 1..arr.len() {
        let chave = arr[i];
        let mut j = i as i32 - 1;
        while j >= 0 && arr[j as usize] > chave {
            arr[(j + 1) as usize] = arr[j as usize];
            j -= 1;
        }
        arr[(j + 1) as usize] = chave;
    }
}

fn rodar_teste(arquivo: &str, n: usize) -> Option<f64> {
    let f = File::open(arquivo).ok()?;
    let reader = BufReader::new(f);
    let mut numeros: Vec<i32> = reader
        .lines()
        .take(n)
        .filter_map(|l| l.ok())
        .filter(|l| !l.trim().is_empty())
        .filter_map(|l| l.trim().parse().ok())
        .collect();

    let start = Instant::now();
    insertion_sort(&mut numeros);
    Some(start.elapsed().as_secs_f64())
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        eprintln!("Uso: {} <n_elementos>", args[0]);
        std::process::exit(1);
    }

    let n: usize = args[1].parse().expect("N invalido");
    println!("--- Iniciando Benchmark Insertion Sort (N: {}) ---\n", n);

    if let Some(t) = rodar_teste("crescente.txt", n) {
        println!("1. Crescente:   {:.6} segundos (Melhor caso)", t);
    }
    if let Some(t) = rodar_teste("aleatorio.txt", n) {
        println!("2. Aleatorio:   {:.6} segundos (Caso Medio)", t);
    }
    if let Some(t) = rodar_teste("decrescente.txt", n) {
        println!("3. Decrescente: {:.6} segundos (Pior caso)", t);
    }

    println!("\n--- Testes concluidos ---");
}