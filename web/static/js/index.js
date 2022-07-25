//SIDEBAR
const menuItems = document.querySelectorAll('.menu-item');


//THEME
const theme = document.querySelector('#theme');
const themeModal = document.querySelector('.customize-theme');
const fontSizes = document.querySelectorAll('.choose-size span')
var root = document.querySelector(':root');
const colorPalette = document.querySelectorAll('.choose-color span'); 
const Bg1 = document.querySelector('.bg-1');
const Bg2 = document.querySelector('.bg-2');
const Bg3 = document.querySelector('.bg-3');

//PROFILE MENU
const profile = document.querySelector('#profile');
const profileModal = document.querySelector('.profile-links');

//Expore MENU
const explore = document.querySelector('#explore');
const exploreModal = document.querySelector('.explore-links');




// THEME/DISPLAY CUSTOMIZATION

//opens model
const openThemeModal = () => {
    themeModal.style.display = 'grid';
}

//closes model
const closeThemeModel = (e) => {
    if(e.target.classList.contains('customize-theme')) {
        themeModal.style.display = 'none';
    }
}

//closing the model
themeModal.addEventListener('click', closeThemeModel);

theme.addEventListener('click', openThemeModal);

// ======================= FONTS ==========================

// remove active class from spans or font size selectors
const removeSizeSelector = () => {
    fontSizes.forEach(size => {
        size.classList.remove('active');
    })
}

fontSizes.forEach(size => {
    

    size.addEventListener('click', () => {

        removeSizeSelector();
        let fontSize;
        size.classList.toggle('active');

        if(size.classList.contains("font-size-1")){
            fontSize = '8px';
            root.style.setProperty('----sticky-top-left','5.4rem');
            root.style.setProperty('----sticky-top-right','5.4rem');
    
        } else  if(size.classList.contains("font-size-2")){
            fontSize = '11px';
            root.style.setProperty('----sticky-top-left','5.4rem');
            root.style.setProperty('----sticky-top-right','-7rem');
        } else  if(size.classList.contains("font-size-3")){
            fontSize = '14px';
            root.style.setProperty('----sticky-top-left','-2rem');
            root.style.setProperty('----sticky-top-right','-17rem');
        } else  if(size.classList.contains("font-size-4")){
            fontSize = '16px';
            root.style.setProperty('----sticky-top-left','-5rem');
            root.style.setProperty('----sticky-top-right','-25rem');
        } else  if(size.classList.contains("font-size-5")){
            fontSize = '18.5px';
            root.style.setProperty('----sticky-top-left','-12rem');
            root.style.setProperty('----sticky-top-right','-35rem');
        }

            // change font size of the root html element
    document.querySelector('html').style.fontSize = fontSize;

    })

})

//remove active class from colors
const changeActiveColorClass = () => {
    colorPalette.forEach(colorPicker => {
        colorPicker.classList.remove('active');
    })
}

//change primary colors

colorPalette.forEach(color => {
    color.addEventListener('click',() => {
        let primary;
        changeActiveColorClass();

        if(color.classList.contains('color-1')){
            primaryHue = 252;
        } else if(color.classList.contains('color-2')){
            primaryHue = 52;
        }
        else if(color.classList.contains('color-3')){
            primaryHue = 352;
        }
        else if(color.classList.contains('color-4')){
            primaryHue = 152;
        }
        else if(color.classList.contains('color-5')){
            primaryHue = 202;
        }
        color.classList.add('active');
        root.style.setProperty('--primary-color-hue', primaryHue)
    })
})



// theme BACKGROUND Values
let lightColorLightness;
let whiteColorLightness;
let darkColorLightness;

// changes background color
const changeBG = () => {
    root.style.setProperty('--light-color-lightness', lightColorLightness);
    root.style.setProperty('--white-color-lightness', whiteColorLightness);
    root.style.setProperty('--dark-color-lightness', darkColorLightness);
}

Bg1.addEventListener('click', () => {
    //add active class
    Bg1.classList.add('active');
    //remove active class from the others
    Bg2.classList.remove('active');
    Bg3.classList.remove('active');
    window.location.reload();
})

Bg2.addEventListener('click', () => {
    darkColorLightness = '95%';
    whiteColorLightness = '20%';
    lightColorLightness = '15%';

    //add active class
    Bg2.classList.add('active');
    //remove active class from the others
    Bg1.classList.remove('active');
    Bg3.classList.remove('active');
    changeBG();
})

Bg3.addEventListener('click', () => {
    darkColorLightness = '95%';
    whiteColorLightness = '10%';
    lightColorLightness = '0%';

    //add active class
    Bg3.classList.add('active');
    //remove active class from the others
    Bg1.classList.remove('active');
    Bg2.classList.remove('active');
    changeBG();
})

//END




// Profile links

//opens model
const openProfileModal = () => {
    profileModal.style.display = 'grid';
}

const closeProfileModel = (e) => {
    if(e.target.classList.contains('profile-links')) {
        profileModal.style.display = 'none';
    }
}


profile.addEventListener('click', openProfileModal);

//closing the model
profileModal.addEventListener('click', closeProfileModel);

//END






// Explore links

//opens model
const openExploreModal = () => {
    exploreModal.style.display = 'grid';
}

const closeExploreModel = (e) => {
    if(e.target.classList.contains('explore-links')) {
        exploreModal.style.display = 'none';
    }
}


explore.addEventListener('click', openExploreModal);

//closing the model
exploreModal.addEventListener('click', closeExploreModel);

//END
