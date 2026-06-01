# DocBook Diploma Thesis — LaTeX

LaTeX version of your thesis (same chapter structure as your friend's: 1–7 + References + Appendix).

## Requirements (install once)

1. **MiKTeX** or **TeX Live**: https://miktex.org/download (Windows)
2. **XeLaTeX** (included with MiKTeX)

## UCD figure (Section 2.2.1)

Copy the UCD diagram from your friend's Word file:

1. Right-click the image in Word → **Save as picture** → `ucd-principles.png`
2. Put it in folder: `thesis-latex/figures/ucd-principles.png`

## Compile

Open terminal in `thesis-latex` folder:

```bash
cd thesis-latex
xelatex main.tex
xelatex main.tex
```

Run **twice** so table of contents and references update.

**Output:** `main.pdf`

### VS Code (optional)

Install extension **LaTeX Workshop**. Open `main.tex` → Build with recipe **xelatex**.

## Edit your details

In `settings.tex`:

- `\thesisnumber` — your thesis number
- `\thesissupervisor` — supervisor name

In `frontmatter.tex`:

- `[SUBMISSION_DATE]`

## Add more content

Full text is in `../DIPLOMA_THESIS.md`. Copy sections into `chapters/ch04-design.tex` etc. as you expand.

## Page count (~66 pages)

- Add screenshots: `\includegraphics[width=\textwidth]{figures/home-page}`
- Add appendices from markdown
- Content from `DIPLOMA_THESIS.md` can be pasted into chapter `.tex` files

## Faculty formatting

| Rule | LaTeX setting |
|------|----------------|
| Times New Roman 12pt | `\setmainfont{Times New Roman}` |
| 1.5 spacing | `\onehalfspacing` |
| Arial headings | `\sffamily` in `titlesec` |
| Margins 40/25/35/25 mm | `geometry` in `settings.tex` |
| Page number bottom center | `fancyfoot[C]` |

## Why XeLaTeX?

Uses real **Times New Roman** and **Arial** fonts installed on Windows (required by Pécs guidelines). Do not use pdfLaTeX unless you change fonts.
