<?php

define("PATH_TO_PARAMS1", "C:\\xampp\\htdocs\\lottery-project\\local\\db_params.inc");

function get_new_lottery_id() {
    include PATH_TO_PARAMS1;
    $conn = mysqli_connect($SERVER, $USER, $PASSWORD, $DATABASE);
    $sql = "SELECT MAX(lottery_id) AS max_lottery_id FROM info";
    $result = mysqli_query($conn, $sql);
    $row = mysqli_fetch_assoc($result);
    $max_lottery_id = $row['max_lottery_id'];
    mysqli_close($conn);
    return ($max_lottery_id !== null) ? $max_lottery_id + 1 : 0;
}
