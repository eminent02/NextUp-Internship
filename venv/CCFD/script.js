const navSlide = () => {
  const burger = document.querySelector('.burger');
  const nav = document.querySelector('.nav-links');
  const navLinks = document.querySelectorAll('.nav-links li');

  
  burger.addEventListener('click', () => {
    // toggle Nav
    nav.classList.toggle('nav-active');
  
  });
}

navSlide();
// const script = () => {
//   navSlide();
// }