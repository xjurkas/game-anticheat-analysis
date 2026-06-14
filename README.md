# Game Anti-Cheat Analysis

An educational cybersecurity project examining how modern game anti-cheat systems detect different cheating techniques. The repository contains three small Python prototypes, a written report, and a reference to recorded demonstrations.

The project was created for the **Principles of Information Security** course at the Faculty of Informatics and Information Technologies, Slovak University of Technology in Bratislava.

> [!CAUTION]
> This repository is intended exclusively for education, defensive security research, and testing in offline or explicitly authorized environments. Do not use the included scripts against online services, other players, or systems without permission. Doing so may violate laws, game terms of service, and platform rules.

## Project goals

The project explores the difference between two broad categories of game cheats:

- **Screen-based automation**, which observes pixels on the screen and simulates user input without directly accessing game memory.
- **Process-memory manipulation**, which attempts to write values directly into a running game process.

The accompanying report also discusses anti-cheat architectures, detection mechanisms, Cheat Engine, hardware-assisted cheats, and practical observations involving systems such as VAC, Easy Anti-Cheat, and Vanguard.

## Repository contents

```text
.
├── pib_detekovatelny.py
├── pib_nedetekovatelny_ctypes.py
├── pib_nedetekovatelny_pyautogui.py
├── pib_Jurkas_127776.pdf
├── pib_Videa.txt
└── README.md
```

| File | Description |
| --- | --- |
| `pib_nedetekovatelny_pyautogui.py` | Screen-based trigger prototype using Pillow, PyAutoGUI, and keyboard input |
| `pib_nedetekovatelny_ctypes.py` | Screen-based trigger prototype using the Windows API through `ctypes` |
| `pib_detekovatelny.py` | Process-memory write experiment using PyMem |
| `pib_Jurkas_127776.pdf` | Full project report in Slovak |
| `pib_Videa.txt` | Link to recorded project demonstrations |

## Implemented prototypes

### 1. Pixel-change trigger using PyAutoGUI

The script captures the screen, monitors the pixel in the center of the display, and simulates a left mouse click when the pixel color changes while the activation key is held.

Main characteristics:

- center-screen pixel monitoring,
- activation while holding the `X` key,
- randomized delay between 50 and 100 milliseconds,
- mouse input generated through PyAutoGUI,
- no direct access to game memory.

### 2. Pixel-change trigger using Windows API

This version uses the same visual detection principle but generates mouse input through the Windows API with `ctypes`.

Main characteristics:

- screen capture through Pillow,
- center-screen pixel comparison,
- activation while holding the `X` key,
- randomized click delay,
- Windows-specific mouse input generation.

### 3. Process-memory write experiment

The PyMem script demonstrates how a Python program can:

1. attach to a running Windows process,
2. accept a hexadecimal memory address,
3. write an integer value to that address.

The script does not contain game-specific offsets and is not a functional universal wallhack. It is a minimal experiment showing the difference between external visual automation and direct process-memory manipulation.

## Requirements

- Windows
- Python 3.10 or newer
- Permission to test the selected process or application
- An offline, private, or otherwise explicitly authorized test environment

Install the Python dependencies:

```bash
python -m pip install pillow pyautogui keyboard pymem
```

`tkinter`, `ctypes`, `time`, and `random` are part of the standard Python distribution. Some Python installations may require Tk support to be installed separately.

## Setup

Create and activate a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Install the dependencies:

```powershell
python -m pip install --upgrade pip
python -m pip install pillow pyautogui keyboard pymem
```

## Running the scripts

Run these scripts only in an offline or authorized test environment.

### PyAutoGUI prototype

```powershell
python pib_nedetekovatelny_pyautogui.py
```

Hold the `X` key to activate center-pixel monitoring.

### Windows API prototype

```powershell
python pib_nedetekovatelny_ctypes.py
```

Hold the `X` key to activate center-pixel monitoring.

### Process-memory experiment

```powershell
python pib_detekovatelny.py
```

The program asks for:

- the process executable name,
- a hexadecimal memory address,
- a new integer value.

Only use this script with a process that you own and are authorized to inspect.

## Technical overview

### Screen-based approach

The two trigger prototypes operate externally. They do not read game objects, entity lists, coordinates, or internal game state. Instead, they compare the current center pixel with a previously stored color.

Advantages:

- simple implementation,
- no game-specific memory offsets,
- no direct modification of the target process.

Limitations:

- visual effects can cause false triggers,
- screen capture introduces latency,
- color changes do not necessarily represent a valid target,
- behavior depends on resolution, crosshair placement, and rendering,
- anti-cheat or application input restrictions may still block generated input.

### Memory-based approach

The PyMem prototype directly accesses a process and attempts to write an integer to a selected memory address.

Advantages:

- demonstrates low-level interaction with a process,
- useful for understanding memory protection and anti-cheat monitoring.

Limitations:

- requires a valid process and address,
- addresses may change because of ASLR and application updates,
- incorrect writes can crash or corrupt the target process,
- modern anti-cheat systems may deny or detect access,
- no automatic offset discovery is implemented.

## Known issues

- The PyAutoGUI version calculates the center coordinates using division, producing floating-point values. Some Pillow versions require integer pixel coordinates. Replace:

```python
x, y = screen_width / 2, screen_height / 2
```

with:

```python
x, y = int(screen_width / 2), int(screen_height / 2)
```

- The scripts monitor only one pixel and therefore cannot reliably distinguish targets from particles, menus, lighting changes, or other visual effects.
- The `ctypes` implementation is Windows-specific.
- The `keyboard` package may require elevated permissions depending on the operating system and configuration.
- The memory-writing script intentionally contains no verified game-specific address or offset.

## Project observations

The report documents experiments involving:

- Counter-Strike 1.6,
- Valorant and Riot Vanguard,
- Deadlock and Valve Anti-Cheat,
- Rust and Easy Anti-Cheat,
- Cheat Engine in controlled testing.

The results are observations from a specific test environment and point in time. They should not be interpreted as a general statement about the current capabilities of any anti-cheat product.

## Documentation

The full Slovak-language report is available in:

[`pib_Jurkas_127776.pdf`](pib_Jurkas_127776.pdf)

Recorded demonstrations are referenced in:

[`pib_Videa.txt`](pib_Videa.txt)

## Responsible use

This project should be used to understand:

- how anti-cheat systems protect game integrity,
- why direct process manipulation is detectable,
- the limitations of visual automation,
- the ethical and technical boundaries of security testing.

Do not use the project to gain an unfair advantage, interfere with other users, bypass access controls, or evade security mechanisms in live environments.

## Author

**Dominik Jurkas**

Faculty of Informatics and Information Technologies  
Slovak University of Technology in Bratislava
