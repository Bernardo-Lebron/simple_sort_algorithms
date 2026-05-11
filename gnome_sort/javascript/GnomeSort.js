const fs = require('fs');
const path = require('path');
const { performance } = require('perf_hooks');

function gnomeSort(arr) {
    let i = 0;
    while (i < arr.length) {
        if (i === 0 || arr[i] >= arr[i - 1]) {
            i++;
        } else {
            [arr[i], arr[i - 1]] = [arr[i - 1], arr[i]];
            i--;
        }
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
        gnomeSort(v);
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
        console.log("Uso: node GnomeSort.js <n_elementos>");
        process.exit(1);
    }

    const n = parseInt(args[0]);
    console.log(`--- Iniciando Benchmark JavaScript (N: ${n}) ---\n`);

    const base = path.join(__dirname, '..', 'inputs');

    const testes = [
        { nome: "Crescente",   path: path.join(base, "melhor_1000000.txt"), desc: "(Melhor caso)" },
        { nome: "Aleatorio",   path: path.join(base, "medio_1000000.txt"),  desc: "(Caso Médio)"  },
        { nome: "Decrescente", path: path.join(base, "pior_1000000.txt"),   desc: "(Pior caso)"   },
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