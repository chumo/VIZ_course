# Visualization Course Slides

This directory is a self-contained Quarto project for the course's Reveal
presentations. The editable sources are plain-text `.qmd`, CSS, SCSS, and small
data or script files. Generated HTML is not committed.

## Presentations

| Source | Published route |
| --- | --- |
| `VISUALIZATION/index.qmd` | `VISUALIZATION/` |
| `D3/index.qmd` | `D3/` |
| `PLOTLY/index.qmd` | `PLOTLY/` |

The project landing page is `index.qmd`. The explicit render list in
`_quarto.yml` prevents notebooks and other repository files from being executed
accidentally.

## Requirements

- [Quarto](https://quarto.org/docs/get-started/) 1.10.18
- [uv](https://docs.astral.sh/uv/) 0.12.1 or a compatible release

Python 3.13 and the build-time Python packages are declared in
`.python-version`, `pyproject.toml`, and `uv.lock`.

Quarto is a standalone application rather than a Python package. On macOS,
install it with Homebrew and confirm that it is available on `PATH`:

```bash
brew install --cask quarto
quarto --version
```

## Preview locally

Run these commands from the repository root:

```bash
uv sync --project SLIDES --frozen
QUARTO_PYTHON="$PWD/SLIDES/.venv/bin/python" quarto preview SLIDES
```

If another virtual environment is active, `uv` may warn that its
`VIRTUAL_ENV` does not match `SLIDES/.venv`. The warning is harmless because
`--project SLIDES` selects the correct environment. Run `deactivate` first if
you prefer to suppress it.

Create the complete static output without starting a preview server:

```bash
QUARTO_PYTHON="$PWD/SLIDES/.venv/bin/python" quarto render SLIDES
```

The output is written to `SLIDES/_site` and ignored by Git.

## Add a presentation

1. Create `SLIDES/TOPIC/index.qmd` with Reveal front matter.
2. Add `TOPIC/index.qmd` to the render list in `_quarto.yml`.
3. Add the presentation link to `index.qmd`.
4. Put shared assets in `assets/`; keep topic-specific assets beside the deck.
5. Render the complete project before committing.

Use level-one headings for sections and level-two headings for individual
slides. Keep speaker notes in `.notes` blocks. Prefer deterministic examples,
small local data files, and pinned browser dependencies.

Add Python packages with:

```bash
uv add --project SLIDES package-name
```

## Plot embedding

- D3 runs in the browser through Quarto Observable JS cells. Pin the D3 version
  in each example that introduces a runtime dependency.
- Plotly Python runs during the Quarto build. The generated figure remains
  interactive on the static site and does not need a Python server.
- Dash and other server-side applications cannot run on GitHub Pages. Link to
  their source or deploy them using a separate application host.

## Deployment

`.github/workflows/publish-slides.yml` renders and deploys the project whenever
changes reach `master`. It can also be run manually from GitHub Actions.

The repository owner must enable GitHub Pages once:

1. Open **Settings > Pages** in `chumo/VIZ_course`.
2. Set **Build and deployment > Source** to **GitHub Actions**.

After a successful deployment, the routes are:

- `https://chumo.github.io/VIZ_course/`
- `https://chumo.github.io/VIZ_course/VISUALIZATION/`
- `https://chumo.github.io/VIZ_course/D3/`
- `https://chumo.github.io/VIZ_course/PLOTLY/`
