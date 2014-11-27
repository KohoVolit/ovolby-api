<?php

set_time_limit(600);

include_once('settings.php');
include_once('include.php');

if (ob_get_level() == 0) ob_start();

$p = json_decode($_GET['p']);
//print_r($p);
$items = get_all_items($settings['api_server'],'results',$p,$smarty,0);

$table = table($settings['api_server'],$items,$p->layout);

if (isset($_GET['format']) and in_array($_GET['format'],$settings['table_available_formats'])) {
  if ($_GET['format'] == 'csv') {
    include_once("output_csv.php");
    die();
  }
}

$smarty->assign('table',$table);

if (isset($error) and $error['error'])
    $smarty->display('error.tpl');
else
    $smarty->display('table.tpl');

?>
