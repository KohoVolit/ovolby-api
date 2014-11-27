<?php

if (isset($_GET['charset']) and in_array($_GET['charset'],$settings['table_available_charsets']))
    $charset = $_GET['charset'];
else
    $charset = 'utf-8';

if (isset($_GET['delimiter']) and in_array($_GET['delimiter'],$settings['table_available_delimiters']))
    $delimiter = $_GET['delimiter'];
else
    $delimiter = ',';

// http://code.stephenmorley.org/php/creating-downloadable-csv-files/
// output headers so that the file is downloaded rather than displayed
header("Content-Type: text/csv; charset=" . $charset);
header('Content-Disposition: attachment; filename=data.csv');

// create a file pointer connected to the output stream
$output = fopen('php://output', 'w');

//header
$outrow = array_merge([''],$table['headers']['column']);
if ($charset != 'utf-8')
  $outrow = iconv_array($outrow,'utf-8',$charset);
fputcsv($output, $outrow, $delimiter);

//rows
foreach ($table['headers']['row'] as $rkey => $row) {
  $outrow = [iconv('utf-8',$charset,$row)];
  foreach ($table['headers']['column'] as $ckey => $column) {
    if (isset($table['data'][$rkey][$ckey])) 
      $outrow[] = $table['data'][$rkey][$ckey];
    else
      $outrow[] = '';
  }
  fputcsv($output, $outrow, $delimiter);
}

function iconv_array($array,$from,$to) {
  $out = [];
  foreach ($array as $item)
    $out[] = iconv($from,$to,$item);
  return $out;
}


?>
