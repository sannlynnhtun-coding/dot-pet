"""Verify the bundled asset identity and PNG header without dependencies."""
import hashlib
import json
from pathlib import Path
import struct

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / 'pet.json').read_text(encoding='utf-8'))
asset = root / manifest['sprite']['path']
data = asset.read_bytes()
if data[:8] != b'\x89PNG\r\n\x1a\n' or data[12:16] != b'IHDR':
    raise SystemExit('FAIL: asset is not a PNG with an IHDR header')
width, height = struct.unpack('>II', data[16:24])
digest = hashlib.sha256(data).hexdigest()
if (width, height) != (manifest['sprite']['width'], manifest['sprite']['height']):
    raise SystemExit(f'FAIL: unexpected dimensions {width}x{height}')
if digest != manifest['sprite']['sha256']:
    raise SystemExit('FAIL: sprite SHA-256 differs from the manifest')
print(f'OK: {asset.name}, {width}x{height}, SHA-256 {digest}')
print('This verifies the published asset identity; it is not a replacement for Pets import validation.')
