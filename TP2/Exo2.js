const input1 = document.createElement("input");
input1.type = "number";
input1.placeholder = "Entrez un nombre";

const input2 = document.createElement("input");
input2.type = "number";
input2.placeholder = "Entrez un autre nombre";

const button = document.createElement("button");
button.textContent = "Calculer la somme";

document.body.appendChild(input1);
document.body.appendChild(input2);
document.body.appendChild(button);

button.addEventListener("click", () => {
  const val1 = Number(input1.value);
  const val2 = Number(input2.value);
  const somme = val1 + val2;
  console.log(`La somme de ${val1} + ${val2} = ${somme}`);
});