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

fn main() {



    let limite = 1000000;

    

    let file = File::open(
        "C:\\Users\\Arthur\\Desktop\\AEDS TRAB 2\\aleatorio.txt"
    )
    .expect("Erro ao abrir arquivo");

    let reader = BufReader::new(file);

    let mut numeros: Vec<i32> = Vec::new();

    for (i, line) in reader.lines().enumerate() {

        if i >= limite {
            break;
        }

        let numero: i32 = line
            .unwrap()
            .trim()
            .parse()
            .unwrap();

        numeros.push(numero);
    }

    
    let start = Instant::now();

    insertion_sort(&mut numeros);

    let duration = start.elapsed();

    println!("Tempo: {:.6} segundos", duration.as_secs_f64());
}