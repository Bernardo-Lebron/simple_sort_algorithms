const fs = require('fs');
const { performance } = require('perf_hooks');

/**
 * Bubble Sort O(n^2)
 * Implementação in-place com otimização de parada antecipada.
 */
function bubbleSort(nums) {
    let n = nums.length;
    for (let i = 0; i < n - 1; i++) {
        let swapped = false;
        for (let j = 0; j < n - i - 1; j++) {
            if (nums[j] > nums[j + 1]) {
                let temp = nums[j];
                nums[j] = nums[j + 1];
                nums[j + 1] = temp;
                swapped = true;
            }
        }
        if (!swapped) break; // Melhor caso: O(n)
    }
}

/**
 * Função para carregar dados e medir o tempo.
 */
function rodarTeste(nomeArquivo, n) {
    try {
        // Lê o arquivo de forma síncrona para simplificar o benchmark
        const data = fs.readFileSync(nomeArquivo, 'utf8');
        // Converte as linhas em números e limita a 'n' elementos
        let v = data.split('\n')
                    .filter(line => line.trim() !== '')
                    .slice(0, n)
                    .map(Number);

        if (v.length < n) {
            console.log(`Aviso: O arquivo ${nomeArquivo} possui apenas ${v.length} registros.`);
        }

        const start = performance.now();
        bubbleSort(v);
        const end = performance.now();

        // performance.now() retorna milissegundos, convertemos para segundos
        return (end - start) / 1000;
    } catch (err) {
        console.error(`Erro ao abrir ${nomeArquivo}:`, err.message);
        return -1;
    }
}

function main() {
    const args = process.argv.slice(2);
    if (args.length < 1) {
        console.log("Uso: node bubble_sort.js <n_elementos>");
        process.exit(1);
    }

    const n = parseInt(args[0]);
    console.log(`--- Iniciando Benchmark JavaScript (N: ${n}) ---\n`);

    const testes = [
        { nome: "Crescente", path: "crescente.txt", desc: "(Melhor caso)" },
        { nome: "Aleatorio", path: "aleatorio.txt", desc: "(Caso Médio)" },
        { nome: "Decrescente", path: "decrescente.txt", desc: "(Pior caso)" }
    ];

    testes.forEach((teste, index) => {
        const tempo = rodarTeste(teste.path, n);
        if (tempo >= 0) {
            console.log(`${index + 1}. ${teste.nome.padEnd(12)}: ${tempo.toFixed(6)} segundos ${teste.desc}`);
        }
    });

    console.log("\n--- Testes concluidos ---");
}

main();