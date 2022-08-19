function gera_cor(qtd=1){
    var bg_color = []
    var border_color = []
    for(let i = 0; i < qtd; i++){
        let r = Math.random() * 255;
        let g = Math.random() * 255;
        let b = Math.random() * 255;
        bg_color.push(`rgba(${r}, ${g}, ${b}, ${0.2})`)
        border_color.push(`rgba(${r}, ${g}, ${b}, ${1})`)
    }
    
    return [bg_color, border_color];
    
}

function renderiza_total_pedidos(url){  
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('total_pedidos').innerHTML = data.total
    })
}

function renderiza_faturamento_mensal(url){

    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){

        const ctx = document.getElementById('faturamento_mensal').getContext('2d');
        const myChart = new Chart(ctx, {
            data: {
                
                labels: data.meses,
                datasets: [
                    {
                    type:'bar',
                    label: 'Faturamento bruto',
                    data: data.fat_bruto,
                    backgroundColor: "rgba(255, 10, 13, 0.1)",
                    borderColor: "#FFFFFF",
                    yAxisID: 'A',
                    borderWidth: 0.2
                },
                {
                    type:'line',
                    label: 'taxa efetiva',
                    data: data.taxa_efetiva,
                    backgroundColor: "#CB1EA8",
                    borderColor: "#FFFFFF",
                    yAxisID: 'B',
                    borderWidth: 0.2
                }
            
            ]
            },
            
            options: {
                responsive: true,
                interaction: {
                  mode: 'index',
                  intersect: false,
                },
                stacked: false,
                plugins: {
                  title: {
                    display: true,
                    text: 'Fat. bruto x Tx. efetiva',
                    font: {
                        size: 20
                    }
                  }
                },
                scales: {
                  A: {
                    type: 'linear',
                    display: true,
                    position: 'left',
                  },
                  B: {
                    type: 'linear',
                    display: true,
                    position: 'right',
            
                    // grid line settings
                    grid: {
                      drawOnChartArea: false, // only want the grid lines for one axis to show up
                    },
                  },
                }
            }
           
        });

    })

}

function renderiza_pedidos_mensal(url){

    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){

        const ctx = document.getElementById('pedidos_mensal').getContext('2d');
        const myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Pedidos',
                    data: data.data,
                    backgroundColor: "#CB1EA8",
                    borderColor: "#FFFFFF",
                    yAxisID: 'A',
                    borderWidth: 0.2
                },
                {
                    label: 'ticket médio',
                    data: data.t_medio,
                    backgroundColor: "#f44336",
                    borderColor: "#FFFFFF",
                    yAxisID: 'B',
                    borderWidth: 0.2
                }
            ]
            },

            options: {
                responsive: true,
                interaction: {
                  mode: 'index',
                  intersect: false,
                },
                stacked: false,
                plugins: {
                  title: {
                    display: true,
                    text: 'Pedidos x Ticket médio',
                    font: {
                        size: 20
                    }
                  }
                },
                scales: {
                  A: {
                    type: 'linear',
                    display: true,
                    position: 'left',
                  },
                  B: {
                    type: 'linear',
                    display: true,
                    position: 'right',
            
                    // grid line settings
                    grid: {
                      drawOnChartArea: false, // only want the grid lines for one axis to show up
                    },
                  },
                }
            }
        });

    })

}

function renderiza_ticket_mensal(url){

    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){

        const ctx = document.getElementById('ticket_mensal').getContext('2d');
        const myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Ticket Médio',
                    data: data.data,
                    backgroundColor: "#CB1EA8",
                    borderColor: "#FFFFFF",
                    borderWidth: 0.2
                }
            
            ]
            },
           
        });

    })

}

function renderiza_pedidos_dia(url){

    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){

        const ctx = document.getElementById('pedidos-dia').getContext('2d');
        const myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: data.df1,
                datasets: [{
                    label: 'Pedidos',
                    data: data.df,
                    backgroundColor: "#CB1EA8",
                    borderColor: "#FFFFFF",
                    borderWidth: 0.2
                }
            
            ]
            },
        
            options: {
                plugins: {
                    title: {
                        display: true,
                        text: 'Pedidos por dia',
                        font: {
                            size: 20
                        }
                    }
                }
            }
           
        });

    })

}

function renderiza_faturamento_dia(url){

    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){

        const ctx = document.getElementById('faturamento-dia').getContext('2d');
        const myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: data.df1,
                datasets: [{
                    label: 'Faturamento',
                    data: data.df,
                    backgroundColor: "#CB1EA8",
                    borderColor: "#FFFFFF",
                    borderWidth: 0.2
                }
            
            ]
            },

            options: {
                lineTension: 0.6,
                    plugins: {
                        title: {
                            display: true,
                            text: 'Faturamento bruto por dia',
                            font: {
                                size: 20
                            }
                        }
                    }
            }
           
        });

    })

}

function renderiza_incentivos(url){

    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){

        const ctx = document.getElementById('incentivos-mensal').getContext('2d');
        const myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: data.df1,
                datasets: [{
                    label: 'ifood',
                    data: data.i_ifood,
                    backgroundColor: "#CB1EA8",
                    borderColor: "#FFFFFF",
                    yAxisID: 'A',
                    borderWidth: 0.2
                },
                {
                    label: 'loja',
                    data: data.i_loja,
                    backgroundColor: "#f44336",
                    borderColor: "#FFFFFF",
                    yAxisID: 'B',
                    borderWidth: 0.2
                }
            
            ]
            },
            
            options: {
                responsive: true,
                interaction: {
                  mode: 'index',
                  intersect: false,
                },
                stacked: false,
                plugins: {
                  title: {
                    display: true,
                    text: 'Incentivos mensal',
                    font: {
                        size: 20
                    }
                  }
                },
                scales: {
                  A: {
                    type: 'linear',
                    display: true,
                    position: 'left',
                  },
                  B: {
                    type: 'linear',
                    display: true,
                    position: 'right',
            
                    // grid line settings
                    grid: {
                      drawOnChartArea: false, // only want the grid lines for one axis to show up
                    },
                  },
                }
            }
           
        });

    })

}

function renderiza_cancelamentos(url){

    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){

        const ctx = document.getElementById('cancelamento-mes').getContext('2d');
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.meses,
                datasets: [{
                    label: 'cliente',
                    data: data.df,
                    backgroundColor: "#CB1EA8",
                    borderColor: "#FFFFFF",
                    borderWidth: 0.2
                },
                {
                    label: 'restaurante',
                    data: data.df2,
                    backgroundColor: "#f44336",
                    borderColor: "#FFFFFF",
                    borderWidth: 0.2
                }
            
            ]
            },

            options: {
                plugins: {
                    title: {
                        display: true,
                        text: 'Relação de cancelamentos R$',
                        font: {
                            size: 20
                        }
                    }
                }
            }
           
        });

    })

}

