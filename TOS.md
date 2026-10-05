# MCLib Terms of Service

Last change: 6th October 2026

These terms apply to everyone who **lists an addon** in MCLib and everyone who
**installs an addon** through MCLib.

By submitting an addon or installing one, you agree to these terms.

---

## 1. What MCLib is

MCLib is an **index**. It contains a short description of each listed addon
and a link to the addon's own repository. MCLib does **not** host, build,
sign or distribute addon code: every install is downloaded directly
from the release published in the addon author's repository. The MCLib moderators
review your code **once** before listing it - only the release available at
that time is reviewed. Later releases are **not** reviewed **unless** the addon
gets reported or seems suspicious.

## 2. Third-party software

Every addon listed in MCLib is **third-party software**. It is written and
maintained by its listed authors, not by the creators of MCPanel, MCPanel-CLI,
MCPanel-WebUI or MCLib.

- Addons are provided **"as is", without warranty of any kind**, express or
  implied, including fitness for a particular purpose.
- An addon runs inside MCPanel-CLI with **the same permissions as the user
  running it**. It can read, modify or delete anything that user can -
  including Minecraft servers, worlds, backups and the account database.
- **The creators and maintainers of MCPanel, MCPanel-CLI, MCPanel-WebUI and
  MCLib are not liable for any harm, damage, data loss, security incident or
  other consequence** arising from installing, updating or using an addon,
  whether or not it is listed in MCLib.
- Being listed in MCLib is **not an endorsement** and is not a security audit.
- You install addons **at your own risk**. Only install addons from authors you
  trust.

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

## 6. Removal

Maintainers may refuse, remove or delist any addon at any time, in particular
when it violates these terms, its repository disappears or stops publishing
usable releases, or it is reported as harmful. Removing an entry from MCLib
does not uninstall the addon from machines that already have it; users can do
that with `mcpanel mclib mclib remove <name>`.

## 7. Changes to these terms

These terms may change. Changes are made through commits to this file; the
version in the repository's default branch is the one that applies.
