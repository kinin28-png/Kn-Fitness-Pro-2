# -*- mode: python ; coding: utf-8 -*-
# Windows PyInstaller specification file for Kn Fitness Pro 2

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('kn_fitness_pro.png', '.'),
        ('kn_fitness_pro.ico', '.'),
        ('workout.py', '.'),
        ('exercise_videos.py', '.'),
    ],
    hiddenimports=['PySide6.QtCore', 'PySide6.QtGui', 'PySide6.QtWidgets'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Kn Fitness Pro',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='kn_fitness_pro.ico',
)

