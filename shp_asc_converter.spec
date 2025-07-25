# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src\\app.py'],
    pathex=[],
    binaries=[],
    datas=[('./venv/Lib/site-packages/geopandas', 'geopandas'), ('./venv/Lib/site-packages/pyproj', 'pyproj'), ('./venv/Lib/site-packages/rasterio', 'rasterio'), ('data/standard_mesh.shx', 'data'), ('data/standard_mesh.shp', 'data'), ('data/standard_mesh.prj', 'data'), ('data/standard_mesh.dbf', 'data'), ('data/standard_mesh.cpg', 'data')],
    hiddenimports=['rasterio._shim', 'rasterio.sample'],
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
    [],
    exclude_binaries=True,
    name='shp_asc_converter',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='shp_asc_converter',
)
