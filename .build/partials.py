"""
Shared HTML partials (nav + footer) for ARIMEC.
Run the scripts in this folder to regenerate HTML pages with consistent
nav/footer. This keeps the site DRY without introducing a runtime framework.
"""

HEAD_BASE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="theme-color" content="#0B1F3B" />

  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="ARIMEC Industries" />
  <meta property="og:title" content="{og_title}" />
  <meta property="og:description" content="{og_description}" />
  <meta property="og:url" content="https://arimec.com{path}" />
  <meta property="og:locale" content="en_GB" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{og_title}" />
  <meta name="twitter:description" content="{og_description}" />

  <link rel="canonical" href="https://arimec.com{path}" />
  <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="/style.css" />
{schema}
</head>
<body>
"""

NAV = """
<header class="nav" role="banner">
  <div class="shell nav__inner">
    <a class="nav__brand" href="/" aria-label="ARIMEC Industries — Home">
      <svg viewBox="0 0 40 40" aria-hidden="true"><path d="M20 3 L37 34 L3 34 Z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="miter"/><path d="M20 14 L28 30 L12 30 Z" fill="currentColor"/></svg>
      <span class="nav__brand-text">
        <span class="nav__brand-name">ARIMEC</span>
        <span class="nav__brand-sub">Industries</span>
      </span>
    </a>
    <nav class="nav__links" aria-label="Primary">
      <a data-nav-link href="/about.html">About</a>
      <a data-nav-link href="/platforms.html">Platforms</a>
      <a data-nav-link href="/projects.html">Projects</a>
      <a data-nav-link href="/contact.html">Contact</a>
    </nav>
    <a class="btn nav__cta" href="/contact.html">Engage with ARIMEC
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
    </a>
    <button class="nav__toggle" type="button" aria-label="Toggle menu" aria-expanded="false" data-nav-toggle>
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
    </button>
  </div>
  <div class="nav__panel" data-nav-panel>
    <div class="shell" style="padding-top:1rem;padding-bottom:1.25rem">
      <ul>
        <li><a href="/about.html">About</a></li>
        <li><a href="/platforms.html">Platforms</a></li>
        <li><a href="/projects.html">Projects</a></li>
        <li><a href="/contact.html">Contact</a></li>
      </ul>
      <a class="btn" href="/contact.html">Engage with ARIMEC
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
      </a>
    </div>
  </div>
</header>
"""

FOOTER = """
<footer class="footer" role="contentinfo">
  <div class="shell">
    <div class="trust reveal">
      <div class="trust__item">
        <span class="trust__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6l8-3z"/></svg></span>
        <div><div class="trust__title">Infrastructure Focused</div><div class="trust__text">Real assets. Real impact.</div></div>
      </div>
      <div class="trust__item">
        <span class="trust__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="9" cy="9" r="3"/><circle cx="17" cy="10" r="2.5"/><path d="M3 19c1-3 3.5-4.5 6-4.5S14 16 15 19"/><path d="M14.5 19c.5-2 2-3 3.5-3s2.5.5 3 2"/></svg></span>
        <div><div class="trust__title">Execution Driven</div><div class="trust__text">From concept to delivery.</div></div>
      </div>
      <div class="trust__item">
        <span class="trust__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/></svg></span>
        <div><div class="trust__title">Global Perspective</div><div class="trust__text">Local insight. Global reach.</div></div>
      </div>
      <div class="trust__item">
        <span class="trust__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M5 19V11M10 19V7M15 19V13M20 19V5"/></svg></span>
        <div><div class="trust__title">Built for Scale</div><div class="trust__text">Platforms designed to grow.</div></div>
      </div>
    </div>
  </div>
  <div class="hairline"></div>
  <div class="shell">
    <div class="footer__main">
      <div class="footer__brand">
        <a class="nav__brand" href="/">
          <svg viewBox="0 0 40 40" aria-hidden="true" style="width:28px;height:28px;color:var(--ink)"><path d="M20 3 L37 34 L3 34 Z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="miter"/><path d="M20 14 L28 30 L12 30 Z" fill="currentColor"/></svg>
          <span class="nav__brand-text">
            <span class="nav__brand-name">ARIMEC</span>
            <span class="nav__brand-sub">Industries</span>
          </span>
        </a>
        <p class="muted" style="margin-top:1.25rem">Infrastructure development and delivery platform. Structured for delivery. Positioned for scale.</p>
        <div class="loc" style="margin-top:1rem">London | International</div>
        <a class="email" href="mailto:contact@arimec.com">contact@arimec.com</a>
      </div>
      <div class="footer__col">
        <h4 class="eyebrow">Platforms</h4>
        <ul>
          <li><a href="/platforms.html#energy">ARIMEC Energy</a></li>
          <li><a href="/platforms.html#construction">ARIMEC Construction</a></li>
          <li><a href="/platforms.html#data-centres">ARIMEC Data Centre Solutions</a></li>
          <li><a href="/platforms.html#adi">ADI — Development Industries</a></li>
        </ul>
      </div>
      <div class="footer__col">
        <h4 class="eyebrow">Company</h4>
        <ul>
          <li><a href="/about.html">About</a></li>
          <li><a href="/projects.html">Projects</a></li>
          <li><a href="/contact.html">Contact</a></li>
        </ul>
      </div>
      <div class="footer__col">
        <h4 class="eyebrow">Contact</h4>
        <ul>
          <li><span class="muted" style="font-size:0.875rem">London | International</span></li>
          <li><a href="mailto:contact@arimec.com">contact@arimec.com</a></li>
        </ul>
      </div>
    </div>
  </div>
  <div class="hairline"></div>
  <div class="shell">
    <div class="footer__legal">
      <p>Information on this site is for general informational purposes only and does not constitute an offer or solicitation. Nothing on this site creates an advisory, fiduciary, or contractual relationship.</p>
      <p class="rights">© <span data-year>2026</span> ARIMEC Industries. All rights reserved.</p>
    </div>
  </div>
</footer>

<script src="/app.js" defer></script>
</body>
</html>
"""
