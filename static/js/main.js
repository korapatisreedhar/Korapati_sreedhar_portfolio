document.addEventListener("DOMContentLoaded", () => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        const fill = entry.target.querySelector(".progress-fill");
        if (fill) fill.style.width = fill.dataset.width;
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });

  document.querySelectorAll(".reveal").forEach(el => observer.observe(el));

  document.querySelectorAll(".nav-link").forEach(link => {
    link.addEventListener("click", () => {
      const menu = document.querySelector(".navbar-collapse");
      if (menu.classList.contains("show")) {
        bootstrap.Collapse.getOrCreateInstance(menu).hide();
      }
    });
  });
});
