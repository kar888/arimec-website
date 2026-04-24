#!/usr/bin/env python3
"""
Generate ARIMEC pages (about, platforms, projects, contact) with the
shared nav/footer. The homepage (index.html) is hand-authored and kept
in sync manually — keep partials.py synchronised if you change the
nav/footer on the home page.

Usage:
    python3 .build/build.py
"""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from partials import HEAD_BASE, NAV, FOOTER  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "website"

SCHEMA_ORG = """
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "ARIMEC Industries",
    "url": "https://arimec.com",
    "logo": "https://arimec.com/images/logo.svg",
    "description": "Infrastructure development and delivery platform operating across energy, construction, data centres, and advanced systems.",
    "email": "contact@arimec.com",
    "address": { "@type": "PostalAddress", "addressLocality": "London", "addressCountry": "GB" },
    "areaServed": ["GB", "Global"]
  }
  </script>
"""


def render(page: dict, body: str) -> str:
    head = HEAD_BASE.format(
        title=page["title"],
        description=page["description"],
        og_title=page.get("og_title", page["title"]),
        og_description=page.get("og_description", page["description"]),
        path=page["path"],
        schema=page.get("schema", SCHEMA_ORG),
    )
    return head + NAV + body + FOOTER


# =============================================================== ABOUT
ABOUT_BODY = """
<section class="page-head">
  <div class="shell page-head__grid">
    <div>
      <p class="eyebrow">About ARIMEC</p>
      <h1 class="accent-rule" style="margin-top:0.75rem">An infrastructure development and delivery platform.</h1>
    </div>
    <p>ARIMEC Industries originates, structures, and delivers infrastructure across energy, construction, data centres, and advanced systems. Our platforms are built for institutional capital and long-duration delivery.</p>
  </div>
</section>

<section style="padding:0">
  <div style="position:relative;width:100%;aspect-ratio:21/9;background:var(--soft);overflow:hidden;border-bottom:1px solid var(--line)">
    <img src="/images/about-site.jpg" alt="Infrastructure construction site with heavy equipment and steel framework" loading="lazy" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover" width="1600" height="686" />
  </div>
</section>

<section>
  <div class="shell">
    <div class="section-head reveal">
      <div>
        <p class="eyebrow">Positioning</p>
        <h2>Structured for delivery.<br />Positioned for scale.</h2>
      </div>
    </div>
    <div class="principles reveal">
      <div>
        <div class="principles__index">01</div>
        <h3>Structured Execution</h3>
        <p>Disciplined engineering, procurement, and delivery embedded across every platform.</p>
      </div>
      <div>
        <div class="principles__index">02</div>
        <h3>Capital Discipline</h3>
        <p>Projects originated and structured to meet institutional bankability standards.</p>
      </div>
      <div>
        <div class="principles__index">03</div>
        <h3>Scalable Platforms</h3>
        <p>Repeatable delivery models built for long-duration pipelines and measured growth.</p>
      </div>
      <div>
        <div class="principles__index">04</div>
        <h3>Institutional Alignment</h3>
        <p>Governance and reporting standards shaped to the expectations of long-term capital.</p>
      </div>
    </div>
  </div>
</section>

<section style="border-top:1px solid var(--line)">
  <div class="shell">
    <div class="narrative reveal">
      <div><p class="eyebrow">Who We Are</p></div>
      <div>
        <p>ARIMEC Industries develops and executes infrastructure platforms across four integrated verticals. Each platform is structured to meet the standards of institutional lenders, equity partners, and long-term counterparties.</p>
        <p>Our approach is disciplined by design. Projects are originated with bankability in mind, structured through rigorous engineering and procurement processes, and scaled through repeatable delivery models. We build platforms — not one-off projects.</p>
        <p>ARIMEC operates from London with an international footprint spanning energy and digital infrastructure markets in growth regions. Our work is focused on real assets, real execution, and measurable outcomes.</p>
      </div>
    </div>
  </div>
</section>

<section style="border-top:1px solid var(--line)">
  <div class="shell">
    <div class="stats reveal">
      <div class="stat"><div class="stat__label">Headquarters</div><div class="stat__value">London</div><div class="stat__caption">United Kingdom</div></div>
      <div class="stat"><div class="stat__label">Coverage</div><div class="stat__value">International</div><div class="stat__caption">Selected growth markets</div></div>
      <div class="stat"><div class="stat__label">Platforms</div><div class="stat__value">Four</div><div class="stat__caption">Integrated verticals</div></div>
      <div class="stat"><div class="stat__label">Pipeline</div><div class="stat__value">Multi-Asset</div><div class="stat__caption">Energy and digital infrastructure</div></div>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="shell cta-band__inner">
    <div>
      <h2>Speak with the team.</h2>
      <p>ARIMEC works with institutional partners across development finance, structured credit, and long-duration capital.</p>
    </div>
    <a class="btn-light" href="/contact.html">Contact
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
    </a>
  </div>
</section>
"""

# =============================================================== PLATFORMS
PLATFORMS_BODY = """
<section class="page-head">
  <div class="shell page-head__grid">
    <div>
      <p class="eyebrow">Platforms</p>
      <h1 class="accent-rule" style="margin-top:0.75rem">Four integrated platforms.<br />One delivery standard.</h1>
    </div>
    <p>ARIMEC operates four platforms across infrastructure, construction, digital infrastructure, and advanced systems. Each is structured as a standalone business vertical and supported by our in-house execution capability.</p>
  </div>
</section>

<section>
  <div class="shell">
    <div class="platform-grid reveal">
      <a class="platform-card" href="#energy" style="text-decoration:none">
        <div class="platform-card__body">
          <div class="platform-card__head">
            <span class="platform-card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="3.2"/><path d="M12 3v2.2M12 18.8V21M3 12h2.2M18.8 12H21M5.6 5.6l1.6 1.6M16.8 16.8l1.6 1.6M5.6 18.4l1.6-1.6M16.8 7.2l1.6-1.6"/></svg></span>
            <div><h3 class="platform-card__name">ARIMEC ENERGY<sup>™</sup></h3><p class="platform-card__tag">Solar Farm Projects</p></div>
          </div>
          <p class="platform-card__copy">Utility-scale solar infrastructure platform developing bankable, PPA-backed projects. Initial pipeline anchored by a 750MW solar platform across West Africa.</p>
          <div class="platform-card__foot"><span class="platform-card__more">Read scope <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M5 12h14M13 5l7 7-7 7"/></svg></span></div>
        </div>
      </a>
      <a class="platform-card" href="#construction" style="text-decoration:none">
        <div class="platform-card__body">
          <div class="platform-card__head">
            <span class="platform-card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="4" y="4" width="7" height="16"/><rect x="13" y="9" width="7" height="11"/><path d="M6 8h3M6 12h3M6 16h3M15 12h3M15 16h3"/></svg></span>
            <div><h3 class="platform-card__name">ARIMEC CONSTRUCTION<sup>™</sup></h3><p class="platform-card__tag">Engineering & Delivery</p></div>
          </div>
          <p class="platform-card__copy">End-to-end engineering, procurement, and construction services. Our execution capability is the backbone across all ARIMEC platforms.</p>
          <div class="platform-card__foot"><span class="platform-card__more">Read scope <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M5 12h14M13 5l7 7-7 7"/></svg></span></div>
        </div>
      </a>
      <a class="platform-card" href="#data-centres" style="text-decoration:none">
        <div class="platform-card__body">
          <div class="platform-card__head">
            <span class="platform-card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="4" y="4" width="16" height="6"/><rect x="4" y="14" width="16" height="6"/><circle cx="8" cy="7" r="0.6" fill="currentColor"/><circle cx="8" cy="17" r="0.6" fill="currentColor"/></svg></span>
            <div><h3 class="platform-card__name">ARIMEC DATA CENTRE SOLUTIONS<sup>™</sup></h3><p class="platform-card__tag">Digital Infrastructure</p></div>
          </div>
          <p class="platform-card__copy">Scalable, secure, and sustainable data centre infrastructure designed to meet the growing demand for high-performance compute and connectivity.</p>
          <div class="platform-card__foot"><span class="platform-card__more">Read scope <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M5 12h14M13 5l7 7-7 7"/></svg></span></div>
        </div>
      </a>
      <a class="platform-card" href="#adi" style="text-decoration:none">
        <div class="platform-card__body">
          <div class="platform-card__head">
            <span class="platform-card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 3l8 4.5v9L12 21l-8-4.5v-9L12 3z"/></svg></span>
            <div><h3 class="platform-card__name">ADI<sup>™</sup></h3><p class="platform-card__tag">ARIMEC Development Industries</p></div>
          </div>
          <p class="platform-card__copy">Advanced systems and special projects focused on applied engineering, infrastructure resilience, and performance-driven technologies.</p>
          <div class="platform-card__foot"><span class="platform-card__more">Read scope <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M5 12h14M13 5l7 7-7 7"/></svg></span></div>
        </div>
      </a>
    </div>
  </div>
</section>

{detail_sections}

<section class="cta-band">
  <div class="shell cta-band__inner">
    <h2>Discuss a platform or project.</h2>
    <a class="btn-light" href="/contact.html">Contact the team
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
    </a>
  </div>
</section>
"""

PLATFORM_DETAILS = [
    {
        "id": "energy",
        "idx": "01",
        "name": "ARIMEC ENERGY<sup>™</sup>",
        "tag": "Solar Farm Projects",
        "copy": "Utility-scale solar infrastructure platform developing bankable, PPA-backed projects. Initial pipeline anchored by a 750MW solar platform across West Africa.",
        "image": "/images/platform-energy.jpg",
        "alt": "Aerial view of a utility-scale solar PV installation",
        "scope": [
            "Utility-scale solar PV development",
            "PPA-backed origination",
            "Long-duration offtake structuring",
            "Phased deployment models",
        ],
        "focus": [
            "West Africa — initial 750MW pipeline",
            "Adjacent growth markets under review",
        ],
    },
    {
        "id": "construction",
        "idx": "02",
        "name": "ARIMEC CONSTRUCTION<sup>™</sup>",
        "tag": "Engineering & Delivery",
        "copy": "End-to-end engineering, procurement, and construction services. Our execution capability is the backbone across all ARIMEC platforms.",
        "image": "/images/platform-construction.jpg",
        "alt": "Large-scale construction site with tower cranes",
        "scope": [
            "Engineering, procurement, and construction (EPC)",
            "In-house project delivery teams",
            "Programme and risk management",
            "Cross-platform integration",
        ],
        "focus": [
            "Core delivery backbone across all ARIMEC platforms",
            "Institutional-grade execution standards",
        ],
    },
    {
        "id": "data-centres",
        "idx": "03",
        "name": "ARIMEC DATA CENTRE SOLUTIONS<sup>™</sup>",
        "tag": "Digital Infrastructure",
        "copy": "Scalable, secure, and sustainable data centre infrastructure designed to meet the growing demand for high-performance compute and connectivity.",
        "image": "/images/platform-datacentre.jpg",
        "alt": "Interior corridor of a modern hyperscale data centre",
        "scope": [
            "Scalable colocation and hyperscale-ready facilities",
            "Power-linked site development",
            "Sustainable cooling and energy design",
            "Long-duration infrastructure leases",
        ],
        "focus": [
            "Multi-site pipeline in selected jurisdictions",
            "Alignment with digital infrastructure investors",
        ],
    },
    {
        "id": "adi",
        "idx": "04",
        "name": "ADI<sup>™</sup>",
        "tag": "ARIMEC Development Industries",
        "copy": "Advanced systems and special projects focused on applied engineering, infrastructure resilience, and performance-driven technologies.",
        "image": "/images/platform-adi.jpg",
        "alt": "Advanced industrial inspection drone on a tarmac",
        "scope": [
            "Applied engineering programmes",
            "Infrastructure resilience systems",
            "Performance-driven industrial technologies",
            "Special project structuring",
        ],
        "focus": [
            "Advanced systems supporting ARIMEC platforms",
            "Research- and engineering-led initiatives",
        ],
    },
]


def build_platform_sections() -> str:
    blocks = []
    for i, p in enumerate(PLATFORM_DETAILS):
        reversed_class = " is-reversed" if i % 2 else ""
        scope_li = "\n".join(f"<li>{s}</li>" for s in p["scope"])
        focus_li = "\n".join(f"<li>{s}</li>" for s in p["focus"])
        blocks.append(f"""
<section id="{p['id']}" class="{('is-reversed' if i % 2 else '').strip()}" style="border-top:1px solid var(--line);scroll-margin-top:90px">
  <div class="shell">
    <div class="platform-detail reveal">
      <div class="platform-detail__img">
        <img src="{p['image']}" alt="{p['alt']}" loading="lazy" width="900" height="675" />
      </div>
      <div class="platform-detail__body">
        <p class="eyebrow">{p['idx']} / Platform</p>
        <h2 style="margin-top:0.75rem">{p['name']}</h2>
        <p class="muted" style="margin-top:0.25rem;font-size:0.9375rem">{p['tag']}</p>
        <p style="margin-top:1.25rem;font-size:1rem;line-height:1.7;max-width:560px">{p['copy']}</p>
        <div class="platform-detail__lists">
          <div>
            <h3 class="eyebrow">Scope</h3>
            <ul style="margin-top:0.75rem">{scope_li}</ul>
          </div>
          <div>
            <h3 class="eyebrow">Focus</h3>
            <ul style="margin-top:0.75rem">{focus_li}</ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>""")
    return "\n".join(blocks)


# =============================================================== PROJECTS
PROJECTS_BODY = """
<section class="page-head">
  <div class="shell page-head__grid">
    <div>
      <p class="eyebrow">Projects</p>
      <h1 class="accent-rule" style="margin-top:0.75rem">Selected platforms<br />and pipeline initiatives.</h1>
    </div>
    <p>A curated view of ARIMEC-originated projects and pipeline platforms. Each initiative is structured for phased deployment and institutional alignment.</p>
  </div>
</section>

<section>
  <div class="shell">
    <div class="projects-grid reveal">
      <article class="project" id="solar-750">
        <div class="project__media">
          <img src="/images/project-solar.jpg" alt="Aerial view of a solar PV platform at sunrise with mountains in the distance" loading="lazy" width="800" height="600" />
        </div>
        <div class="project__body">
          <span class="project__status">In Development</span>
          <h3 class="project__title">Solar Platform (750MW)</h3>
          <p class="project__copy">Utility-scale solar PV platform delivering clean, reliable power across West Africa. Structured for phased deployment and long-term value creation.</p>
          <dl class="project__metrics">
            <div class="metric"><span class="metric__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="3.2"/><path d="M12 3v2.2M12 18.8V21M3 12h2.2M18.8 12H21"/></svg></span><div><dt class="metric__label">Pipeline Capacity</dt><dd class="metric__value">750MW</dd></div></div>
            <div class="metric"><span class="metric__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 21s-7-6.2-7-11a7 7 0 1114 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.2"/></svg></span><div><dt class="metric__label">Focus Region</dt><dd class="metric__value">West Africa</dd></div></div>
          </dl>
          <div style="margin-top:1.25rem;padding-top:1rem;border-top:1px solid var(--line)">
            <span class="eyebrow">Structure</span>
            <p style="margin-top:0.5rem;font-size:0.9375rem">Bankable solar platform originated for institutional capital. PPA-backed with phased build programme. Construction delivery through ARIMEC Construction.</p>
          </div>
        </div>
      </article>

      <article class="project" id="data-centres">
        <div class="project__media">
          <img src="/images/project-datacentre.jpg" alt="Modern data centre building exterior with landscaped grounds" loading="lazy" width="800" height="600" />
        </div>
        <div class="project__body">
          <span class="project__status">In Development</span>
          <h3 class="project__title">Data Centre Infrastructure Pipeline</h3>
          <p class="project__copy">Multi-site data centre development pipeline designed for scalable compute demand and sustainable operations. Power-linked and future-ready.</p>
          <dl class="project__metrics">
            <div class="metric"><span class="metric__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="4" y="5" width="16" height="4"/><rect x="4" y="11" width="16" height="4"/><rect x="4" y="17" width="16" height="2"/></svg></span><div><dt class="metric__label">In Development</dt><dd class="metric__value">Multiple Sites</dd></div></div>
            <div class="metric"><span class="metric__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/></svg></span><div><dt class="metric__label">Global Locations</dt><dd class="metric__value">Strategic</dd></div></div>
          </dl>
          <div style="margin-top:1.25rem;padding-top:1rem;border-top:1px solid var(--line)">
            <span class="eyebrow">Structure</span>
            <p style="margin-top:0.5rem;font-size:0.9375rem">Site-selected pipeline with power-linked development strategy. Structured for long-duration infrastructure leases and sustainable operations.</p>
          </div>
        </div>
      </article>

      <article class="project" id="construction-programme">
        <div class="project__media">
          <img src="/images/platform-construction.jpg" alt="Large-scale construction site with tower cranes" loading="lazy" width="800" height="600" />
        </div>
        <div class="project__body">
          <span class="project__status">Ongoing</span>
          <h3 class="project__title">Construction Delivery Programme</h3>
          <p class="project__copy">In-house engineering and delivery capability supporting ARIMEC platforms end-to-end — from site works to commissioning. Institutional-grade execution standards.</p>
          <dl class="project__metrics">
            <div class="metric"><span class="metric__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="4" y="4" width="7" height="16"/><rect x="13" y="9" width="7" height="11"/></svg></span><div><dt class="metric__label">Scope</dt><dd class="metric__value">EPC Delivery</dd></div></div>
            <div class="metric"><span class="metric__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M4 20V6M20 20V6M4 10h16M4 15h16"/></svg></span><div><dt class="metric__label">Integration</dt><dd class="metric__value">Cross-Platform</dd></div></div>
          </dl>
        </div>
      </article>

      <article class="project" id="adi-initiatives">
        <div class="project__media">
          <img src="/images/platform-adi.jpg" alt="Advanced industrial inspection drone on a tarmac" loading="lazy" width="800" height="600" />
        </div>
        <div class="project__body">
          <span class="project__status">Pre-Development</span>
          <h3 class="project__title">ADI — Advanced Systems Initiatives</h3>
          <p class="project__copy">Applied engineering and special-project programmes focused on infrastructure resilience and performance-driven industrial technologies.</p>
          <dl class="project__metrics">
            <div class="metric"><span class="metric__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 3l8 4.5v9L12 21l-8-4.5v-9L12 3z"/></svg></span><div><dt class="metric__label">Focus</dt><dd class="metric__value">Applied R&D</dd></div></div>
            <div class="metric"><span class="metric__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M4 12h6m4 0h6M12 4v6m0 4v6"/></svg></span><div><dt class="metric__label">Support</dt><dd class="metric__value">Platform-Wide</dd></div></div>
          </dl>
        </div>
      </article>
    </div>

    <p class="muted" style="margin-top:2rem;font-size:0.8125rem;max-width:640px">Project statuses reflect current development stage and are subject to change. Nothing on this page constitutes an offer, solicitation, or guarantee of execution.</p>
  </div>
</section>

<section class="cta-band">
  <div class="shell cta-band__inner">
    <h2>Discuss a project.</h2>
    <a class="btn-light" href="/contact.html">Contact the team
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
    </a>
  </div>
</section>
"""

# =============================================================== CONTACT
CONTACT_BODY = """
<section class="page-head">
  <div class="shell page-head__grid">
    <div>
      <p class="eyebrow">Contact</p>
      <h1 class="accent-rule" style="margin-top:0.75rem">Engage with ARIMEC.</h1>
    </div>
    <p>For institutional partners, lenders, counterparties, and project enquiries. We respond to serious enquiries within two working days.</p>
  </div>
</section>

<section>
  <div class="shell contact-grid">
    <div class="contact-detail">
      <p>For direct enquiries, contact the team by email. Written correspondence is preferred for formal project discussions.</p>
      <dl>
        <dt>Email</dt>
        <dd><a href="mailto:contact@arimec.com">contact@arimec.com</a></dd>
        <dt>Offices</dt>
        <dd>London | International</dd>
        <dt>Response</dt>
        <dd>Within two working days</dd>
      </dl>
      <p class="compliance" style="margin-top:2rem">Messages submitted through this form are received for informational purposes only and do not create an advisory, fiduciary, or contractual relationship. Please do not submit confidential or privileged information.</p>
    </div>

    <form class="form" data-contact-form novalidate aria-label="Contact form">
      <div class="form__row form__row--2">
        <div class="field">
          <label for="name">Name *</label>
          <input type="text" id="name" name="name" autocomplete="name" required />
        </div>
        <div class="field">
          <label for="email">Email *</label>
          <input type="email" id="email" name="email" autocomplete="email" required />
        </div>
      </div>
      <div class="field">
        <label for="company">Company</label>
        <input type="text" id="company" name="company" autocomplete="organization" />
      </div>
      <div class="field">
        <label for="message">Message *</label>
        <textarea id="message" name="message" required></textarea>
      </div>
      <div class="form__status" data-form-status aria-live="polite"></div>
      <div>
        <button type="submit" class="btn">Send enquiry
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
        </button>
      </div>
    </form>
  </div>
</section>
"""


# =============================================================== PAGES
PAGES = [
    {
        "file": "about.html",
        "path": "/about.html",
        "title": "About | ARIMEC Industries",
        "description": "ARIMEC Industries is an infrastructure development and delivery platform. Structured execution. Capital discipline. Scalable platforms. Institutional alignment.",
        "og_title": "About | ARIMEC Industries",
        "og_description": "Infrastructure development and delivery platform. Structured for delivery. Positioned for scale.",
        "body": ABOUT_BODY,
    },
    {
        "file": "platforms.html",
        "path": "/platforms.html",
        "title": "Platforms | ARIMEC Industries",
        "description": "ARIMEC Industries operates four integrated platforms — energy, construction, data centres, and advanced systems.",
        "og_title": "Platforms | ARIMEC Industries",
        "og_description": "Four integrated platforms — energy, construction, data centres, and advanced systems.",
        "body": PLATFORMS_BODY.replace("{detail_sections}", build_platform_sections()),
    },
    {
        "file": "projects.html",
        "path": "/projects.html",
        "title": "Projects | ARIMEC Industries",
        "description": "Selected platforms and pipeline initiatives originated by ARIMEC Industries across energy, construction, and data centre infrastructure.",
        "og_title": "Projects | ARIMEC Industries",
        "og_description": "Selected platforms and pipeline initiatives across energy, construction, and data centres.",
        "body": PROJECTS_BODY,
    },
    {
        "file": "contact.html",
        "path": "/contact.html",
        "title": "Contact | ARIMEC Industries",
        "description": "Contact ARIMEC Industries. London and international offices. contact@arimec.com.",
        "og_title": "Contact | ARIMEC Industries",
        "og_description": "Contact the ARIMEC team for institutional and project enquiries.",
        "body": CONTACT_BODY,
    },
]


def main():
    OUT.mkdir(exist_ok=True)
    for page in PAGES:
        html = render(page, page["body"])
        dest = OUT / page["file"]
        dest.write_text(html, encoding="utf-8")
        print(f"Wrote {dest.relative_to(ROOT)} ({len(html):,} bytes)")


if __name__ == "__main__":
    main()
