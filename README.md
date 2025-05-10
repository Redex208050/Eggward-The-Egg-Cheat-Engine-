## Description
The purpose of this project is to reverse engineer Egg, a game available on the Steam platform.

## Tools/Languages
- Visual Studio Code
- DnSpy
- Python
- Unity Editor (Attempted to edit various assets, not used in final submission.)
- Cheat engine(to find where values were stored in memory, not used in final submission.)

## Game Modifications
- Cheat where you can win the game and get the achievment through one button press. This cheat works by assigning one click of the button equal to 1,000,000 instead of 1.
- Cheat that allows the user to trigger the Valentine's Day and St.Patrick's day events skins/backgrounds. The user interface will allow the user to mix and match the unlocked customizations. 

## Results
We used a technique called DLL swapping. DLL swapping consists of switching out DLLs using our Python program to achieve the desired result. There is an option to play the base game unmodified in EggWard.py. When you select the desired modification, the modified DLL will be swapped in in place of the original DLL. In the case of the instant win cheat, we modified the DLL with one that would change the EggClick function to add 1,000,000 (1m) to the value of the egg instead of 1. The result of this mod allows the user to view the win screen, as well as give the user an achievement. The background and skin assets were modified similarly. EggWard.py changes how the skin check is performed and always lets you use a limited-time skin.​
