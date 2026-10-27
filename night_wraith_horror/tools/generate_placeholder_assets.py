#!/usr/bin/env python3
import os
import struct
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BEHAVIOR_PACK = ROOT / 'behavior_pack'
RESOURCE_PACK = ROOT / 'resource_pack'


def write_png(path: Path, width: int, height: int, color_fn):
    raw = bytearray()
    for y in range(height):
        raw.append(0)
        for x in range(width):
            r, g, b, a = color_fn(x, y)
            raw.extend((r, g, b, a))
    def chunk(tag: bytes, data: bytes) -> bytes:
        return struct.pack('>I', len(data)) + tag + data + struct.pack('>I', zlib.crc32(tag + data) & 0xffffffff)
    ihdr = struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0)
    png = b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', ihdr) + chunk(b'IDAT', zlib.compress(bytes(raw), 9)) + chunk(b'IEND', b'')
    path.write_bytes(png)


def generate_pack_icon(path: Path):
    width = 256
    height = 256

    def color_fn(x, y):
        nx = x / (width - 1)
        ny = y / (height - 1)
        r = int(10 + 30 * (1 - ny))
        g = int(10 + 15 * (1 - nx))
        b = int(18 + 20 * (1 - ny))
        a = 255
        if x > 64 and x < 192 and y > 64 and y < 192:
            # dark red center glow
            r = 90
            g = 10
            b = 20
        # simple geometric N-ish silhouette
        if (x > 70 and x < 95 and y > 36 and y < 220) or (x > 160 and x < 185 and y > 36 and y < 220):
            r = 160
            g = 40
            b = 60
        if (x > 95 and x < 160 and y > 36 and y < 220 and abs((x - 128) / 55) < 1.1):
            r = 120
            g = 20
            b = 30
        return r, g, b, a

    write_png(path, width, height, color_fn)


def generate_wraith_texture(path: Path):
    width = 512
    height = 512

    def color_fn(x, y):
        dx = x - 256
        dy = y - 256
        dist = (dx * dx + dy * dy) ** 0.5
        r = 15 + int(min(80, dist * 0.1))
        g = 10 + int(min(40, dist * 0.05))
        b = 18 + int(min(55, dist * 0.08))
        a = 255
        # add bright eye glow
        if (x - 180) ** 2 + (y - 170) ** 2 < 120:
            r, g, b = 220, 200, 220
        if (x - 330) ** 2 + (y - 170) ** 2 < 120:
            r, g, b = 220, 200, 220
        if (x > 120 and x < 390 and y > 120 and y < 390):
            r = max(8, r - 10)
            g = max(8, g - 10)
            b = max(12, b - 8)
        return r, g, b, a

    write_png(path, width, height, color_fn)


def generate_wav(path: Path, frequency: int = 220, seconds: float = 1.0):
    sample_rate = 22050
    total_samples = int(sample_rate * seconds)
    import math
    with path.open('wb') as f:
        f.write(b'RIFF')
        f.write((36 + total_samples * 2).to_bytes(4, 'little', signed=False))
        f.write(b'WAVE')
        f.write(b'fmt ')
        f.write(struct.pack('<IHHIIHH', 16, 1, 1, sample_rate, sample_rate * 2, 2, 16, 0))
        f.write(b'data')
        f.write((total_samples * 2).to_bytes(4, 'little', signed=False))
        for i in range(total_samples):
            t = i / sample_rate
            amp = int(32767 * 0.15 * math.sin(2 * math.pi * frequency * t))
            f.write(struct.pack('<h', amp))


def main():
    (ROOT / 'behavior_pack').mkdir(parents=True, exist_ok=True)
    (ROOT / 'resource_pack').mkdir(parents=True, exist_ok=True)
    (ROOT / 'tools').mkdir(parents=True, exist_ok=True)

    generate_pack_icon(BEHAVIOR_PACK / 'pack_icon.png')
    generate_pack_icon(RESOURCE_PACK / 'pack_icon.png')
    generate_wraith_texture(RESOURCE_PACK / 'textures' / 'entity' / 'night_wraith.png')

    for p in [
        RESOURCE_PACK / 'sounds' / 'ambient',
        RESOURCE_PACK / 'sounds' / 'mob',
        RESOURCE_PACK / 'textures' / 'entity',
    ]:
        p.mkdir(parents=True, exist_ok=True)

    generate_wav(RESOURCE_PACK / 'sounds' / 'ambient' / 'creepy_wind_1.wav', 90, 1.8)
    generate_wav(RESOURCE_PACK / 'sounds' / 'ambient' / 'creepy_wind_2.wav', 140, 1.7)
    generate_wav(RESOURCE_PACK / 'sounds' / 'mob' / 'night_wraith_roar_1.wav', 180, 1.4)

    print('Generated placeholder assets successfully.')
    print(f'Behavior pack icon: {BEHAVIOR_PACK / "pack_icon.png"}')
    print(f'Resource pack icon: {RESOURCE_PACK / "pack_icon.png"}')
    print(f'Texture: {RESOURCE_PACK / "textures" / "entity" / "night_wraith.png"}')
    print(f'Sounds: {RESOURCE_PACK / "sounds"}')


if __name__ == '__main__':
    main()
