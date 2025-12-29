Here’s a cleaner, more professional reframing of your **README.md**, with clearer structure and wording while keeping it concise and Windows-friendly.

---

# ztools_win

A collection of lightweight Windows utility scripts designed to simplify common automation tasks.

## Prerequisites

Some tools rely on Python. Install the package manager `uv` if needed:

```bash
python -m pip install uv
```

## Project Structure

All tool launchers are located in the **`sword`** folder.

```
ztools_win/
└── sword/
    ├── click.bat
    └── delete_empty_folders.bat
```

## Available Tools

### `click.bat`

Automatically performs a click action when `image.png` or `image2.png` is detected on the screen.

**Use case:**
UI automation, repetitive clicking tasks, or simple workflow automation.

---

### `delete_empty_folders.bat`

Recursively deletes all empty folders under a specified path.

**Use case:**
Cleaning up directory structures after builds, extractions, or file migrations.

---

## Notes

* All scripts are intended for **Windows** environments.
* Run batch files with appropriate permissions.
* Modify paths or parameters inside the scripts as needed for your workflow.

---

If you want, I can also:

* Add usage examples for each `.bat` file
* Rewrite this in a more **minimal**, **enterprise**, or **open-source-friendly** style
* Convert it to bilingual (EN / 中文) README
