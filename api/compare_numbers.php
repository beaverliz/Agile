<?php

include "../db/select_numbers.php";
include "../db/update_compare_results.php";

$lottery_id = $_REQUEST["lottery"];
$number = $_REQUEST["number"];

$numbers = get_numbers_by_lottery_id($lottery_id);

$command = escapeshellcmd("python ../python/compare_numbers.py $number " . implode(" ", $numbers));
$output = shell_exec($command);
$result_arrays = json_decode($output, true);

$p_array = $result_arrays[0];
$n_array = $result_arrays[1];
update_p_n($lottery_id, $numbers, $p_array, $n_array);

echo json_encode($result_arrays);
