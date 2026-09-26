// Modelo 1: "Mostrar respuesta" revela la respuesta y los botones sin petición al servidor
(function () {
  const reveal = document.getElementById("reveal");
  const answer = document.getElementById("answer");
  if (!reveal || !answer) {
    return;
  }
  reveal.addEventListener("click", function () {
    answer.hidden = false;
    document.getElementById("reveal-box").hidden = true;
    // El foco va a "Bien" (o "Siguiente"), nunca a "Fallé", para que Enter no falle por accidente
    const preferred = answer.querySelector(".rate-good, .primary");
    if (preferred) {
      preferred.focus();
    }
  });
})();
