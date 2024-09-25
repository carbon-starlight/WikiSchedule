# WikiSchedule
An open, free and easy to self-host Telegram bot for wiki-like class, homework and notes scheduling.

<div align="left">
<a>
  <img src="https://github.com/user-attachments/assets/c120f1d9-f505-479f-8a36-f253703f7ebd" width="320px">
</a>
<a>
  <img src="https://github.com/user-attachments/assets/fefab97e-58b7-4a68-9a9b-93bcbb947dcd" width="358px">
</a>
</div>

_Matrix support is in development_

Managing class schedlule may be repetative. A situation where 15-30 students manage their personal diaries and notebooks cooperating at most via a shared group chat is full of inconvinient, boring and repetative actions. I was not able to find a suitable solution for it, so I created WikiSchedule. It is a Telegram bot that takes the hastle of managing organizational and conspect papers and divides it into the amount of students in your class or group.

The main instance of the bot (hosted by me) is located at https://t.me/wikiscbot. https://t.me/wikischbot is my development (unstable) version running the latest commit.

## Operation
Enter `/help` to see the manual. 

`/cs` to create a schedule or `/lg` to join an existing timetable.

`/add` will allow you to add a lesson, homework or a note.

`/today` will show lessons for today

`/ls`, `/ls_h` and `/ls_n` will list lessons, homework or notes for the current week. Postpend with a number or a letter ([c]urrent/[n]ext) to specify the week.

## How to self-host
You will need a computer that will run 24/7 with active internet connection. You will not need a graphical enviroment or a window manager installed on it's operating system. A lightweight OS is recommended.

Possible options:

- [Fedora Server](https://fedoraproject.org/) *No version for IA-32 processors*
- [Debian](https://www.debian.org/) *Supports most architectures, but finding an option right for your machine on their website might be challenging*
- [Alpine Linux](https://www.alpinelinux.org/) *Lightest of them all, but dual-boot may be challenging and some users reported it being slow specifically for Python code*

If you have DE/VM installed you can exit GUI with `Ctrl+Alt+F2` (on some systems `Alt+Ctrl+F4`) to save some RAM. Turning it back may be accomprished with `Ctrl+Alt+F1`

After getting the system up and running you may disable GUI to save CPU and RAM resources with `sudo systemctl set-default multi-user.target`; `reboot` ([read article](https://www.cyberciti.biz/faq/switch-boot-target-to-text-gui-in-systemd-linux/)). Works with systemd-based OSes (Fedora, Debian, etc.). Doesn't work with Alpine, but it should come without intrusive GUI anyway.

If you connected to your server via SSH all the processes you see and launch in this console will get killed as soon as your connection is broken. You will need a process detacher or a terminal multiplexer so your launched processes won't get killed as soon as there is a `broken pipe` — `dtach`, `screen`, `tmux` or `byobu`. I recommend `byobu` to beginners. Install `byobu` with your OS's package manager and launch it. Press F9 to open it's TUI menu with a tutorial, `Esc` to go back, F6 to exit, enter `byobu` to get back to your terminal.

Install `git` to your operating system. 

[Navigate](https://andysbrainbook.readthedocs.io/en/latest/unix/Unix_01_Navigation.html) to the folder where you want this program to be stored. Clone this repo to your machine with the following command:  
`git clone carbon-starlight/WikiSchedule`

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

## Copying
AGPLv3 or any later version, as defined by the Free Software Foundation. Contact me for possible excetpions.

## Contributing
Just open a pull request and I will review it.

## Any CLA?
There are cases when there is a need to grant exceptions from GPL/AGPL _(the most famous one is a case with VLC that had to attach an exception to their license to qualify for AppStore publishing)_. I will assume that you preserve a right to grant exceptions from AGPL terms soulely by me _(note: after these exceptions the software will not become less Free by any definition, granting such exceptions is explicitly prohibited by AGPL, it may just drift into being more permissive, to the side where MIT and BSD lay)_. If you are a GPL purist and you do not want me to grant any exceptions from software with your code, mention it in your pull request, I will respect that wish.

## Contact me
There is a chance I will respond in Telegram: https://t.me/carbon_starlight. I have a bad habit of not checking inbox often, and not scrolling to see all the messages when I do, so if I do not see you message for some time and your inqury is kinda important, fell free to send new messages until I will see you and come up with some sort of response. I do not ghost anyone except for automatic spam accounts.

## Donate
It is my personal project where I pay for hosting out of my personal pocket, so, if you found my project useful or promising, donations will be really apperciated. I'm working on adding all dono info here: until that, please, contact me personally.
