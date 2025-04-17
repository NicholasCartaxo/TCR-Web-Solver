function adicionarEquacao() {
    const container = document.getElementById('equacoes-container');

    // Cria o template da nova linha
    const novaLinha = document.createElement('div');
    novaLinha.className = "d-flex justify-content-center equacao";
    novaLinha.innerHTML = `
         <div class="row">
            <div class="d-flex align-items-center">
                <input type="text" name="valor1[]" class="form-control p-1 text-center" style="width: 60px; height: 60px;">
                <span style="font-size: 70px; margin-left: 10px;">x</span>
                <span style="font-size: 70px; margin-left: 10px;">≡</span>

                <input type="text" name="valor2[]" class="form-control p-1 text-center ms-4" style="width: 60px; height: 60px;">
                <span style="font-size: 70px; margin-left: 10px;">mod</span>
                <input type="text" name="modulo[]" class="form-control p-1 text-center ms-4" style="width: 60px; height: 60px;">
            </div>
        </div>
    `;

    container.appendChild(novaLinha);
}

const removeBtn = document.querySelector("#removeEquacaoBtn");
const alertModal = document.getElementById("alertModal");
const closeAlertBtn = document.getElementById("closeAlertBtn");
const equacoesContainer = document.querySelector("#equacoesContainer");

function removerUltimaEquacao() {
    const container = document.getElementById('equacoes-container');
    const equacoes = container.getElementsByClassName('equacao');

    if (equacoes.length > 0) {
        container.removeChild(equacoes[equacoes.length - 1]);
    } else {
      mostrarModal("Você não pode remover a última equação");
    }
}


closeAlertBtn.onclick = () => {
  alertModal.style.display = "none";
};

window.onclick = (e) => {
  if (e.target === alertModal) {
    alertModal.style.display = "none";
  }
};

document.getElementById("form").addEventListener("submit", function(e) {
  e.preventDefault(); // Impede o envio tradicional

  const formData = new FormData(this);

  fetch("/calcular", {
      method: "POST",
      body: formData
  })
  .then(async response => {
      const contentType = response.headers.get("Content-Type") || "";
      const body = await response.text();

      if (!response.ok) {
          mostrarModal(body);  // ← Mostra erro no modal (string vinda do back)
      } else {
          // Se sucesso, substitui o conteúdo da página inteira com o HTML de resultado
          const form = document.createElement("form");
            form.method = "POST";
            form.action = "/calcular";

            for (const [key, value] of formData.entries()) {
              const input = document.createElement("input");
              input.type = "hidden";
              input.name = key;
              input.value = value;
              form.appendChild(input);
          }

          document.body.appendChild(form);
          form.submit(); // envia de verdade
      }
  })
  .catch(err => {
      mostrarModal("Erro de rede ou inesperado no servidor.");
      console.error(err);
  });
});

function mostrarModal(msg) {
  const modal = document.getElementById("alertModal");
  document.getElementById("mensagem-modal").innerHTML = msg;
  modal.style.display = "flex";

  document.getElementById("closeAlertBtn").onclick = () => {
      modal.style.display = "none";
  };
}