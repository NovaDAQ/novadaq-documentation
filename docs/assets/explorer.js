(() => {
  "use strict";
  const host = document.getElementById("dependency-explorer");
  if (!host) return;
  const scriptURL = document.currentScript.src;
  const select = document.getElementById("package-select");
  const extra = document.getElementById("include-extra");
  const summary = document.getElementById("dependency-summary");
  const graph = document.getElementById("dependency-graph");
  const targetTable = document.getElementById("dependency-table");
  const NS = "http://www.w3.org/2000/svg";
  const core = new Set(["source include", "build link", "runtime command"]);
  function svgElement(name, attrs, value) {
    const e = document.createElementNS(NS, name);
    for (const [k, v] of Object.entries(attrs || {})) e.setAttribute(k, v);
    if (value !== undefined) e.textContent = value;
    return e;
  }
  function packageURL(name) { return `../packages/${encodeURIComponent(name)}.html`; }
  fetch(new URL("dependencies.json", scriptURL))
    .then(r => { if (!r.ok) throw new Error(`HTTP ${r.status}`); return r.json(); })
    .then(data => {
      for (const name of Object.keys(data.packages).sort()) {
        const option = document.createElement("option");
        option.value = name; option.textContent = `${name} — ${data.packages[name].group}`;
        select.appendChild(option);
      }
      const requested = new URLSearchParams(location.search).get("package");
      select.value = Object.hasOwn(data.packages, requested) ? requested : "NovaDataLogger";
      function render() {
        const name = select.value;
        const edges = data.edges.filter(e => (extra.checked || core.has(e.kind)) &&
          (e.source === name || e.target === name));
        const incoming = [...new Set(edges.filter(e => e.target === name).map(e => e.source))].sort();
        const outgoing = [...new Set(edges.filter(e => e.source === name).map(e => e.target))].sort();
        summary.textContent = `${name}: ${incoming.length} direct consumers, ${outgoing.length} dependencies, ` +
          `${edges.length} typed relationships. ${data.packages[name].purpose}`;
        graph.replaceChildren(); targetTable.replaceChildren();
        const rows = Math.max(1, incoming.length, outgoing.length);
        const height = rows * 52 + 90;
        const svg = svgElement("svg", {viewBox:`0 0 1050 ${height}`, width:1050, height,
          role:"img", "aria-label":`Consumers and dependencies of ${name}`});
        svg.appendChild(svgElement("title", {}, `Consumer to dependency graph: ${name}`));
        const defs = svgElement("defs");
        const marker = svgElement("marker", {id:"dep-arrow", markerWidth:8, markerHeight:8,
          refX:7, refY:4, orient:"auto"});
        marker.appendChild(svgElement("path", {d:"M0,0 L8,4 L0,8 z", fill:"#64748b"}));
        defs.appendChild(marker); svg.appendChild(defs);
        const yCenter = height / 2;
        svg.appendChild(svgElement("text", {x:150,y:25,"text-anchor":"middle",class:"graph-label"}, "Consumers"));
        svg.appendChild(svgElement("text", {x:525,y:25,"text-anchor":"middle",class:"graph-label"}, "Selected package"));
        svg.appendChild(svgElement("text", {x:900,y:25,"text-anchor":"middle",class:"graph-label"}, "Dependencies"));
        function y(i, total) { return (height - total * 52) / 2 + i * 52 + 26; }
        function arrow(x1,y1,x2,y2) {
          const dx = (x2-x1)/2;
          svg.appendChild(svgElement("path", {d:`M${x1},${y1} C${x1+dx},${y1} ${x2-dx},${y2} ${x2},${y2}`,
            fill:"none",stroke:"#94a3b8","stroke-width":1.4,"marker-end":"url(#dep-arrow)"}));
        }
        incoming.forEach((n,i) => arrow(290,y(i,incoming.length),385,yCenter));
        outgoing.forEach((n,i) => arrow(665,yCenter,760,y(i,outgoing.length)));
        function box(n,x,cy,selected) {
          const a=svgElement("a",{href:packageURL(n),"aria-label":`Open ${n} documentation`});
          a.appendChild(svgElement("rect",{x,y:cy-19,width:280,height:38,rx:5,
            fill:selected?"#0f4c81":"#f1f5f9",stroke:selected?"#0f4c81":"#cbd5e1"}));
          a.appendChild(svgElement("text",{x:x+140,y:cy+5,"text-anchor":"middle",
            fill:selected?"white":"#172b4d","font-size":12},n));
          svg.appendChild(a);
        }
        incoming.forEach((n,i)=>box(n,10,y(i,incoming.length),false));
        outgoing.forEach((n,i)=>box(n,760,y(i,outgoing.length),false));
        box(name,385,yCenter,true); graph.appendChild(svg);
        graph.scrollLeft = Math.max(0, (1050 - graph.clientWidth) / 2);
        const table=document.createElement("table");
        const caption=document.createElement("caption");caption.textContent="Relationship evidence";table.appendChild(caption);
        const tr=document.createElement("tr");
        for(const h of ["Consumer","Dependency","Type","Evidence"]){
          const th=document.createElement("th");th.scope="col";th.textContent=h;tr.appendChild(th);
        }
        const thead=document.createElement("thead");thead.appendChild(tr);table.appendChild(thead);
        const tbody=document.createElement("tbody");
        for(const e of edges){
          const row=document.createElement("tr");
          for(const n of [e.source,e.target]){
            const td=document.createElement("td"),a=document.createElement("a");
            a.href=packageURL(n);a.textContent=n;td.appendChild(a);row.appendChild(td);
          }
          const kind=document.createElement("td");kind.textContent=e.kind;row.appendChild(kind);
          const ev=document.createElement("td"), a=document.createElement("a"), proof=e.evidence[0];
          const commit=data.packages[e.source].commit;
          a.href=`https://github.com/NovaDAQ/${e.source}/blob/${commit}/${proof.path.split('/').map(encodeURIComponent).join('/')}#L${proof.line}`;
          a.textContent=`${proof.path}:${proof.line}`;ev.appendChild(a);row.appendChild(ev);tbody.appendChild(row);
        }
        table.appendChild(tbody);targetTable.appendChild(table);
      }
      select.addEventListener("change",render);extra.addEventListener("change",render);render();
    }).catch(error => { summary.textContent=`Could not load dependency data: ${error.message}. Serve the site over HTTP or use the static dependency pages.`; });
})();
