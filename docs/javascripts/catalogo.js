document$.subscribe(() => {
  const catalog = document.querySelector("[data-cert-catalog]");
  if (!catalog) return;

  const search = document.querySelector("[data-cert-search]");
  const buttons = [...document.querySelectorAll("[data-cert-filter]")];
  const cards = [...catalog.querySelectorAll("[data-cert-card]")];
  const empty = document.querySelector("[data-cert-empty]");
  let activeStream = "all";

  const applyFilters = () => {
    const query = search.value.trim().toLocaleLowerCase("it");
    let visible = 0;
    cards.forEach((card) => {
      const matchesStream = activeStream === "all" || card.dataset.stream === activeStream;
      const matchesQuery = card.textContent.toLocaleLowerCase("it").includes(query);
      const show = matchesStream && matchesQuery;
      card.hidden = !show;
      if (show) visible += 1;
    });
    empty.hidden = visible !== 0;
  };

  search.addEventListener("input", applyFilters);
  buttons.forEach((button) => {
    button.addEventListener("click", () => {
      activeStream = button.dataset.certFilter;
      buttons.forEach((candidate) => candidate.setAttribute("aria-pressed", String(candidate === button)));
      applyFilters();
    });
  });
});
