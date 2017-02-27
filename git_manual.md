# GitHub Installation. (window)
Download > https://git-scm.com/download/win

# GitHub Basic Command.
 ##CREATE AT LOCAL REPOSITORY DIRECTORY.##
 
    run on gitbash.cmd type > git init [my project] > enter
  
  (In [my project] must have **.git** folder)
 
 ##CLONE FORM EXTERNAL REPOSITORY DIRECTORY.##

    run on git.cmd type > git clone [repository] [directory] > enter
 
 ##BASIC CONFIGULATION##
 
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
          
##IGNORE FUNCTION##

use for ignore file before [add] and [commit].

1. create file name is [.gitignore]
2. edit in .gitignore Ex.
```
[file name].js    #ignore file specify type.
*jpeg             #ignore all .jpeg
```

##WORK FLOW##

[work tree]--git add command-->[index]--git commit command-->[repository]

##CHECK STATUS##

use for check status before commit and push to repository.
  goto [myproject] directory > run on git type > git status

status meaning

1. untracked (git add file1 file2 fileN) 
2. staged (git commit -m [comment message]) 
3. unmodified (edit file event)  
4. modified (git add file1 file2 fileN) (goto back 2.staged) 
5. (git commit -m [comment message]) (goto 3. unmodified again)
