# Night Wraith Horror Add-on

This repository contains a Bedrock Edition horror add-on structure for a creature named `Night Wraith`.

Important:
- This is not a Java mod.
- Bedrock uses resource packs + behavior packs, packed into a `.mcaddon` file.
- You must zip the `behavior_pack` and `resource_pack` directories together and rename the final archive to `.mcaddon`.

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
```

## Create the `.mcaddon`

On Windows PowerShell:

```powershell
Compress-Archive -Path .\night_wraith_horror\behavior_pack -DestinationPath .\bp.zip -Force
Compress-Archive -Path .\night_wraith_horror\resource_pack -DestinationPath .\rp.zip -Force
# then place both zipped packs into a parent folder and zip the parent folder
Rename-Item .\bp.zip .\behavior_pack.zip
Rename-Item .\rp.zip .\resource_pack.zip
```

Manual method:

1. Create a parent folder named `night_wraith_horror`
2. Put `behavior_pack` and `resource_pack` inside it
3. Zip the parent folder
4. Rename the final archive from `.zip` to `.mcaddon`

## In Minecraft

1. Open Bedrock Edition.
2. Import the `.mcaddon` file.
3. Enable both packs.
4. Use:
   - `/summon myaddon:night_wraith`

## Notes

- The repo contains the source structure and JSON logic.
- Binary asset files such as `.png` and `.ogg` must be added locally or created with GIMP / Krita / Audacity.
- The repo is intentionally source-oriented so you can customize the creature, textures, sounds, and animation behavior.

The goal is to make it feel like a dark horror creature that stalks the player, watches through windows, and feels threatening in low-light and cave environments.
