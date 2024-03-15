# `beeptext`
!["Hey, how may I help you?"](https://github.com/HastagGuigui/beeptext/assets/47950669/7f932e05-655f-4412-a6b2-8b6bb0cdd990)


## what's this?
Beeptext is a python script (that can be executed as a command) that allows you to quickly make a Windows 95-style popup, with custom text and everything, and directly put it as a screenshot in your clipboard!

## what is this made for?
anyone that would feel like sparkling a little bit of `popup box`es into their messages, ~~or if you want to roleplay as a computer program~~. I made this out of boredom because the idea striked me, feel free to use it!

## how do i install?
Prerequisites: Python (anything still supported works, i personnally use 3.11)
- Clone the repo
- Install `pillow` using `pip`
- Copy `template.json` to `config.json`, and edit that config file.
- voilà! you can now use it with `python index.py` or on linux you can also use the `bt` batch script (that you can symlink into `/usr/bin/` or another folder on your PATH)

## how do I use?
run the program using `python index.py` (in the folder), but it supports a couple of parameters!

### Use icons
If you have the png file in `assets/icons/`, you can have a popup with the icon by typing `python index.py [iconname]`. There are about 70 icons sourced from the Atom Smasher Error Message Generator, obtained from [kirsle's errorgen](https://git.kirsle.net/apps/errorgen). (I honestly thought that website was a mandela effect.)

## how do I make a theme?
Here's a json example, with colors sourced from the default Windows 95 theme. 
```jsonc
{
    "metadata": { // This entire section is ignored by the script and is mostly meant for crediting.
        "title": "my very cool theme", // A font title.
        "creator": "meeee :3", // The author.
        "description": "beep boop" //
    },
    "background": "#d4d0c8", // Window background color
    "titlebar": {
        "backdrop": "#00aaaa", // Title background color
        "textcolor": "#ffffff" // Title text color.
    },
    "textcolor": "#000000", // The color of all text that's not the title
    "style": { // This section styles the borders around the "OK" button and the window.
        "highlight":"#ffffff",
        "shadow": "#646464",
        "outline": "#000000"
    }
}
```
To use it, simply use the `--theme:[theme]` option, or change the theme
## I have a suggestion...

feel free to open an issue! or, if you know python, make a pull request!

# Credits

Code by #Guigui (Guillaume G.)

inspired by (C) Atom Smasher.

The MIT license only applies to the codebase itself. Everything inside the assets folder belong to their respective owners.
`Windows Regular.ttf` is ["Windows"](https://loremipsum.ro/fonts/windows/) by [Levi Szekeres](https://loremipsum.ro/). Available as "free for personal use".
