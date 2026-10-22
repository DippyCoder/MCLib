# MCLib

The addon and theme library for **MCPanel-CLI**, **MCPanel** (desktop) and **MCPanel-WebUI**.

>**Note:** MCLib and all MCPanel related repositorys will be at [MCPanel-Studios](https://github.com/MCPanel-Studios) soon!

MCLib is an index: one small JSON file per addon, pointing at the addon's own
GitHub or Codeberg repository. MCLib never hosts addon code — MCPanel-CLI
downloads it straight from the addon's **releases**.

MCLib lists **community themes** for MCPanel and MCPanel-WebUI the same way,
in a separate [`themes-index.json`](themes-index.json) — see [Themes](#themes).

> **Third-party software.** Addons and themes are written by their listed authors, not by
> the MCPanel or MCLib maintainers. The creators of MCPanel and MCLib are not
> liable for any harm an addon or theme causes. Read the [Terms of Service](TOS.md).

## Browsing

Open [`index.html`](index.html) (or the repository's GitHub Pages site). It
lists every addon with its description, authors, project link and which MCPanel
product it's for, can filter by product, shows each addon's releases, and gives
you the install command. From the terminal:

```bash
mcpanel mclib mclib list            # every addon in MCLib
mcpanel mclib mclib list accounts   # one addon's releases
```

## Installing

```
mcpanel mclib <library|repo-url> <list|install|update|downgrade|remove> [name] [version]
mclib         <library|repo-url> <list|install|update|downgrade|remove> [name] [version]
```

`mclib` on its own is a shorthand for `mcpanel mclib`, and `/mclib` (or just
`mclib`) works inside the interactive TUI (`mcpanel cli`).

```bash
mclib mclib install accounts            # newest stable release
mclib mclib install accounts v1.1.0     # a specific release (its tag)
mclib mclib update accounts             # to the newest release
mclib mclib update                      # everything installed from MCLib
mclib mclib downgrade accounts          # to the release before the installed one
mclib mclib downgrade accounts v1.0.0   # to a specific older release
mclib mclib remove accounts

# A repository URL skips the library and the name:
mclib https://github.com/owner/repo list
mclib https://codeberg.org/owner/repo install v2.0.0
```

Before anything is downloaded from an addon's repository you're shown the
third-party disclaimer and asked to accept it. Pass `-y`/`--yes` to accept it
up front (required in scripts). In JSON mode (`mcpanel api mclib …`) an
unaccepted install returns `{"error": …, "code": "disclaimer_required",
"disclaimer": …, "tos": …}` so an app can show it and retry with `--yes`.

Every addon — whichever product it's for — is installed into **MCPanel-CLI's
addons directory** and runs inside the CLI. Addons for MCPanel / MCPanel-WebUI
can also ship UI scripts and styles (new pages, new server tabs, changes to
existing ones, styled by the user's theme) that those apps load from the CLI —
see the [addon API](https://github.com/DippyCoder/MCPanel-CLI/blob/main/ADDONS.md).
Reload the app/WebUI after installing one.

Both apps also have this browser built in: the **Addons** page lists the
libraries, installs/updates/downgrades/removes addons (showing the disclaimer
first), and manages installed ones.

## More libraries

MCLib is just the default. Anyone can publish a library with the same
[`index.json`](index.json) format; users add it to
`<MCPanel data dir>/addons/libraries.json`:

```json
{
  "libraries": {
    "mclib":  { "url": "https://raw.githubusercontent.com/DippyCoder/MCLib/main/index.json",
                "description": "The official MCPanel addon library" },
    "mylib":  { "url": "https://example.org/my-library/index.json",
                "description": "Someone else's library" }
  }
}
```

…and then `mclib mylib list`. Whatever the library, MCPanel-CLI only installs
addons from GitHub or Codeberg releases.

## Adding an addon

**Open an issue** with the *Submit an addon* template — that's the only way to
get listed. An entry looks like this (`addons/<name>.json`, see
[`addon.schema.json`](addon.schema.json)):

```json
{
  "name": "accounts",
  "description": "User accounts, roles and permissions (SQLite-backed).",
  "project": "https://github.com/DippyCoder/MCPanel-Accounts",
  "authors": ["DippyCoder"],
  "products": ["cli", "webui"]
}
```

| Field | Meaning |
|---|---|
| `name` | Unique; what users type in `mclib mclib install <name>`. Must match the file name. |
| `description` | One or two sentences, max 300 characters. |
| `project` | `https://github.com/<owner>/<repo>` or `https://codeberg.org/<owner>/<repo>` — **no other platforms**. |
| `authors` | Who wrote it. |
| `products` | Which MCPanel product(s) it's for: `cli`, `mcpanel`, `webui`. |

The repository needs at least one **release** whose `.zip` asset (or source
archive) contains the addon package — a folder with an `__init__.py` that
follows the [MCPanel-CLI addon API](https://github.com/DippyCoder/MCPanel-CLI/blob/main/ADDONS.md).
Every published tag becomes an installable version.

**Appeals** (a rejected submission, a removal, a changed entry) are also made
by opening an issue, with the *Appeal* template. Malicious or broken addons are
reported with *Report an addon*.

## Themes

Themes change how MCPanel and MCPanel-WebUI look. They're listed exactly like
addons: one `themes/<name>.json` per theme, pointing at the theme's own GitHub
or Codeberg repository, built into [`themes-index.json`](themes-index.json)
(addons stay in `index.json`). MCLib never
hosts theme files — the apps install the `.zip` attached to the theme's newest
stable **release**, and the release tag is the theme's version.

Both apps read two theme catalogues and show them together in **Settings →
Themes → Browse Online**:

| Source | Where | What's there |
|---|---|---|
| MCPanel | [`DippyCoder/MCPanel@themes`](https://github.com/DippyCoder/MCPanel/tree/themes) | The official themes |
| MCLib | [`themes-index.json`](themes-index.json) on `main` | Community themes (marked *MCLib*) |

A theme is a folder with a `theme.json` (metadata) and a `theme.css` (CSS
overrides), zipped. The format, the CSS variables, the pack script and the
entry format are documented in [`THEMES.md`](THEMES.md).

```json
{
  "name": "monotone",
  "description": "Greyscale dark theme in the style of Android dark mode.",
  "project": "https://github.com/DippyCoder/monotone",
  "authors": ["DippyCoder"]
}
```

**To get a theme listed, open an issue** with the *Submit a theme* template. A
maintainer reviews it and adds the entry. New releases need no new submission.
Themes are reported and appealed with the *Report* and *Appeal* templates, like
addons.

## Maintaining

```bash
python3 tools/build_index.py          # validate addons/ + themes/, rebuild index.json + themes-index.json
python3 tools/build_index.py --check  # what CI runs
```

The validator enforces the terms that can be checked mechanically — required
fields, the name/file match, unique names and the GitHub/Codeberg-only rule —
for addons and themes alike.

## Layout

```
MCLib/
├── addons/<name>.json   ← one entry per addon (the source of truth)
├── index.json           ← generated; what MCPanel-CLI and index.html read
├── themes/<name>.json   ← one entry per theme (the source of truth)
├── themes-index.json    ← generated; what MCPanel and MCPanel-WebUI read
├── index.html           ← the browser
├── addon.schema.json    ← JSON Schema for an addon entry
├── theme.schema.json    ← JSON Schema for a theme entry
├── TOS.md               ← terms of service
├── THEMES.md            ← making, releasing and submitting themes
├── tools/build_index.py ← validator + builder for both indexes
├── tools/pack-theme.js  ← zips a theme folder for a release
└── .github/             ← issue templates (submit addon / submit theme / appeal / report) and CI
```
