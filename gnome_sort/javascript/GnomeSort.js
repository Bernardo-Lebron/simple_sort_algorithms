const fs = require('fs');
 
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
    return arr;
}
 
if (process.argv.length < 3) {
    console.error('Uso: node gnome.js <arquivo.txt>');
    process.exit(1);
}
 
const content = fs.readFileSync(process.argv[2], 'utf8');
const arr = content.split('\n')
    .filter(l => l.trim() !== '')
    .map(l => parseInt(l.trim(), 10));
 
const start = performance.now();
 
gnomeSort(arr);
 
const ms = performance.now() - start;
 
console.log(`  n=${arr.length.toString().padEnd(8)}  tempo: ${ms.toFixed(4)} ms`);
 
