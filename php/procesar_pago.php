<?php
// Conexión a la base de datos
$conexion = new mysqli("localhost", "user", "password", "simplifybiz");

if ($conexion->connect_error) {
    die("Error de conexión: " . $conexion->connect_error);
}

// Obtener el correo del usuario
$usuario = $_POST['email'];

// Generar un código de compra único
$codigoCompra = uniqid();

// Insertar en la base de datos con consulta segura
$stmt = $conexion->prepare("INSERT INTO compras (email, codigo) VALUES (?, ?)");
$stmt->bind_param("ss", $usuario, $codigoCompra);
$stmt->execute();
$stmt->close();

// Cerrar la conexión
$conexion->close();

echo "✅ Pago exitoso. Tu código de compra es: <strong>$codigoCompra</strong>. Guárdalo para descargar el software.";
?>
