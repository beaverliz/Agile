<?php

define("PATH_TO_PARAMS", "C:\\xampp\\htdocs\\lottery-project\\Agile\\local\\db_params.inc");

function insert_number($lottery_id, $number) {
    include PATH_TO_PARAMS;
    $conn = mysqli_connect($SERVER, $USER, $PASSWORD, $DATABASE);
    $sql = "INSERT INTO info (lottery_id, number) VALUES (?, ?)";
    $stmt = mysqli_prepare($conn, $sql);
    mysqli_stmt_bind_param($stmt, "ii", $lottery_id, $number);
    mysqli_stmt_execute($stmt);
    mysqli_close($conn);
}

function insert_generated_numbers($lottery_id, $numbers_array) {
    include PATH_TO_PARAMS;
    $conn = mysqli_connect($SERVER, $USER, $PASSWORD, $DATABASE);
    $sql = "INSERT INTO numbers (lottery_id, number) VALUES (?, ?)";
    $stmt = mysqli_prepare($conn, $sql);
    foreach ($numbers_array as $number) {
        mysqli_stmt_bind_param($stmt, "ii", $lottery_id, $number);
        mysqli_stmt_execute($stmt);
    }
    mysqli_close($conn);
}
