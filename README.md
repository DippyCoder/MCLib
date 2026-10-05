# MCLib

The addon library for **MCPanel-CLI**, **MCPanel** (desktop) and **MCPanel-WebUI**.

MCLib is an index: one small JSON file per addon, pointing at the addon's own
GitHub or Codeberg repository. MCLib never hosts addon code — MCPanel-CLI
downloads it straight from the addon's **releases**.

> **Third-party software.** Addons are written by their listed authors, not by
> the MCPanel or MCLib maintainers. The creators of MCPanel and MCLib are not
> liable for any harm an addon causes. Read the [Terms of Service](TOS.md).

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

## Maintaining

```bash
python3 tools/build_index.py          # validate addons/*.json and rebuild index.json
python3 tools/build_index.py --check  # what CI runs
```

The validator enforces the terms that can be checked mechanically — required
fields, the name/file match, unique names and the GitHub/Codeberg-only rule.

## Layout

```
MCLib/
├── addons/<name>.json   ← one entry per addon (the source of truth)
├── index.json           ← generated; what MCPanel-CLI and index.html read
├── index.html           ← the browser
├── addon.schema.json    ← JSON Schema for an entry
├── TOS.md               ← terms of service
├── tools/build_index.py ← validator + index builder
└── .github/             ← issue templates (submit / appeal / report) and CI
```
