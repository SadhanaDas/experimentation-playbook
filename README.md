
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>A/B Testing Guide — README</title>
  <style>
    :root{
      --bg:#0f1724;
      --card:#0b1220;
      --muted:#94a3b8;
      --accent:#60a5fa;
      --glass: rgba(255,255,255,0.03);
      --code-bg:#071025;
      --radius:12px;
      --maxw:980px;
      color-scheme: dark;
    }
    html,body{height:100%}
    body{
      margin:0;
      font-family:Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
      background: linear-gradient(180deg,#071029 0%, #081027 40%, #04121a 100%);
      color:#e6eef8;
      -webkit-font-smoothing:antialiased;
      -moz-osx-font-smoothing:grayscale;
      line-height:1.5;
      padding:32px;
      display:flex;
      justify-content:center;
    }

  .container{
      width:100%;
      max-width:var(--maxw);
      background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
      border-radius:18px;
      box-shadow: 0 10px 30px rgba(2,6,23,0.7), inset 0 1px 0 rgba(255,255,255,0.02);
      overflow:hidden;
      border: 1px solid rgba(255,255,255,0.03);
      display:grid;
      grid-template-columns: 260px 1fr;
      gap:0;
    }

    /* Sidebar */
    aside{
      padding:20px;
      background: linear-gradient(180deg, rgba(255,255,255,0.01), rgba(255,255,255,0.00));
      border-right:1px solid rgba(255,255,255,0.02);
      min-height:420px;
    }
  .brand{
      display:flex;
      gap:12px;
      align-items:center;
      margin-bottom:14px;
    }
    .logo{
      width:44px;
      height:44px;
      border-radius:10px;
      background:linear-gradient(135deg,var(--accent),#3b82f6);
      display:flex;
      align-items:center;
      justify-content:center;
      font-weight:700;
      color:white;
      box-shadow:0 6px 20px rgba(60,90,160,0.18);
    }
    .brand h1{font-size:15px;margin:0}
    .muted{color:var(--muted);font-size:13px;margin-top:6px}

  nav{margin-top:14px}
    nav a{
      display:block;
      color:var(--muted);
      text-decoration:none;
      padding:8px 6px;
      border-radius:8px;
      font-size:14px;
    }
    nav a:hover{background:var(--glass); color:var(--accent)}
    nav a.active{background:rgba(96,165,250,0.09); color:var(--accent)}

    /* Main content */
  main{
      padding:28px;
      overflow:auto;
    }
    header h2{margin:0;font-size:20px}
    header p{color:var(--muted);margin-top:8px}

  section{margin-top:20px;padding-bottom:6px}
  h3{color:#dbeafe;margin-top:18px}
  p{color:#d8e7f8}
   ul{color:var(--muted); margin-left:18px}
    pre.code, code.inline{
      background:var(--code-bg);
      padding:10px;
      border-radius:8px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, "Roboto Mono", "Courier New", monospace;
      font-size:13px;
      color:#cbe7ff;
      overflow:auto;
    }
    pre.code{white-space:pre-wrap;word-break:break-word}

    .file-structure{
      background: linear-gradient(180deg, rgba(255,255,255,0.01), rgba(255,255,255,0.00));
      border: 1px solid rgba(255,255,255,0.03);
      padding:12px;border-radius:10px;color:var(--muted);
    }

    .btn{
      display:inline-block;
      margin-top:10px;
      color:white;
      text-decoration:none;
      background:var(--accent);
      padding:8px 12px;
      border-radius:8px;
      font-weight:600;
      box-shadow: 0 6px 18px rgba(59,130,246,0.12);
    }

    .meta{
      display:flex;
      gap:8px;
      margin-top:12px;
      color:var(--muted);
      font-size:13px;
    }

    footer{
      margin-top:26px;
      padding-top:16px;
      border-top:1px solid rgba(255,255,255,0.02);
      color:var(--muted);
      font-size:13px;
    }

    /* responsive */
    @media (max-width:900px){
      .container{grid-template-columns:1fr; padding:0}
      aside{order:2;border-right:none;border-top:1px solid rgba(255,255,255,0.02)}
      main{order:1}
    }

    /* copy button */
    .copy-btn{
      float:right;
      background:transparent;
      border:none;
      color:var(--muted);
      cursor:pointer;
      font-size:13px;
      padding:6px;
    }
    .code-header{display:flex;align-items:center;gap:8px;margin-bottom:8px}
  </style>
</head>
<body>
  <div class="container" role="document" aria-label="A/B Testing README">
    <aside>
      <div class="brand">
        <div class="logo">AB</div>
        <div>
          <h1>A/B Testing Guide</h1>
          <div class="muted">Comprehensive README</div>
        </div>
      </div>

      <nav aria-label="Table of contents">
        <a href="#introduction" class="active">Introduction</a>
        <a href="#what-is-ab-testing">What is A/B Testing?</a>
        <a href="#experiment-brief">Experiment Brief</a>
        <a href="#roles-responsibilities">Roles & Responsibilities</a>
        <a href="#ab-test-calculators">A/B Test Calculators</a>
        <a href="#practical-significance">Practical Significance</a>
        <a href="#how-to-use-this-repo">How to Use This Repository</a>
        <a href="#license">License</a>
      </nav>

      <div class="meta" aria-hidden="true">
        <div>⭐ Template</div>
        <div>•</div>
        <div>Version: 1.0</div>
      </div>
    </aside>

    <main>
      <header>
        <h2>📊 A/B Testing Guide</h2>
        <p>A comprehensive overview of methodology, experiment design, and analysis tools — ready to be used as a README or docs page.</p>
      </header>

      <section id="introduction">
        <h3>🧭 Introduction</h3>
        <p>
          This document provides an in-depth explanation of <strong>A/B testing</strong>, including its methodology,
          how to structure an <strong>Experiment Brief</strong>, and recommended calculators for sample size,
          test duration, and statistical significance. Designed for Product Managers, Product Analysts, Engineers, and Data Scientists.
        </p>
      </section>

      <section id="what-is-ab-testing">
        <h3>🔍 What Is A/B Testing?</h3>
        <p>
          A/B testing is a controlled experimentation framework where two experiences — <strong>Control (A)</strong> and
          <strong>Variant (B)</strong> — are compared to determine which performs better.
        </p>
        <ul>
          <li><strong>P-value</strong>: Probability that observed differences are due to chance.</li>
          <li><strong>Effect size</strong>: The magnitude of the difference you want to detect.</li>
          <li><strong>Type I & II errors</strong>: False positives / false negatives.</li>
          <li><strong>Confidence & Power</strong>: Ensure reliability and minimize missed effects.</li>
        </ul>
      </section>

      <section id="experiment-brief">
        <h3>📝 Experiment Brief</h3>
        <p>
          The Experiment Brief aligns stakeholders before running a test. It should be concise but complete.
          Typically authored by a <strong>Product Manager</strong> with input from Analysts and Engineers.
        </p>

        <h4>Typical Contents</h4>
        <ul>
          <li><strong>Objective</strong> — Why we're running the test.</li>
          <li><strong>Hypothesis</strong> — Expected change and reason.</li>
          <li><strong>Design details</strong> — What changes in the variant.</li>
          <li><strong>Audience</strong> — Inclusion/exclusion criteria.</li>
          <li><strong>Primary & Secondary metrics</strong> — How success is measured.</li>
          <li><strong>Expected impact</strong> — Business outcomes anticipated.</li>
          <li><strong>Rollout & guardrails</strong> — Duration, monitoring, and rollback plan.</li>
          <li><strong>Analysis plan</strong> — Statistical tests, segmentation, and ramp rules.</li>
        </ul>

        <div class="file-structure" aria-hidden="true">
          <strong>Experiment brief template (quick example):</strong>
          <pre class="code" id="brief-example">
Objective:
  Increase signup conversion on the landing page by improving the CTA copy and layout.

Hypothesis:
  Changing CTA text from "Get Started" to "Join Free" and moving it above the fold will increase signup rate by 3%.

Design:
  - Control: current layout
  - Variant B: updated CTA text and moved position

Audience:
  - Desktop & mobile web visitors
  - Exclude logged-in users and internal traffic

Primary metric:
  - Signup conversion rate (track: events.signup.completed)

Secondary metrics:
  - CTR on CTA
  - Bounce rate on landing page
  - Average time on page

Duration & sample:
  - See calculators for sample size & duration
          </pre>
        </div>
      </section>

      <section id="roles-responsibilities">
        <h3>👩‍💻 Roles & Responsibilities</h3>

    <h4>Product Manager</h4>
        <ul>
          <li>Owns hypothesis, objectives, and experiment brief.</li>
          <li>Aligns cross-functional partners (Design, Eng, Analytics).</li>
          <li>Decides on rollouts, guardrails, and business-case trade-offs.</li>
        </ul>

    <h4>Product Analyst</h4>
        <ul>
          <li>Defines and validates success metrics.</li>
          <li>Calculates sample size & estimated duration.</li>
          <li>Validates instrumentation and builds dashboards.</li>
          <li>Helps interpret statistical and practical significance.</li>
        </ul>

     <h4>Engineering</h4>
        <ul>
          <li>Implements bucketing and logging.</li>
          <li>Ensures experiment integrity and rollback capability.</li>
        </ul>
      </section>

      <section id="ab-test-calculators">
        <h3>🧮 A/B Test Calculators</h3>
        <p>Recommended tools to include in your repo:</p>

     <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:10px">
          <div style="flex:1;min-width:220px">
            <strong>1. Sample Size Calculator</strong>
            <p class="muted" style="color:var(--muted)">Determines minimum required users for detecting an effect.</p>
          </div>

    <div style="flex:1;min-width:220px">
            <strong>2. Test Duration Calculator</strong>
            <p class="muted" style="color:var(--muted)">Estimates run-time given current traffic and sample size.</p>
          </div>

     <div style="flex:1;min-width:220px">
            <strong>3. Statistical Significance Calculator</strong>
            <p class="muted" style="color:var(--muted)">Performs z-tests / t-tests and returns p-values / confidence intervals.</p>
          </div>
        </div>

    <h4 style="margin-top:12px">Example: Simple Python sample-size function</h4>
        <div class="code-header">
          <button class="copy-btn" onclick="copyText('#python-sample')">Copy</button>
        </div>
        <pre class="code" id="python-sample">
# Simple sample size calc (approx)
# Requires: baseline (p0), minimum detectable effect (d) as absolute change,
# power (0.8) and alpha (0.05).

<section id="practical-significance">
    <h3>🎯 Practical Significance</h3>
        <p>
          Practical significance answers: <em>“Is the observed improvement meaningful for the business?”</em>
          It matters when statistical thresholds are not clear-cut or when marginal changes have outsized business impact.
        </p>
        <ul>
          <li>Assess absolute and relative change vs business thresholds.</li>
          <li>Check consistency across segments and time windows.</li>
          <li>Estimate revenue or cost impact from the observed delta.</li>
          <li>Consider operational trade-offs and UX implications.</li>
        </ul>
</section>



  <h4>Suggested workflow</h4>
        <ol>
          <li>Draft the Experiment Brief and get stakeholder alignment.</li>
          <li>Validate tracking and instrumentation with Engineering.</li>
          <li>Use calculators to check feasibility (sample size & duration).</li>
          <li>Run experiment and monitor dashboards for data quality.</li>
          <li>Analyze results for statistical and practical significance.</li>
          <li>Document outcome & next steps in the experiment brief.</li>
        </ol>

  <p> Use the provided calculators (or plug-ins in your analytics stack) to run quick checks. Keep notes in the Experiment Brief for every experiment — this makes knowledge transfer and post-mortems simple.
 </p>
  </section>

  <section id="license">
        <h3>📄 License</h3>

Copyright (c) 2025 Sadhana Das

Permission is hereby granted, free of charge, to any person obtaining a copy...
        </pre>
      </section>

  <footer>
        <div style="display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap">
          <div>Made with ❤️ — Copy, customize, and use in your projects.</div>
        </div>
      </footer>
    </main>
  </div>
</body>
</html>
