'use strict';
const filters = document.querySelector('.filters');
const papers = [...document.querySelectorAll('.paper')];
if (filters) {
  filters.hidden = false;
  filters.addEventListener('click', (event) => {
    const button = event.target.closest('button[data-filter]');
    if (!button) return;
    const selected = button.dataset.filter;
    for (const item of filters.querySelectorAll('button')) item.setAttribute('aria-pressed', String(item === button));
    for (const paper of papers) paper.hidden = selected !== 'all' && paper.dataset.category !== selected;
    const count = papers.filter(paper => !paper.hidden).length;
    document.querySelector('#publication-count').textContent = `${count} ${count === 1 ? 'paper' : 'papers'}`;
  });
}
