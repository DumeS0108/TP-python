let N = parseInt(prompt("Entrez un entier N :"));

let somme = 0;
for (let i = 1; i <= N; i++) {
    somme += i;
}

console.log("La somme des nombres de 1 à " + N + " est : " + somme);
