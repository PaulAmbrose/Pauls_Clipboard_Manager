#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage:
#        python3 /home/pi/pi2_admin_tools/mcb.pyw instructions save <keyword> - Saves clipboard to keyword.
#        python3 /home/pi/pi2_admin_tools/mcb.pyw instructions <keyword> - Loads keyword to clipboard.
#        python3 /home/pi/pi2_admin_tools/mcb.pyw instructions list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 2 and sys.argv[1].lower() =='instructions':
    print ("python3 /home/pi/pi2_admin_tools/mcb.pyw instructions save <keyword> - Saves clipboard to keyword.\n" + "python3 /home/pi/pi2_admin_tools/mcb.pyw instructions <keyword> - Loads keyword to clipboard.\n" + "python3 /home/pi/pi2_admin_tools/mcb.pyw instructions list - Loads all keywords to clipboard.")

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
# List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])


mcbShelf.close()
