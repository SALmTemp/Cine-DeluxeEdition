// Lógica para que aparezca el contenido cuando reciba la escucha del boton
document.addEventListener('DOMContentLoaded', function() {
    const learnMoreButton = document.getElementById('learnMoreButton');
    const additionalInfo = document.getElementById('additionalInfo');

    learnMoreButton.addEventListener('click', function() {
        additionalInfo.classList.toggle('hidden');
    });
});

function Login() {
    const Email = document.getElementById('email-input');
    const Password = document.getElementById('password-input');
    axios.post('login', {
            fullemail: Email.value,
            fullpassword: Password.value,
        })
        .then(function(response) {
            // Si la respuesta del servidor es exitosa, obtenemos el token generado
            // const token = response.data.token;
            // console.log(token);
            window.location.href = '/fronted/indexmain';
            // Ahora puedes almacenar el token en el local storage o en una cookie para usarlo posteriormente
            // ...
        })
        .catch(function(error) {
            // Si la respuesta del servidor es un error, mostramos un mensaje de error al usuario.
            console.log(error);
            alert('Invalid username or password');
        });
};