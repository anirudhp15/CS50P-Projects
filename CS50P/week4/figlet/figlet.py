import random
import sys
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    f = random.choice(fonts)
    figlet.setFont(font=f)
    s = input("Input: ")
    print(figlet.renderText(s))
elif len(sys.argv) == 3:
    if sys.argv[1] != '-f' and sys.argv[1] != '--font' or sys.argv[2] not in fonts:
        sys.exit("Invalid Usage")
    else:
        font_choice = sys.argv[2]
        figlet.setFont(font=font_choice)
        s = input("Input: ")
        print(figlet.renderText(s))
else:
    sys.exit("Invalid Usage")
