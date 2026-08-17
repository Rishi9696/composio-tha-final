/* Integration Readiness dashboard — renders the static audited dataset.
   Data globals are provided by data.js:
     window.RESULTS, window.METRICS, window.REASONING, window.COMPOSIO_COVERAGE */
(function () {
  "use strict";

  var RESULTS = Array.isArray(window.RESULTS) ? window.RESULTS : [];
  var METRICS = window.METRICS || {};
  var REASONING = window.REASONING || {};
  var COVERAGE = window.COMPOSIO_COVERAGE || {};
  var COVER_APPS = COVERAGE.apps || {};
  var PATTERNS = METRICS.patterns || {};

  var ACTIONS = ["Build Now", "Needs Outreach", "Partner-Gated", "Blocked"];
  var ACTION_CLASS = {
    "Build Now": "a-build",
    "Needs Outreach": "a-outreach",
    "Partner-Gated": "a-partner",
    "Blocked": "a-blocked",
  };
  var BUILD_RANK = { Easy: 0, Moderate: 1, Hard: 2, Blocked: 3 };

  // --- helpers ---------------------------------------------------------------
  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function el(id) { return document.getElementById(id); }
  function pct(x) { return Math.round((Number(x) || 0) * 100); }
  function count(arr, fn) { return arr.reduce(function (n, r) { return n + (fn(r) ? 1 : 0); }, 0); }
  function coverStatus(slug) { return (COVER_APPS[slug] || {}).status || "Missing"; }

  // --- hero: action distribution --------------------------------------------
  function renderPulse() {
    var dist = {};
    ACTIONS.forEach(function (a) { dist[a] = count(RESULTS, function (r) { return r.recommended_next_action === a; }); });
    var total = RESULTS.length || 1;

    var bar = el("action-bar");
    var legend = el("action-legend");
    bar.innerHTML = "";
    legend.innerHTML = "";
    ACTIONS.forEach(function (a) {
      var n = dist[a];
      if (n > 0) {
        var seg = document.createElement("span");
        seg.className = "seg " + ACTION_CLASS[a];
        seg.style.flex = String(n);
        seg.title = a + ": " + n;
        bar.appendChild(seg);
      }
      var li = document.createElement("span");
      li.className = "legend-item";
      li.innerHTML = '<i class="dot ' + ACTION_CLASS[a] + '"></i>' + esc(a) +
        ' <b>' + n + '</b>';
      legend.appendChild(li);
    });

    var buildNow = dist["Build Now"];
    el("decision-title").innerHTML =
      "<b>" + buildNow + "</b> of " + RESULTS.length +
      " apps are build-ready today; the rest need outreach, a partner path, or are blocked.";
    var q = METRICS.quality;
    if (q && q.label) el("quality-badge").textContent = q.label;
  }

  // --- KPI tiles -------------------------------------------------------------
  function tile(value, label, sub) {
    return '<div class="kpi"><div class="kpi-value">' + esc(value) + '</div>' +
      '<div class="kpi-label">' + esc(label) + '</div>' +
      (sub ? '<div class="kpi-sub">' + esc(sub) + '</div>' : '') + '</div>';
  }
  function renderKpis() {
    var sum = COVERAGE.summary || {};
    var buildNow = count(RESULTS, function (r) { return r.recommended_next_action === "Build Now"; });
    var queue = count(RESULTS, function (r) {
      return r.recommended_next_action === "Build Now" && coverStatus(r.slug) !== "Active";
    });
    var avgConf = PATTERNS.avg_confidence != null
      ? PATTERNS.avg_confidence
      : (RESULTS.reduce(function (s, r) { return s + (Number(r.confidence) || 0); }, 0) / (RESULTS.length || 1));
    var hc = METRICS.handcheck || {};
    var acc = hc.api_type_accuracy != null ? hc.api_type_accuracy : METRICS.headline_accuracy;

    var html = "";
    html += tile(RESULTS.length, "Apps evaluated", "Locked 19-field schema");
    html += tile(buildNow, "Build Now", "Self-serve, documented surface");
    html += tile(queue, "Uncovered build queue", "Build-ready, no active toolkit");
    html += tile(sum.active != null ? sum.active : "—", "Active toolkits", "In the Composio SDK");
    html += tile(sum.tools_total != null ? Number(sum.tools_total).toLocaleString() : "—", "Tools exposed", "Median " + (sum.tools_median != null ? sum.tools_median : "—"));
    html += tile((acc != null ? pct(acc) + "%" : "—"), "Hand-checked API type", (hc.n ? hc.n + " apps vs official docs" : "Adjudicated"));
    el("kpi-grid").innerHTML = html;
  }

  // --- priority queue --------------------------------------------------------
  function renderPriorities() {
    var queue = RESULTS.filter(function (r) {
      return r.recommended_next_action === "Build Now" && coverStatus(r.slug) !== "Active";
    });
    queue.sort(function (a, b) {
      var ax = (a.access_model || {}).kind === "Self-Serve" ? 0 : 1;
      var bx = (b.access_model || {}).kind === "Self-Serve" ? 0 : 1;
      if (ax !== bx) return ax - bx;
      var ab = BUILD_RANK[a.buildability] == null ? 9 : BUILD_RANK[a.buildability];
      var bb = BUILD_RANK[b.buildability] == null ? 9 : BUILD_RANK[b.buildability];
      if (ab !== bb) return ab - bb;
      return (Number(b.confidence) || 0) - (Number(a.confidence) || 0);
    });
    var host = el("priority-queue");
    if (!queue.length) { host.innerHTML = '<p class="empty">No uncovered build-ready apps in the current dataset.</p>'; return; }
    host.innerHTML = queue.slice(0, 9).map(function (r, i) {
      var kind = (r.access_model || {}).kind || "—";
      return '<button class="queue-card" data-slug="' + esc(r.slug) + '">' +
        '<div class="queue-top"><span class="rank">' + (i + 1) + '</span>' +
        '<span class="chip ' + ACTION_CLASS[r.recommended_next_action] + '">' + esc(r.recommended_next_action) + '</span></div>' +
        '<h3>' + esc(r.app) + '</h3>' +
        '<p class="queue-line">' + esc(r.one_liner || "") + '</p>' +
        '<div class="queue-meta">' +
        '<span>' + esc(r.api_type) + '</span><span>' + esc(kind) + '</span><span>' + esc(r.buildability) + '</span>' +
        '</div></button>';
    }).join("");
  }

  // --- catalog ---------------------------------------------------------------
  function chip(text, cls) { return '<span class="chip ' + (cls || "") + '">' + esc(text) + '</span>'; }
  function confBar(v) {
    var p = pct(v);
    return '<div class="conf"><span class="conf-fill" style="width:' + p + '%"></span></div><small>' + p + '%</small>';
  }

  function renderFilters() {
    var cats = {}, builds = {};
    RESULTS.forEach(function (r) { if (r.category) cats[r.category] = 1; if (r.buildability) builds[r.buildability] = 1; });
    fill("f-cat", Object.keys(cats).sort());
    fill("f-next", ACTIONS);
    fill("f-build", ["Easy", "Moderate", "Hard", "Blocked"].filter(function (b) { return builds[b]; }));
  }
  function fill(id, values) {
    var sel = el(id);
    values.forEach(function (v) {
      var o = document.createElement("option"); o.value = v; o.textContent = v; sel.appendChild(o);
    });
  }

  function catalogRows() {
    var q = (el("q").value || "").toLowerCase().trim();
    var fc = el("f-cat").value, fn = el("f-next").value, fb = el("f-build").value;
    return RESULTS.filter(function (r) {
      if (fc && r.category !== fc) return false;
      if (fn && r.recommended_next_action !== fn) return false;
      if (fb && r.buildability !== fb) return false;
      if (q) {
        var hay = [r.app, r.category, (r.auth_methods || []).join(" "), r.main_blocker, r.api_type].join(" ").toLowerCase();
        if (hay.indexOf(q) === -1) return false;
      }
      return true;
    });
  }
  function renderCatalog() {
    var rows = catalogRows();
    el("catalog-count").textContent = rows.length + " of " + RESULTS.length + " apps — open any row for full reasoning and sources.";
    el("catalog-body").innerHTML = rows.map(function (r) {
      var cov = coverStatus(r.slug);
      var covCls = cov === "Active" ? "s-active" : (cov === "Catalog-only" ? "s-catalog" : "s-missing");
      var kind = (r.access_model || {}).kind || "—";
      return '<tr data-slug="' + esc(r.slug) + '">' +
        '<td class="c-app"><b>' + esc(r.app) + '</b><small>' + esc(r.category) + '</small></td>' +
        '<td>' + esc((r.auth_methods || []).join(", ") || "—") + '</td>' +
        '<td>' + chip(kind, kind === "Self-Serve" ? "s-active" : "s-missing") + '</td>' +
        '<td>' + esc(r.api_type) + '</td>' +
        '<td>' + esc(r.existing_mcp) + '</td>' +
        '<td>' + chip(cov, covCls) + '</td>' +
        '<td>' + esc(r.buildability) + '</td>' +
        '<td>' + chip(r.recommended_next_action, ACTION_CLASS[r.recommended_next_action]) + '</td>' +
        '<td class="c-conf">' + confBar(r.confidence) + '</td>' +
        '<td class="c-open">›</td>' +
        '</tr>';
    }).join("");
  }

  function renderSdkSummary() {
    var s = COVERAGE.summary;
    if (!s) { el("sdk-summary").textContent = "Composio SDK coverage unavailable."; return; }
    el("sdk-summary").innerHTML =
      '<b>Composio SDK audit</b> · ' +
      '<span class="s-active">' + s.active + ' active</span> · ' +
      s.catalog_only + ' catalog-only · ' +
      '<span class="s-missing">' + s.missing + ' missing</span> · ' +
      Number(s.tools_total).toLocaleString() + ' tools · ' + s.trigger_enabled + ' trigger-enabled';
  }

  // --- detail drawer ---------------------------------------------------------
  function mdSection(md, heading) {
    if (!md) return "";
    var re = new RegExp("##\\s*" + heading + "\\s*\\n([\\s\\S]*?)(?:\\n##\\s|$)", "i");
    var m = md.match(re);
    return m ? m[1].trim() : "";
  }
  function openDetail(slug) {
    var r = RESULTS.filter(function (x) { return x.slug === slug; })[0];
    if (!r) return;
    el("detail-title").textContent = r.app;
    el("detail-sub").textContent = r.category + " · " + r.slug + " · verified " + (r.last_verified || "—");
    var access = r.access_model || {};
    var cov = COVER_APPS[slug] || {};
    var reasoning = mdSection(REASONING[slug], "Model reasoning");

    function row(dt, dd) { return '<div class="d-row"><dt>' + esc(dt) + '</dt><dd>' + dd + '</dd></div>'; }
    var links = (r.evidence_urls || []).map(function (u) {
      return '<li><a href="' + esc(u) + '" target="_blank" rel="noopener">' + esc(u) + '</a></li>';
    }).join("");

    el("detail-body").innerHTML =
      '<p class="d-liner">' + esc(r.one_liner || "") + '</p>' +
      '<div class="d-badges">' +
        chip(r.recommended_next_action, ACTION_CLASS[r.recommended_next_action]) +
        chip(access.kind || "—", access.kind === "Self-Serve" ? "s-active" : "s-missing") +
        chip(r.buildability, "") +
        chip(r.verification_status, "s-catalog") +
      '</div>' +
      '<dl class="d-grid">' +
        row("API type", esc(r.api_type) + " · " + esc(r.api_breadth) + " breadth") +
        row("Auth methods", esc((r.auth_methods || []).join(", ") || "—")) +
        row("Production access", '<b>' + esc(access.kind || "—") + '</b> — ' + esc(access.note || "")) +
        row("Existing MCP", esc(r.existing_mcp)) +
        row("Composio", esc(cov.status || "—") + (cov.tools_count != null ? " · " + cov.tools_count + " tools" : "")) +
        row("Main blocker", esc(r.main_blocker || "—")) +
        row("Rate limits", esc(r.rate_limit_note || "—")) +
        row("Confidence", pct(r.confidence) + "%") +
      '</dl>' +
      (reasoning ? '<div class="d-section"><h3>Model reasoning</h3><p>' + esc(reasoning) + '</p></div>' : '') +
      (links ? '<div class="d-section"><h3>Evidence</h3><ul class="d-links">' + links + '</ul></div>' : '');

    var dlg = el("detail-dialog");
    if (typeof dlg.showModal === "function") dlg.showModal(); else dlg.setAttribute("open", "");
  }

  // --- verification ----------------------------------------------------------
  function vcard(title, note, stats) {
    var body = stats.map(function (s) {
      return '<div class="v-stat"><span>' + esc(s[0]) + '</span><b>' + esc(s[1]) + '</b></div>';
    }).join("");
    return '<div class="v-card"><h3>' + esc(title) + '</h3>' +
      (note ? '<p>' + esc(note) + '</p>' : '') + '<div class="v-stats">' + body + '</div></div>';
  }
  function renderVerification() {
    var out = [];
    var hc = METRICS.handcheck;
    if (hc) {
      out.push(vcard("Official-doc adjudication", hc.metric_scope || "", [
        ["Apps", hc.n],
        ["API type", pct(hc.api_type_accuracy) + "%"],
        ["Auth set", pct(hc.auth_accuracy) + "%"],
        ["Access", pct(hc.access_accuracy) + "%"],
        ["MCP", pct(hc.mcp_accuracy) + "%"],
      ]));
    }
    var am = METRICS.accuracy_movement;
    if (am) {
      out.push(vcard("Correction replay", "First-pass snapshot vs corrected dataset against the same truth set.", [
        ["First pass", am.first_pass != null ? pct(am.first_pass) + "%" : "—"],
        ["Corrected", am.corrected != null ? pct(am.corrected) + "%" : "—"],
        ["Truth apps", am.n != null ? am.n : "—"],
      ]));
    }
    var bu = METRICS.browser_use;
    if (bu) {
      out.push(vcard("Independent browser check", "Browser Use Cloud re-derived key fields from live docs.", [
        ["Sampled", bu.sample != null ? bu.sample : (bu.n != null ? bu.n : "—")],
        ["Agreed", bu.agreement != null ? pct(bu.agreement) + "%" : (bu.agreed != null ? bu.agreed : "—")],
      ]));
    }
    if (!out.length) out.push('<p class="empty">Verification metrics will populate after a run.</p>');
    el("verification-grid").innerHTML = out.join("");
  }

  // --- reproduce tabs --------------------------------------------------------
  var COMMANDS = {
    research: "python research.py --all --fresh-run --model gpt-4.1\npython research.py --metrics\npython research.py --build-report",
    verify: "python browser_verify.py --sample 12\npython research.py --fold-handcheck\npython research.py --apply-handcheck\npython research.py --accuracy-movement",
    composio: "python research.py --composio-audit\npython research.py --composio-agent otter-ai\npython research.py --build-report",
  };
  function bindTabs() {
    el("command-output").textContent = COMMANDS.research;
    Array.prototype.forEach.call(document.querySelectorAll(".command-tab"), function (btn) {
      btn.addEventListener("click", function () {
        document.querySelectorAll(".command-tab").forEach(function (b) { b.classList.remove("active"); b.setAttribute("aria-selected", "false"); });
        btn.classList.add("active"); btn.setAttribute("aria-selected", "true");
        el("command-output").textContent = COMMANDS[btn.dataset.command] || "";
      });
    });
  }

  // --- chrome ----------------------------------------------------------------
  function renderChrome() {
    el("reasoning-count").textContent = Object.keys(REASONING).length;
    if (METRICS.generated) el("generated-note").textContent = "Generated " + String(METRICS.generated).slice(0, 10);
    var repo = METRICS.repo_url;
    if (repo) el("repo-link").href = repo;
    var live = METRICS.live_url;
    el("footer").innerHTML =
      '<div><b>Composio × OpenAI Integration Readiness</b><span>' + RESULTS.length + ' apps · static build from audited JSON</span></div>' +
      '<div class="footer-links">' +
      (repo ? '<a href="' + esc(repo) + '" target="_blank" rel="noopener">Source ↗</a>' : '') +
      (live ? '<a href="' + esc(live) + '" target="_blank" rel="noopener">Live report ↗</a>' : '') +
      '</div>';
  }

  // --- wire up ---------------------------------------------------------------
  function bindEvents() {
    ["q", "f-cat", "f-next", "f-build"].forEach(function (id) {
      el(id).addEventListener("input", renderCatalog);
      el(id).addEventListener("change", renderCatalog);
    });
    el("catalog-body").addEventListener("click", function (e) {
      var tr = e.target.closest("tr[data-slug]");
      if (tr) openDetail(tr.dataset.slug);
    });
    el("priority-queue").addEventListener("click", function (e) {
      var card = e.target.closest("[data-slug]");
      if (card) openDetail(card.dataset.slug);
    });
    var dlg = el("detail-dialog");
    dlg.addEventListener("click", function (e) { if (e.target === dlg) dlg.close(); });
  }

  function init() {
    if (!RESULTS.length) {
      el("decision-title").textContent = "No data loaded. Run `python research.py --build-report` to generate report/data.js.";
      return;
    }
    renderPulse();
    renderKpis();
    renderPriorities();
    renderFilters();
    renderSdkSummary();
    renderCatalog();
    renderVerification();
    renderChrome();
    bindTabs();
    bindEvents();
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
