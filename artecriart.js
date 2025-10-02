const texto = "CriArt";
const containerTexto = document.getElementById("texto");
const pincel = document.getElementById("pincel");

let index = 0;
let delay = 100; // tempo entre letras
let inicioX = 60; // posição inicial da esquerda
let espacamento = 28; // espaçamento entre letras

function desenharTexto() {
  if (index < texto.length) {
    containerTexto.textContent += texto[index];

    // mover pincel horizontalmente
    let novaPosicao = inicioX + (index * espacamento);
    pincel.style.left = novaPosicao + "px";

    index++;
    setTimeout(desenharTexto, delay);
  } else {
    // Após escrever tudo, mover pincel para baixo
    setTimeout(() => {
      pincel.style.top = "100%";
    }, 300);
  }
}

window.onload = desenharTexto;
