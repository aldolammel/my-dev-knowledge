// Associating the button tag on HTML (that's calling this script file) to this var:
const btnEl = document.querySelector('button');
const iptEl = document.querySelector('input');
const lstEl = document.querySelector('ul');

function addGoal() {
  const iptValue = iptEl.value;
  // Built-in browser feature to create a new DOM elements:
  const lstGoalEl = document.createElement('li');
  lstGoalEl.textContent = iptValue;
  lstEl.appendChild(lstGoalEl);
}

// Defining what function's called if the click occurs:
btnEl.addEventListener('click', addGoal);