# Space Pig:  A game made with Pygame Zero

## Objective
The aim of the game is simple – avoid the falling space debris.

## Technology
This game is written is Python 3, using Pygame Zero, a wrapper around Pygame, which itself is a wrapper around SDL (used for 2D window creation and to provide hardware support). I used Vectornator to design the graphics.

## To run
`pgzrun main.py`

## Build requirements
- pgzero
- pyinstaller

## Build instructions (macOS)
1. `pyinstaller --windowed --collect-all pgzero main.py`
2. Interrupt the previous command with CTRL+C as soon as a main.spec file is created. Edit the main.spec file so that it matches the one in this repo (if starting with just the source files and assets). The  most important part is the `datas` list on line 4. It should be `datas = [('images/*', 'images'), ('fonts/*', 'fonts'), ('music/*', 'music'), ('sounds/*', 'sounds')]`. The reason for this is explained [here](https://thecodingfun.com/2022/11/27/use-pyinstaller-to-create-executable-of-python-pgzero-game-windows-version/). The other change I made was to change the name from `main.app` to `Space Pig.app` in the `app = BUNDLE` section and to add an icon on the line below (`icon='space_pig_icon.icns'`). Alternatively, you can just use the spec file in this repo (which was created on macOS).
3. `pyinstaller --windowed --collect-all pgzero main.spec`

## Build instructions (Windows)
1. `pyinstaller --collect-all pgzero --onefile --windowed main.py`
2. Pretty much the same as step 2 for macOS. However, the spec file for Windows will look slightly different. The `app = BUNDLE` section will not exist, so you may want to change the name in the `exe = EXE` section instead. Also, if you would like an app icon, change the last line of the `exe = EXE` section to `entitlements_file=None, icon='space_pig_icon.ico'`.
3. `pyinstaller --collect-all pgzero --onefile --windowed main.spec`
