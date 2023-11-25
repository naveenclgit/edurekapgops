from pyfiglet import Figlet
from cs50 import get_string
import sys
import random

figlet = Figlet()
figfont = figlet.getFonts()

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(figfont))
elif len(sys.argv) > 1:
    if sys.argv[1] not in ['-f','--font'] or sys.argv[2] not in figfont:
        print ('Invalid Usage')
        sys.exit(1)
    else:
        figlet.setFont(font=sys.argv[2])
        greeting = get_string("Input: ").strip()
        print ("Output:", figlet.renderText(greeting))




