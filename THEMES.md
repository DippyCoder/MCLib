# MCLib Themes

MCLib is also the community theme library for **MCPanel** (desktop) and
**MCPanel-WebUI**.

Just like addons, themes are listed with one small JSON file per theme
(`themes/<name>.json`), pointing at the theme's own GitHub or Codeberg
repository. [`tools/build_index.py`](tools/build_index.py) builds them into
[`themes-index.json`](themes-index.json) - a separate file from the addon
`index.json`. MCLib never hosts theme files - the apps download them straight
from the theme's **releases**.

The official themes live on [MCPanel's `themes` branch](https://github.com/DippyCoder/MCPanel/tree/themes).
Both apps read both catalogues and show them together; themes from MCLib are
marked *MCLib*.

> **Third-party software.** Themes listed here are made by their listed
> authors, not by the MCPanel or MCLib maintainers. Read the
> [Terms of Service](TOS.md) -
> section 6 covers themes.

---

## Installing a theme

1. Open MCPanel or MCPanel-WebUI → **Settings** → **Themes**
2. Click **Browse Online** and **Install** the theme you want
3. Click **Apply** next to it

The theme browser shows each MCLib theme's newest stable release and installs
its `.zip`. You can also download a `.zip` from a theme's releases yourself and
use **Import ZIP**. **Reset to Default** brings back the default look.

---

## Creating a theme

A theme is a folder with two files, plus any images or fonts its CSS uses:

```
my-theme/
├── theme.json   ← metadata
├── theme.css    ← CSS overrides
└── assets/…     ← optional, referenced with relative url(...)
```

### theme.json

```json
{
  "name": "My Theme",
  "creator": "YourName",
  "creatorUrl": "https://github.com/YourName",
  "version": "1.0.0",
  "appVersion": "2.4.0",
  "description": "A short description of your theme."
}
```

| Field | Required | Notes |
|-------|----------|-------|
| `name` | yes | Display name shown in MCPanel once installed |
| `creator` | yes | Your name or handle |
| `creatorUrl` | no | Clickable link next to your name |
| `version` | yes | Theme version, keep it equal to the release tag |
| `appVersion` | yes | MCPanel version this targets |
| `description` | no | Short description |

### theme.css

Override MCPanel's CSS custom properties — only the ones you want to change:

```css
:root {
  /* Backgrounds */
  --bg-base:      #0d0d0d;   /* app background */
  --bg-surface:   #141414;   /* panels, sidebar */
  --bg-elevated:  #1c1c1c;   /* inputs, buttons */
  --bg-card:      #16161680; /* server/profile cards */
  --bg-hover:     #222222;   /* hover state */

  /* Accent palette (maps to purple-* internally) */
  --purple-900: …;  /* darkest shade */
  /* … --purple-800 to --purple-200 … */
  --purple-100: …;  /* lightest shade */

  /* Shorthand accent tokens */
  --accent:       #60a5fa;
  --accent-glow:  rgba(96,165,250,0.25);
  --accent-dim:   rgba(96,165,250,0.10);

  /* Text */
  --text-primary:   #e2e8f0;
  --text-secondary: #94a3b8;
  --text-muted:     #475569;
  --text-accent:    #93c5fd;

  /* Borders */
  --border:       rgba(255,255,255,0.07);
  --border-focus: rgba(96,165,250,0.5);

  /* Shadows */
  --shadow-purple: 0 4px 24px rgba(96,165,250,0.15);
}
```

You can also target specific components directly — the
[official themes](https://github.com/DippyCoder/MCPanel/tree/themes) are good
examples.

**Rules** (from the Terms of Service): styling only — no scripts or HTML — and
nothing loaded from the internet. Every `url(...)` must point at a file inside
your `.zip` or be a `data:` URI.

---

## Publishing a release

Put the theme in a public **GitHub or Codeberg** repository and publish a
**release** for every version:

- The **release tag is the version** (e.g. `v1.0.0`).
- Attach the packed theme as a **`.zip` asset**. Pack it with:

  ```bash
  npm install archiver            # once
  node tools/pack-theme.js my-theme
  ```

  This writes `my-theme.zip` (with `theme.json` and `theme.css` at its root) to
  the current directory.

The apps install the newest release that isn't a pre-release.

---

## Adding a theme

**Open an issue** with the
[*Submit a theme*](https://github.com/DippyCoder/MCLib/issues/new?template=submit-theme.yml)
template - that's the only way to get listed. An entry looks like this
(`themes/<name>.json`, see [`theme.schema.json`](theme.schema.json)) -
it ends up in `themes-index.json`:

```json
{
  "name": "monotone",
  "description": "Greyscale dark theme in the style of Android dark mode.",
  "project": "https://github.com/DippyCoder/monotone",
  "authors": ["DippyCoder"]
}
```

| Field | Meaning |
|---|---|
| `name` | Unique. Must match the file name. |
| `description` | One or two sentences, max 300 characters. |
| `project` | `https://github.com/<owner>/<repo>` or `https://codeberg.org/<owner>/<repo>` — **no other platforms**. |
| `authors` | Who made it. |

New releases need no new submission. Report or appeal a theme with MCLib's
*Report* and *Appeal* templates.


---

## Maintaining

`python3 tools/build_index.py` validates `addons/*.json` **and**
`themes/*.json` and rebuilds both `index.json` and `themes-index.json`; CI runs
it with `--check`. See the [README](README.md#maintaining).
