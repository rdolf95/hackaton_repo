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

  const ctx2 = document.getElementById('myChart2')
  // eslint-disable-next-line no-unused-vars
  const myChart2 = new Chart(ctx2, {
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

function get_total() {
  let premium = parseFloat(document.getElementById("premium").value)
  let amount = parseFloat(document.getElementById("amount").value)
  let result = '+' + (premium * amount * 250000).toLocaleString();
  return result
}


var graph = null;

async function draw_profit_graph(isFirst) {
  console.log("Draw!!")

  const cur_kospi = 320.0 
  strike_price = 0
  if (isFirst){
    strike_price = 335.0
  }
  else{
    strike_price = document.getElementById("strike_price").value
  }
  const amount_ratio = parseFloat(document.getElementById("amount").value) / 60
  
  
  console.log("strike", parseFloat(document.getElementById("amount").value))
  console.log("ratio", amount_ratio)


  const premium = parseFloat(document.getElementById("premium").value)
  const kospi_axis = []
  const kospi_value = []
  const cc_value = []
  console.log("pre", premium)  
  var price_diff = Math.ceil(strike_price - cur_kospi)
  console.log(price_diff)
  const_strike_graph = []


  
  for(let i=-20; i<price_diff; i++){
    // console.log(data[i])
    kospi_axis.push(cur_kospi + i)
    kospi_value.push(i)
    if(!isFirst){
      cc_value.push(i + premium * amount_ratio)
    }
  }
  for(let i=price_diff; i<30; i++){
    // console.log(data[i])
    kospi_axis.push(cur_kospi + i)
    kospi_value.push(i)
    if(!isFirst){
      cc_value.push(i + premium* amount_ratio - (i-price_diff) *(amount_ratio))
    }
  }
  var first_padding = 0
  if (isFirst){
    price_diff = 100
    first_padding = 100
  }
  console.log(cc_value)
  // console.log(date)
  if (graph != null){
    graph.destroy()
  }
  graph = new Chart(document.getElementById("profit_graph"), {
    type: 'line',
    data: {
        labels: kospi_axis,
        datasets: [
          {
            label: 'KOSPI',
            data: kospi_value,
            lineTension: 0,
            backgroundColor: 'transparent',
            borderColor: '#007bff',
            borderWidth: 4,
            pointRadius: 0,
            pointBackgroundColor: '#007bff',
            pointStyle: 'rectRounded'
          },
          {
            label: 'With option',
            data: cc_value,
            lineTension: 0,
            backgroundColor: 'transparent',
            borderColor: '#EC6D1E',
            borderWidth: 4,
            pointRadius: 0,
            pointBackgroundColor: '#EC6D1E',
            pointStyle: 'rectRounded'
          }
        ]
    },
    options: {
      scales:{
        y: {
          title: {
            display: true,
            text: '수익',
          }
        },
        x: {
          title: {
            display: true,
            text: 'KOSPI'
          }
        }
      },
      plugins: {
        annotation: {
          annotations: {
            line1: {
              type: 'line',
              xMin: 20 + price_diff,
              xMax: 20 + price_diff,

              endValue: 0,
              borderColor: 'rgb(255, 99, 132)',
              borderWidth: 4,
              label: {
                enabled: true,
                content: '행사 가격',
                position: '80%',
                backgroundColor: 'rgb(255, 99, 132)',
              }
            },
            line2: {
              type: 'line',
              xMin: 20,
              xMax: 20,

              endValue: 0,
              borderColor: 'rgb(0, 0, 0)',
              borderWidth: 4,
              label: {
                enabled: true,
                content: '현재 KOSPI',
                position: '92%',
                backgroundColor: 'rgb(0, 0, 0)',
              }
            },
          }
        },
        legend: {
          display: true,
          labels: {
            usePointStyle: true,
            fontSize: 13,
          }
        },
      },
      responsive: false
    }
  });
  
}
