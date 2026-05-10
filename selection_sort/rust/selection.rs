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
        // Troca os elementos de lugar
        arr.swap(i, min_idx);
    }
}

fn main() {
    // 1. Captura o N do Makefile (argumento de linha de comando)
    let args: Vec<String> = env::args().collect();
    let n: usize = if args.len() > 1 {
        args[1].parse().unwrap_or(1000)
    } else {
        1000
    };

    // 2. Caminho do arquivo (seguindo o padrão ../dados/...)
    let path = "../dados/aleatorio.txt";
    let file = match File::open(path) {
        Ok(f) => f,
        Err(_) => {
            println!("Erro ao abrir arquivo em rust/selection!");
            return;
        }
    };

    let reader = BufReader::new(file);
    let mut data: Vec<f64> = Vec::with_capacity(n);

    // 3. Lê exatamente N linhas
    for line in reader.lines().take(n) {
        if let Ok(value) = line {
            if let Ok(num) = value.trim().parse::<f64>() {
                data.push(num);
            }
        }
    }

    // 4. Medição de tempo (padrão Rust High Precision)
    let start = Instant::now();
    selection_sort(&mut data);
    let duration = start.elapsed();

    // 5. Saída formatada para o seu terminal
    println!("Tempo: {:.6} s", duration.as_secs_f64());
    if !data.is_empty() {
        println!("Menor valor: {:.2}", data[0]);
    }
}