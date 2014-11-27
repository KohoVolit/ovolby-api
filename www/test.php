<?php

set_time_limit(600);

include_once('settings.php');
include_once('include.php');

print_r($_GET);die();

$p = json_decode('{"where":{"classification":{"$nin":["district"]}}}');


$areas = get_all_items($settings['api_server'],'areas',$p,$smarty,0);

$out = [];
foreach ($areas as $area) {
  $out[] = ['id'=>$area->id,'name'=>$area->name];
}

$myfile = fopen("filter.json", "w");

echo count($out);

fwrite($myfile, json_encode($out));

fclose($myfile);

?>
