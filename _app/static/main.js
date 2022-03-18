const myForm = document.getElementById('formulario');
const txt_username = document.getElementById('txt_username');
const txt_email = document.getElementById('txt_email');
const mensajeAlerta = document.getElementById('mensajeAlerta');

myForm.onsubmit = function(e){
    e.preventDefault();
    var form = new FormData(myForm);
    fetch("/create_usuario", { method :'POST', body : form})
        .then( response => response.json() )
        .then( data => {
            switch(data.message)
            {
                case 'User name must be at least 2 characters':
                    txt_username.value = "";
                    mensajeAlerta.innerHTML = data.message;
                    mensajeAlerta.classList.add("alert");
                    mensajeAlerta.classList.add("alert-danger");
                    break;
                case 'Enter an email':
                    txt_email.value = ""
                    mensajeAlerta.innerHTML = data.message;
                    mensajeAlerta.classList.add("alert");
                    mensajeAlerta.classList.add("alert-danger");
                    break;
                case 'Invalid Email':
                    txt_email.value = ""
                    mensajeAlerta.innerHTML = data.message;
                    mensajeAlerta.classList.add("alert");
                    mensajeAlerta.classList.add("alert-danger");
                    break;
                case 'Email already exists!':
                    txt_email.value = ""
                    mensajeAlerta.innerHTML = data.message;
                    mensajeAlerta.classList.add("alert");
                    mensajeAlerta.classList.add("alert-danger");
                    break;
                case 'Add a user!!!':
                    txt_username.value = ""
                    txt_email.value = ""
                    mensajeAlerta.innerHTML = "";
                    mensajeAlerta.classList.remove("alert");
                    mensajeAlerta.classList.remove("alert-danger");
                    console.log(data)
                    window.location.href = "/";
            }
        });
}