{extends file='page.tpl'}
{block name=body}

<div class="radio bg-info well">
<label class="">
  <input type="radio" name="election_id" id="inlineRadio1" value="europarl.europa.eu-cz-2014" {if ($election_id == "europarl.europa.eu-cz-2014")} checked="checked"{/if}> Volby do Evropského parlamentu 2014 v České republice
</label>
<label class="">
  <input type="radio" name="election_id" id="inlineRadio2" value="europarl.europa.eu-cz-2009" {if ($election_id == "europarl.europa.eu-cz-2009")} checked="checked"{/if}> Volby do Evropského parlamentu 2009 v České republice
</label>
<label class="">
  <input type="radio" name="election_id" id="inlineRadio3" value="europarl.europa.eu-cz-2004" {if ($election_id == "europarl.europa.eu-cz-2004")} checked="checked"{/if}> Volby do Evropského parlamentu 2004 v České republice
</label>
</div>
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

$.urlParam = function(name){
    var results = new RegExp('[\?&amp;]' + name + '=([^&amp;#]*)').exec(window.location.href);
    return results[1] || 0;
}

$(function(){

    $('input:radio').change(
        function(){
            window.location.href = 'area_children.php?area_id='+$.urlParam('area_id')+'&election_id='+$('input[name=election_id]:checked').val();
        }
    );          

});

</script>

{/block}
