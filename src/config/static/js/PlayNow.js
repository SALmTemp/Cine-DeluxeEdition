function PlayNow() {
    // Verifica si hay un movieId almacenado en el localStorage
    const storedMovieId = window.localStorage.getItem("movieId");

    if (storedMovieId) {
        // Construye la URL externa con el movieId
        const externalLink = `https://akamai.interplanetary.video/?v=aHR0cHM6Ly9maWxlbGlvbnMudG8vdi9scjc0d3JqYnhvcTk=${storedMovieId}`;

        // Redirige a la nueva URL
        window.location.href = externalLink;
    } else {
        // Manejo si no hay un movieId almacenado
        alert("No se ha encontrado un ID de película almacenado.");
    }
}