CursingSpock
============

A [SpockBot](https://github.com/SpockBotMC/SpockBot) plugin for controlling the client from the terminal. Built with [Curses](https://docs.python.org/3.5/library/curses.html).

![screenshot of a CursingSpock session](https://i.imgur.com/nHVMu4v.png)

Thanks to [gamingrobot](https://github.com/gamingrobot) for the [inspiration](https://github.com/SpockBotMC/SpockBot-Extra/blob/ea07c87b147d7c489c56046b6b8d72fd209d194b/plugins/curses_command.py).

Installation
------------

- Install the latest [SpockBot](https://github.com/SpockBotMC/SpockBot#installation)
- Install CursingSpock: `pip install CursingSpock` (or get the code and run `setup.py install`)
- Add these lines to your starting script ([example](https://github.com/SpockBotMC/SpockBot/blob/master/examples/basic/example.py)) in the right places:

```python
# probably at the very top
import cursingspock

# before initializing the Client
plugins.append(('curses', cursingspock.CursesPlugin))`
```

Note that this plugin does not implement any commands itself. Other plugins need to listen on `cmd_*` events and actually execute the command ([example](https://github.com/SpockBotMC/SpockBot-Extra/blob/master/plugins/base_commands.py)). The emitted events per command are:
```python
command, *args = 'somecommand arg1 arg2'.split(' ')
self.event.emit('cmd', {'cmd': command, 'args': args})
self.event.emit('cmd_%s' % command, {'args': args})
```

Usage
-----

Move the cursor with the `Left/Right` arrow and `Home/End` keys. When holding `Ctrl`, the cursor skips words.

Load a previously used command by using the `Up/Down` arrow keys.

Scroll the logs with the `PageUp/PageDown` keys.

While the client runs, any log messags are saved in `curses.log` and any commands you enter are saved in `curses.cmds`.
You can configure these file names by changing `cursingspock.log_path` and `cursingspock.cmd_path`.

---

Copyright (c) 2015 Gjum <code.gjum@gmail.com>

Licensed under the MIT License, see `LICENSE.txt`.
