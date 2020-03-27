bgougar/p1-start

Software dependencies:
If working on a Mac operating system, x11 forwarding is required to generate and view python plots. 
Link to tutorial on setting up x11 forwarding, made by Jenny Fothergill - https://youtu.be/bEyhUyolevU
You also need a python program to create your plots- download Anaconda-Navigator or Miniconda.

If working on another operating system on @coen-bascottie, to edit the code, you need a Boise State account, as well as the Cisco AnyConnect Secure Mobility Client to run the BSU VPN. Or if you're immune to Covid-19, break into an engineering computer lab at Boise State and use a university computer.

Github account and computer terminal required to pull the ssh key and run on your local device. 

To get the code - 
log onto github and navigate to https://github.com/bgougar/p1-start. Click on the green "Clone or download" key to create an SSH key, and copy it to your clipboard. In your local terminal, enter "git clone (ssh key)" at the command line to clone the p1-start/ repository onto your computer. 

To run the code- 
Navigate from your home directory to p1-start/ using the cd command. Enter "python plot.py" at the command line. A linear stress-strain should appear, titled with the appropriate file name, with with black dotted line overlaying that indicates the calculated Young's Modulus (slope). 

Working from a Mac, bash and git can be a pain- when running the code logged onto @coen-bascottie, the plots would not appear, hence why the x11 forwarding system was required. Additionally, I ended up having to work on a couple different computers due to lack of availability. Despite cloning my most current code from github onto the computer I was working on, I received some bash barf saying I still have to git pull some info from github in order to commit more updates. After I did this, one of my raw data files was corrupted and wouldn't run with the code, and an untracked file appeared in my computer's p1-start/. I solved this by deleting p1-start/ from my computer and recloning it from github, but any time I try to add something new to my local p1-start/ (like a folder for my saved plot) the same thing happens. UPDATE: turns out this was because the savefig(filename) command I was using was overwriting the files! The problem was fixed by changing this command to savefig(filename+".png"). Going through this process I thoroughly acquainted myself with git commands (clean -f, rm -rf, git pull, git add/commit/push, etc) and now feel much more comfortable working on my Mac's terminal! 


