import subprocess
import webbrowser
import os
from Xlib import X, display, error, Xatom, Xutil
import Xlib.protocol.event


def sendEvent(win, ctype, data, mask=None):
    data = (data + [0] * (5 - len(data)))[:5]
    ev = Xlib.protocol.event.ClientMessage(window=win, client_type=ctype, data=(32, (data)))
    if not mask:
        mask = (X.SubstructureRedirectMask | X.SubstructureNotifyMask)
    root.send_event(ev, event_mask=mask)


# connect shadowsocks

display = Xlib.display.Display()
screen = display.screen()
root = screen.root

sendEvent(root, display.intern_atom("_NET_CURRENT_DESKTOP"), [0, X.CurrentTime])
display.flush()
webbrowser.open('https://duckduckgo.com/')

# switch to desktop 2
# open ide
sendEvent(root, display.intern_atom("_NET_CURRENT_DESKTOP"), [1, X.CurrentTime])
display.flush()
subprocess.call(["bash", "/opt/pycharm/bin/pycharm.sh"])
# subprocess.call(["bash", "/opt/phpstorm/bin/phpstorm.sh"])

# switch to desktop 3
# open terminal
sendEvent(root, display.intern_atom("_NET_CURRENT_DESKTOP"), [2, X.CurrentTime])
display.flush()
os.system("gnome-terminal -e 'bash -c \"cd ~/Code; exec bash\"'")

# switch to desktop 3
# open mysql-workbench
