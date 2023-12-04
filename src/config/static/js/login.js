// Lógica para que aparezca el contenido cuando reciba la escucha del boton
document.addEventListener('DOMContentLoaded', function() {
    const learnMoreButton = document.getElementById('learnMoreButton');
    const additionalInfo = document.getElementById('additionalInfo');

    learnMoreButton.addEventListener('click', function() {
        additionalInfo.classList.toggle('hidden');
    });
});