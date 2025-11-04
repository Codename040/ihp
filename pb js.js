const arena = document.getElementById('arena');
const ctScoreEl = document.getElementById('ctScore');
const frScoreEl = document.getElementById('frScore');
const timerEl = document.getElementById('timer');
const shotSound = document.getElementById('shotSound');

let ctScore = 0;
let frScore = 0;
let gameTime = 60; // detik

function spawnTarget() {
  const target = document.createElement('div');
  const team = Math.random() < 0.5 ? 'ct-force' : 'free-rebels';

  target.classList.add('target', team);
  target.style.top = Math.random() * (window.innerHeight - 50) + 'px';
  target.style.left = Math.random() * (window.innerWidth - 50) + 'px';

  target.onclick = () => {
    shotSound.play();
    if (team === 'ct-force') ctScore++;
    else frScore++;
    ctScoreEl.textContent = ctScore;
    frScoreEl.textContent = frScore;
    target.remove();
  };

  arena.appendChild(target);

  setTimeout(() => {
    if (arena.contains(target)) target.remove();
  }, 1500); // hilang setelah 1.5 detik
}

function startGame() {
  const spawnInterval = setInterval(spawnTarget, 1000);
  const countdown = setInterval(() => {
    gameTime--;
    timerEl.textContent = gameTime;
    if (gameTime <= 0) {
      clearInterval(spawnInterval);
      clearInterval(countdown);
      alert(`Game Over!\nCT-Force: ${ctScore}\nFree Rebels: ${frScore}`);
    }
  }, 1000);
}

startGame();
