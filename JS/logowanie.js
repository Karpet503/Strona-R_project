

/*function bluruj() {
  document.querySelector('.overlay').style.display = "block";

}*/



const menuBtnopen = document.querySelector('.logowanie',);
if (menuBtnopen) { 
    menuBtnopen.addEventListener('click', () => {
      
        document.querySelector('body').classList.toggle('closed');
        document.querySelector('.overlay').style.display = "block";
    })
}

const menuBtnclose = document.querySelector('.zamknij',);
if (menuBtnclose) { 
    menuBtnclose.addEventListener('click', () => {
      
        document.querySelector('body').classList.toggle('closed');
        document.querySelector('.overlay').style.display = "none";
        
    })
}