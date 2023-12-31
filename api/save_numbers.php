<?php

include "../db/get_lottery_id.php";
include "../db/insert_numbers.php";

$number = $_REQUEST["number"];

$lottery_id = get_new_lottery_id();
insert_number($lottery_id, $number);

$number_amount = 1000;
$random_numbers = array();
for ($i = 0; $i < $number_amount; $i++) {
    $random_numbers[] = rand(100000, 999999);
}
insert_generated_numbers($lottery_id, $random_numbers);

echo json_encode(array($lottery_id, $random_numbers));
