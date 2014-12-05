{extends file='page.tpl'}
{block name=body}
{literal}
<div class="modal-dialog modal-lg">
  <div class="modal-content">
    <div class="modal-header" id="infobox_header">
      <h1>Volební výsledky flexibilně - ukázky</h1>
      Aplikace je umístěna na dočasné doméně.
      <h3>API</h3>
      <p>Výsledky voleb jsou nejen uloženy v databázy, ale jsou strojově čitelné pomocí <strong>API</strong>. Je možné pomocí něho jak číst data, tak (s příslušným oprávněním) do databáze zapisovat. U jednotlivých území jsou dodržovány kódy z ČSÚ. API umožňuje budovat získávat data velice flexibilně i budovat další aplikace nad těmito daty.
      </p>
      <p>Příklady:<br/>
      <ul>
      <li><code>http://api.czechia.tk/ovolby/results?where={%22area_classification%22:%22province%22,%22election_id%22:%22europarl.europa.eu-cz-2004%22}</code> - výsledky evropských voleb 2004 po krajích</li>
      <li><code>http://api.czechia.tk/ovolby/areas?where={%22parents.area_id%22:%226203%22,%22parents.election_id%22:%22europarl.europa.eu-cz-2014%22}</code> - všechny obce, které při evropských volbách 2014 spadala pod Brno-venkov</li>
      <li><code>http://api.czechia.tk/ovolby/areas?where={%22parents.area_id%22:%22550973%22,%22parents.election_id%22:%22europarl.europa.eu-cz-2014%22}</code> - všechny okrsky, které při evropských volbách 2014 spadaly pod Brno-střed</li>
      <li><code>http://api.czechia.tk/ovolby/elections?where={%22start_date%22:{%22$gte%22:%222010-01-01%22}}</code> - všechny volby, které proběhly od roku 2010</li>
      </ul>
      </p>
      
      <h3>Výsledky voleb za všechna nižší území jednoho regionu</h3>
      <strong><a href="area_children.php?election_id=europarl.europa.eu-cz-2014">Aplikace</a></strong><br/>
      <p>Ukázková aplikace umožňuje vyhledat libovolné území (obce, okresy, kraje) a zobrazit výsledky jedněch voleb za všechny nižší území (tj. např. pro obce za okrsky, pro okresy za obce)</p>
      <p>Tabulky lze řadit dle jednotlivých sloupců</p>
      <p>Data z tabulek se dají stáhnout do <code>csv</code> a <code>csv pro český Excel</code> (tj. v kódování pro Windows a se středníky místo čárek).</p>
      
      <h3>Výsledky voleb z různých pohledů</h3>
      <p>Jako základní kámen aplikace je libovolné zobrazení dat v tabulkách, např.
      <ul>
      <li><a href="tables.php?p={%22where%22:{%22area_classification%22:%22county%22,%22election_id%22:%22europarl.europa.eu-cz-2004%22},%22layout%22:{%22row%22:%22areas%22,%22column%22:%22options%22}}&format=html">Evropské volby 2014 po okresech</a></li>
      <li><a href="tables.php?p={%22where%22:{%22area_id%22:%22582786%22},%22layout%22:{%22row%22:%22options%22,%22column%22:%22elections%22}}&format=html">Všechny volby 2004-2014 v Brně</a></li>
      <li><a href="tables.php?p={%22where%22:{%22area_classification%22:%22province%22,%22election_id%22:{%22$in%22:[%22europarl.europa.eu-cz-2004%22,%22europarl.europa.eu-cz-2009%22,%22europarl.europa.eu-cz-2014%22]}},%22layout%22:{%22row%22:%22areas%22,%22column%22:%22elections%22}}&format=html">Účast v evropských volbách 2004-2014 po krajích</a></li>
      </ul>
      <p>Tabulky lze řadit dle jednotlivých sloupců</p>
      <p>Data z tabulek se dají stáhnout do <code>csv</code> a <code>csv pro český Excel</code> (tj. v kódování pro Windows a se středníky místo čárek).</p>
     
      
      
      
      
      
    </div>
  </div>
</div>
 {/literal}       

{/block}
