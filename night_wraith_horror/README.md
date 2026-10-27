# Night Wraith Horror Add-on

This repository contains a Bedrock Edition horror add-on template for a creature called `Night Wraith`.

Important:
- This is not a Java mod.
- Bedrock add-ons are built with `behavior_pack` + `resource_pack` and packaged into a `.mcaddon` archive.
- To be valid for Bedrock 1.20–1.26, the pack must have:
  - a valid `manifest.json` in each pack root
  - `pack_icon.png` in each pack root
  - `sound_definitions.json` in `resource_pack/sounds/`
  - all actual sound assets in `.ogg` format

## Folder structure

```text
night_wraith_horror/
  behavior_pack/
    manifest.json
    pack_icon.png
    entities/
      night_wraith.entity.json
  resource_pack/
    manifest.json
    pack_icon.png
    entity/
      night_wraith.entity.json
    models/
      entity/
        night_wraith.geo.json
    animations/
      night_wraith.animation.json
    animation_controllers/
      night_wraith.animation_controllers.json
    render_controllers/
      night_wraith.render_controllers.json
    sounds/
      sound_definitions.json
      ambient/
        creepy_wind_1.ogg
        creepy_wind_2.ogg
      mob/
        night_wraith_roar_1.ogg
    textures/
      entity/
        night_wraith.png
    texts/
      en_US.lang
    pack_icon.png
```

## Corrected issues in this repo

The earlier version had several common Bedrock add-on problems:
- missing `scripts.animate` in the client entity definition
- no automatic placeholder asset generation for `pack_icon.png` and texture/sound files
- no build helper script for creating the final `.mcaddon`
- doc instructions were too vague for a real Bedrock pack flow

This version fixes the core structure and adds a local placeholder generation workflow.

## Generate placeholder art + sound files

Run:

```bash
cd night_wraith_horror
python3 tools/generate_placeholder_assets.py
```

This script creates:
- `behavior_pack/pack_icon.png`
- `resource_pack/pack_icon.png`
- `resource_pack/textures/entity/night_wraith.png`
- `resource_pack/sounds/ambient/creepy_wind_1.wav`
- `resource_pack/sounds/ambient/creepy_wind_2.wav`
- `resource_pack/sounds/mob/night_wraith_roar_1.wav`

Then convert WAV → OGG with ffmpeg:

```bash
ffmpeg -i resource_pack/sounds/ambient/creepy_wind_1.wav -c:a libvorbis resource_pack/sounds/ambient/creepy_wind_1.ogg
ffmpeg -i resource_pack/sounds/ambient/creepy_wind_2.wav -c:a libvorbis resource_pack/sounds/ambient/creepy_wind_2.ogg
ffmpeg -i resource_pack/sounds/mob/night_wraith_roar_1.wav -c:a libvorbis resource_pack/sounds/mob/night_wraith_roar_1.ogg
```

## Build the Bedrock package

This repo includes direct packaging helpers.

### Linux/macOS

```bash
cd night_wraith_horror
./build_release.sh
```

### Windows

```powershell
cd night_wraith_horror
./build_release.ps1
```

The build script packages both `behavior_pack` and `resource_pack` into a final zip file that you rename to `.mcaddon`.

## Bedrock correctness checklist

- `manifest.json` exists at the root of each pack
- `pack_icon.png` exists in both the behavior and resource pack root
- `sound_definitions.json` exists in `resource_pack/sounds/`
- references in sound JSON omit file extensions
- entity IDs match between behavior and resource packs
- model/animation IDs match the resource pack references
- final audio files are `.ogg`

## Install in Minecraft

1. Rename the generated zip to `.mcaddon`
2. Open Bedrock Edition
3. Import the add-on
4. Enable both behavior + resource packs
5. Spawn the creature with:
   - `/summon myaddon:night_wraith`

## Notes

- This is a pack template, not a final commercial-grade asset pack.
- Replace generated placeholder art and audio with hand-made art and custom recordings for a better horror experience.
- Bedrock add-ons are folder-based; they are not Java mod jars.
