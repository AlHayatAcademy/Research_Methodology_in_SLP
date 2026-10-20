# Research Methodology in SLP

A responsive, dependency-free exam study website based on the nine supplied research-methodology files. Includes 930 MCQs, 295 illustrated glossary concepts and nine original module essays. Questions progress from easy recall through application to challenging distinctions. Each concept is revisited through multiple question facets; the question count does not imply 930 distinct theories.

## Run and publish

Open `index.html` directly, or serve this directory with `python -m http.server 8000`. No installation or build is needed. For GitHub Pages, upload all files to the repository root and select Deploy from a branch → main → / (root) in Settings → Pages. The included `.nojekyll` supports static serving.

## Study features

Nine module colors; light/dark themes; responsive mobile, tablet and desktop layouts; selectable 10/20/50/100 questions per page (short final page); instant answer and contextual explanation after selection; randomized option positions; smooth next/previous question and page navigation; deep links; glossary search; lecture essays with reader controls; bookmarks; wrong-answer revision; progress dashboard; progress backup export/import.

Progress is saved in this browser's local storage. It is not an account or cross-device sync. Export a backup before clearing browser data or moving devices. Research-course storage is separate from the older speech-language course. No student data is sent to a server.

## Content and sources

See `COVERAGE.md` and the website's Sources tab for the supplied-file map, supplementary references and clarifications. Original learning material supplements the handouts with established research-methodology concepts, SLP examples and explicit corrections where a handout simplifies a point. The clinical-change tutorial uses hypothetical data; examples must not be interpreted as treatment-efficacy evidence. Publisher samples and open primary guidance were used within their accessible scope; inaccessible textbook chapters were not claimed as reviewed.

All questions are original practice material, not official examination items. Coverage is mapped to supplied topics; supplementary methods coverage is not a guarantee of every possible examiner question. Provided slide decks and the copyrighted tutorial PDF are not redistributed.

## Files and maintenance

`data.json` / `data.js`: question bank, glossary and references. `essays.json` / `essays.js`: module essays. `app.js`: interface. `engine.js`: shared progress/pagination logic. `visuals.js`: inline vector illustrations. `styles.css`: responsive themes. Python authoring scripts are in `tools/`.

Run checks with Node.js:

```
node tests/check.js
node tests/interface.js
node --check app.js
```

Read `VALIDATION.md` for verification scope. No packages, CDN, tracking scripts or external fonts are required. Source links require internet access.
