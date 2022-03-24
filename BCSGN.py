#BCSGN, basic script to Generate a HTML file for basedcarz.club
#Created By Xyresh, Github: https://github.com/xyresh
#Provided under GPL V3, Do as you like with this.
from pathlib import Path

from matplotlib.pyplot import close

asciiart = """\n\n██████╗  █████╗ ███████╗███████╗██████╗  ██████╗ █████╗ ██████╗ ███████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗╚══███╔╝
██████╔╝███████║███████╗█████╗  ██║  ██║██║     ███████║██████╔╝  ███╔╝ 
██╔══██╗██╔══██║╚════██║██╔══╝  ██║  ██║██║     ██╔══██║██╔══██╗ ███╔╝  
██████╔╝██║  ██║███████║███████╗██████╔╝╚██████╗██║  ██║██║  ██║███████╗
╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═════╝  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝"""


Part1 = """<!DOCTYPE html>
<html>
<head>
<title>
BasedCarz</title>
<link rel="icon" href="../img/based.png">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="keywords" content="cars based
basedcarz">
<meta name="description" content="no soydev crap only based carz">
<link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <div style="text-align: center;">
        <br>
        <br>
        <div class="tops">
            <div>
              <img src="../img/based.png" width = "80px">
            </div>
            <div>
              <a href="../index.html" class="basedcar" >
                BASED CARZ
              </a>    
            </div>
          </div>
      </div>   
    </div>
<div></div>
<div></div>
<p>this is the anti Soydev site for based cars,</p>

<br>

<div style="text-align: center;">
    <!--Car name-->"""


Part2 = """<br>
    <br>
    <p style="display: inline-block; text-align: left; max-width: 600px; font-size: 12pt; line-height: 1.5;">"""

Part3 = """</p>
    <br>
    <br>
    <br>
    <h3>So what makes this car BASED??</h3>
    <!--What makes based-->"""

Part4 = """    <h3>Overall BASED!</h3>
</div>

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br><br>

<footer style="text-align: center;">
    <a href="../disclaimers.html">Disclaimers</a>
    <a href="../about.html">About</a>
</footer>

</body>
</html>
"""

def main():
    print(asciiart)
    print("basedcarz.club")
    maintext = open('main.txt', 'r').read()
    close('main.txt')
    CarName = input('\nEnter The name of The Car:  ')
    FileName = input('\nEnter a File Name for your contribution(ex. car.html): ')
    
    f = open(FileName, 'w')
    
    f.write(Part1)
    f.write("   <h2>"+CarName+"</h2><br>\n")
    
    Imagefile = input('\nEnter The Precise filename of your Image(Make sure The File is located within the img Folder):  ')
    
    f.write("""    <img src="../img/"""+Imagefile+"""" width = "50%" style="min-width: 300px;"> """)
    f.write(Part2)
    f.write("\n<br>\n")
    
    print("\nThe main text will be automatically added from the main.txt File,\n found within the same Directory")
    print("\n\n Your Text"+maintext+"\n\n")
    
    f.write(maintext)
    f.write(Part3)

    print("\nNow enter the reasons why Your car is Based\nEnd your reasons by typing(END)")
    reason = None
    numr = 1
    while(reason != "END"):
        reason = input("Reason {} : ".format(numr))
        if(reason != "END"):
            f.write("\n     <h5>>"+reason+"</h5>")
            numr += 1
    print("\nNow enter the reasons why Your car shoudln't be given a go")
    f.write("\n    <h3>So why not give it a go??</h3>")
    goreason = None
    numrr = 1
    while(goreason != "END"):
        goreason = input("Reason {} : ".format(numrr))
        if(goreason != "END"):
            f.write("\n     <p>"+goreason+"</p>")
            numrr += 1
    
    f.write(Part4)

    print("\n\nThank you For Creating a Contribution\n\nTo submit it, clone https://github.com/xyresh/basedcarz \ncopy the html file generated and push to it, make sure your image is within the img folder, make sure to request access as a contributor")

if __name__ == "__main__":
    main()
