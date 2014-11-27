<?php

include("settings.php");
include_once("functions.php");
include("text.php");

require($settings['smarty_path']);
global $smarty;
$smarty = new Smarty();
$smarty->setTemplateDir($settings['page2smarty_path'] . 'templates');
$smarty->setCompileDir($settings['page2smarty_path'] . 'templates_c');

?>
