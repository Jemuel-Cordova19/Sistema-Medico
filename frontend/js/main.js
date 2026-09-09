document.getElementById("loginForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const correo = document.getElementById("correo").value;
    const password = document.getElementById("password").value;
    const mensajeEl = document.getElementById("mensaje");

    mensajeEl.style.color = "black";
    mensajeEl.textContent = "Verificando...";

    try {
        // Enviar credenciales al servidor Backend local
        const respuesta = await fetch("/api/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ correo, password })
        });

        const data = await respuesta.json();

        if (respuesta.ok) {
            mensajeEl.style.color = "green";
            mensajeEl.textContent = `¡Bienvenido ${data.usuario.correo} (${data.usuario.rol})!`;
        } else {
            mensajeEl.style.color = "red";
            mensajeEl.textContent = data.detail || "Error al iniciar sesión";
        }
    } catch (error) {
        mensajeEl.style.color = "red";
        mensajeEl.textContent = "No se pudo conectar con el servidor Backend";
    }
});