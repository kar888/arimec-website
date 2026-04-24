/* =================================================================
   ARIMEC Industries — app.js
   Tiny, dependency-free enhancements: mobile nav toggle, scroll-
   aware reveals, contact form frontend validation.
================================================================= */

(() => {
  "use strict";

  /* -------- Mobile nav toggle -------- */
  const toggle = document.querySelector("[data-nav-toggle]");
  const panel = document.querySelector("[data-nav-panel]");
  if (toggle && panel) {
    toggle.addEventListener("click", () => {
      const isOpen = panel.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(isOpen));
    });
    // Close on link click
    panel.querySelectorAll("a").forEach((a) =>
      a.addEventListener("click", () => {
        panel.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
      })
    );
  }

  /* -------- Active nav state -------- */
  const here = (location.pathname.replace(/\/index\.html$/, "/") || "/").replace(/\/$/, "") || "/";
  document.querySelectorAll("[data-nav-link]").forEach((a) => {
    const href = a.getAttribute("href") || "";
    const norm = href.replace(/\/index\.html$/, "/").replace(/\/$/, "") || "/";
    if (norm === here || (norm !== "/" && here.startsWith(norm))) {
      a.classList.add("is-active");
    }
  });

  /* -------- Reveal utility (kept as a no-op class hook) -------- */
  // Reveal-on-scroll intentionally disabled for institutional tone.
  // Content is visible immediately, consistent with restrained design.

  /* -------- Contact form (frontend validation only) -------- */
  const form = document.querySelector("[data-contact-form]");
  if (form) {
    const status = form.querySelector("[data-form-status]");
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      status.classList.remove("is-error", "is-ok");

      const data = new FormData(form);
      const name = String(data.get("name") || "").trim();
      const email = String(data.get("email") || "").trim();
      const message = String(data.get("message") || "").trim();

      if (!name || !email || !message) {
        status.textContent = "Please complete the required fields.";
        status.classList.add("is-error");
        return;
      }
      const emailOk = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
      if (!emailOk) {
        status.textContent = "Please enter a valid email address.";
        status.classList.add("is-error");
        return;
      }

      // Build a mailto fallback so the message is never lost.
      const subject = `ARIMEC enquiry — ${name}`;
      const body =
        `Name: ${name}\n` +
        `Email: ${email}\n` +
        `Company: ${String(data.get("company") || "").trim()}\n\n` +
        `${message}\n`;
      const mailto = `mailto:contact@arimec.com?subject=${encodeURIComponent(
        subject
      )}&body=${encodeURIComponent(body)}`;

      status.textContent =
        "Thank you. Opening your email client to send the message.";
      status.classList.add("is-ok");
      window.location.href = mailto;
    });
  }

  /* -------- Current year in footer -------- */
  const y = document.querySelector("[data-year]");
  if (y) y.textContent = String(new Date().getFullYear());
})();
