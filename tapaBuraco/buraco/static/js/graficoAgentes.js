$(function(){
  var num_m = [10, 24, 77, 113, 124, 130, 154, 157, 170, 172, 177, 183];

  feather.replace()
  var ctx = document.getElementById("myChart");
  var buracos_mapeados = new Chart(ctx, {
    type: 'line',
    data: {
      labels: ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"],
      datasets: [{
        data: [num_m[0], num_m[1], num_m[2], num_m[3], num_m[4], num_m[5], num_m[6], num_m[7], num_m[8], num_m[9], num_m[10], num_m[11]],
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#007bff',
        borderWidth: 4,
        pointBackgroundColor: '#007bff'
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: true
          }
        }]
      },
      legend: {
        display: false,
      }
    }
  });
});

