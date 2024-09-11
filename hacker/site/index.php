<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <link href="https://fonts.googleapis.com/css?family=Raleway" rel="stylesheet">
    <title>Сайт</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <link rel="stylesheet" type="text/css" href="css/main.css">
</head>
<body>
    <div>
        <h1>Моя первая страница!</h1>
        <!-- Форма отправляет данные на этот же сайт -->
        <form action="index.php" method="post">
            <label for="POST-name">Введите Логин:</label>
            <input id="POST-name" type="text" name="login" required />
            
            <label for="POST-password">Введите Пароль:</label>
            <input id="POST-password" type="password" name="password" required />
            
            <input type="submit" value="Войти" />
        </form>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit...</p>
        <img src="img/img1.jpeg">
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit...</p>
        <img src="img/img2.jpeg">
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit...</p>
        <img src="img/img3.jpeg">
    </div>
</body>

<?php
// Проверяем, пришли ли данные через POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $login = htmlspecialchars($_POST['login']);
    $password = htmlspecialchars($_POST['password']);

    // Открываем файл logins.txt для записи
    $file = fopen("logins.txt", "a");
    
    // Записываем логин и пароль в файл
    fwrite($file, "Логин: $login, Пароль: $password\n");
    
    // Закрываем файл
    fclose($file);

    // Сообщение пользователю
    echo "Ваши данные успешно сохранены!";
}
?>

</html>
