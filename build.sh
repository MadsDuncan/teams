#!/bin/bash


clean_clutter() {
	rm teams.spec
	rm -rf __pycache__
	rm -rf build
}


rm -rf output
mkdir output


# Linux version
pyinstaller --onefile \
			--distpath output \
			--clean \
			teams.py

clean_clutter


# Windows version
PYINSTALLER_EXE=$(find ~/.wine -name "pyinstaller.exe")

wine "$PYINSTALLER_EXE"	--onefile \
						--distpath output \
						--clean \
						teams.py

clean_clutter
