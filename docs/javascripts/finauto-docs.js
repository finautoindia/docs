/**
 * FinAuto docs — light UX enhancements
 */
(function () {
  document.querySelectorAll(".md-typeset a[href^='http']").forEach(function (a) {
    if (a.hostname !== window.location.hostname) {
      a.setAttribute("target", "_blank");
      a.setAttribute("rel", "noopener");
    }
  });

  // Style step headings (### Step N: ...)
  document.querySelectorAll(".md-typeset h3").forEach(function (h3) {
    if (/^step\s+\d+/i.test(h3.textContent.trim())) {
      h3.classList.add("fa-docs-step-heading");
      var card = document.createElement("div");
      card.className = "fa-docs-step";
      h3.parentNode.insertBefore(card, h3);
      card.appendChild(h3);
      var sib = card.nextSibling;
      while (sib && !(sib.nodeType === 1 && /^H[23]$/.test(sib.tagName))) {
        var next = sib.nextSibling;
        card.appendChild(sib);
        sib = next;
      }
    }
  });
})();
