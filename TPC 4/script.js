// Para mostrar a imagem grande
function showImage(image_path) {
    document.getElementById('mainImage').src = image_path;
    const extraInfo = document.getElementById('extraInfo');
    const allDetails = document.querySelectorAll('.car_details');

    changeCarSpecs()

    if (extraInfo.style.display === 'block' || extraInfo.style.display === '') {
        extraInfo.style.opacity = 0;
        setTimeout(() => {
            extraInfo.style.display = 'none';
            allDetails.forEach(detail => detail.style.display = 'none');
        }, 500);
    }

    moreInfo();
}


// Para mostrar as specs de cada modelo
function changeCarSpecs() {
    const image = document.getElementById('mainImage');
    const specs = document.getElementById('carSpecs');

    if (image.src.includes('m3-e30.jpg')) {
        specs.innerHTML = '<strong>Specs BMW M3 E30:</strong><br><hr>' +
                          '<strong>Engine</strong>: 2.3L (S14)<br>' +
                          '<strong>Fuel</strong>: Petrol<br>' +
                          '<strong>Power</strong>: 200 HP - 238 HP<br>' +
                          '<strong>Year</strong>: 1986 - 1991';
    }
    else if (image.src.includes('m3-e36.jpg')) {
        specs.innerHTML = '<strong>Specs BMW M3 E36:</strong><br><hr>' +
                          '<strong>Engine</strong>: 3.0L (S50B30) or 3.2L (S50B32)<br>' +
                          '<strong>Fuel</strong>: Petrol<br>' +
                          '<strong>Power</strong>: 286 HP (S50B30) or 321 HP (S50B32)<br>' +
                          '<strong>Year</strong>: 1992 - 1999';
    }
    else if (image.src.includes('m3-e46.jpg')) {
        specs.innerHTML = '<strong>Specs BMW M3 E46:</strong><br><hr>' +
                          '<strong>Engine</strong>: 3.2L (S54)<br>' +
                          '<strong>Fuel</strong>: Petrol<br>' +
                          '<strong>Power</strong>: 343 HP<br>' +
                          '<strong>Year</strong>: 2000 - 2006';
    }
    else if (image.src.includes('m3-e90.jpg')) {
        specs.innerHTML = '<strong>Specs BMW M3 E90:</strong><br><hr>' +
                          '<strong>Engine</strong>: 4.0L V8 (S65)<br>' +
                          '<strong>Fuel</strong>: Petrol<br>' +
                          '<strong>Power</strong>: 420 HP - 450 HP<br>' +
                          '<strong>Year</strong>: 2007 - 2013';
    }
    else if (image.src.includes('m3-f80.jpg')) {
        specs.innerHTML = '<strong>Specs BMW M3 F80:</strong><br><hr>' +
                          '<strong>Engine</strong>: 3.0L (S55)<br>' +
                          '<strong>Fuel</strong>: Petrol<br>' +
                          '<strong>Power</strong>: 431 HP - 460 HP<br>' +
                          '<strong>Year</strong>: 2014 - 2018';
    }
    else if (image.src.includes('m3-g80.jpg')) {
        specs.innerHTML = '<strong>Specs BMW M3 G80:</strong><br><hr>' +
                          '<strong>Engine</strong>: 3.0L (S58)<br>' +
                          '<strong>Fuel</strong>: Petrol<br>' +
                          '<strong>Power</strong>: 480 HP - 550 HP<br>' +
                          '<strong>Year</strong>: 2020 - ...';
    }
}


// Para mostrar mais info
function moreInfo(scroll = false) {
    const extraInfo = document.getElementById('extraInfo');
    const allDetails = document.querySelectorAll('.car_details');
    const image = document.getElementById('mainImage').src;
    let button = document.getElementById('seeMore');

    if (image.includes('all-m3.jpg')) {
        button.style.display = 'none';
    }
    else {
        button.style.display = 'block';
    }

    if (extraInfo.style.display === 'block') {
        extraInfo.style.opacity = 0;
        setTimeout(() => {
            extraInfo.style.display = 'none';
        }, 500);
    }

    allDetails.forEach(detail => {
        detail.style.display = 'none';
    });

    let carId = '';
    if (image.includes('m3-e30.jpg')) {
        carId = 'infoE30';
    } else if (image.includes('m3-e36.jpg')) {
        carId = 'infoE36';
    } else if (image.includes('m3-e46.jpg')) {
        carId = 'infoE46';
    } else if (image.includes('m3-e90.jpg')) {
        carId = 'infoE90';
    } else if (image.includes('m3-f80.jpg')) {
        carId = 'infoF80';
    } else if (image.includes('m3-g80.jpg')) {
        carId = 'infoG80';
    }

    if (scroll) {
        setTimeout(() => {
            document.getElementById(carId).style.display = 'block';
            extraInfo.style.display = 'block';
            setTimeout(() => {
                extraInfo.style.opacity = 1;
            }, 100);
            extraInfo.scrollIntoView({behavior: 'smooth'});
        }, 500);
    }
}

function buttonClick() {
    moreInfo(true);
}


// Para controlar o som do motor
function toggleAudio(audioId, stopButtonId) {
    const audio = document.getElementById(audioId);
    if (audio.paused) {
        audio.play();
    } else {
        audio.pause();
    }
}

function showStopButton(stopButtonId) {
    document.getElementById(stopButtonId).style.display = "inline";
}

function hideStopButton(stopButtonId) {
    document.getElementById(stopButtonId).style.display = "none";
}

function stopAudio(audioId, stopButtonId) {
    const audio = document.getElementById(audioId);
    audio.pause();
    audio.currentTime = 0;
    hideStopButton(stopButtonId);
}