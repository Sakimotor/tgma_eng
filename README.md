# Tetris The Grand Master: Ace - English Patch

Patch for TGM: Ace that was made in an afternoon by using Ghidra and wxMEdit.

The `docs/` folder contains the game's promotional Flash website that, I modified with JPEXS and Adobe Flash CS6, [check it out](https://sakimotor.github.io/tgma_eng/)

## Installation


### The English Patch
To install the patch, you need to dump your game, find "default.xex" and apply the delta patch thanks to xdeltaGUI or Delta Patcher.

**NOTE:** In order to apply the patch to an updated version of the game, the original executable needs to have its update file applied. This can be done by extracting the `default.xexp` file from your dumped Title Update, then applying it to the original `default.xex` with the program [xextool](https://digiex.net/threads/xextool-6-3-download.9523/), and the following command:

```bash
xextool -o default_updated.xex -p default.xexp default_original.xex
```

### The Force Unlock (Xenia Canary only, pre-applied to the patch)
Xenia users who wish to keep the japanese text/don't want to alter their .xex file, while still making use of the **Force Unlock Patch** can download [my patch](https://github.com/Sakimotor/tgma_eng/blob/main/434107D2%20-%20Tetris%20The%20Grand%20Master%20Ace.patch.toml) (for the 1.0.3 version it's [this one](https://github.com/Sakimotor/tgma_eng/blob/main/434107D2%20v1.0.3%20-%20Tetris%20The%20Grand%20Master%20Ace.patch.toml) and put it in their `Xenia/patches` folder as indicated by [the official guide](https://github.com/xenia-canary/game-patches)



Xenia uses the .xex file's hashing to decide whether it should apply the .toml patch or not so please reach out to me if it doesn't work for you.

## Notes

As my Xbox 360 is a retail western console, I do not have the ability to play the game online. Therefore, all translations of the online features are untested.

Plus, **this patch only supports the 1.0 version of the game**, please reach out to me if you have a dump of the update (`Sakimotor#7923`)

## Screenshots

Updated Version:
![xenia_canary_FH0ILvM7ot](https://github.com/user-attachments/assets/e4b3fd42-efda-4067-a491-bf92735d89ef)


Original Patch:
![xenia_canary_eF7mTWgKax](https://github.com/user-attachments/assets/2130fd1e-1559-482e-b9b8-576a334bea77)
![xenia_canary_KLjHT7AAud](https://github.com/user-attachments/assets/bd418e6d-f1b0-4424-8695-54439664603a)
![xenia_canary_4o4ZqqO5r4](https://github.com/user-attachments/assets/52dee005-512f-4f67-96d8-d3ae254384d1)
![xenia_canary_VneuBa0iP1](https://github.com/user-attachments/assets/0bc7fcd7-5114-4e26-8e06-2288a1e86777)
![xenia_canary_puv6WMStsf](https://github.com/user-attachments/assets/c4c22e63-c3f9-4468-a22e-f29105e043e1) 
![xenia_canary_UEifuSrxtg](https://github.com/user-attachments/assets/c6a8a031-44b5-4ca9-8f48-d834e9aa7351)






![chrome_Gm8Io0QsOv](https://github.com/user-attachments/assets/58c6d2d9-0417-4bb2-aa58-a48732b21209) ![image](https://github.com/user-attachments/assets/e4d3cb7a-da9f-46b4-a6bc-0822abb3f48a)

