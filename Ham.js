window.onload = function () {
    const menu_btn = document.querySelector('.hamburger');
    const mobile_menu = document.querySelector('.mobile-nav')
    menu_btn.addEventListener('click',function(){
        menu_btn.classList.toggle('is-active');
        mobile_menu.classList.toggle('is-active');
    });
    function updateScreenSize() {
        const screenWidth = window.innerWidth;       
        if (screenWidth > 850) {
            const menu_btn = document.querySelector('.hamburger');
            const element = document.querySelector('.mobile-nav');
            menu_btn.classList.remove('is-active')
            element.classList.remove('is-active');
        }
    }    
    window.addEventListener('resize', updateScreenSize);
    updateScreenSize();

}