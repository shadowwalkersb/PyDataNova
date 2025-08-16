const greeting = document.querySelector('.hero h2');
const btn = document.getElementById('greetBtn');

// Update greeting based on time
const hour = new Date().getHours();
if(hour < 12) greeting.textContent += ' — Good Morning!';
else if(hour < 18) greeting.textContent += ' — Good Afternoon!';
else greeting.textContent += ' — Good Evening!';

// Button interaction
btn.addEventListener('click', () => {
    alert('You clicked the PyDataNova button!');
});
