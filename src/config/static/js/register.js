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

function VerificarEmail() {
    // Obtener el correo electrónico ingresado por el usuario
    const correo = document.getElementById('textemail').value;

    // Actualizar el contenido del label con el correo ingresado
    const labelCodigo = document.getElementById('label-content');
    labelCodigo.textContent = `Te hemos enviado un código de verificación a la dirección de correo ${correo}. ¡Por favor, tómate un momento para revisar tu bandeja de entrada y asegúrate de echar un vistazo!`;
    labelCodigo.style.color = '#6b38c1'; // Color morado oscuro

    // Deshabilitar el botón de avance
    document.getElementById('Next1').disabled = true;

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
                mostrarMensaje('Código de verificación enviado. Revise su correo electrónico.');
                // Habilitar el botón de avance
            } else {
                // Manejar otros casos según tu lógica
                mostrarMensaje('Error al enviar el código de verificación. Inténtelo nuevamente.');
                // Restablecer la bandera para bloquear el avance
                // Puedes agregar más acciones aquí si es necesario
            }
        })
        .catch((error) => {
            console.error(error);

            // Manejar errores según tu lógica
            if (error.response && error.response.status === 429) {
                // Error 429 - Too Many Requests
                mostrarMensajeError('Demasiadas solicitudes. Por favor, espere un momento antes de intentarlo nuevamente.');
                // Restablecer la bandera para bloquear el avance
                formStepsNum--;
                updateFormSteps();
                updateProgressbar();
                // Puedes agregar más acciones aquí si es necesario
            } else {
                mostrarMensajeError('Error al enviar el código de verificación. Inténtelo nuevamente.');
                // Restablecer la bandera para bloquear el avance
                // Puedes agregar más acciones aquí si es necesario
            }
        });
}

function mostrarMensajeError(mensaje) {
    // Mostrar el mensaje de error en el elemento con id 'label-Step'
    const mensajeErrorElement = document.getElementById('label-Step');

    // Verificar si el elemento existe antes de actualizar su contenido
    if (mensajeErrorElement) {
        mensajeErrorElement.textContent = mensaje;
        // Establecer el color del texto a rojo
        mensajeErrorElement.style.color = 'red';
    }
}


function mostrarMensaje(mensaje) {
    // Mostrar el mensaje en algún elemento HTML
    const mensajeElement = document.getElementById('mensaje');

    // Verificar si el elemento existe antes de actualizar su contenido
    if (mensajeElement) {
        mensajeElement.textContent = mensaje;
    }
}



function mostrarMensaje(mensaje) {
    // Mostrar el mensaje en algún elemento HTML
    const mensajeElement = document.getElementById('mensaje');

    // Verificar si el elemento existe antes de actualizar su contenido
    if (mensajeElement) {
        mensajeElement.textContent = mensaje;
    }
}


function mostrarMensaje(mensaje) {
    // Mostrar el mensaje en algún elemento HTML
    const mensajeElement = document.getElementById('mensaje');

    // Verificar si el elemento existe antes de actualizar su contenido
    if (mensajeElement) {
        mensajeElement.textContent = mensaje;

        // Avanzar al siguiente formulario solo si la bandera permite el avance
        if (puedeAvanzar) {
            avanzarAlSiguienteFormulario();
        }
    }
}

function avanzarAlSiguienteFormulario() {
    // Lógica para avanzar al siguiente formulario
    // Puedes agregar más acciones aquí si es necesario

    // Ejemplo: Mostrar el siguiente formulario o realizar otras acciones
    formStepsNum++;
    updateFormSteps();
    updateProgressbar();
    // Restablecer la bandera para futuras verificaciones
    puedeAvanzar = false;
}


function mostrarMensaje(mensaje) {
    // Mostrar el mensaje en algún elemento HTML
    const mensajeElement = document.getElementById('mensaje');

    // Verificar si el elemento existe antes de actualizar su contenido
    if (mensajeElement) {
        mensajeElement.textContent = mensaje;

        // Avanzar al siguiente formulario solo si la bandera permite el avance
        if (puedeAvanzar) {
            avanzarAlSiguienteFormulario();
        }
    }
}

function avanzarAlSiguienteFormulario() {
    // Lógica para avanzar al siguiente formulario
    // Puedes agregar más acciones aquí si es necesario

    // Ejemplo: Mostrar el siguiente formulario o realizar otras acciones
    formStepsNum++;
    updateFormSteps();
    updateProgressbar();
    // Restablecer la bandera para futuras verificaciones
    puedeAvanzar = false;
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