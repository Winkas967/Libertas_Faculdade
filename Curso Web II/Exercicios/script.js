let resposta = 'sim';
while (resposta === 'sim'){
    console.log("Olá, quer ser cumprimentado novamente?");
    resposta = prompt("Digite 'sim' para continuar ou qualquer outra coisa para sair.");
}

let base = 2;
let expoente = 0;
while (expoente <=3){
    console.log(`2 elevado a ${expoente} é`,
        Math.pow(base, expoente));
        expoente++;
}

let msg = "";
let j = 0;
do {
    msg += j + '\n';
    j++;
} while (j <= 10);
console.log(msg);

do {
    num = Number(prompt("Número"));
    if (num == 0|| isNaN(num)){
        alert("Digite um número válido...")
    }
} while (num==0 || isNaN(num));
let pares = "Pares entre 1 e"+num+ ': ';
if (num > 1) {
    pares = pares + "2";
}

for (let i = 4; i <= num; i = i + 2){
    pares = pares + ", " + i
}

alert(pares);