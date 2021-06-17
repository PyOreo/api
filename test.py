import os

os.system("cd E:\Datei-Management\Request_Litbot_RAW")

os.system("git init")
os.system("git add *")
os.system('git commit -m "init"')
os.system("git branch -M main")
os.system("git remote add origin https://github.com/PyOreo/api.git")
os.system("git push -u origin main")
os.system("git checkout -b gh-pages")
os.system("git push -u origin gh-pages")

