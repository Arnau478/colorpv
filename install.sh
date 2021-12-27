DEST="/usr/local/bin/colorpv"

if [ "$EUID" -ne 0 ]
    then echo "Please run as root"
    exit
fi

echo "ColorPV installer"
echo ""

echo "Installing..."

cp ./colorpv.py "$DEST"
chmod +x "$DEST"

echo ""
echo "Checking installation..." 
if test -f "$DEST"; then
    echo ""
    echo "DONE!"
else
    echo ""
    echo "An error ocurred"
    echo "Couldn't install colorpv"
fi