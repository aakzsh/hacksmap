// const prev = document.querySelector('.previous');
// const next = document.querySelector('.next');
const items = document.querySelectorAll('.item');

const side1 = document.getElementById('side1');
const middle = document.getElementById('middle')
const side2 = document.getElementById('side2');

const middleBtn = document.querySelector('.middle-btn')
const side1Btn = document.querySelector('.side1-btn')
const side2Btn = document.querySelector('.side2-btn')

const baamzi = document.querySelector('.baamzi')
var username = window.location.href.split("/").at(-1)


m = 0;
s1 = -1;
s2 = 1;

middleBtn.addEventListener("click", (e) => {
    nextSlide(e)
})

const images = [2,3,5,7,9,10,12,14]

baamzi.onended = function(e) {
    // alert("The audio has ended");
    s1 += 1
    if(images.includes(s1)){

        side1.innerHTML = `
            <img src="../static/users/${username}/${s1}.png">
        `

        

    }else {
        side1.innerHTML = `
            <video  src="../static/carousel/${s1}.mp4">
        `
    }
    
    m += 1
    if(images.includes(m)){

        middle.innerHTML = `
            <img src="../static/users/${username}/${m}.png">
        `

    }else {
        middle.innerHTML = `
            <video class="baamzi" src="../static/carousel/${m}.mp4" autoplay>
        `
    }

    s2 += 1
    if(images.includes(s2)){

        side2.innerHTML = `
            <img src="../static/users/${username}/${s2}.png">
        `

    }else {
        side2.innerHTML = `
            <video src="../static/carousel/${s2}.mp4">
        `
    }

};

function prevSlide(e) {
    clearTimeout(t)
    if(m <= 1){
        return
    }

    console.log("clicked")
    s1 -= 1
    if(images.includes(s1)){

        side1.innerHTML = `
            <img src="../static/users/${username}/${s1}.png">
        `

    }else {
        side1.innerHTML = `
            <video  src="../static/carousel/${s1}.mp4">
        `
    }
    
    m -= 1

    if(m==15){
        console.log("last slide")
        middle.innerHTML = `
                <video class="baamzi" src="../static/carousel/${m}.mp4" autoplay>
                <button class="replay-btn">Replay</button>
            `

        const replayBtn = document.querySelector('.replay-btn')
        replayBtn.addEventListener("click", e => {
            m = 0;
            s1 = -1;
            s2 = 1;
        })

    }else{

        if(images.includes(m)){
    
            middle.innerHTML = `
                <img src="../static/users/${username}/${m}.png">
            `
    
            var t = setTimeout(nextSlide, 5000)
    
        }else {
            middle.innerHTML = `
                <video class="baamzi" src="../static/carousel/${m}.mp4" autoplay>
            `
            clearTimeout(t)
        }
    }

    s2 -= 1
    if(images.includes(s2)){

        side2.innerHTML = `
            <img src="../static/users/${username}/${s2}.png">
        `

    }else {
        side2.innerHTML = `
            <video src="../static/carousel/${s2}.mp4">
        `
    }

    baamzi.onended = function(e) {
        // alert("The audio has ended");
        prevSlide(e)
    };

}

function nextSlide(e) {
    clearTimeout(t)
    if(m >= 15){
        return
    }

    console.log("clicked")
    s1 += 1
    if(images.includes(s1)){

        side1.innerHTML = `
            <img src="../static/users/${username}/${s1}.png">
        `

    }else {
        side1.innerHTML = `
            <video  src="../static/carousel/${s1}.mp4">
        `
    }
    
    m += 1
    if(m==15){
        console.log("last slide")
        middle.innerHTML = `
                <video src="../static/carousel/${m}.mp4" autoplay>
            `
function delaykaro(){
    window.location.href=`/summary/${username}`
}
        setTimeout(delaykaro, 6000)
    }
        else{

            if(images.includes(m)){
        
                middle.innerHTML = `
                    <img src="../static/users/${username}/${m}.png">
                `
                 
                var t = setTimeout(nextSlide, 5000)
        
            }else {
                middle.innerHTML = `
                    <video class="baamzi" src="../static/carousel/${m}.mp4" autoplay>
                `
                clearTimeout(t)
            }
        }

    s2 += 1
    if(images.includes(s2)){

        side2.innerHTML = `
            <img src="../static/users/${username}/${s2}.png">
        `

    }else {
        side2.innerHTML = `
            <video src="../static/carousel/${s2}.mp4">
        `
    }

    const baamzi = document.querySelector('.baamzi')

    baamzi.onended = function(e) {
        // alert("The audio has ended");
        nextSlide(e)
    };

    // const middleImg = middle.children[0]
    // middleImg.src = images[(m - 1)%4]
    // m -= 1
    
    // const side1Img = side1.children[0]
    // side1Img.src = images[(s1-1)%4]
    // s1 -= 1

    // const side2Img = side2.children[0]
    // side2Img.src = images[(s2-1)%4]
    // s2 -= 1
}

// next.addEventListener('click', (e)=> {
//     nextSlide(e);
// })

// prev.addEventListener('click', (e)=> {
//     prevSlide(e);
// })