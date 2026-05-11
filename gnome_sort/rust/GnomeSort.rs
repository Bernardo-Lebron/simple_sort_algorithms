use std::env;
use std::fs;
use std::time::Instant;

fn gnome_sort(arr: &mut Vec<i32>) {
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

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        eprintln!("Uso: {} <arquivo.txt>", args[0]);
        std::process::exit(1);
    }
    let content = fs::read_to_string(&args[1])
        .expect("Erro ao abrir arquivo");
    let mut arr: Vec<i32> = content
        .lines()
        .filter(|l| !l.trim().is_empty())
        .map(|l| l.trim().parse().expect("Número inválido"))
        .collect();
    let start = Instant::now();
    gnome_sort(&mut arr);
    let ms = start.elapsed().as_secs_f64() * 1000.0;
    println!("  n={:<8}  tempo: {:.4} ms", arr.len(), ms);
}
