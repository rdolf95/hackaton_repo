/* globals Chart:false, feather:false */

(() => {
  'use strict'

  feather.replace({ 'aria-hidden': 'true' })

  // Graphs
  const ctx = document.getElementById('myChart')
  // eslint-disable-next-line no-unused-vars
  const myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: [
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday'
      ],
      datasets: [{
        data: [
          15339,
          21345,
          18483,
          24003,
          23489,
          24092,
          12034
        ],
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
            beginAtZero: false
          }
        }]
      },
      legend: {
        display: false
      }
    }
  })
})()

function add_month_option(year) {
  let select_month = document.querySelector("#maturity_month");
  
  var objOption = document.createElement("option");
  objOption.text = 'Month';
  objOption.value = -1;
  select_month.options.add(objOption);

  if(year == 2023){
    for (let i = 3; i <= 9; i++) {
      var objOption = document.createElement("option");
      objOption.text = i;
      objOption.value = i;
      select_month.options.add(objOption);
    }
    var objOption = document.createElement("option");
    objOption.text = 12;
    objOption.value = 12;
    select_month.options.add(objOption);
  }
  else if(year == 2024){
    var objOption = document.createElement("option");
    objOption.text = 6;
    objOption.value = 6;
    select_month.options.add(objOption);

    objOption = document.createElement("option");
    objOption.text = 12;
    objOption.value = 12;
    select_month.options.add(objOption);
  }
  else if(year == 2025){
    var objOption = document.createElement("option");
    objOption.text = 12;
    objOption.value = 12;
    select_month.options.add(objOption);
  }
}

function default_strike_price(){
  let strike_price = document.querySelector("#strike_price");
  var objOption = document.createElement("option");
  objOption.text = '행사가격';
  objOption.value = -1;
  strike_price.options.add(objOption);
}

function add_strike_price_option() {
  let strike_price = document.querySelector("#strike_price");
  
  for (let i = 170.0; i <= 450.0; i = i+2.5) {
    var objOption = document.createElement("option");
    objOption.text = i.toFixed(1);
    objOption.value = i;
    strike_price.options.add(objOption);
  }
}
