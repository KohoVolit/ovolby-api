{extends file='page.tpl'}
{block name=body}

Download: 
{foreach $links as $k => $link}
  <span class="tag label label-info"><a href="{$link}">{$k}</a></span>
{/foreach}

{$table}

<script>
$(document).ready(function(){
    $(function(){
        $("#table").tablesorter();
    });
});

</script>

{/block}
