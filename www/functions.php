<?php


#$psjson = '{"where":{"area_classification":"province","election_id":"europarl.europa.eu-cz-2014","area_id":"1000","counts.option_id":"strana-zelenych"}}';
#$psjson = '{"where":{"area_classification":"county"}}';
//$psjson = '{"where":{"name":{"$in":{["strana-zelenych","vize-2014"]}}}}';
//$psjson = '{}';
//$psjson = 'nic';

//print_r(json_decode($psjson));die();

#if (ob_get_level() == 0) ob_start();

#$items = get_all_items($settings['api_server'],'results',json_decode($psjson),$smarty);

#$table = tableize($items,['row'=>'election_id','column'=>'area_id']);

#$table['headers'] = [];
#$table['headers']['row'] = get_names($settings['api_server'],'elections',array_keys($table['data']));
#$ids = [];
#foreach ($table['data'] as $row) {
#  foreach ($row as $k => $item) {
#    $ids[$k] = (string) $k;
#  }
#}
#$table['headers']['column'] = get_names($settings['api_server'],'areas',array_values($ids));
#print_r($table);


//all children of an area for 1 elections
function area_children($api_server,$area_id,$election_id) {
  global $smarty;
  $pstring = '{"where":{"parents.area_id":"'.$area_id.'", "parents.election_id":"'.$election_id.'"}}';
  $parameters = json_decode($pstring);
  $areas = get_all_items($api_server,'areas',$parameters,$smarty,0);
  $out = get_all_properties_from_items($areas);
  return $out;
}

function get_all_properties_from_items($items,$property='id') {
  $out = [];
  foreach($items as $item)
    $out[$item->$property] = $item->$property;
  return array_values($out);
}

// $resource may be either 'areas' or 'elections'
function get_all_resource_ids_from_items($resource,$items) {
  $id = resource2id($resource);
  $out = [];
  foreach($items as $item)
    $out[$item->$id] = $item->$id;
  return array_values($out);
}

function table($api_server,$items,$layout) {
//print_r($items);die();
    $table = tableize($items,$layout);
    $table['headers'] = [];
    $table['headers']['row'] = get_names($api_server, $layout->row, array_keys($table['data']));  
    $ids = [];
    foreach ($table['data'] as $row) {
        foreach ($row as $k => $item) {
            $ids[$k] = (string) $k;
        }
    }
    $table['headers']['column'] = get_names($api_server, $layout->column,array_values($ids)); 
    return $table;
}

function get_names($api_server,$resource,$ids) {
  $names = [];
  
  $parameters = new StdClass();
  $parameters->where = new StdClass();
  $parameters->where->id = new StdClass();
  $in = '$in';
  $ids = array_map('strval', $ids);
  $parameters->where->id->$in = $ids;
  
  $parameters->projection = new StdClass();
  $parameters->projection->name= 1;
  $parameters->projection->id = 1;
  global $smarty;
  //print_r($parameters);die();
  $items = get_all_items($api_server,$resource,$parameters,$smarty,0);
  
  foreach($items as $item) {
    $names[$item->id] = $item->name;
  }
  return $names;
}

/*
* areas -> area_id
*/
function resource2id($resource) {
  return substr($resource,0,-1) . '_id';
}

function tableize($items,$layout,$option_filter=false) {
    $table = ['data' => []];
    $layout_row = resource2id($layout->row);
    $layout_column = resource2id($layout->column);
    foreach($items as $item) {
        foreach($item->counts as $count) {
          $option_id = $count->option_id;
          $item->option_id = $count->option_id;
          if (isset($table['data'][$item->$layout_row][$item->$layout_column]))
            $table['data'][$item->$layout_row][$item->$layout_column] = $table['data'][$item->$layout_row][$item->$layout_column] + $count->votes;
          else
            $table['data'][$item->$layout_row][$item->$layout_column] = $count->votes;
        }
    }
    return $table;
}

function get($api_server,$resource,$parameters,$smarty) {
    $url_params = [];
    foreach ($parameters as $k => $parameter) {
        $url_params[$k] = json_encode($parameter);
    }
    $url = urldecode($api_server . $resource . '?' . http_build_query($url_params));
#    echo $url . "\n";
#    ob_flush();flush();
    $contents = @file_get_contents($url);
    if (!$contents) {
      set_error('api returned error',$smarty,'nic');
      return;
    } else {
      $data = json_decode($contents);
    }
    return $data;
}

function get_all_items($api_server,$resource,$parameters,$smarty,$limit=2) {
    //$items = [];
    $response_obj = get($api_server,$resource,$parameters,$smarty);
    $items = $response_obj->_items;
    $i = 2;
    while (isset($response_obj->_links->next)) {
        $parameters->page = $i;
        $response_obj = get($api_server,$resource,$parameters,$smarty);
        $new_items = $response_obj->_items;
        $items = array_merge($items,$new_items);
        $i++;
        if (($i >= $limit) and ($limit != 0)) return $items;
    }
    return $items;
}
function extract_all_items($data) {
    $items = [];
    if (isset($data->_items))
        $items = $data->_items;
    return $items;
}

function set_error($message,$smarty,$text) {
    $error = [
      'error' => true,
      'description' => $message
    ];
    $smarty->assign('title',$error['description']);
    $smarty->assign('error',$error);
#    echo 'ERROR';
    return $error;
}

/**
* curl downloader, with possible options
* @return html
* example:
* grabber('http://example.com',array(CURLOPT_TIMEOUT,180));
*/
function download($url,$options = array())
{
    $ch = curl_init ();
    curl_setopt ($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt ($ch, CURLOPT_URL, $url);
    //curl_setopt ($ch, CURLOPT_TIMEOUT, 120);
    if (count($options) > 0) {
    foreach($options as $option) {
        curl_setopt ($ch, $option[0], $option[1]);
    }
    }
    return curl_exec($ch);
    //curl_close ($ch);
}

?>
