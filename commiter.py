
# This is a bot to make any directory a git repo.
# you just need to run this code using python 3.10 + interpreter in your directory
# and input commit message and repo link. And that's it.
# Make changes and then just run this file.

import os
initializer = "git init"
add ="git add ."
msg = str(input("Commit message?\n"))
cmt = f"git commit -m {msg}"
k = 1
while True:
    os.system(f"{initializer}")
    os.system(f"{add}")
    os.system(f"{cmt}")
    yN = input("want to push (Y/N)?")
    yN.capitalize();
    if yN =='Y':
        if k==1:
            repolink = str(input("What link?\n"))
            os.system("git remote add newo {}".format(repolink)) 
            k=k+1
        os.system("git push -f newo main")
    else:
        pass
