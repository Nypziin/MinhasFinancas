function chamarApi() {
  console.log("API chamada!");

  fetch("/minha-api")
    .then(response => response.json())
    .then(data => {
      document.getElementById("resposta").innerText = JSON.stringify(data, null, 2);
    })
    .catch(err => {
      console.error(err);
      document.getElementById("resposta").innerText = "Erro ao chamar a API.";
    });
}

  document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("btnChamarApi").addEventListener("click", chamarApi);
});