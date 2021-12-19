const prev = document.querySelector('.previous');
const next = document.querySelector('.next');
const items = document.querySelectorAll('.item');

const side1 = document.getElementById('side1');
const middle = document.getElementById('middle')
const side2 = document.getElementById('side2');

const middleBtn = document.querySelector('.middle-btn')
const side1Btn = document.querySelector('.side1-btn')
const side2Btn = document.querySelector('.side2-btn')

const baamzi = document.querySelector('.baamzi')

m = 1;
s1 = 0;
s2 = 2;

const images = [2,3,5,7,9,10,12,14]

baamzi.onended = function(e) {
    // alert("The audio has ended");
    s1 += 1
    if(images.includes(s1)){

        side1.innerHTML = `
            <img src="../static/carousel/${s1}.png">
        `

        

    }else {
        side1.innerHTML = `
            <video  src="../static/carousel/${s1}.mp4">
        `
    }
    
    m += 1
    if(images.includes(m)){

        middle.innerHTML = `
            <img src="../static/carousel/${m}.png">
        `

    }else {
        middle.innerHTML = `
            <video class="baamzi" src="../static/carousel/${m}.mp4" autoplay>
        `
    }

    s2 += 1
    if(images.includes(s2)){

        side2.innerHTML = `
            <img src="../static/carousel/${s2}.png">
        `

    }else {
        side2.innerHTML = `
            <video src="../static/carousel/${s2}.mp4">
        `
    }

};

function prevSlide(e) {

    if(m <= 1){
        return
    }

    console.log("clicked")
    s1 -= 1
    if(images.includes(s1)){

        side1.innerHTML = `
            <img src="../static/carousel/${s1}.png">
        `

    }else {
        side1.innerHTML = `
            <video  src="../static/carousel/${s1}.mp4">
        `
    }
    
    m -= 1
    if(images.includes(m)){

        middle.innerHTML = `
            <img src="../static/carousel/${m}.png">
        `

        

    }else {
        middle.innerHTML = `
            <video class="baamzi" src="../static/carousel/${m}.mp4" autoplay>
        `
    }

    s2 -= 1
    if(images.includes(s2)){

        side2.innerHTML = `
            <img src="../static/carousel/${s2}.png">
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
    
    if(m >= 15){
        return
    }

    console.log("clicked")
    s1 += 1
    if(images.includes(s1)){

        side1.innerHTML = `
            <img src="../static/carousel/${s1}.png">
        `

    }else {
        side1.innerHTML = `
            <video  src="../static/carousel/${s1}.mp4">
        `
    }
    
    m += 1
    if(images.includes(m)){

        middle.innerHTML = `
            <img src="../static/carousel/${m}.png">
        `

        setTimeout(nextSlide, 3000)

    }else {
        middle.innerHTML = `
            <video class="baamzi" src="../static/carousel/${m}.mp4" autoplay>
        `
    }

    s2 += 1
    if(images.includes(s2)){

        side2.innerHTML = `
            <img src="../static/carousel/${s2}.png">
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

next.addEventListener('click', (e)=> {
    nextSlide(e);
})

prev.addEventListener('click', (e)=> {
    prevSlide(e);
})