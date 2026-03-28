

/*function bluruj() {
  document.querySelector('.overlay').style.display = "block";

}*/



const menuBtnOpenLog = document.querySelector('.logowanie');
if (menuBtnOpenLog) { 
    menuBtnOpenLog.addEventListener('click', () => {
      
        document.querySelector('body').classList.toggle('Open_Log');
        document.querySelector('.overlay').style.display = "block";
    })
}

const menuBtnCloseLog = document.querySelector('.Z_log');
if (menuBtnCloseLog) { 
    menuBtnCloseLog.addEventListener('click', () => {
      
        document.querySelector('body').classList.toggle('Open_Log');
        document.querySelector('.overlay').style.display = "none";
        
    })
}


const menuBtnOpenRej = document.querySelector('.rejestracja');
if (menuBtnOpenRej) { 
    menuBtnOpenRej.addEventListener('click', () => {
      
        document.querySelector('body').classList.toggle('Open_Rej');
        document.querySelector('.overlay').style.display = "block";
    })
}

const menuBtnCloseRej = document.querySelector('.Z_rej');
if (menuBtnCloseRej) { 
    menuBtnCloseRej.addEventListener('click', () => {
      
        document.querySelector('body').classList.toggle('Open_Rej');
        document.querySelector('.overlay').style.display = "none";
        
    })
}