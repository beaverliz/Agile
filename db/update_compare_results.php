<?php

define("PATH_TO_PARAMS2", "C:\\xampp\\htdocs\\lottery-project\\Agile\\local\\db_params.inc");

function update_p_n($lottery_id, $numbers, $p_array, $n_array) {
    include PATH_TO_PARAMS;
    $conn = mysqli_connect($SERVER, $USER, $PASSWORD, $DATABASE);
    foreach ($numbers as $key => $number) {
        $p_value = $p_array[$key];
        $n_value = $n_array[$key];
        $sql = "UPDATE numbers SET p = ?, n = ? WHERE lottery_id = ? AND number = ?";
        $stmt = mysqli_prepare($conn, $sql);
        mysqli_stmt_bind_param($stmt, "iiii", $p_value, $n_value, $lottery_id, $number);
        mysqli_stmt_execute($stmt);
        mysqli_stmt_close($stmt);
    }
    mysqli_close($conn);
}
