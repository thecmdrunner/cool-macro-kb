# Macro KB

A dedicated macro keyboard, which runs on X11, Wayland and even TTY!

Inspiration: https://www.reddit.com/r/linux/comments/8geyru/diy_linux_macro_board/

# To add features

- [ ] Using Macrokb as Autohotkey + In

    - Macrokb will press complex macro shortcuts which will be picked up by the OS macro handler (KDE, Gnome, etc. have their own keyboard shortcut handling), which in turn will launch a bash or python script with functions inside them. This also helps mitigate security concerns over using a priviledged python script (macrokb) to do stuff in userland...



> Example: I press "F" on Macro kb -> ydotool/xdotool presses "Super + Shift + F" -> KDE handles that keyboard combination pressed and executes some action defined in the KDE settings menu (KDE shortcuts is actually very powerful!)

# Functions to add:
- [ ] Switch keyboard and mouse from VM to host
- [ ] Turn on a VM with GPU passthrough
- [ ] Switch to applications (Brave, Firefox, Code)
- [ ] Cycle between Tabs (Ctrl + Tab, Ctrl + Shift + tab)
- [ ] Screenshot this (full screen?) immediately
- [ ] Open certain urgent needed apps. [Audio recorder, OBS, terminal (with distrobox profiles?)]
- [ ] Maybe a frequently opened pdf or excel doc?
- [ ] Reload macrokb?


## Install dependencies


### Fedora:

```bash
sudo dnf install python3-evdev ydotool
```

## Run

## Why is **`sudo`** required?

- `ydotool`: See the [docs](https://github.com/ReimuNotMoe/ydotool)
- For the script: To use `evdev` for grabbing exclusive access to the Keyboard.

```bash
# Kill any other running instances of ydotoold (not sure if this is required, but for memory sake)
sudo killall ydotoold

# Start ydotoold and the python script simultaneously.
sudo ydotoold & sudo python3 macrokb.py
```