let notesStr = prompt("Entrez les notes séparées par des espaces :");
let notes = notesStr.split(" ").map(Number);

let somme = 0;
for (let n of notes) {
    somme += n;
}

// Calcul de la moyenne
let moyenne = somme / notes.length;

console.log("La moyenne est : " + moyenne);
