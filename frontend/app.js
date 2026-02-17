const API = "http://127.0.0.1:8000"


async function login() {
    const email = document.getElementById("email").value
    const senha = document.getElementById("senha").value

    const response = await fetch(API + "/login", {
        method: "POST",
        credentials: "include",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: `email=${email}&senha=${senha}`
    })

    const data = await response.json()

    if (data.msg) {
        window.location.href = "dashboard.html"
    } else {
        document.getElementById("msg").innerText = "Erro no login"
    }
}


async function carregarDashboard() {
    const hoje = new Date()
let ano = hoje.getFullYear()
let mes = hoje.getMonth() + 2 // próximo mês

if (mes === 13) {
    mes = 1
    ano += 1
}

const previsaoResponse = await fetch(
    API + `/previsao/previsao?ano=${ano}&mes=${mes}`
)

const previsaoData = await previsaoResponse.json()

document.getElementById("previsao").innerText =
    "R$ " + previsaoData.previsao_gasto

    const response = await fetch(API + "/dashboard/me", {
        credentials: "include"
    })

    const data = await response.json()

    document.getElementById("total").innerText = "R$ " + data.total_gasto

    // gráfico categoria
    const ctxCat = document.getElementById('graficoCategoria')
    new Chart(ctxCat, {
        type: 'pie',
        data: {
            labels: data.gastos_por_categoria.map(x => x.categoria),
            datasets: [{
                data: data.gastos_por_categoria.map(x => x.total)
            }]
        }
    })

    // gráfico mensal
    const ctxMes = document.getElementById('graficoMensal')
    new Chart(ctxMes, {
        type: 'line',
        data: {
            labels: data.gastos_mensais.map(x => x.mes),
            datasets: [{
                data: data.gastos_mensais.map(x => x.total)
            }]
        }
    })

    gerarRecomendacoes(data)
}


function gerarRecomendacoes(data) {

    const lista = document.getElementById("recomendacoes")
    lista.innerHTML = ""

    if (data.total_gasto > 2000) {
        lista.innerHTML += "<li>Seus gastos estão altos este mês.</li>"
    }

    const maiorCategoria = data.gastos_por_categoria.sort((a,b)=>b.total-a.total)[0]

    if (maiorCategoria) {
        lista.innerHTML += `<li>Sua maior categoria é ${maiorCategoria.categoria}</li>`
    }

    lista.innerHTML += "<li>Tente reduzir gastos recorrentes.</li>"
}
