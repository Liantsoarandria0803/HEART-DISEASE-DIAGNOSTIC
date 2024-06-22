<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RESPONSE</title>
    <style>
        body{
            font-family: Arial, sans-serif;
            text-align:center;
            background-color: #f0f0f0;
        }
        section{
            width:max-content;
            height:34em;
            text-align:center;
        }
    </style>
</head>
<body>
    

<?php
// recuperation des valeurs venant de la formulaire 
$infoPerso = array("data"=> array(
    "nom" => $_POST['nom'],
    "age" => $_POST['age'],
    "sex" => $_POST['sex'],
    "cp" => $_POST['cp'],
    "trestbps" => $_POST['trestbps'],
    "chol" => $_POST['chol'],
    "fbs" => $_POST['fbs'],
    "restecg" => $_POST['restecg'],
    "thalach" => $_POST['thalach'],
    "exang" => $_POST['exang'],
    "oldpeak" => $_POST['oldpeak'],
    "slope" => $_POST['slope'],
    "ca" => $_POST['ca'],
    "thal" => $_POST['thal'])
);

// Conversion du tableau associatif en chaîne JSON
$jsonData = json_encode($infoPerso);

// Chemin du fichier JSON
$filePath = 'requestData.json';

// Ouverture du fichier en mode écriture
$file = fopen($filePath, 'w');

// Écriture de la chaîne JSON dans le fichier
fwrite($file, $jsonData);

// Fermeture du fichier
fclose($file);
$command=escapeshellcmd('python3 HeartDisease.py');
$output=exec($command);
echo "<section><h1>";
echo "$output";
echo "</section></h1>"
?>
</body>
</html>