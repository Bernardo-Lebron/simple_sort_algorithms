const fs = require('fs');

function insertionSort(arr) {

    for (let i = 1; i < arr.length; i++) {

        let chave = arr[i];
        let j = i - 1;

        while (j >= 0 && arr[j] > chave) {
            arr[j + 1] = arr[j];
            j--;
        }

        arr[j + 1] = chave;
    }
}

const limite = 1000000;



let data = fs.readFileSync(
    "C:\\Users\\Arthur\\Desktop\\AEDS TRAB 2\\aleatorio.txt",
    "utf8"
);

let numeros = data
    .split('\n')
    .filter(linha => linha.trim() !== '')
    .slice(0, limite)
    .map(Number);


let start = process.hrtime.bigint();

insertionSort(numeros);

let end = process.hrtime.bigint();

let tempo = Number(end - start) / 1e9;

console.log("Tempo:", tempo.toFixed(6), "segundos");