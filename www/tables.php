<?php

set_time_limit(600);

include_once('include.php');

if (ob_get_level() == 0) ob_start();


if (isset($_GET['format']))
  $format = $_GET['format'];
else
  $format = 'html';

if (isset($_GET['charset']))
  $charset = $_GET['charset'];
else
  $charset = 'utf-8';

if (isset($_GET['delimiter']))
  $delimiter = $_GET['delimiter'];
else
  $delimiter = ',';

$url_params = [
  'p' => $_GET['p'],
  'format' => $format,
  'charset' => $charset,
  'delimiter' => $delimiter
];

$url = urldecode($settings['www_server'] . 'table.php?' . http_build_query($url_params));

if ($format == 'csv') { 
    header("Location: " . $url);
    die();
}

$table = download($url);

$get = $url_params;
$get['format'] = 'csv';
$csvlink = $settings['www_server'] . 'table.php?' . http_build_query($get);
$get['delimiter'] = ';';
$get['charset'] = 'cp1250';
$csvlink2 = $settings['www_server'] . 'table.php?' . http_build_query($get);


$links = [
  'CSV' => $csvlink,
  'CSV pro český Excel' => $csvlink2,
];

$smarty->assign('table',$table);
$smarty->assign('text',$text);
$smarty->assign('links',$links);

$smarty->display('tables.tpl');

?>
