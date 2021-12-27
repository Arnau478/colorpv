import sys

class Color:
    def __init__(self, par_a=None, par_b=None, par_c=None):
        r = 0
        g = 0
        b = 0

        if(par_a != None and par_b == None and par_c == None):
            r = par_a
            g = par_a
            b = par_a
        elif(par_a != None and par_b != None and par_c != None):
            r = par_a
            g = par_b
            b = par_c

        self.r = r
        self.g = g
        self.b = b
    
    def hexFormat(self):
        return '#%02x%02x%02x' % (self.r, self.g, self.b)

def colorize(text, color: Color):
    return "\x1b[38;2;{};{};{}m{}\x1b[0m".format(color.r, color.g, color.b, text)

def invert(text):
    return "\x1b[7m{}\x1b[0m".format(text)

def generateRect(text, color, offset):
    offset *= 11
    return " "*offset + invert(colorize(" "*(len(text)+4), color))+"\n" + " "*offset + invert(colorize("  "+text+"  \n", color)) + " "*offset + invert(colorize(" "*(len(text)+4), color))

def generateColorPreview(color, offset):
    text = color.hexFormat()
    return generateRect(text, color, offset)

def parseColor(s):
    if(len(s) == 7 and s[0] == '#'):
        return Color(int(s[1:3], 16), int(s[3:5], 16), int(s[5:7], 16))
    if(len(s) == 6 and s[0] != '#'):
        return Color(int(s[0:2], 16), int(s[2:4], 16), int(s[4:6], 16))
    if(len(s) == 4 and s[0] == '#'):
        return Color(int(s[1:2]*2, 16), int(s[2:3]*2, 16), int(s[3:4]*2, 16))
    if(len(s) == 3 and s[0] != '#'):
        return Color(int(s[0:1]*2, 16), int(s[1:2]*2, 16), int(s[2:3]*2, 16))

    print("Invalid color: '{}'".format(s))
    exit(1)

def startsWithHyphen(s):
    return len(s) > 0 and s[0] == '-';

def anyElement(arr, con):
    for el in arr:
        if(con(el)):
            return True
    return False

if(len(sys.argv) == 1):
    print("Use -h for help")
    exit(1)
elif(len(sys.argv) >= 2 and anyElement(sys.argv[1:len(sys.argv)], startsWithHyphen)):
    if(len(sys.argv) == 2 and sys.argv[1] == '-h'):
        print(
            """
{yellow}═════════════════╗{reset}
     {blue}ColorPV{reset}     {yellow}║{reset}
   {faint}by Arnau478{reset}   {yellow}║{reset}
{yellow}═╦═══════════════╝{reset}
 {yellow}║{reset}
 {yellow}╟─{reset} A tool for previewing colors in hexadecimal format
 {yellow}║{reset}
 {yellow}╟──{reset} Try this:
 {yellow}║{reset}
 {yellow}║{reset}     colorpv "#c86400"
 {yellow}║{reset}
 {yellow}║{reset}     colorpv 0064c8
 {yellow}║{reset}
 {yellow}║{reset}     colorpv b47
 {yellow}║{reset}
 {yellow}║{reset}     colorpv "#835"
 {yellow}║{reset}
 {yellow}╚═══════════════{reset}
        """.format(
            yellow="\x1b[33m",
            reset="\x1b[0m",
            blue="\x1b[34m",
            faint="\x1b[2m"
        ))
    else:
        print("Use -h for help")
        exit(1)
elif(len(sys.argv) >= 2):
    args = sys.argv
    args.pop(0)
    args = args[::-1]
    colors = [0] * len(args)
    for i, arg in enumerate(args):
        colors[i] = parseColor(arg)
    print("\n\n\n" + "", end="")
    for i, arg in enumerate(args):
        color = colors[i]
        print("\x1B[3A" + "", end="")
        print(generateColorPreview(color, len(args)-i-1))