function guardarDatos() {
    var nombreCliente = document.getElementById('nombreCliente').value;
    var tipoMoto = document.getElementById('tipoMoto').value;
    var placaMoto = document.getElementById('placaMoto').value;

    // Envía los datos al servidor
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "guardar_datos.php", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        
    xhr.onreadystatechange = function () {

        if (xhr.readyState === 4 && xhr.status === 200) {
                // Respuesta del servidor (puedes manejarla según tus necesidades)
                console.log(xhr.responseText);
            }
        };
        
    var params = "nombreCliente=" + nombreCliente + "&tipoMoto=" + tipoMoto + "&placaMoto=" + placaMoto;
    xhr.send(params);
    }

