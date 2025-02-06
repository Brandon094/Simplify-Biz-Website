<?php
// Conexión a la base de datos
$conexion = new mysqli("localhost", "user", "password", "simplifybiz");

if ($conexion->connect_error) {
    die("Error de conexión: " . $conexion->connect_error);
}

// Obtener el código de compra ingresado por el usuario
$codigo = $_POST['codigoCompra'];

// Consultar en la base de datos con consulta segura
$stmt = $conexion->prepare("SELECT * FROM compras WHERE codigo = ?");
$stmt->bind_param("s", $codigo);
$stmt->execute();
$resultado = $stmt->get_result();

if ($resultado->num_rows > 0) {
    echo "<a href='/downloads/simplify-biz-windows.exe' class='download-btn'>Descargar ahora</a>";
} else {
    echo "❌ Código inválido. Verifica tu compra.";
}

$stmt->close();
$conexion->close();
?>
