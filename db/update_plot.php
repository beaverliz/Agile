<?php

define("PATH_TO_PARAMS2", "C:\\xampp\\htdocs\\lottery-project\\Agile\\local\\db_params.inc");

function update_image($lottery_id, $new_image_path) {
    include PATH_TO_PARAMS2;
    $conn = mysqli_connect($SERVER, $USER, $PASSWORD, $DATABASE);
    $sql = "UPDATE info SET image = ? WHERE lottery_id = ?";
    $stmt = mysqli_prepare($conn, $sql);
    mysqli_stmt_bind_param($stmt, "si", $new_image_path, $lottery_id);
    mysqli_stmt_execute($stmt);
    mysqli_close($conn);
}
