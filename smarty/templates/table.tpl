<table id="table" class="table tablesorter">
  <thead>
    <tr>
      <th></th>
      {foreach $table['headers']['column'] as $column}
        <th>{$column|truncate:50:"..."}</th>
      {/foreach}
    </tr>
  </thead>
  <tbody>
    {foreach $table['headers']['row'] as $rkey => $row}
      <tr>
        <td class="first-column">{$row}</td>
        {foreach $table['headers']['column'] as $ckey => $column}
          <td>{if (isset($table['data'][$rkey][$ckey]))}{$table['data'][$rkey][$ckey]}{/if}</td>
        {/foreach}
      </tr>
    {/foreach}
  </tbody>
</table>
