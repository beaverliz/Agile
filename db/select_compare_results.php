<?php

define("PATH_TO_PARAMS", "C:\\xampp\\htdocs\\lottery-project\\Agile\\local\\db_params.inc");

function get_p_n_arrays($lottery_id) {
    include PATH_TO_PARAMS;
    $conn = mysqli_connect($SERVER, $USER, $PASSWORD, $DATABASE);
    $sql = "SELECT p, n FROM numbers WHERE lottery_id = ?";
    $stmt = mysqli_prepare($conn, $sql);
    mysqli_stmt_bind_param($stmt, "i", $lottery_id);
    mysqli_stmt_execute($stmt);
    mysqli_stmt_bind_result($stmt, $p_value, $n_value);
    $p_array = array();
    $n_array = array();
    while (mysqli_stmt_fetch($stmt)) {
        $p_array[] = $p_value;
        $n_array[] = $n_value;
    }
    mysqli_close($conn);
    return array('p' => $p_array, 'n' => $n_array);
}
