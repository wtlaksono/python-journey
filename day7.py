print("learn about:")

# install git using homebrew
print("git installation using homebrew => brew install git")

# git --version
print("check git version => git --version")

# setup user.name in git
print("git config --global user.name 'Wira Laksono' => Hey Git, for every project on this computer (global), please set my identity (user.name) to 'Wira Laksono' so I can sign my work.")

# setup user.email
print("git config --global user.email 'Wira.Laksono@gmail.com' => Hey Git, for every project on this computer (global), please set my email (user.email) to 'Wira.Laksono@gmail.com' so I can sign my work.")

print("=> the basic workflow of git: git status, git log --online, git add, git diff, git commit -m 'message', git push ")

# git init
print("git init => Hey Git, start a brand new, empty vault in this folder so you can begin tracking my changes.'Open a new vault'")

# git status
print("git status => Hey Git, start a brand new, empty vault in this folder so you can begin tracking my changes.")

# git diff
print("git diff => Hey Git, show me the exact line-by-line differences between the files I just edited and the last version I saved.")

# git add .
print("git add . => Hey Git, take all my current changes and put them into the 'waiting room' (stage them) so they are ready to be saved. 'Put my new work in the shipping box'")

# git commit -m 'initial save'
print ("git commit -m 'initial save' => Hey Git, take everything in the waiting room and save it as a permanent snapshot in the vault, and label it with the message 'initial save'. 'Seal the box and label it'")

# git log --oneline
print ("git log --oneline => Hey Git, show me my history of saved snapshots, but keep it brief—just one line per save point.")

# git push
print("git push => Hey Git, take all the snapshots I've saved in my local vault and push them up to the cloud(e.g. repo in github.com). 'Ship the box to that address'")

# opening a repo in github.com
print("=> opening a github.com account and create and empty repo named python-journey => https://github.com/your-username/python-journey")

# rename the branch name in git to main to match the branch name in github
print("git branch -M main => Hey Git, look at my current branch and forcibly rename (-M) it to main so it matches the standard on GitHub")

# to always rename the branch name in git for future project to main to match the branch name in github
print("git config --global init.defaultBranch main => Hey Git, from now on, whenever I start a brand new project on this computer, don't use the old 'master' name. Automatically name my very first chapter 'main' instead.")

# connect local main to the github repo
print("git remote add origin https://github.com/your-username/python-journey => Hey Git, I want to connect to a server on the internet (remote). Let's give it the nickname 'origin' and 'origin' is the specific address where it lives.")

# check the connection to github
print("git remote -v => Hey Git, show me my address book (verbose). I want to see the full URLs for the servers I'm pushing to and fetching from the github")

# git push -u origin main ( 1-time only)
print("git push -u origin main => Hey Git, take all the snapshots I've saved in my local vault and push them up to the repo cloud. Send them to the server I nicknamed 'origin' and put them in the branch called 'main' and remember (-u, for upstream) this specific path so that next time I can just say 'push' and you'll know exactly where to go")



