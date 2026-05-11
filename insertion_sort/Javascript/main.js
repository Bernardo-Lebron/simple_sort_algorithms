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

function rodarTeste(arquivo, n) {
    try {
        const data = fs.readFileSync(arquivo, 'utf8');
        const numeros = data
            .split('\n')
            .filter(l => l.trim() !== '')
            .slice(0, n)
            .map(Number);

        const start = process.hrtime.bigint();
        insertionSort(numeros);
        const tempo = Number(process.hrtime.bigint() - start) / 1e9;
        return tempo;
    } catch (e) {
        return null;
    }
}

if (process.argv.length < 3) {
    console.error('Uso: node main.js <n_elementos>');
    process.exit(1);
}

const n = parseInt(process.argv[2]);
console.log(`--- Iniciando Benchmark Insertion Sort (N: ${n}) ---\n`);

let t1 = rodarTeste('crescente.txt', n);
if (t1 !== null) console.log(`1. Crescente:   ${t1.toFixed(6)} segundos (Melhor caso)`);

let t2 = rodarTeste('aleatorio.txt', n);
if (t2 !== null) console.log(`2. Aleatorio:   ${t2.toFixed(6)} segundos (Caso Medio)`);

let t3 = rodarTeste('decrescente.txt', n);
if (t3 !== null) console.log(`3. Decrescente: ${t3.toFixed(6)} segundos (Pior caso)`);

console.log('\n--- Testes concluidos ---');