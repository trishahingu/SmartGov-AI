const ctx = document.getElementById('verificationChart');

new Chart(ctx, {

type: 'line',

data: {

labels: [

'Mon',

'Tue',

'Wed',

'Thu',

'Fri',

'Sat',

'Sun'

],

datasets: [

{

label: 'Documents Verified',

data: [

120,

180,

150,

250,

300,

420,

520

],

borderColor: '#0B3D91',

backgroundColor: 'rgba(11,61,145,.15)',

fill: true,

tension: .4

}

]

},

options: {

responsive: true,

plugins: {

legend: {

display: true

}

}

}

});