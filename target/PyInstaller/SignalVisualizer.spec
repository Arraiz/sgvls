# -*- mode: python -*-

block_cipher = None


a = Analysis(['/Users/mikeldiez/PycharmProjects/SignalVisualizer/src/main/python/main.py'],
             pathex=['/Users/mikeldiez/PycharmProjects/SignalVisualizer/target/PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='SignalVisualizer',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , icon='/Users/mikeldiez/PycharmProjects/SignalVisualizer/target/Icon.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='SignalVisualizer')
app = BUNDLE(coll,
             name='SignalVisualizer.app',
             icon='/Users/mikeldiez/PycharmProjects/SignalVisualizer/target/Icon.icns',
             bundle_identifier='arraiz.com')
