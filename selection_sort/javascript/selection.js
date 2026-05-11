const fs = require('fs');
const path = require('path');
const { performance } = require('perf_hooks');

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

/**
 * Função para carregar dados e medir o tempo.
 */
function rodarTeste(nomeArquivo, n) {
    try {
        const data = fs.readFileSync(nomeArquivo, 'utf8');
        let v = data.split('\n')
                    .filter(line => line.trim() !== '')
                    .slice(0, n)
                    .map(Number);

        if (v.length < n) {
            console.log(`Aviso: O arquivo ${nomeArquivo} possui apenas ${v.length} registros.`);
        }

        const start = performance.now();
        selectionSort(v);
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
        console.log("Uso: node selection.js <n_elementos>");
        process.exit(1);
    }

    const n = parseInt(args[0]);
    console.log(`--- Iniciando Benchmark JavaScript (N: ${n}) ---\n`);

    const base = path.join(__dirname, '..', 'dados');

    const testes = [
        { nome: "Crescente",   path: path.join(base, "crescente.txt"),   desc: "(Melhor caso)" },
        { nome: "Aleatorio",   path: path.join(base, "aleatorio.txt"),   desc: "(Caso Médio)"  },
        { nome: "Decrescente", path: path.join(base, "decrescente.txt"), desc: "(Pior caso)"   },
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