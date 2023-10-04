<?php
$host = "mi_postgres"; // nombre del contenedor PostgreSQL
$usuario = "tu_usuario";
$contrasena = "tu_contrasena";
$base_datos = "tu_base_de_datos";

$conexion = pg_connect("host=$host dbname=$base_datos user=$usuario password=$contrasena");

if (!$conexion) {
    die("Error en la conexión a la base de datos: " . pg_last_error());
}
?>
