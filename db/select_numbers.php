<?php

define("PATH_TO_PARAMS", "C:\\xampp\\htdocs\\lottery-project\\Agile\\local\\db_params.inc");

function get_numbers_by_lottery_id($lottery_id) {
    include PATH_TO_PARAMS;
    $conn = mysqli_connect($SERVER, $USER, $PASSWORD, $DATABASE);
    $sql = "SELECT number FROM numbers WHERE lottery_id = ?";
    $stmt = mysqli_prepare($conn, $sql);
    mysqli_stmt_bind_param($stmt, "i", $lottery_id);
    mysqli_stmt_execute($stmt);
    $result = mysqli_stmt_get_result($stmt);
    $numbers = [];
    while ($row = mysqli_fetch_assoc($result)) {
        $numbers[] = $row['number'];
    }
    mysqli_close($conn);
    return $numbers;
}
