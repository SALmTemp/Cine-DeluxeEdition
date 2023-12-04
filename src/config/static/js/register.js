const prevBtns = document.querySelectorAll(".btn-prev");
const nextBtns = document.querySelectorAll(".btn-next");
const progress = document.getElementById("progress");
const formSteps = document.querySelectorAll(".form-step");
const progressSteps = document.querySelectorAll(".progress-step");

let formStepsNum = 0;

nextBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
        formStepsNum++;
        updateFormSteps();
        updateProgressbar();
    });
});

prevBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
        formStepsNum--;
        updateFormSteps();
        updateProgressbar();
    });
});

function updateFormSteps() {
    formSteps.forEach((formStep) => {
        formStep.classList.contains("form-step-active") &&
            formStep.classList.remove("form-step-active");
    });

    formSteps[formStepsNum].classList.add("form-step-active");
}

function updateProgressbar() {
    progressSteps.forEach((progressStep, idx) => {
        if (idx < formStepsNum + 1) {
            progressStep.classList.add("progress-step-active");
        } else {
            progressStep.classList.remove("progress-step-active");
        }
    });

    const progressActive = document.querySelectorAll(".progress-step-active");

    progress.style.width =
        ((progressActive.length - 1) / (progressSteps.length - 1)) * 100 + "%";
}

// Función para verificar datos y mostrar/ocultar el botón
function verificarDatos() {
    // Obtener los valores ingresados por el usuario
    const correo = document.getElementById('textemail').value;
    const contrasena = document.getElementById('password').value;

    // Verificar si la contraseña y el correo son válidos
    if (validarContrasena(contrasena) && validarCorreo(correo)) {
        // Mostrar el botón si ambos campos son válidos
        mostrarBotonNext();
    } else {
        // Ocultar el botón si alguno de los campos no es válido
        ocultarBotonNext();
    }
}

function mostrarBotonNext() {
    // Seleccionar el botón por su id
    const btnNext = document.getElementById('Next1');

    // Cambiar el estilo para mostrar el botón
    btnNext.style.display = 'block';
}

function ocultarBotonNext() {
    // Seleccionar el botón por su id
    const btnNext = document.getElementById('Next1');

    // Cambiar el estilo para ocultar el botón
    btnNext.style.display = 'none';
}

// Función para validar la contraseña
function validarContrasena(contrasena) {
    // Verificar que la contraseña tenga al menos 8 caracteres y contenga '@' y '.com'
    return contrasena.length >= 8
}

/***
 * 
 * ------FUNCION PARA ENVIAR CORREO CON UN CÓDIGO---------
 * 
 */

// Función para validar el correo electrónico
function validarCorreo(correo) {
    // Verificar que el correo contenga '@' y '.com'
    return correo.includes('@') && correo.includes('.com');
}

// Función para enviar correo
function VerificarEmail() {
    // Obtener el correo electrónico ingresado por el usuario
    const correo = document.getElementById('textemail').value;

    // Realizar la solicitud al servidor para enviar el código de verificación
    axios.post('forgotpassword', {
            fullcorreo: correo,
        }, {
            headers: {
                'Content-Type': 'application/json',
            }
        })
        .then((response) => {
            console.log(response.data);

            // Verificar si la solicitud fue exitosa
            if (response.status === 200) {
                // Mostrar un mensaje al usuario indicando que se envió el código
                alert('Código de verificación enviado. Revise su correo electrónico.');
            } else {
                // Manejar otros casos según tu lógica
                alert('Error al enviar el código de verificación.');
            }
        })
        .catch((error) => {
            console.error(error);

            // Manejar errores según tu lógica
            alert('Error al enviar el código de verificación.');
        });
}


function VerificarCode() {
    const digit1 = document.getElementById('Code-text');
    const gmailInput = document.getElementById('textemail');
    const email = gmailInput.value;

    // Realizar la solicitud al servidor para verificar el código
    axios.post('verificarcode', {
            verification_code: digit1.value,
        })
        .then(function(response) {
            // Verificación exitosa
            console.log('Verificación exitosa');
        })
        .catch(function(error) {
            // Verificación fallida
            console.error('Verificación fallida', error);
            // Puedes agregar acciones adicionales para la verificación fallida aquí
        });
}