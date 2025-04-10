function adicionarEquacao() {
    const container = document.getElementById('equacoes-container');

    // Cria o template da nova linha
    const novaLinha = document.createElement('div');
    novaLinha.className = "d-flex justify-content-center equacao";
    novaLinha.innerHTML = `
        <div class="row">
            <div class="d-flex align-items-center">
                <input type="text" name="valor1[]" class="form-control p-1 text-center" style="width: 60px; height: 60px;">
                <span style="font-size: 70px; margin-left: 10px;">X</span>
                <span style="font-size: 70px; margin-left: 10px;">≡</span>
    
                <input type="text" name="valor2[]" class="form-control p-1 text-center ms-4" style="width: 60px; height: 60px;">
                <span style="font-size: 70px; margin-left: 10px;">MOD</span>
                <input type="text" name="modulo[]" class="form-control p-1 text-center ms-4" style="width: 60px; height: 60px;">
            </div>
        </div>
    `;

    container.appendChild(novaLinha);
}

function removerUltimaEquacao() {
    const container = document.getElementById('equacoes-container');
    const equacoes = container.getElementsByClassName('equacao');

    if (equacoes.length > 0) {
        container.removeChild(equacoes[equacoes.length - 1]);
    } else {
        alert("Só resta uma equação na tela.");
    }
}

