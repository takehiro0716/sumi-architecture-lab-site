// main.js — shared behavior for every page: header scroll state + scroll-reveal

(function () {
  var header = document.getElementById("siteHeader");
  if (header) {
    var onScroll = function () {
      header.classList.toggle("scrolled", window.scrollY > 30);
    };
    document.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  var navToggle = document.querySelector(".nav-toggle");
  if (navToggle) {
    var closeNav = function () {
      navToggle.setAttribute("aria-expanded", "false");
    };
    navToggle.addEventListener("click", function (e) {
      e.stopPropagation();
      var isOpen = navToggle.getAttribute("aria-expanded") === "true";
      navToggle.setAttribute("aria-expanded", isOpen ? "false" : "true");
    });
    document.addEventListener("click", function (e) {
      if (!navToggle.contains(e.target) && !e.target.closest(".icon-nav")) {
        closeNav();
      }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") closeNav();
    });
  }

  var toTopBtn = document.querySelector(".to-top");
  if (toTopBtn) {
    var toggleToTop = function () {
      toTopBtn.classList.toggle("is-visible", window.scrollY > window.innerHeight * 0.6);
    };
    document.addEventListener("scroll", toggleToTop, { passive: true });
    toggleToTop();
    toTopBtn.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.1, rootMargin: "0px 0px -4% 0px" }
    );
    revealEls.forEach(function (el) {
      io.observe(el);
    });
  } else {
    revealEls.forEach(function (el) {
      el.classList.add("is-visible");
    });
  }

  var moreBtn = document.getElementById("blogMoreBtn");
  if (moreBtn) {
    var pageSize = parseInt(moreBtn.getAttribute("data-page-size"), 10) || 10;
    var moreLabel = "もっと見る";
    var lessLabel = "閉じる";
    var labelEl = moreBtn.querySelector(".blog-more-label");
    moreBtn.addEventListener("click", function () {
      var expanded = moreBtn.classList.toggle("is-expanded");
      var cards = document.querySelectorAll(".blog-card");
      cards.forEach(function (el, i) {
        if (i < pageSize) return;
        if (expanded) {
          el.classList.remove("is-hidden");
          el.classList.add("is-visible");
        } else {
          el.classList.add("is-hidden");
          el.classList.remove("is-visible");
        }
      });
      if (labelEl) labelEl.textContent = expanded ? lessLabel : moreLabel;
      if (!expanded) {
        moreBtn.scrollIntoView({ behavior: "smooth", block: "center" });
      }
    });
  }
})();
