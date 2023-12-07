<?php

include "../db/select_compare_results.php";
include "../db/update_plot.php";

$lottery_id = $_REQUEST["lottery"];

$compare_results = get_p_n_arrays($lottery_id);
$p_array = $compare_results['p'];
$n_array = $compare_results['n'];

$command = escapeshellcmd("python ../python/clustering.py " . escapeshellarg(json_encode($p_array)) . " " . escapeshellarg(json_encode($n_array)));
$output = shell_exec($command);
$plot_path = json_decode($output, true);

update_image($lottery_id, $plot_path);

echo json_encode($plot_path);
