const fs = require('fs');
const path = require('path');

function selectionSort(arr) {
    let n = arr.length;
    for (let i = 0; i < n; i++) {
        let minIdx = i;
        for (let j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        // Troca (Swap)
        [arr[i], arr[minIdx]] = [arr[minIdx], arr[i]];
    }
}

// O Makefile envia o N como terceiro argumento (index 2)
const numLinhas = process.argv[2] ? parseInt(process.argv[2]) : 1000;

// Caminho para o arquivo na pasta dados
const filePath = path.join(__dirname, '..', 'dados', 'aleatorio.txt');

try {
    // Lê o arquivo e converte para array de números
    const content = fs.readFileSync(filePath, 'utf-8');
    let data = content.trim().split('\n')
        .slice(0, numLinhas) // Usa o N recebido do Makefile
        .map(Number);

    // Medição de tempo de alta precisão
    const start = process.hrtime.bigint();
    selectionSort(data);
    const end = process.hrtime.bigint();

    // Calcula o tempo em segundos
    const duration = Number(end - start) / 1e9;
    
    console.log(`Tempo: ${duration.toFixed(6)} s`);
    if (data.length > 0) {
        console.log(`Menor valor: ${data[0]}`);
    }

} catch (err) {
    console.error("Erro ao ler o arquivo em javascript/selection.js:", err.message);
}