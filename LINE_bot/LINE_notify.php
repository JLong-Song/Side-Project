<?php
    if(isset($_GET['message'])){
        $headers = array(
            'Content-Type: multipart/form-data',
            'Authorization: Bearer DC2XlHbknzs3n5vI4D5FRFmObMnmEqpBrlsyvPNPMKz'
        );
        $message = array(
            'message' => $_GET['message']
        );
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, "https://notify-api.line.me/api/notify");
        curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $message);
        $result = curl_exec($ch);
        curl_close($ch);
    }
?>