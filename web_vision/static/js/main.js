let isDown = false;
let startX;
let scrollLeft;
const slider = document.querySelector('.items-skills');

const end = () => {
	isDown = false;
  slider.classList.remove('active');
}

const start = (e) => {
  isDown = true;
  slider.classList.add('active');
  startX = e.pageX || e.touches[0].pageX - slider.offsetLeft;
  scrollLeft = slider.scrollLeft;	
}

const move = (e) => {
	if(!isDown) return;

  e.preventDefault();
  const x = e.pageX || e.touches[0].pageX - slider.offsetLeft;
  const dist = (x - startX);
  slider.scrollLeft = scrollLeft - dist;
}

(() => {
	slider.addEventListener('mousedown', start);
	slider.addEventListener('touchstart', start);

	slider.addEventListener('mousemove', move);
	slider.addEventListener('touchmove', move);

	slider.addEventListener('mouseleave', end);
	slider.addEventListener('mouseup', end);
	slider.addEventListener('touchend', end);
})();


// SHOW MENU MOBILE
function showMenuMobile(){
  var menuState = document.getElementById('menu-mobile-options');
  if (menuState.style.display === 'none'){
      menuState.style.display = 'block';
  } else {
      menuState.style.display = 'none';
  }}
  const nav = document.querySelector('#navbar-button button');
  nav.addEventListener('click', e =>{
  nav.classList.toggle('open');
  });
