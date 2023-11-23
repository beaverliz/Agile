<?php

include "../db/select_numbers.php";

$number = $_REQUEST["number"];
$lottery_id = $_REQUEST["lottery"];

$numbers = get_numbers_by_lottery_id($lottery_id);

$command = escapeshellcmd("python ../python/compare_numbers.py $number " . implode(" ", $numbers));
$output = shell_exec($command);
$result_arrays = json_decode($output, true);

echo json_encode($result_arrays);
