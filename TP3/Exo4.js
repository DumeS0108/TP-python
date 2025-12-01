// Définition de la fonction
function maximumDeTrois(a, b, c) {
    return Math.max(a, b, c);
}

// Programme principal
let x = parseInt(prompt("Entrez le premier nombre :"));
let y = parseInt(prompt("Entrez le deuxième nombre :"));
let z = parseInt(prompt("Entrez le troisième nombre :"));

let maxVal = maximumDeTrois(x, y, z);
console.log("Le maximum est : " + maxVal);
