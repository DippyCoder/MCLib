#!/usr/bin/env python3
"""Validate addons/*.json and themes/*.json and build the two indexes:
index.json (addons — what MCPanel-CLI reads) and themes-index.json (themes —
what MCPanel and MCPanel-WebUI read).

    python3 tools/build_index.py           # validate + write both indexes
    python3 tools/build_index.py --check   # validate + fail if either is stale (CI)

Rules enforced here mirror TOS.md, so a pull request that breaks them fails CI
rather than relying on review alone. MCPanel-CLI enforces the platform rule
again at install time.
"""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ADDONS_DIR = os.path.join(ROOT, "addons")
INDEX = os.path.join(ROOT, "index.json")
THEMES_DIR = os.path.join(ROOT, "themes")
THEMES_INDEX = os.path.join(ROOT, "themes-index.json")

LIBRARY = {
    "name": "MCLib",
    "description": "The addon library for MCPanel-CLI, MCPanel and MCPanel-WebUI.",
    "homepage": "https://github.com/DippyCoder/MCLib",
    "tos": "https://github.com/DippyCoder/MCLib/blob/main/TOS.md",
    "issues": "https://github.com/DippyCoder/MCLib/issues",
}

FIELDS = {"name", "description", "project", "authors", "products"}
# Themes are entries without `products` — every theme is for MCPanel and MCPanel-WebUI.
THEME_FIELDS = FIELDS - {"products"}
PRODUCTS = {"cli", "mcpanel", "webui"}
NAME_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{0,63}$")
# Only GitHub and Codeberg — see TOS.md §3.
PROJECT_RE = re.compile(r"^https://(github\.com|codeberg\.org)/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")


def validate(path, data, fields=FIELDS):
    errors = []
    fname = os.path.basename(path)
    if not isinstance(data, dict):
        return [f"{fname}: must be a JSON object"]
    extra = set(data) - fields
    if extra:
        errors.append(f"{fname}: unknown field(s) {sorted(extra)}")
    for key in sorted(fields - set(data)):
        errors.append(f"{fname}: missing '{key}'")
    name = data.get("name")
    if not isinstance(name, str) or not NAME_RE.match(name):
        errors.append(f"{fname}: 'name' must match {NAME_RE.pattern}")
    elif fname != f"{name}.json":
        errors.append(f"{fname}: file must be named {name}.json")
    desc = data.get("description")
    if not isinstance(desc, str) or not desc.strip() or len(desc) > 300:
        errors.append(f"{fname}: 'description' must be 1-300 characters")
    project = data.get("project")
    if not isinstance(project, str) or not PROJECT_RE.match(project):
        errors.append(f"{fname}: 'project' must be a https://github.com/<owner>/<repo> or "
                      "https://codeberg.org/<owner>/<repo> URL (no other platforms are allowed)")
    authors = data.get("authors")
    if (not isinstance(authors, list) or not authors
            or not all(isinstance(a, str) and a.strip() for a in authors)):
        errors.append(f"{fname}: 'authors' must be a non-empty list of names")
    if "products" not in fields:
        return errors
    products = data.get("products")
    if (not isinstance(products, list) or not products or len(set(products)) != len(products)
            or not set(products) <= PRODUCTS):
        errors.append(f"{fname}: 'products' must be a non-empty list from {sorted(PRODUCTS)}")
    return errors


def build(directory, fields, key_name, description):
    entries, errors, seen = [], [], {}
    for fname in sorted(os.listdir(directory)):
        if not fname.endswith(".json"):
            continue
        path = os.path.join(directory, fname)
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except ValueError as e:
            errors.append(f"{fname}: invalid JSON ({e})")
            continue
        errs = validate(path, data, fields)
        if errs:
            errors += errs
            continue
        key = data["name"].lower()
        if key in seen:
            errors.append(f"{fname}: name '{data['name']}' is already used by {seen[key]}")
            continue
        seen[key] = fname
        entries.append({k: data[k] for k in ("name", "description", "project", "authors", "products")
                        if k in fields})
    entries.sort(key=lambda e: e["name"].lower())
    return {**LIBRARY, "description": description, "schema": 1, key_name: entries}, errors


# (entries directory, allowed fields, index file, list key, singular, description)
INDEXES = [
    (ADDONS_DIR, FIELDS, INDEX, "addons", "addon",
     "The addon library for MCPanel-CLI, MCPanel and MCPanel-WebUI."),
    (THEMES_DIR, THEME_FIELDS, THEMES_INDEX, "themes", "theme",
     "The community theme library for MCPanel and MCPanel-WebUI."),
]


def main(argv):
    status = 0
    for directory, fields, out, key, singular, description in INDEXES:
        index, errors = build(directory, fields, key, description)
        out_name = os.path.basename(out)
        if errors:
            print(f"Invalid {singular} entries:", file=sys.stderr)
            for e in errors:
                print("  - " + e, file=sys.stderr)
            status = 1
            continue
        text = json.dumps(index, indent=2, ensure_ascii=False) + "\n"
        count = f"{len(index[key])} {singular}(s)"
        if "--check" in argv:
            try:
                with open(out, "r", encoding="utf-8") as f:
                    current = f.read()
            except OSError:
                current = ""
            if current != text:
                print(f"{out_name} is out of date — run: python3 tools/build_index.py", file=sys.stderr)
                status = 1
            else:
                print(f"OK: {count}, {out_name} up to date")
            continue
        with open(out, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Wrote {out_name} with {count}")
    return status


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
