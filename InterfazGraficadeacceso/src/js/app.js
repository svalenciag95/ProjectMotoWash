function guardarDatos(event) {
    event.preventDefault();

    var nombreCliente = document.getElementById('nombre').value;
    var marcaMoto = document.getElementById('marca').value;
    var cilindraje = document.getElementById('cilindraje').value;
    var placaMoto = document.getElementById('placa').value.toUpperCase(); 
    var tipoLavado = document.getElementById('tipoLavado').value;

    // Puedes hacer lo que necesites con los datos, por ejemplo, enviarlos a un servidor
    console.log("Nombre del Cliente:", nombreCliente);
    console.log("Marca de la Moto:", marcaMoto);
    console.log("Cilindraje:", cilindraje);
    console.log("Placa de la Moto:", placaMoto);
    console.log("Tipo de Lavado:", tipoLavado);
}