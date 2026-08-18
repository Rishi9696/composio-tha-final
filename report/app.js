/* Readiness Console — sidebar app shell over the static audited dataset.
   Data globals from data.js: window.RESULTS, window.METRICS, window.REASONING,
   window.COMPOSIO_COVERAGE */
(function () {
  "use strict";

  var RESULTS = Array.isArray(window.RESULTS) ? window.RESULTS : [];
  var METRICS = window.METRICS || {};
  var REASONING = window.REASONING || {};
  var COVERAGE = window.COMPOSIO_COVERAGE || {};
  var COVER_APPS = COVERAGE.apps || {};
  var PATTERNS = METRICS.patterns || {};

  var ACTIONS = ["Build Now", "Needs Outreach", "Partner-Gated", "Blocked"];
  var ACTION_TAG = {
    "Build Now": "tag-build", "Needs Outreach": "tag-outreach",
    "Partner-Gated": "tag-partner", "Blocked": "tag-blocked",
  };
  var BUILD_RANK = { Easy: 0, Moderate: 1, Hard: 2, Blocked: 3 };

  function el(id) { return document.getElementById(id); }
  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function pct(x) { return Math.round((Number(x) || 0) * 100); }
  function count(arr, fn) { return arr.reduce(function (n, r) { return n + (fn(r) ? 1 : 0); }, 0); }
  function coverStatus(slug) { return (COVER_APPS[slug] || {}).status || "Missing"; }
  function tag(text, cls) { return '<span class="tag ' + (cls || "") + '">' + esc(text) + '</span>'; }

  // ---------------------------------------------------------------- navigation
  // Single scrolling page: rail buttons scroll to their section, and an
  // IntersectionObserver keeps the rail's active state in sync with scroll.
  function scrollToView(name) {
    var section = document.getElementById("view-" + name);
    if (section) section.scrollIntoView({ behavior: "smooth", block: "start" });
    if (history.replaceState) history.replaceState(null, "", "#" + name);
  }

  function setActiveRailItem(name) {
    document.querySelectorAll(".rail-item").forEach(function (b) {
      b.classList.toggle("active", b.dataset.view === name);
    });
  }

  function bindScrollSpy() {
    var sections = Array.prototype.slice.call(document.querySelectorAll(".view"));
    if (!("IntersectionObserver" in window) || !sections.length) return;
    var observer = new IntersectionObserver(function (entries) {
      var visible = entries.filter(function (e) { return e.isIntersecting; });
      if (!visible.length) return;
      visible.sort(function (a, b) { return b.intersectionRatio - a.intersectionRatio; });
      setActiveRailItem(visible[0].target.dataset.view);
    }, { rootMargin: "-15% 0px -55% 0px", threshold: [0, 0.25, 0.5, 0.75, 1] });
    sections.forEach(function (s) { observer.observe(s); });
  }

  // ---------------------------------------------------------------- overview
  function renderStrip() {
    var buildNow = count(RESULTS, function (r) { return r.recommended_next_action === "Build Now"; });
    var sum = COVERAGE.summary || {};
    var stats = [
      [String(RESULTS.length), "apps"],
      [String(buildNow), "build now"],
      [sum.active != null ? String(sum.active) : "—", "active toolkits"],
    ];
    el("strip-stats").innerHTML = stats.map(function (s) {
      return '<div class="strip-stat"><b>' + esc(s[0]) + '</b><span>' + esc(s[1]) + '</span></div>';
    }).join("");
  }

  function renderOverview() {
    var dist = {};
    ACTIONS.forEach(function (a) { dist[a] = count(RESULTS, function (r) { return r.recommended_next_action === a; }); });

    var bar = el("action-bar"), legend = el("action-legend");
    bar.innerHTML = "";
    legend.innerHTML = "";
    ACTIONS.forEach(function (a) {
      var n = dist[a];
      if (n > 0) {
        var seg = document.createElement("span");
        seg.className = "seg " + ACTION_TAG[a];
        seg.style.flex = String(n);
        seg.title = a + ": " + n;
        bar.appendChild(seg);
      }
      var li = document.createElement("span");
      li.className = "dist-item";
      li.innerHTML = '<i class="dot ' + ACTION_TAG[a] + '"></i>' + esc(a) + '<b>' + n + '</b>';
      legend.appendChild(li);
    });

    el("decision-title").innerHTML =
      '<b>' + dist["Build Now"] + '</b> of ' + RESULTS.length +
      ' apps are self-serve buildable today; the rest need outreach, a partner path, or are blocked.';
    var q = METRICS.quality;
    if (q && q.label) el("quality-badge").textContent = q.label;

    var sum = COVERAGE.summary || {};
    var meters = [
      ["active", sum.active, sum.n_apps],
      ["catalog-only", sum.catalog_only, sum.n_apps],
      ["missing", sum.missing, sum.n_apps],
    ];
    el("sdk-meters").innerHTML = meters.map(function (m) {
      var p = m[2] ? Math.round((m[1] / m[2]) * 100) : 0;
      return '<div class="meter"><div class="meter-top"><span>' + esc(m[0]) + '</span><b>' + m[1] + '</b></div>' +
        '<div class="meter-track"><span style="width:' + p + '%"></span></div></div>';
    }).join("") + '<p class="meter-foot">' + Number(sum.tools_total || 0).toLocaleString() +
      ' tools exposed · median ' + (sum.tools_median != null ? sum.tools_median : "—") +
      ' · ' + (sum.trigger_enabled != null ? sum.trigger_enabled : "—") + ' trigger-enabled</p>';

    var hc = METRICS.handcheck || {};
    var avgConf = PATTERNS.avg_confidence != null
      ? pct(PATTERNS.avg_confidence)
      : pct(RESULTS.reduce(function (s, r) { return s + (Number(r.confidence) || 0); }, 0) / (RESULTS.length || 1));
    var unresolvedSlugs = {};
    (METRICS.unresolved_failures || []).forEach(function (f) { unresolvedSlugs[f.slug] = 1; });
    var facts = [
      ["Schema fields", "19 locked"],
      ["Avg. confidence", avgConf + "%"],
      ["Unresolved (fail-closed)", Object.keys(unresolvedSlugs).length + " apps"],
      ["Hand-checked", (hc.n || 0) + " apps"],
      ["Reasoning traces", Object.keys(REASONING).length],
    ];
    el("fact-list").innerHTML = facts.map(function (f) {
      return '<div class="fact"><dt>' + esc(f[0]) + '</dt><dd>' + esc(f[1]) + '</dd></div>';
    }).join("");

    var byCat = {};
    RESULTS.forEach(function (r) { byCat[r.category] = (byCat[r.category] || 0) + 1; });
    var top = Object.keys(byCat).map(function (k) { return [k, byCat[k]]; })
      .sort(function (a, b) { return b[1] - a[1]; }).slice(0, 6);
    var max = top.length ? top[0][1] : 1;
    el("category-bars").innerHTML = top.map(function (c) {
      var w = Math.round((c[1] / max) * 100);
      return '<div class="cat-row"><span>' + esc(c[0]) + '</span>' +
        '<div class="cat-track"><span style="width:' + w + '%"></span></div><b>' + c[1] + '</b></div>';
    }).join("");
  }

  // ---------------------------------------------------------------- queue
  function renderQueue() {
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
    el("queue-body").innerHTML = queue.map(function (r, i) {
      var kind = (r.access_model || {}).kind || "—";
      return '<tr data-slug="' + esc(r.slug) + '">' +
        '<td class="q-rank">' + (i + 1) + '</td>' +
        '<td><b>' + esc(r.app) + '</b></td>' +
        '<td>' + esc(r.category) + '</td>' +
        '<td>' + esc(r.api_type) + '</td>' +
        '<td>' + tag(kind, kind === "Self-Serve" ? "tag-build" : "tag-blocked") + '</td>' +
        '<td>' + esc(r.buildability) + '</td>' +
        '<td class="q-conf">' + pct(r.confidence) + '%</td>' +
        '</tr>';
    }).join("") || '<tr><td colspan="7" class="empty">No uncovered build-ready apps in the current dataset.</td></tr>';
  }

  // ---------------------------------------------------------------- catalog
  function fillSelect(id, values) {
    var sel = el(id);
    values.forEach(function (v) {
      var o = document.createElement("option"); o.value = v; o.textContent = v; sel.appendChild(o);
    });
  }
  function initFilters() {
    var cats = {};
    RESULTS.forEach(function (r) { if (r.category) cats[r.category] = 1; });
    fillSelect("f-cat", Object.keys(cats).sort());
    fillSelect("f-next", ACTIONS);
  }
  function catalogRows() {
    var q = (el("q").value || "").toLowerCase().trim();
    var fc = el("f-cat").value, fn = el("f-next").value;
    return RESULTS.filter(function (r) {
      if (fc && r.category !== fc) return false;
      if (fn && r.recommended_next_action !== fn) return false;
      if (q) {
        var hay = [r.app, r.category, (r.auth_methods || []).join(" "), r.main_blocker].join(" ").toLowerCase();
        if (hay.indexOf(q) === -1) return false;
      }
      return true;
    });
  }
  var selectedSlug = null;
  function renderCatalogList() {
    var rows = catalogRows();
    el("catalog-count").textContent = rows.length + " / " + RESULTS.length;
    el("catalog-rows").innerHTML = rows.map(function (r) {
      var cov = coverStatus(r.slug);
      var active = r.slug === selectedSlug ? " active" : "";
      return '<li class="row-item' + active + '" data-slug="' + esc(r.slug) + '">' +
        '<div class="row-main"><b>' + esc(r.app) + '</b><span>' + esc(r.category) + '</span></div>' +
        '<div class="row-tags">' +
        tag(r.recommended_next_action, ACTION_TAG[r.recommended_next_action]) +
        (cov === "Active" ? tag("composio", "tag-build") : "") +
        '</div></li>';
    }).join("") || '<li class="empty">No apps match these filters.</li>';
  }

  function mdSection(md, heading) {
    if (!md) return "";
    var re = new RegExp("##\\s*" + heading + "\\s*\\n([\\s\\S]*?)(?:\\n##\\s|$)", "i");
    var m = md.match(re);
    return m ? m[1].trim() : "";
  }
  function renderDetail(slug) {
    selectedSlug = slug;
    var r = RESULTS.filter(function (x) { return x.slug === slug; })[0];
    var host = el("catalog-detail");
    if (!r) { host.innerHTML = '<div class="detail-empty">Select an app from the list to inspect its evidence-backed decision.</div>'; return; }
    var access = r.access_model || {};
    var cov = COVER_APPS[slug] || {};
    var reasoning = mdSection(REASONING[slug], "Model reasoning");
    function row(dt, dd) { return '<div class="d-row"><dt>' + esc(dt) + '</dt><dd>' + dd + '</dd></div>'; }
    var links = (r.evidence_urls || []).map(function (u) {
      return '<li><a href="' + esc(u) + '" target="_blank" rel="noopener">' + esc(u) + '</a></li>';
    }).join("");

    host.innerHTML =
      '<div class="detail-head">' +
        '<div><h2>' + esc(r.app) + '</h2><span>' + esc(r.category) + ' · ' + esc(r.slug) + ' · verified ' + esc(r.last_verified || "—") + '</span></div>' +
        tag(r.recommended_next_action, ACTION_TAG[r.recommended_next_action]) +
      '</div>' +
      '<p class="detail-liner">' + esc(r.one_liner || "") + '</p>' +
      '<dl class="d-grid">' +
        row("API type", esc(r.api_type) + " · " + esc(r.api_breadth) + " breadth") +
        row("Auth methods", esc((r.auth_methods || []).join(", ") || "—")) +
        row("Production access", '<b>' + esc(access.kind || "—") + '</b> — ' + esc(access.note || "")) +
        row("Existing MCP", esc(r.existing_mcp)) +
        row("Composio", esc(cov.status || "—") + (cov.tools_count != null ? " · " + cov.tools_count + " tools" : "")) +
        row("Main blocker", esc(r.main_blocker || "—")) +
        row("Confidence", pct(r.confidence) + "%") +
      '</dl>' +
      (reasoning ? '<div class="d-section"><h3>Model reasoning</h3><p>' + esc(reasoning) + '</p></div>' : '') +
      (links ? '<div class="d-section"><h3>Evidence</h3><ul class="d-links">' + links + '</ul></div>' : '');
  }

  // ---------------------------------------------------------------- verify
  function scoreCard(title, note, stats) {
    var body = stats.map(function (s) {
      return '<div class="sc-stat"><span>' + esc(s[0]) + '</span><b>' + esc(s[1]) + '</b></div>';
    }).join("");
    return '<div class="score-card"><h3>' + esc(title) + '</h3>' +
      (note ? '<p>' + esc(note) + '</p>' : '') + '<div class="sc-stats">' + body + '</div></div>';
  }
  function renderVerify() {
    var out = [];
    var hc = METRICS.handcheck;
    if (hc) out.push(scoreCard("Official-doc adjudication", hc.metric_scope || "", [
      ["apps", hc.n], ["api type", pct(hc.api_type_accuracy) + "%"],
      ["auth set", pct(hc.auth_accuracy) + "%"], ["access", pct(hc.access_accuracy) + "%"],
      ["mcp", pct(hc.mcp_accuracy) + "%"],
    ]));
    var am = METRICS.accuracy_movement;
    if (am) out.push(scoreCard("Correction replay", "First pass vs corrected, same truth set.", [
      ["first pass", am.first_pass != null ? pct(am.first_pass) + "%" : "—"],
      ["corrected", am.corrected != null ? pct(am.corrected) + "%" : "—"],
      ["truth apps", am.n != null ? am.n : "—"],
    ]));
    var bu = METRICS.browser_use;
    if (bu) out.push(scoreCard("Independent browser check", "Browser Use Cloud re-derived key fields.", [
      ["sampled", bu.sample != null ? bu.sample : (bu.n != null ? bu.n : "—")],
      ["agreed", bu.agreement != null ? pct(bu.agreement) + "%" : (bu.agreed != null ? bu.agreed : "—")],
    ]));
    el("score-grid").innerHTML = out.join("") || '<p class="empty">Verification metrics populate after a run.</p>';
  }

  // ---------------------------------------------------------------- method
  var STEPS = [
    ["SDK coverage audit", "Composio SDK classifies every app active / catalog-only / missing and records tool depth.", "--composio-audit"],
    ["Docs research", "OpenAI web search plus direct fetch collect official API, auth, access, and MCP pages.", "docs_research.py"],
    ["Schema synthesis", "OpenAI returns a locked 19-field record with cited URLs via structured output.", "synthesis.py"],
    ["Deterministic gate", "Invalid labels, weak coverage, contradictions, and invented links fail closed.", "schema.py"],
    ["Official-doc check", "Priority apps adjudicated against vendor docs; every miss preserved.", "handcheck.py"],
    ["Session diagnostic", "A read-only OpenAI Session runs one bounded Browser Tool check.", "--composio-agent"],
  ];
  function renderMethod() {
    el("flow").innerHTML = STEPS.map(function (s, i) {
      return '<div class="flow-node">' +
        '<div class="flow-num">' + String(i + 1).padStart(2, "0") + '</div>' +
        '<div class="flow-body"><b>' + esc(s[0]) + '</b><p>' + esc(s[1]) + '</p><code>' + esc(s[2]) + '</code></div>' +
        '</div>';
    }).join("");
  }
  var COMMANDS = {
    research: "python research.py --all --fresh-run --model gpt-5\npython research.py --metrics\npython research.py --build-report",
    verify: "python browser_verify.py --sample 12\npython research.py --fold-handcheck\npython research.py --apply-handcheck\npython research.py --accuracy-movement",
    composio: "python research.py --composio-audit\npython research.py --composio-agent otter-ai\npython research.py --build-report",
  };
  function bindMethodTabs() {
    el("command-output").textContent = COMMANDS.research;
    document.querySelectorAll(".seg-tab").forEach(function (btn) {
      btn.addEventListener("click", function () {
        document.querySelectorAll(".seg-tab").forEach(function (b) { b.classList.remove("active"); });
        btn.classList.add("active");
        el("command-output").textContent = COMMANDS[btn.dataset.cmd] || "";
      });
    });
  }

  // ---------------------------------------------------------------- wire up
  function bindEvents() {
    document.querySelectorAll(".rail-item").forEach(function (b) {
      b.addEventListener("click", function () { scrollToView(b.dataset.view); });
    });
    ["q", "f-cat", "f-next"].forEach(function (id) {
      el(id).addEventListener("input", renderCatalogList);
      el(id).addEventListener("change", renderCatalogList);
    });
    el("catalog-rows").addEventListener("click", function (e) {
      var li = e.target.closest("li[data-slug]");
      if (!li) return;
      renderDetail(li.dataset.slug);
      renderCatalogList();
    });
    el("queue-body").addEventListener("click", function (e) {
      var tr = e.target.closest("tr[data-slug]");
      if (!tr) return;
      renderDetail(tr.dataset.slug);
      renderCatalogList();
      scrollToView("catalog");
    });
    if (el("repo-link") && METRICS.repo_url) el("repo-link").href = METRICS.repo_url;
  }

  function init() {
    if (!RESULTS.length) {
      el("decision-title").textContent = "No data loaded. Run `python research.py --build-report` to generate report/data.js.";
      return;
    }
    el("view-sub").textContent = "Live audit — " + RESULTS.length + " of 100 requested apps resolved";
    renderStrip();
    renderOverview();
    renderQueue();
    initFilters();
    renderCatalogList();
    renderVerify();
    renderMethod();
    bindMethodTabs();
    bindEvents();
    bindScrollSpy();
    setActiveRailItem("overview");
    if (location.hash) {
      var target = document.getElementById("view-" + location.hash.replace("#", ""));
      if (target) target.scrollIntoView({ block: "start" });
    }
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
