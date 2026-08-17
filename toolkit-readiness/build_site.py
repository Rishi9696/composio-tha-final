#!/usr/bin/env python3
"""
Builds site/index.html: a single self-contained HTML case-study page from the
research results. Run after results/results_final.json, results/patterns_final.json,
and results/verification_report.json exist.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
results = json.load(open(os.path.join(HERE, 'results/results_final.json')))
patterns = json.load(open(os.path.join(HERE, 'results/patterns_final.json')))
verif = json.load(open(os.path.join(HERE, 'results/verification_report.json')))

DATA_JS = f"""
const APPS = {json.dumps(results)};
const PATTERNS = {json.dumps(patterns)};
const VERIF = {json.dumps(verif)};
"""

html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Can an AI Agent Call This App? — 100-App Toolkit Readiness Study</title>
<style>
  :root{
    --bg:#0b0d12; --panel:#12151d; --panel2:#181c26; --border:#262b38;
    --text:#e8eaf0; --muted:#8b93a7; --accent:#5eead4; --accent2:#818cf8;
    --green:#34d399; --yellow:#fbbf24; --red:#f87171; --pink:#f472b6;
    --font: -apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, Roboto, sans-serif;
    --mono: 'SF Mono', 'Roboto Mono', Consolas, monospace;
  }
  *{box-sizing:border-box;}
  body{
    margin:0; font-family:var(--font); background:var(--bg); color:var(--text);
    line-height:1.5; font-size:15px;
  }
  .wrap{max-width:1180px; margin:0 auto; padding:0 24px;}
  header.hero{
    padding:56px 0 40px; border-bottom:1px solid var(--border);
    background: radial-gradient(1200px 400px at 20% -20%, rgba(94,234,212,0.08), transparent),
                radial-gradient(1000px 400px at 90% -10%, rgba(129,140,248,0.10), transparent);
  }
  .kicker{
    font-family:var(--mono); font-size:12px; letter-spacing:.14em; text-transform:uppercase;
    color:var(--accent); margin-bottom:14px; display:flex; gap:8px; align-items:center;
  }
  .kicker .dot{width:6px;height:6px;border-radius:50%;background:var(--accent);}
  h1{font-size:2.5rem; line-height:1.15; margin:0 0 14px; letter-spacing:-0.02em;}
  h1 em{font-style:normal; color:var(--accent);}
  .sub{color:var(--muted); font-size:1.05rem; max-width:760px; margin:0 0 26px;}
  .links{display:flex; gap:12px; flex-wrap:wrap;}
  .btn{
    display:inline-flex; align-items:center; gap:8px; padding:10px 16px; border-radius:8px;
    text-decoration:none; font-size:13.5px; font-weight:600; border:1px solid var(--border);
    color:var(--text); background:var(--panel2); transition:.15s;
  }
  .btn:hover{border-color:var(--accent); color:var(--accent);}
  .btn.primary{background:var(--accent); color:#03231e; border-color:var(--accent);}
  .btn.primary:hover{opacity:.9; color:#03231e;}

  section{padding:44px 0; border-bottom:1px solid var(--border);}
  .eyebrow{
    font-family:var(--mono); font-size:11.5px; letter-spacing:.12em; text-transform:uppercase;
    color:var(--muted); margin-bottom:8px;
  }
  h2{font-size:1.5rem; margin:0 0 6px; letter-spacing:-0.01em;}
  .lead{color:var(--muted); max-width:760px; margin-bottom:28px; font-size:14.5px;}

  /* Headline stat grid */
  .stats{display:grid; grid-template-columns:repeat(4,1fr); gap:14px; margin-bottom:8px;}
  .stat{
    background:var(--panel); border:1px solid var(--border); border-radius:12px; padding:20px;
  }
  .stat .num{font-size:2.1rem; font-weight:700; letter-spacing:-0.02em;}
  .stat .num.green{color:var(--green);} .stat .num.accent{color:var(--accent);}
  .stat .num.accent2{color:var(--accent2);} .stat .num.pink{color:var(--pink);}
  .stat .label{color:var(--muted); font-size:13px; margin-top:6px;}

  .findings{
    display:grid; grid-template-columns:repeat(2,1fr); gap:14px; margin-top:22px;
  }
  .finding{
    background:var(--panel); border:1px solid var(--border); border-left:3px solid var(--accent);
    border-radius:10px; padding:16px 18px;
  }
  .finding b{color:var(--text);}
  .finding{color:var(--muted); font-size:13.8px;}

  /* category bars */
  .catgrid{display:flex; flex-direction:column; gap:10px; margin-top:20px;}
  .catrow{display:grid; grid-template-columns:230px 1fr 90px; gap:14px; align-items:center;}
  .catname{font-size:13px; color:var(--text);}
  .catbar{height:20px; border-radius:6px; overflow:hidden; display:flex; background:var(--panel2); border:1px solid var(--border);}
  .catbar .seg-self{background:var(--green);}
  .catbar .seg-gated{background:var(--red);}
  .catbar .seg-unclear{background:var(--muted);}
  .catpct{font-family:var(--mono); font-size:12px; color:var(--muted); text-align:right;}

  .legend{display:flex; gap:18px; margin-top:14px; font-size:12.5px; color:var(--muted);}
  .legend span{display:inline-flex; align-items:center; gap:6px;}
  .sw{width:10px;height:10px;border-radius:3px;display:inline-block;}

  /* table */
  .table-controls{display:flex; gap:10px; margin-bottom:14px; flex-wrap:wrap;}
  input[type=text], select{
    background:var(--panel2); border:1px solid var(--border); color:var(--text);
    padding:9px 12px; border-radius:8px; font-size:13.5px; font-family:var(--font);
  }
  input[type=text]{flex:1; min-width:200px;}
  .table-wrap{border:1px solid var(--border); border-radius:12px; overflow:hidden;}
  table{width:100%; border-collapse:collapse; font-size:13px;}
  thead th{
    text-align:left; padding:11px 12px; background:var(--panel2); color:var(--muted);
    font-weight:600; font-size:11.5px; text-transform:uppercase; letter-spacing:.05em;
    border-bottom:1px solid var(--border); position:sticky; top:0; cursor:pointer; user-select:none;
  }
  thead th:hover{color:var(--accent);}
  tbody td{padding:10px 12px; border-bottom:1px solid var(--border); vertical-align:top;}
  tbody tr:hover{background:var(--panel);}
  tbody tr:last-child td{border-bottom:none;}
  .app-cell b{display:block; color:var(--text);}
  .app-cell span{color:var(--muted); font-size:11.5px;}
  .badge{
    display:inline-block; padding:3px 9px; border-radius:20px; font-size:11px; font-weight:600;
    white-space:nowrap;
  }
  .badge.green{background:rgba(52,211,153,.15); color:var(--green);}
  .badge.yellow{background:rgba(251,191,36,.15); color:var(--yellow);}
  .badge.red{background:rgba(248,113,113,.15); color:var(--red);}
  .badge.blue{background:rgba(129,140,248,.15); color:var(--accent2);}
  .badge.grey{background:rgba(139,147,167,.15); color:var(--muted);}
  .ev-link{color:var(--accent); text-decoration:none; font-size:11.5px;}
  .ev-link:hover{text-decoration:underline;}
  .row-count{color:var(--muted); font-size:12.5px; margin-bottom:10px;}

  /* pipeline diagram */
  .pipeline{display:flex; flex-wrap:wrap; gap:10px; margin:22px 0;}
  .pstep{
    flex:1; min-width:150px; background:var(--panel); border:1px solid var(--border);
    border-radius:10px; padding:14px 16px; position:relative;
  }
  .pstep .n{font-family:var(--mono); color:var(--accent); font-size:11px; margin-bottom:6px;}
  .pstep h4{margin:0 0 6px; font-size:13.5px;}
  .pstep p{margin:0; color:var(--muted); font-size:12px;}
  .arrow{align-self:center; color:var(--muted); font-size:18px;}

  .humanbox{
    background:var(--panel); border:1px solid var(--border); border-left:3px solid var(--pink);
    border-radius:10px; padding:18px 20px; margin-top:18px;
  }
  .humanbox h4{margin:0 0 10px; font-size:14px; color:var(--pink);}
  .humanbox ul{margin:0; padding-left:18px; color:var(--muted); font-size:13.5px;}
  .humanbox li{margin-bottom:6px;}

  /* verification */
  .accmove{display:flex; align-items:center; gap:18px; margin:22px 0;}
  .accbox{
    flex:1; background:var(--panel); border:1px solid var(--border); border-radius:12px;
    padding:22px; text-align:center;
  }
  .accbox .n{font-size:2.4rem; font-weight:700;}
  .accbox.before .n{color:var(--yellow);}
  .accbox.after .n{color:var(--green);}
  .accbox .l{color:var(--muted); font-size:12.5px; margin-top:6px;}
  .accarrow{font-size:26px; color:var(--muted);}

  .vcards{display:grid; grid-template-columns:1fr; gap:10px; margin-top:20px;}
  .vcard{
    background:var(--panel); border:1px solid var(--border); border-radius:10px; padding:14px 18px;
    font-size:13.3px;
  }
  .vcard .vhead{display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;}
  .vcard .vapp{font-weight:700;}
  .vcard .vfield{font-family:var(--mono); font-size:11px; color:var(--muted);}
  .vcard .vwas{color:var(--red);}
  .vcard .varrow{color:var(--muted); margin:0 6px;}
  .vcard .vnow{color:var(--green);}
  .vcard .vwhy{color:var(--muted); margin-top:6px;}

  .defeated{
    background:rgba(248,113,113,.06); border:1px solid rgba(248,113,113,.25); border-radius:10px;
    padding:16px 20px; margin-top:16px; font-size:13.5px; color:var(--muted);
  }
  .defeated b{color:var(--red);}

  footer{padding:36px 0 60px; color:var(--muted); font-size:13px; text-align:center;}
  footer a{color:var(--accent); text-decoration:none;}

  @media (max-width:900px){
    .stats{grid-template-columns:repeat(2,1fr);}
    .findings{grid-template-columns:1fr;}
    .catrow{grid-template-columns:140px 1fr 70px;}
    h1{font-size:1.9rem;}
  }
</style>
</head>
<body>

<header class="hero">
  <div class="wrap">
    <div class="kicker"><span class="dot"></span>Composio AI Product Ops — Take-Home</div>
    <h1>Can an AI agent call this app <em>today</em>?<br>We checked, for 100 of them.</h1>
    <p class="sub">A research agent (not a human) went through 100 real apps across 10 categories, checked their auth model, whether credentials are self-serve or gated, how broad their API is, and whether an MCP server already exists — then a second, independent pass caught its mistakes. This page is the full result: the patterns, the pipeline, the receipts.</p>
    <div class="links">
      <a class="btn primary" href="#findings">Jump to findings ↓</a>
      <a class="btn" href="#table">Full 100-app table</a>
      <a class="btn" href="#agent">How the agent works</a>
      <a class="btn" href="#verification">Verification &amp; accuracy</a>
      <a class="btn" href="https://github.com/REPLACE_ME/REPLACE_ME" target="_blank" rel="noopener">Source repo ↗</a>
    </div>
  </div>
</header>

<section id="findings">
  <div class="wrap">
    <div class="eyebrow">01 — Headline</div>
    <h2>The patterns, in four numbers</h2>
    <p class="lead">Read this section and you have the whole story. Everything below is the receipts.</p>
    <div class="stats" id="statgrid"></div>
    <div class="findings" id="findingsgrid"></div>
  </div>
</section>

<section id="categories">
  <div class="wrap">
    <div class="eyebrow">02 — By category</div>
    <h2>Self-serve vs. gated, by category</h2>
    <p class="lead">Developer/infra tools and productivity apps are almost entirely self-serve. Marketing/ads and finance are where the gates concentrate — mostly for good reason (ad platforms and money movement need review).</p>
    <div class="catgrid" id="catgrid"></div>
    <div class="legend">
      <span><i class="sw" style="background:var(--green)"></i>Self-serve (free or trial)</span>
      <span><i class="sw" style="background:var(--red)"></i>Gated (paid plan / approval / partnership)</span>
      <span><i class="sw" style="background:var(--muted)"></i>Unclear</span>
    </div>
  </div>
</section>

<section id="table">
  <div class="wrap">
    <div class="eyebrow">03 — The data</div>
    <h2>All 100 apps</h2>
    <p class="lead">Every row has at least one real evidence URL the agent actually read. Click a category or search to filter; click a column header to sort.</p>
    <div class="table-controls">
      <input type="text" id="search" placeholder="Search app name…">
      <select id="catfilter"><option value="">All categories</option></select>
      <select id="buildfilter">
        <option value="">All buildability</option>
        <option value="buildable_now">Buildable now</option>
        <option value="buildable_with_workaround">Buildable w/ workaround</option>
        <option value="blocked">Blocked</option>
      </select>
      <select id="mcpfilter">
        <option value="">All MCP status</option>
        <option value="official">Official MCP</option>
        <option value="community">Community MCP</option>
        <option value="none_found">No MCP found</option>
        <option value="unknown">Unknown</option>
      </select>
    </div>
    <div class="row-count" id="rowcount"></div>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th data-k="app">App</th>
            <th data-k="category">Category</th>
            <th data-k="auth_methods">Auth</th>
            <th data-k="access">Access</th>
            <th data-k="api_breadth">API</th>
            <th data-k="existing_mcp">MCP</th>
            <th data-k="buildability">Verdict</th>
            <th>Evidence</th>
          </tr>
        </thead>
        <tbody id="tbody"></tbody>
      </table>
    </div>
  </div>
</section>

<section id="agent">
  <div class="wrap">
    <div class="eyebrow">04 — The agent</div>
    <h2>What actually did the research</h2>
    <p class="lead">Ten parallel research agents (one per category, general-purpose agents with live web search + page-fetching tools), each given the same locked schema and told to cite a real URL for every field or mark it "unknown." No answer was accepted from training-data memory alone.</p>
    <div class="pipeline">
      <div class="pstep"><div class="n">STEP 1</div><h4>Fan out</h4><p>100 apps split into 10 category batches, one agent per batch, running in parallel.</p></div>
      <div class="pstep"><div class="n">STEP 2</div><h4>Research per app</h4><p>Each agent live-searches + fetches official docs, pricing pages, and MCP registries for every field in the schema.</p></div>
      <div class="pstep"><div class="n">STEP 3</div><h4>Structured output</h4><p>Locked 15-field JSON schema per app: auth, access model, API breadth, MCP status, buildability verdict, blocker, evidence URLs, confidence.</p></div>
      <div class="pstep"><div class="n">STEP 4</div><h4>Blind re-check</h4><p>A separate agent, with no access to the first pass, independently re-researches a 20-app sample from scratch.</p></div>
      <div class="pstep"><div class="n">STEP 5</div><h4>Human adjudication</h4><p>Every disagreement gets a direct doc fetch and a human call on which answer (or neither) is right.</p></div>
    </div>
    <div class="humanbox">
      <h4>Where a human was actually needed</h4>
      <ul>
        <li><b>Resolving disagreements between the two research passes</b> — 31 of 60 sampled fields disagreed on first read; most were reconciled by directly re-fetching the primary source rather than trusting either agent's summary.</li>
        <li><b>Judgment-call consistency</b> — deciding whether "you must already be a paying customer to get API access" counts as <code>blocked</code> or <code>buildable_with_workaround</code>, and applying that rule consistently across apps like Brex, Aircall, and DealCloud.</li>
        <li><b>Catching stale research</b> — Clay's first pass cited older, plan-gated webhook docs; a direct fetch of the current developer docs showed a brand-new (2026) free self-serve Public API had since shipped. An agent working from search-result summaries missed the product had moved.</li>
        <li><b>Naming/rebrand drift</b> — fanbasis.com silently rebranded to "Commas" mid-research; the agent had to be told to check whether the assignment's app name was even still current.</li>
        <li><b>Declaring defeat</b> — "Paygent Connect" could not be matched to any real, findable product by either research pass. Rather than guessing, it's reported honestly as unresolved (see Verification).</li>
      </ul>
    </div>
  </div>
</section>

<section id="verification">
  <div class="wrap">
    <div class="eyebrow">05 — Verification</div>
    <h2>How we know this is trustworthy</h2>
    <p class="lead">A 20-app stratified sample (2 per category, weighted toward the first pass's own medium/low-confidence flags) was independently re-researched blind, then every disagreement was adjudicated against the actual primary source.</p>
    <div class="accmove">
      <div class="accbox before"><div class="n" id="accbefore">—</div><div class="l">First-pass accuracy<br>(60 fields checked)</div></div>
      <div class="accarrow">→</div>
      <div class="accbox after"><div class="n" id="accafter">—</div><div class="l">After correction loop<br>(same 60 fields)</div></div>
    </div>
    <p class="lead" style="margin-top:-6px;">9 of 20 sampled apps needed at least one field corrected. The verification loop also caught <em>false alarms</em> — cases where the independent check disagreed but was itself wrong, confirmed by going back to the primary source. Both directions are shown below, honestly.</p>

    <h4 style="margin:26px 0 10px; font-size:14px; color:var(--text);">Real corrections made to the dataset</h4>
    <div class="vcards" id="corrections"></div>

    <h4 style="margin:26px 0 10px; font-size:14px; color:var(--text);">Cases where the first pass was right and the re-check was wrong</h4>
    <div class="vcards" id="confirmed"></div>

    <div class="defeated" id="defeated"></div>
  </div>
</section>

<footer>
  <div class="wrap">
    Built by researching all 100 apps with parallel AI agents, cross-checked by an independent blind pass, and adjudicated by hand.
    Full methodology, prompts, and raw data in the <a href="https://github.com/REPLACE_ME/REPLACE_ME" target="_blank" rel="noopener">source repo</a>.
  </div>
</footer>

<script>
__DATA_JS__
</script>
<script>
const ACCESS_LABEL = {
  self_serve_free: 'Free · self-serve', self_serve_trial: 'Trial · self-serve',
  gated_paid_plan: 'Gated · paid plan', gated_approval: 'Gated · approval',
  gated_partnership: 'Gated · partnership', unclear: 'Unclear'
};
const ACCESS_BADGE = {
  self_serve_free:'green', self_serve_trial:'green',
  gated_paid_plan:'red', gated_approval:'red', gated_partnership:'red', unclear:'grey'
};
const BUILD_LABEL = { buildable_now:'Buildable now', buildable_with_workaround:'Workaround needed', blocked:'Blocked' };
const BUILD_BADGE = { buildable_now:'green', buildable_with_workaround:'yellow', blocked:'red' };
const MCP_LABEL = { official:'Official', community:'Community', none_found:'None found', unknown:'Unknown' };
const MCP_BADGE = { official:'blue', community:'grey', none_found:'grey', unknown:'grey' };

function pct(n,total){ return Math.round(1000*n/total)/10; }

// ---- Stats ----
(function(){
  const total = PATTERNS.total_apps;
  const g = document.getElementById('statgrid');
  const stats = [
    {num: PATTERNS.buildability_distribution.buildable_now, cls:'green', label:'apps buildable as an agent toolkit right now, no waiting on anyone'},
    {num: PATTERNS.existing_mcp_distribution.official, cls:'accent', label:'already ship an official, vendor-built MCP server'},
    {num: PATTERNS.auth_method_distribution.OAuth2, cls:'accent2', label:'use OAuth2 in some form — the dominant auth pattern by far'},
    {num: PATTERNS.needs_outreach_count, cls:'pink', label:'are gated AND not cleanly buildable — the real "needs outreach" queue'},
  ];
  g.innerHTML = stats.map(s=>`<div class="stat"><div class="num ${s.cls}">${s.num}</div><div class="label">${s.label}</div></div>`).join('');

  const fg = document.getElementById('findingsgrid');
  const findings = [
    `<b>Access is more open than expected:</b> ${pct(PATTERNS.access_distribution.self_serve_free||0,total)}% of apps let a developer get free credentials with zero human review, and another ${pct(PATTERNS.access_distribution.self_serve_trial||0,total)}% offer a genuine no-card trial. Only ${pct((PATTERNS.access_distribution.gated_approval||0)+(PATTERNS.access_distribution.gated_partnership||0),total)}% require a formal approval or partnership process.`,
    `<b>MCP adoption is already mainstream:</b> ${PATTERNS.existing_mcp_distribution.official} of 100 apps ship an official MCP server today, and another ${PATTERNS.existing_mcp_distribution.community} have at least a community one — only ${PATTERNS.existing_mcp_distribution.none_found} have nothing at all. This moved faster than expected even within the ~3 weeks of research.`,
    `<b>REST + OAuth2/API-key is the default:</b> ${PATTERNS.api_type_distribution.REST} of 100 apps expose a plain REST API, and OAuth2 (${PATTERNS.auth_method_distribution.OAuth2}) plus API keys (${PATTERNS.auth_method_distribution['API Key']}) cover the overwhelming majority of auth — GraphQL-only (${PATTERNS.api_type_distribution.GraphQL||0}) and no-public-API (${PATTERNS.api_type_distribution.no_public_api||0}) are both rare.`,
    `<b>The blockers are concentrated, not random:</b> where an app IS gated, the #1 reason is a formal approval/review process (ad platforms, payments), not missing docs — the API usually already exists and is documented, it's the credential that's slow.`,
  ];
  fg.innerHTML = findings.map(f=>`<div class="finding">${f}</div>`).join('');
})();

// ---- Category bars ----
(function(){
  const el = document.getElementById('catgrid');
  const cats = PATTERNS.categories;
  el.innerHTML = cats.map(c=>{
    const b = PATTERNS.category_access_bucket[c];
    const total = (b.self_serve||0)+(b.gated||0)+(b.unclear||0);
    const selfPct = Math.round(100*(b.self_serve||0)/total);
    const gatedPct = Math.round(100*(b.gated||0)/total);
    const unclearPct = 100-selfPct-gatedPct;
    return `<div class="catrow">
      <div class="catname">${c}</div>
      <div class="catbar">
        <div class="seg-self" style="width:${selfPct}%"></div>
        <div class="seg-gated" style="width:${gatedPct}%"></div>
        <div class="seg-unclear" style="width:${unclearPct}%"></div>
      </div>
      <div class="catpct">${b.self_serve||0}/${total} self-serve</div>
    </div>`;
  }).join('');
})();

// ---- Table ----
let sortKey = 'app', sortDir = 1;
function renderTable(){
  const q = document.getElementById('search').value.toLowerCase();
  const cat = document.getElementById('catfilter').value;
  const build = document.getElementById('buildfilter').value;
  const mcp = document.getElementById('mcpfilter').value;
  let rows = APPS.filter(r=>{
    if(q && !r.app.toLowerCase().includes(q)) return false;
    if(cat && r.category!==cat) return false;
    if(build && r.buildability!==build) return false;
    if(mcp && r.existing_mcp!==mcp) return false;
    return true;
  });
  rows = rows.slice().sort((a,b)=>{
    let av=a[sortKey], bv=b[sortKey];
    if(Array.isArray(av)) av=av.join(',');
    if(Array.isArray(bv)) bv=bv.join(',');
    if(typeof av==='string') av=av.toLowerCase();
    if(typeof bv==='string') bv=bv.toLowerCase();
    if(av<bv) return -1*sortDir;
    if(av>bv) return 1*sortDir;
    return 0;
  });
  document.getElementById('rowcount').textContent = `${rows.length} of ${APPS.length} apps`;
  document.getElementById('tbody').innerHTML = rows.map(r=>{
    const ev = (r.evidence&&r.evidence[0]) ? r.evidence[0].url : null;
    return `<tr>
      <td class="app-cell"><b>${r.app}</b><span>${r.one_liner.slice(0,70)}${r.one_liner.length>70?'…':''}</span></td>
      <td>${r.category}</td>
      <td>${r.auth_methods.join(', ')}</td>
      <td><span class="badge ${ACCESS_BADGE[r.access]||'grey'}">${ACCESS_LABEL[r.access]||r.access}</span></td>
      <td>${r.api_breadth}</td>
      <td><span class="badge ${MCP_BADGE[r.existing_mcp]||'grey'}">${MCP_LABEL[r.existing_mcp]||r.existing_mcp}</span></td>
      <td><span class="badge ${BUILD_BADGE[r.buildability]||'grey'}">${BUILD_LABEL[r.buildability]||r.buildability}</span></td>
      <td>${ev?`<a class="ev-link" href="${ev}" target="_blank" rel="noopener">docs ↗</a>`:'—'}</td>
    </tr>`;
  }).join('');
}
(function(){
  const catSel = document.getElementById('catfilter');
  PATTERNS.categories.forEach(c=>{
    const o = document.createElement('option'); o.value=c; o.textContent=c; catSel.appendChild(o);
  });
  document.getElementById('search').addEventListener('input', renderTable);
  catSel.addEventListener('change', renderTable);
  document.getElementById('buildfilter').addEventListener('change', renderTable);
  document.getElementById('mcpfilter').addEventListener('change', renderTable);
  document.querySelectorAll('thead th[data-k]').forEach(th=>{
    th.addEventListener('click', ()=>{
      const k = th.getAttribute('data-k');
      if(sortKey===k) sortDir*=-1; else { sortKey=k; sortDir=1; }
      renderTable();
    });
  });
  renderTable();
})();

// ---- Verification section ----
(function(){
  document.getElementById('accbefore').textContent = VERIF.first_pass_accuracy_after_adjudication.accuracy_pct + '%';
  document.getElementById('accafter').textContent = VERIF.corrected_accuracy_after_verification_loop.accuracy_pct + '%';

  const corr = document.getElementById('corrections');
  corr.innerHTML = VERIF.apps_corrected.map(c=>`
    <div class="vcard">
      <div class="vhead"><span class="vapp">${c.app}</span><span class="vfield">${c.field}</span></div>
      <div><span class="vwas">${c.was}</span><span class="varrow">→</span><span class="vnow">${c.corrected_to}</span></div>
      <div class="vwhy">${c.why}</div>
    </div>`).join('');

  const conf = document.getElementById('confirmed');
  conf.innerHTML = VERIF.confirmed_correct_despite_blind_disagreement.map(c=>`
    <div class="vcard">
      <div class="vhead"><span class="vapp">${c.app}</span><span class="vfield">${c.field}</span></div>
      <div><span class="vnow">first pass: ${c.first_pass_said}</span><span class="varrow">vs</span><span class="vwas">re-check: ${c.blind_check_said}</span></div>
      <div class="vwhy">${c.resolution}</div>
    </div>`).join('');

  const d = VERIF.apps_that_defeated_the_research[0];
  document.getElementById('defeated').innerHTML = `<b>Honest miss — ${d.app}:</b> ${d.issue}`;
})();
</script>
</body>
</html>
"""

html = html.replace("__DATA_JS__", DATA_JS)

out_dir = os.path.join(HERE, 'site')
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, 'index.html'), 'w') as f:
    f.write(html)

print("Wrote", os.path.join(out_dir, 'index.html'), "size:", len(html), "bytes")
