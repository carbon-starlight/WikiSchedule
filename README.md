# WikiSchedule
 An open, free and easy to self-host Telegram bot for wiki-like class, homework and notes scheduling.

-----
### ⚠ This document is under development
-----

## How to self-host:
You will need a computer that will run 24/7 with active internet connection. You will not need a graphical enviroment or a window manager installed on it's operating system. A lightweight OS is recommended.

Possible options:

- [Debian](https://www.debian.org/) *Finding an option right for your machine on their website might be challenging*
- [Fedora Server](https://fedoraproject.org/)
- [Alpine Linux](https://www.alpinelinux.org/) *Lightest of them all, but dual-boot may be challenging and some users reported it being slow specifically for Python code*

If you have DE/VM installed you can exit GUI with `Ctrl+Alt+F2` (on some systems `Alt+Ctrl+F4`) to save some RAM. Turning it back may be accomprished with `Ctrl+Alt+F1`

Install GitHub to your operating system. 

Clone this repo to your machine with the following command:  
`gh repo clone carbon-starlight/WikiSchedule`

If you already hosted WikiSchedule on a different computer and now are moving to a new machine and want to preserve the database, move your `config.json` and `mainArray.json` files to their locations. Since 2.0 they are the only database files _(I hope)_. Addition of `mediaArray` file or catalog/folder to this list is planned in the future.  

Navigate to project's folder. Launch cli.py to start the program.  
`python3 cli.py`

Follow the instructions.

## License / Copying:
Under consideration.
