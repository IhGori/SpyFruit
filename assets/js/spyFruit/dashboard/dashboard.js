function renderiza_relatorio_temperatura(url) {

    fetch(url, {
        method: 'get',
    }).then(function (result) {
        return result.json()
    }).then(function (data) {
        const ctx = document.getElementById('relatorio_temperatura').getContext('2d');
        const myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: data.labels,
                datasets: [{
                    data: data.dataTemperatura,
                    label: 'Temperatura Uno R3 - A6 GSM/GPRS',
                    borderColor: "#198754",
                    backgroundColor: "#198754",
                    fill: false
                },

                ]
            },
            options: {
                title: {
                    display: true,
                    text: 'Relatório de temepratura do Módulo A6',
                    responsive: true,
                }
            }
        })
    })
}