const acil = document.querySelectorAll('.acil')
const acilmis = document.querySelectorAll('.acilmis')
const deneme = document.getElementById('deneme')

for(let i = 0;i<acil.length;i++){
    acil[i].addEventListener('click',ac)
}

function ac(){    
    let icerik = this.parentElement.children[1]
    let icon = this.children[1]

    if(icerik.classList.contains('goster')){
        icerik.classList.remove('goster')
        icon.classList.remove('dondur')
    }else{
      acilmis.forEach(e =>{
        e.classList.remove('goster')
      })
      acil.forEach(e =>{
        let icon = e.children[1]
        icon.classList.remove('dondur')
      })
      icerik.classList.add('goster')
      icon.classList.add('dondur')
    }
}

const media = document.querySelector('.media')



