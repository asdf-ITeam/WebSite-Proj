window.onload = function() {
    const users_btn= document.querySelector('.users_btn');
    const remove_btn= document.querySelector('.user_minus');
    const add_btn= document.querySelector('.user_plus');
    const show_user1= document.querySelector('.user_list_title');
    const show_user2= document.querySelector('.user_list_detail');
    const show_user3= document.querySelector('.seprator');
    const show_add_user= document.querySelector('.add_user');
    const show_remove_user= document.querySelector('.remove_user');
    users_btn.addEventListener('click', function(){
        show_user1.classList.remove('isnt_active');
        show_user2.classList.remove('isnt_active');
        show_user3.classList.remove('isnt_active');
        show_add_user.classList.add('isnt_active');
        show_remove_user.classList.add('isnt_active');
    });
    remove_btn.addEventListener('click', function(){
        show_remove_user.classList.remove('isnt_active');
        show_user1.classList.add('isnt_active');
        show_user2.classList.add('isnt_active');
        show_user3.classList.add('isnt_active');
        show_add_user.classList.add('isnt_active');
    });
    add_btn.addEventListener('click', function(){
        show_add_user.classList.remove('isnt_active');
        show_remove_user.classList.add('isnt_active');
        show_user1.classList.add('isnt_active');
        show_user2.classList.add('isnt_active');
        show_user3.classList.add('isnt_active');
    });
}