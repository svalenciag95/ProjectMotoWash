<?php
include 'db_config.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nombreCliente = $_POST['nombreCliente'];
    $tipoMoto = $_POST['tipoMoto'];
    $placaMoto = $_POST['placaMoto'];

    $query = "INSERT INTO lavadero_motos (nombre_cliente, tipo_moto, placa_moto) VALUES ('$nombreCliente', '$tipoMoto', '$placaMoto')";
    $resultado = pg_query($conexion, $query);

    if (!$resultado) {
        echo "Error al insertar datos: " . pg_last_error();
    } else {
        echo "Datos insertados correctamente.";
    }
}

pg_close($conexion);
?>
