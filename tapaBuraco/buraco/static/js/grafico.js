$(function(){
  $('#btn-mapeados').attr('disabled',true);
  var num_m = [139, 245, 183, 243, 234, 202, 304, 321, 403, 201, 413, 415];
  var num_t = [10, 24, 8, 13, 24, 30, 34, 31, 40, 21, 43, 15];

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

  $("#btn-mapeados").click(function() {
    $(".title-chart").html("Buracos Mapeados");
    $('#btn-mapeados').attr('disabled',true);
    $('#btn-tapados').attr('disabled',false);
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

  $("#btn-tapados").click(function() {
    $(".title-chart").html("Buracos Tapados");
    $('#btn-tapados').attr('disabled',true);
    $('#btn-mapeados').attr('disabled',false);
    var buracos_mapeados = new Chart(ctx, {
      type: 'line',
      data: {
        labels: ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"],
        datasets: [{
          data: [num_t[0], num_t[1], num_t[2], num_t[3], num_t[4], num_t[5], num_t[6], num_t[7], num_t[8], num_t[9], num_t[10], num_t[11]],
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

});

