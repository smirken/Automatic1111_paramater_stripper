Really simple script.
It just read the PNG files in the current director, pops (removes) The 'parameters', and puts a copy in a "Parameters" directory

Feel free to give me hints etc, I'm a newb, but I'm going to try and be a helpful newb.

Note this version is very basic, but better than nothing, and does what I need today.

You might need to install pyhon dependancies, just run
$ pip install pillow

I've included a windows executable that you can just drop in your path.
It was created with the following if you want to make your own (you'll have to install pyinstaller and Pillow)

>pyinstaller.exe --onefile --hidden-import=Pillow -wcF .\PNG-view-rem-param.py

