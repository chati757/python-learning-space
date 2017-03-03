# GitHub Installation. (window)
Download > https://git-scm.com/download/win

# GitHub Basic Command.

### CREATE AT LOCAL REPOSITORY DIRECTORY.
 
    run on gitbash.cmd type > git init [my project] > enter
  
  (In [my project] must have **.git** folder)
 
### CLONE FORM EXTERNAL REPOSITORY DIRECTORY.

    run on git.cmd type > git clone [repository] [directory] > enter
    
### SSH SETTING 

-b 4096 = create key length 4096 character.

-c = comment

-t = type
    
    run on git-bash.cmd type > ssh-keygen -t rsa -b 4096 -c <comment>

In [home directory]/.ssh have to be 2 files github_rsa and github_rsa.pub
then create new textfile name is [config] for ssh and type follow..

```
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/github_rsa 
```
next..open file github_rsa.pub and copy all content and put content in the github/setting/ssh keys/add ssh key..

and test connection with..

    ssh -T git@github.com

 
### BASIC CONFIGULATION
 
 1. SET USERNAME 
  1. GLOBAL TYPE:use config all repository in pc
  
          run on git type > git config --global user.name [username]
  2. SYSTEM TYPE:use config specify repository
  
          goto [myproject] directory > run on git type > git config user.name [username]
 2. SET EMAIL
  1. GLOBAL TYPE:use config all repository in pc
  
          run on git type > git config --global user.email [email]
  2. SYSTEM TYPE:use config specify repository
  
          goto [myproject] directory > run on git type > git config user.email [email]
          
### IGNORE FUNCTION

use for ignore file before [add] and [commit].

1. create file name is [.gitignore]
2. edit in .gitignore Ex.
```
[file name].js    #ignore file specify type.
*jpeg             #ignore all .jpeg
```

### WORK FLOW

**[work tree (local)] --git add command--> [index(local)] --git commit command--> [repository(local)]**

1. LOCAL command
 1. add command
 2. commit command
 3. log command (for view commit history)
 
           run on git.cmd type > git log
 4. remove command
 5. check out command (back to old commit) (read only operation) (commit = version)
     
     **DIAGRAM**
     ```
     [head pointer c2]
     [master branch c2]
     [c0]<------[c1]<------[c2] *lastcommit
     
     Ex.git.cmd type > git checkout head~2
     
     [head pointer c0]
     [master branch c2]
     [c0]<------[c1]<------[c2] *lastcommit
     
     and then git.cmd type > git commit
     
     [head pointer c3]
     [sub branch c3]
     [master branch c2]
     *c3 have been created new branch form c0
     
     [branch c3]
     [c3]------>[c0]<------[c1]<------[c2]
     
     and then git.cmd type > git checkout master
     
     [head pointer c2]
     [sub branch c3]
     [master branch c2]
     [c3]------>[c0]<------[c1]<------[c2]
     
     if git.cmd type > git checkout head~2 test.js
     
     [head pointer c2]
     [master branch c2]
     [worktree pointer c0]
     [c0]<------[c1]<------[c2]
     
     in case git.cmd type > git commit
     
     [master branch c3]
     [worktree pointer c3] *continue c2 [be careful!]
     [c0]<------[c1]<------[c2]<------[c3]
     ```
     
     for each commit
 
           run on git.cmd type > git checkout <commit unique id (Ex.xxxxxx)>
           
     last commit
           
           run on git.cmd type > git checkout head
           
     x commit before head (x=number of commit before head)
     
           run on git.cmd type > git checkout head~x
           
     specify files for commit
     
           run on git.cmd type > git checkout <commit unique id (Ex.xxxxxx)> <filename Ex.test.js>
     
 6. revert command (edit old commit)
 7. reset command

2. SYNC command
 1. put command
 2. pull command

### CHECK STATUS

use for check status before commit and push to repository.
  goto [myproject] directory > run on git type > git status

status meaning

1. untracked (git add file1 file2 fileN) 
2. staged (git commit -m [comment message]) 
3. unmodified (edit file event)  
4. modified (git add file1 file2 fileN) (goto back 2.staged) 
5. (git commit -m [comment message]) (goto 3. unmodified again)