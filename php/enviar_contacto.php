<?php
// Verificar si el formulario ha sido enviado
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Obtener los datos del formulario
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $subject = htmlspecialchars($_POST['subject']);
    $message = htmlspecialchars($_POST['message']);

    // Validación básica de los datos (si lo necesitas)
    if (!empty($name) && !empty($email) && !empty($subject) && !empty($message)) {
        
        // Dirección de correo electrónico donde recibirás el mensaje
        $to = "tu_correo@dominio.com";
        
        // Asunto del correo
        $mail_subject = "Nuevo mensaje de contacto: $subject";
        
        // Cuerpo del correo
        $mail_message = "
        <html>
        <head>
            <title>$mail_subject</title>
        </head>
        <body>
            <h2>Nuevo mensaje de contacto</h2>
            <p><strong>Nombre:</strong> $name</p>
            <p><strong>Correo Electrónico:</strong> $email</p>
            <p><strong>Asunto:</strong> $subject</p>
            <p><strong>Mensaje:</strong></p>
            <p>$message</p>
        </body>
        </html>
        ";
        
        // Encabezados del correo
        $headers = "MIME-Version: 1.0" . "\r\n";
        $headers .= "Content-Type:text/html;charset=UTF-8" . "\r\n";
        $headers .= "From: $email" . "\r\n"; // El correo del remitente

        // Enviar el correo
        if (mail($to, $mail_subject, $mail_message, $headers)) {
            echo "¡Gracias por tu mensaje! Nos pondremos en contacto contigo pronto.";
        } else {
            echo "Hubo un problema al enviar el mensaje. Intenta nuevamente.";
        }
    } else {
        echo "Por favor, completa todos los campos del formulario.";
    }
} else {
    echo "Error en la solicitud.";
}
?>
