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

-C = comment

-t = type
    
    run on git-bash.cmd type > ssh-keygen -t rsa -b 4096 -C <comment>
    
    and setting path output if skip [enter] it will be set default at [c:/Users/[username]/.ssh/id_rsa]
    
    then go to .ssh file > create file name > config > typing follow this below
    
    Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/github_rsa
    
    > save > and rename private key to "github_rsa" and public key "github_rsa.pub" [.pub is extension]
    > add public key in to github > copy content at file id_rsa.pub and put to ssh setting in github

test ssh connection

    run on git-bash.cmd type > ssh -T github.com > [enter] > type "yes"
    
    if show"Hi <gituser> You've successfully.." it's mean .. it's work!
 
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
     
     basic all commit
     
           run on git.cmd type > git commit -A -m "<comment>"
     
     commit specify type      
     
           run on git.cmd type > git commit -o [filename] -m "<comment>"
          
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
 
         **DIAGRAM**
           
           [c0]---->[c1]---->[c2]---->[c3]
           
           Ex. git revert c2
           
           [c0]---->[c1]---->[c2]---->[c3]---->[c4 revert from c2]
           
           run on git.cmd type > git revert <commit unique id (Ex.xxxxxx)> 
           
 7. reset command
 
         **DIAGRAM**
         
           [c0]---->[c1]---->[c2]---->[c3]
           
           Ex. git reset --hard c2
           
           [c0]---->[c1]---->[c2]
 
           run on git.cmd type > git reset --hard <commit unique id (Ex.xxxxxx)>

2. SYNC command

 1. check origin and master data
 
           run on git.cmd type > git config --list
 
 2. check global origin and master data
 
           run on git.cmd type > git config --global --list
 
 3. pull command
 
           run on git.cmd type > git pull origin master
 
 4. push command
 
           run on git.cmd type > git push origin master
 

### CHECK STATUS

use for check status before commit and push to repository.
  goto [myproject] directory > run on git type > git status

status meaning

1. untracked (git add file1 file2 fileN) 
2. staged (git commit -m [comment message]) 
3. unmodified (edit file event)  
4. modified (git add file1 file2 fileN) (goto back 2.staged) 
5. (git commit -m [comment message]) (goto 3. unmodified again)
