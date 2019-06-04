chrome ="chrome.png"
youtube ="youtube.png"
fullscreen ="fullscreen.png"
favorties = "favorties.png"
artist = "Reiner and Bertholdt's Transformation Theme [HD] (OFFICIAL) - Attack on Titan S2"
album1 = "album1.png"
album2 = "album.png"
search = "search.png"
searchBut ="searchBut.png"
x = "x.png"
if exists(x):
    click(x)
doubleClick(chrome)
wait("1559663936719.png", 30*60)

if(exists(fullscreen)):
        click(fullscreen)
click(youtube)
wait("1559663381672.png", 30*60)

click(favorties)

wait("1559663462776.png", 30*60)
wait(.5)
if( exists(album1) or exists(album2)):
        click(album1)
        wait(10)
        click(x)
        
else:
        click(search)
        type(artist)
        click(searchBut)
        wait("1559663504878.png", 30*60)
        
        if( exists(album1)  or exists(album2) ):
            click(album2)
            wait(10)
            click(x)
click(x)
        
