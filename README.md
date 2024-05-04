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

Install GitHub [CLI] to your operating system. 

[Navigate](https://andysbrainbook.readthedocs.io/en/latest/unix/Unix_01_Navigation.html) to the folder where you want this program to be stored. Clone this repo to your machine with the following command:  
`gh repo clone carbon-starlight/WikiSchedule`

If you already hosted WikiSchedule on a different computer and now are moving to a new machine and want to preserve the database, move your configuration/database files/cataloges to their locations. Since 2.0 these are the only database files _(I hope)_. Addition of `mediaArray` file or catalog/folder to this list is planned in the future.  

```
"config.json"
"masterfolders/getpage MASTERFOLDER/textbooks"
"masterfolders/wsbot MASTERFOLDER/interchange"
"masterfolders/wsbot MASTERFOLDER/forward_group-table_dictionary.json"
"masterfolders/wsbot MASTERFOLDER/lg_logs"
"masterfolders/wsbot MASTERFOLDER/mainArray"
"masterfolders/wsbot MASTERFOLDER/sg_toggle_logs"
"masterfolders/wsbot MASTERFOLDER/start_logs"
```

Navigate to project's folder. Launch cli.py to start the program.  
`python3 cli.py`

Follow the instructions.

If you encounter `error: externally-managed-environment` some solutions are listed here: https://stackoverflow.com/a/75696359

## License / Copying:
Under consideration.
