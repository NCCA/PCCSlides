<link rel="stylesheet" href="../js/asciinema-player.css">
<script src="../js/asciinema-player.js"></script>

# Lab 1 Ibtroduction to Linux

# Aims

The aim of this lab is to introduce some basic Linux commands and tools
  1. The terminal and why it is important
  2. basic linux commands ls,pwd,mkdir,cd,rm,man,history.
  3. The environment and how to set it up


## Getting Started

The first thing we need to do is to get a terminal open.  On Linux this is usually done by pressing the `ctrl-alt-t` keys.  I actually have a default terminal open on login as I use it so much.

## The Terminal

I have a nice GUI with icons and menus, why do I need to use the terminal?  The answer is that the terminal is the most powerful tool you have on your computer.  It is the gateway to the operating system and allows you to do things that are not possible with a GUI.  It is also the most efficient way to do things.  If you want to copy a file from one place to another you can use the GUI, but it is much faster to use the terminal.  If you want to copy a file from one place to another on a remote machine you have to use the terminal and a tool called scp. While you can use a GUI to do this it is much more efficient to use the terminal as typically under linux this is setup by default and doesn't require any additional software.

When we open the terminal it runs a program called a shell.  The shell is a program that allows us to interact with the operating system.  There are many different shells available, but the most common is called [bash](https://www.gnu.org/software/bash/).  Bash is the default shell on most Linux distributions and is the shell we will be using. If you are using a Mac you may be familiar with  [zsh](https://www.zsh.org/) which is a more modern shell.  If you are using Windows you can install a Linux subsystem that will allow you to run bash or you can use [powershell](https://learn.microsoft.com/en-us/powershell/) which is a more modern shell for Windows however it is based on the .NET framework and is not compatible with bash.

The shell is a program that runs in the terminal and allows us to interact with the operating system.  It is a command line interface (CLI) and allows us to run programs and scripts.  

## Navigation

Most of the work we do is based on a filesystem and navigating it. There are a number of tools and commands that allow us to navigate the filesystem but first it is important to know a few concepts. 

It really helps to make a mental model of a filesystem and how it is organized.  The filesystem is a tree structure with a root at the top.  The root is the top level of the filesystem and is represented by a `/` character.  Under the root are a number of directories.  Directories are like folders on a Windows or Mac system.  They are used to organize files and other directories.  Directories can contain other directories and files.  Directories are separated by a `/` character.  For example the directory `home` is a directory under the root.  The directory `home` contains a number of other directories such as `jmacey` which is my home directory.  My home directory contains a number of other directories such as `Documents` and `Downloads`.  The directory `Documents` contains a number of other directories and files.  This is a typical structure of a filesystem.  It is a tree structure with a root at the top and directories and files below it.  The root is represented by a `/` character and directories are separated by a `/` character. 

## Home Directory

Each of you have a home directory, in your case it will be /home/[istudent number]. This is actually on a remote [NetApp](https://www.netapp.com/) server and will have some level of backup. As this is networked it is not that fast to access but is useful to store long term data.

You have full control of your home directory and can Read, Write and eXecute (RWX) files and directories within this area.

In linux we use ```~``` to represent the home directory.  For example if I want to list the contents of my home directory I can type

```bash
ls ~
```

As a shortcut we can always travel home by typing cd followed by enter or

```bash 
cd ~ 
```

<asciinema-player src="/jmacey/sfdcc/labs/lab1/cd.cast" cols=120 rows=10></asciinema-player>

In the example above we use the [```pwd```](https://man7.org/linux/man-pages/man1/pwd.1.html) command to show us where we are. ```pwd```  stands for "print working directory" and you will find this sort of acronym is very common in Linux / Unix. In fact ```cd``` stands for change directory.  

### quotas

You home directory is on a server the quota for the home directories is set at 100GB and if full, things will likely  stop working.  Use ```quota -s``` from a terminal to check or the more user friendly  output script ```/public/bin/2023/homequota```

<asciinema-player src="/jmacey/sfdcc/labs/lab1/quota.cast" cols=120 rows=10></asciinema-player>

{{% alert warning %}}
Using the file manager to delete files will not remove them from your home folder, it will move them into a recycle bin. This still counts to your quota. It is stored in the folder .local/share/Trash/files. You can delete this folder to free up space, or use the command ```gio trash --empty``` in the terminal.
{{% /alert %}} 


## push / popd

The build in  commands ```pushd``` and ```popd``` can be used to move around the filesystem.  ```pushd``` will change to a directory and save the current directory on a stack.  ```popd``` will change to the directory on the top of the stack.  This is useful if you want to move to a directory and then return to the previous directory.  The following examples show this in action.

<asciinema-player src="/jmacey/sfdcc/labs/lab1/pushd.cast" cols=120 rows=10></asciinema-player>


## Directories

We can use the ```mkdir``` command to create a directory.  For example to create a directory called ```LinuxTest``` we can type

```bash
mkdir LinuxTest
```

We can then use the ```ls``` command to list the contents of the current directory.  We can also use the ```ls``` command to list the contents of a directory other than the current directory.  For example to list the contents of the ```LinuxTest``` directory we can type

```bash
ls LinuxTest
```

This path is relative to the current directory.  We can also use an absolute path to list the contents of the ```LinuxTest``` directory.  An absolute path is a path that starts at the root of the filesystem.  For example to list the contents of the ```LinuxTest``` directory we can type

```bash
ls /home/jmacey/LinuxTest
```

<asciinema-player src="/jmacey/sfdcc/labs/lab1/mkdir.cast" cols=120 rows=10></asciinema-player>


To change into the LinuxTest directory we can use the ```cd``` command.  As we are in the root folder we can just type the name of the directory

```bash
cd LinuxTest
```

We can also use the command ```cd ~/LinuxTest``` to say change relative to root (~/). This can be useful when we are somewhere else and need to change.

<asciinema-player src="/jmacey/sfdcc/labs/lab1/cd2.cast" cols=120 rows=10></asciinema-player>

## The [```touch```](https://man7.org/linux/man-pages/man1/touch.1.html) command

The ```touch``` command is very useful in linux, it's main role is to Update the access and modification times of each FILE to the current time.

However if the file does not exist when passed on the command line an empty file will be created.

<asciinema-player src="/jmacey/sfdcc/labs/lab1/touch.cast" cols=120 rows=10></asciinema-player>

## the [```rm``` command](https://linux.die.net/man/1/rm)

The rm command is one of the most dangerous commands in the linux toolbox.  It is used to remove files and directories.  It is very easy to delete files and directories with this command and it is very difficult to get them back.  There is no recycle bin in linux terminal (there is in the file manager) so once it is gone it is gone.

The following example will remove the files we created in the previous example.

<asciinema-player src="/jmacey/sfdcc/labs/lab1/rm1.cast" cols=120 rows=10></asciinema-player>

You will note there is no prompt to delete, it just assumes you know what you are doing and does it! 

Luckily rm has a number of flags we can use to help avoid some of these issues. In particular we can set the ```-i``` flag for interactive usage as follows. 

<asciinema-player src="/jmacey/sfdcc/labs/lab1/rm2.cast" cols=120 rows=10></asciinema-player>


## Sessions

A linux session is a period of time where you are logged into the system.  When you login to a linux system you are given a session.  This session will last until you logout or the system is shutdown.  When you login to a linux system you are given a shell.  This shell is a program that allows you to interact with the operating system, typically on linux systems this is bash. We do also have the choice of adding other shells such as zsh.

When you open a terminal in the gui or via ssh you are also given a shell. 

You can see who is logged into the machine and how many sessions are running using the who command. 

<asciinema-player src="/jmacey/sfdcc/labs/lab1/who.cast" cols=120 rows=10></asciinema-player>

Typically when opening a terminal in linux we get a new session, and each session is unique. 

<asciinema-player src="/jmacey/sfdcc/labs/lab1/loginctl.cast" cols=120 rows=10></asciinema-player>


 This means that if we open a terminal and set a variable it will not be set in a different session.  This is because each session has its own environment.  The environment is a set of variables that are set when the session is created.  These variables are used by the shell and other programs to determine how they behave.  For example the PATH variable is used by the shell to determine where to look for programs.  If we type a command in the terminal the shell will look in the directories listed in the PATH variable for the program.  
 
 This can be useful for testing things and getting a fresh environment, however a lot of the time we want to make permanent setups for each time we login or create a new session. There are a number of system files that help to do this. 

 ## login files and resources

When we login to a system there are a number of files that can be read, these are called login files.  These files are read by the shell when we login and can be used to setup the environment.  There are a number of different files that are read depending on the shell and the type of session. For bash it works as follows. 

 ```/etc/profile``` (system wide) and ```~/.profile``` (user specific) are the first files that are read when you log in to a shell

```~/.bash_profile``` (user specific) is read when you log in to a bash shell ```~/.profile``` is read if ```~/.bash_profile``` does not exist.


```~/.bashr_login``` is read if ```~/.bash_profile``` does not exist.

Non login shells (like when you open a terminal window in a graphical interface) read only the ```~/.bashrc```

So where do I put things? If you want to set an environment variable (like PATH) you probably want to set it in ~/.profile or ~/.bash_profile. If you want to set aliases, you probably want to put them in ~/.bashrc.

There is also a ```.bash_logout``` file that is read when you logout of a shell.  This can be used to clean up the environment or do other things (I don't use this). 

## .bashrc and .profile

we are going to create two new empty files in the root of our home folder.

```bash
touch ~/.bashrc ~/.profile
code ~/.bashrc ~/.profile
```

This will open both files in [VisualStudio Code](https://code.visualstudio.com/) editor which is the main editor I use in the GUI. 

Now I'm going to add some text to each file, and we will do this over the next few weeks as we gradually setup our system, so remember when I say "open you .bashrc this is what we do"!

In the .profile add the following

```bash
if [ "$BASH" ]; then
    . ~/.bashrc
fi

```

This bash code checks if the $BASH environment variable is set and if it is, it sources the ~/.bashrc file. Sourcing a file means that the commands in the file are executed in the current shell environment. The purpose of this script is to ensure that the user's Bash configuration is loaded when running Bash scripts as a login shell.

In the ```.bashrc``` file we will add the following

```bash
source /etc/profile.d/prompt.sh
alias rm='rm -i'
alias ls='ls --color'
alias ll='ls -al'
``` 

The alias command allows us to create shortcuts for commands.  In this case we are creating aliases for the ```rm```, ```ls``` and ```ll``` commands.  The ```rm``` command will now prompt us before deleting a file.  The ```ls``` command will now show us the contents of a directory in color.  The ```ll``` command will show us the contents of a directory in long format.  

To make this work in the current environment we need to source the .bashrc file.  

<asciinema-player src="/jmacey/sfdcc/labs/lab1/alias.cast" cols=120 rows=10></asciinema-player>

we can now always override the default -i mode using the -f (force) flag. 


## History

Part of the power of the terminal is the ability to repeat commands.  This is done using the history.  The history is a list of commands that have been typed into the terminal.  We can use the history to repeat commands.  For example if we type

```bash
history
```

we will get a list of all the commands we have typed into the terminal.  Each command has a number associated with it.  

<asciinema-player src="/jmacey/sfdcc/labs/lab1/history.cast" cols=120 rows=10></asciinema-player>

We can use the ```!!``` shortcut to run the last command. ![letters] gives us the last command with the starting letters. 

## RTFM

Linux comes with a user manual built in, we use the man command to access this.

<asciinema-player src="/jmacey/sfdcc/labs/lab1/man.cast" cols=120 rows=30></asciinema-player>

We can page through the manual using the space bar and quit using the q key.  We can also search for text using the / key.  For example to search for the word "directory" we can type /directory

All man pages are formatted in a particular way, once you get used to them it is quite easy to read them. They also have different sections we can lookup in.

|Section	|Description|
|----|----|
|1|	General commands|
|2|	System calls|
|3|	Library functions, covering in particular the C standard library|
|4|	Special files (usually devices, those found in /dev) and drivers|
|5|	File formats and conventions|
|6|	Games and screensavers|
|7|	Miscellaneous|
|8|	System administration commands and daemons|

<asciinema-player src="/jmacey/sfdcc/labs/lab1/man2.cast" cols=120 rows=30></asciinema-player>

## Conclusions

This is a basic introduction to some of the simpler commands we use in linux we will look at more in the next session. Try not to be too intimidated by using the terminal / shell. It takes time and practice but once you have it you will find it is much more efficient than using a GUI. 

With the addition of some other tools and features we will look at we can make working in the shell very simple and pleasant. Hopefully by the end of this unit you will miss it when you use a Windows machine.

## Homework

Get used to using the man pages and look at what the command line options of the other commands do.

Practice making folders and files and navigating around the filesystem. Setup new folders on your home directory for each of the units you are doing (If you like to see them you can add them in the ~/Desktop folder) and they will appear on the desktop.


## References

https://man7.org/linux/man-pages/

{{<youtube yIuPu4iLcY4>}}

The following requires you to login with your university account 

https://www.linkedin.com/learning/learning-linux-command-line-14447912/learning-linux-command-line?u=57077769


