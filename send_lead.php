<?php
/**
 * Fischer Abdichtungstechnik - Lead Form Mailer
 * Secure, modern PHP script to receive lead data and send as email.
 * Perfect for standard German web hosting (Strato, Ionos, All-Inkl, etc.).
 */

// Only allow POST requests
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('HTTP/1.1 405 Method Not Allowed');
    exit('Method Not Allowed');
}

// Set JSON response header
header('Content-Type: application/json');

// Get raw JSON body
$json = file_get_contents('php://input');
$data = json_decode($json, true);

if (!$data) {
    echo json_encode(['success' => false, 'message' => 'No data received']);
    exit;
}

// Sanitize inputs to prevent email injection & XSS
$name    = filter_var(trim($data['name'] ?? ''), FILTER_SANITIZE_SPECIAL_CHARS);
$phone   = filter_var(trim($data['phone'] ?? ''), FILTER_SANITIZE_SPECIAL_CHARS);
$email   = filter_var(trim($data['email'] ?? ''), FILTER_VALIDATE_EMAIL);
$message = filter_var(trim($data['message'] ?? ''), FILTER_SANITIZE_SPECIAL_CHARS);

// Validation
if (empty($name) || empty($phone) || !$email) {
    echo json_encode(['success' => false, 'message' => 'Ungültige Eingaben. Bitte Name, Telefon und gültige E-Mail angeben.']);
    exit;
}

// --- CONFIGURATION ---
// Change this to the target inbox where leads should arrive:
$recipient_email = "info@fischer-abdichtungstechnik.de"; 
$subject = "🔥 Neuer Lead: Horizontalsperre Landingpage - " . $name;

// --- EMAIL BODY (HTML) ---
$email_content = "
<html>
<head>
    <title>Neuer Lead von der Landingpage</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; color: #333333; }
        .container { max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #e2e8f0; border-radius: 8px; }
        .header { background-color: #1e293b; color: #ffffff; padding: 15px; border-radius: 6px 6px 0 0; text-align: center; }
        .header h2 { margin: 0; font-size: 20px; }
        .content { padding: 20px; }
        .field { margin-bottom: 15px; border-bottom: 1px solid #f1f5f9; padding-bottom: 10px; }
        .label { font-weight: bold; color: #475569; font-size: 13px; text-transform: uppercase; }
        .value { font-size: 16px; margin-top: 5px; color: #0f172a; }
        .footer { font-size: 11px; color: #94a3b8; text-align: center; margin-top: 20px; border-top: 1px solid #e2e8f0; padding-top: 10px; }
    </style>
</head>
<body>
    <div class='container'>
        <div class='header'>
            <h2>🔥 Neue Online-Terminanfrage</h2>
        </div>
        <div class='content'>
            <div class='field'>
                <div class='label'>Name des Interessenten:</div>
                <div class='value'>{$name}</div>
            </div>
            <div class='field'>
                <div class='label'>Telefonnummer:</div>
                <div class='value'><a href='tel:{$phone}'>{$phone}</a></div>
            </div>
            <div class='field'>
                <div class='label'>E-Mail-Adresse:</div>
                <div class='value'><a href='mailto:{$email}'>{$email}</a></div>
            </div>
            <div class='field'>
                <div class='label'>Beschreibung des Feuchtigkeitsproblems:</div>
                <div class='value'>" . (!empty($message) ? nl2br($message) : "<i>Keine Beschreibung angegeben.</i>") . "</div>
            </div>
        </div>
        <div class='footer'>
            Diese E-Mail wurde automatisch von der Fischer Horizontalsperren-Landingpage generiert.<br>
            Datum/Uhrzeit: " . date("d.m.Y H:i:s") . " Uhr
        </div>
    </div>
</body>
</html>
";

// --- HEADERS ---
$headers = [];
$headers[] = 'MIME-Version: 1.0';
$headers[] = 'Content-type: text/html; charset=utf-8';
$headers[] = 'From: Fischer Landingpage <no-reply@fischer-abdichtungstechnik.de>';
$headers[] = "Reply-To: {$name} <{$email}>";
$headers[] = 'X-Mailer: PHP/' . phpversion();

// --- SEND EMAIL ---
$mail_success = mail($recipient_email, $subject, $email_content, implode("\r\n", $headers));

if ($mail_success) {
    echo json_encode(['success' => true, 'message' => 'E-Mail erfolgreich gesendet.']);
} else {
    echo json_encode(['success' => false, 'message' => 'Fehler beim Senden der E-Mail über PHP mail().']);
}
?>
