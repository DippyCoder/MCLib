# MCLib Terms of Service

Last change: 22nd October 2026

These terms apply to everyone who **lists an addon or a theme** in MCLib and
everyone who **installs an addon or a theme** through MCLib.

By submitting an addon or theme, or installing one, you agree to these terms.

---

## 1. What MCLib is

MCLib is an **index**. It contains a short description of each listed addon
and a link to the addon's own repository. MCLib does **not** host, build,
sign or distribute addon code: every install is downloaded directly
from the release published in the addon author's repository. The MCLib moderators
review your code **once** before listing it - only the release available at
that time is reviewed. Later releases are **not** reviewed **unless** the addon
gets reported or seems suspicious.

Themes are listed the same way, in MCLib's `themes-index.json` (see **6.
Themes**). MCPanel and MCPanel-WebUI read that file, together with the
official themes on MCPanel's own `themes` branch.
## 2. Third-party software

Every addon and every theme listed in MCLib is **third-party software**. It is written and
maintained by its listed authors, not by the creators of MCPanel, MCPanel-CLI,
MCPanel-WebUI or MCLib.

- Addons and themes are provided **"as is", without warranty of any kind**, express or
  implied, including fitness for a particular purpose.
- An addon runs inside MCPanel-CLI with **the same permissions as the user
  running it**. It can read, modify or delete anything that user can -
  including Minecraft servers, worlds, backups and the account database.
- **The creators and maintainers of MCPanel, MCPanel-CLI, MCPanel-WebUI and
  MCLib are not liable for any harm, damage, data loss, security incident or
  other consequence** arising from installing, updating or using an addon or
  theme, whether or not it is listed in MCLib.
- Being listed in MCLib is **not an endorsement** and is not a security audit.
- You install addons and themes **at your own risk**. Only install them from
  authors you trust.

MCPanel-CLI shows this disclaimer and requires you to accept it before it
downloads anything from an addon's repository.

## 3. Allowed platforms

**Only GitHub (`https://github.com`) and Codeberg (`https://codeberg.org`) are
allowed as platforms for addons listed in MCLib.**

- An addon's `project` must be a public repository on github.com or
  codeberg.org.
- Installable versions are taken **only from that repository's releases**.
  Each release must provide a `.zip` asset, or a source archive, containing
  the addon package (a folder with an `__init__.py`).
- Self-hosted Git servers, other forges, file hosters, package mirrors and
  direct download links are **not allowed** - not for the project, and not as
  a substitute for releases. Entries pointing anywhere else are rejected
  automatically, and MCPanel-CLI refuses to install from any other host.
- Loaders are not allowed. What is a **Loader**? - A loader is an addon which
  fetches the actual addon's code from third-party sources. Loaders are
  **strictly prohibited**.

## 4. Requirements for listed addons

An addon may be listed only if:

1. Its entry (`addons/<name>.json`) is accurate: name, description, project,
   authors and the MCPanel product(s) it is for.
2. Its source code is publicly readable in the linked repository, and the
   released archives are built from that code.
3. It contains **no malware**, no obfuscated or encrypted code, no hidden
   downloads of further code, and no credential, token or password harvesting.
4. It sends no data off the user's machine without clearly saying so in its
   README.
5. It uses the documented MCPanel-CLI addon API and does not tamper with
   MCPanel-CLI, other addons, or files outside its own data directory beyond
   what its description states.
6. It does not impersonate MCPanel, another addon or another author.

## 5. Submitting an addon

- **To get an addon listed**, open an issue in this repository which includes
  **the name, description, project (repository URL), authors and the MCPanel
  product(s) it is for**. A maintainer reviews it and adds the entry.
- You can **resubmit** your addon, if it fulfills all requirements (see **4. Requirements for listed addons**). If your
  addon contains malware on purpose, you're **no longer** allowed to (re)submit any addons.
- **To appeal** a rejected submission, a removal or a change to your addon's
  entry, open an issue with the *Appeal* template.
- **To report** a malicious, misleading or broken addon (for example, a release
  that cannot be installed), open an issue with proof.
- **To report bugs** in an addon's features, contact the addon's maintainer,
  NOT MCLib!

## 6. Themes

Themes are listed and reviewed like addons (sections 1, 3 and 5), with these
differences and additions:

1. A theme's `project` must be a public GitHub or Codeberg repository, and
   installs come **only from its releases**: each release must have a `.zip`
   asset containing a `theme.json` (accurate name, creator, version, targeted
   MCPanel version and description) and a `theme.css`. It may also contain the
   images and fonts its CSS uses. The **release tag is the theme's version**.
   Loaders and download links to anywhere else are not allowed.
2. A theme contains **only styling**: CSS and static assets. No scripts, no
   executables, no HTML.
3. A theme loads **nothing from the internet**. Every `url(...)` must point at a
   file inside the theme's own `.zip` (or be a `data:` URI). Remote fonts,
   images, trackers and `@import`s of remote stylesheets are not allowed.
4. You must have the right to distribute everything in the `.zip`.
5. A theme does not impersonate MCPanel, an official theme or another author,
   and does not hide or fake parts of the UI to mislead the user (for example,
   disguising buttons or hiding warnings).
6. **To get a theme listed**, open an issue with the *Submit a theme* template
   which includes the name, description, project (repository URL) and authors.
   A maintainer reviews the release available at that time and adds the entry.
   Like addons, later releases are not reviewed unless the theme is reported
   or seems suspicious.
7. Themes are reported and appealed the same way as addons (see **5.
   Submitting an addon**).

## 7. Removal

Maintainers may refuse, remove or delist any addon or theme at any time, in
particular when it violates these terms, its repository disappears or stops
publishing usable releases, or it is reported as harmful. Removing an entry
from MCLib does not uninstall the addon or theme from machines that already
have it; users can remove an addon with `mcpanel mclib mclib remove <name>`,
and a theme in **Settings → Themes**.

## 8. Changes to these terms

These terms may change. Changes are made through commits to this file; the
version in the repository's default branch is the one that applies.
