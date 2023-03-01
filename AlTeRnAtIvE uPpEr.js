const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

function swapCase(text) {
    return text.split('').map((c,i) => 
        i % 2 == 0 ? c.toLowerCase() : c.toUpperCase()
    ).join('');   
}

readline.question("Qual a frase para ficar alterada?\n", phrase => {
    console.log(swapCase(phrase))
    readline.close()
})