# NCP-GENL

Study site for the NVIDIA NCP-GENL exam: https://venkatacrc.github.io/ncpgenl/

- **GenL Cards** (`index.html`) — a mobile-first flashcard web app (installable PWA, works
  offline): beginner track, foundations, the official study guide's objectives and readings,
  200 verses, practice questions and exam traps, with Learn/Test modes and a due-today review
  schedule. Progress is kept in the browser.
- **Verses** (`verses.html`, `domains/`) — 200 forward-chained study verses across 10 domains.

The app files are generated; rebuild them from the course repo with
`scripts/build_web.sh --public <path-to-this-repo>`.
