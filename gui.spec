#!/usr/bin/env python3
# -*- mode: python ; coding: utf-8 -*-

import sys
from pathlib import Path
from PyInstaller.building.api import PYZ, EXE, COLLECT
from PyInstaller.building.build_main import Analysis
from PyInstaller.building.datastruct import Tree
from PyInstaller.utils.hooks import collect_all

# Paths
block_cipher = None

# Analysis
a = Analysis(
    ['gui.py'],
    pathex=[str(Path.cwd())],
    binaries=[],
    datas=[
        ('templates', 'templates'),
        ('data', 'data'),
    ],
    hiddenimports=['weasyprint', 'flask', 'tkinter'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# Create PYZ
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# Create EXE
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='gui',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

app = BUNDLE(exe,
             name='gui.app',
             icon=None,
             bundle_identifier=None)
