// Mock dataset
const mockData = {
  labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
  datasets: [{
    label: 'Demo Data',
    data: [12, 19, 3, 5, 2, 7],
    backgroundColor: [
      'rgba(255, 99, 132, 0.6)',
      'rgba(54, 162, 235, 0.6)',
      'rgba(255, 206, 86, 0.6)',
      'rgba(75, 192, 192, 0.6)',
      'rgba(153, 102, 255, 0.6)',
      'rgba(255, 159, 64, 0.6)'
    ],
    borderColor: [
      'rgba(255,99,132,1)',
      'rgba(54,162,235,1)',
      'rgba(255,206,86,1)',
      'rgba(75,192,192,1)',
      'rgba(153,102,255,1)',
      'rgba(255,159,64,1)'
    ],
    borderWidth: 1
  }]
};

// Chart config
const ctx = document.getElementById('myChart').getContext('2d');
const myChart = new Chart(ctx, {
  type: 'bar',
  data: mockData,
  options: {
    responsive: true,
    plugins: {
      legend: { display: true, position: 'top' },
      title: { display: true, text: 'Mock Data Bar Chart' }
    }
  }
});
