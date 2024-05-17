<link rel="stylesheet" href="../js/asciinema-player.css">
<script src="../js/asciinema-player.js"></script>

# Lab 2 More Linux

## Aims

The aim of this lab is to introduce more basic Linux commands and tools 


## Essential Linux Directories

Most linux environments have a similar directory structure.  The following is a list of the most important directories and their purpose.

| Directory | Purpose |
|-----------|---------|
| /bin      | Essential user command binaries (for use by all users) |
| /boot     | Static files of the boot loader |
| /dev      | Device files |
| /etc      | Host-specific system configuration |
| /home     | User home directories (optional) |
| /lib /lib64      | Essential shared libraries and kernel modules |
| /opt      | Add-on application software packages |
| /proc     | Virtual filesystem providing process and kernel information as files |
| /root     | Home directory for the root user (optional) |
| /sbin     | Essential system binaries |
| /srv      | Data directory for services provided by this system |
| /tmp      | Temporary files |
| /usr      | Secondary hierarchy |
| /var      | Variable data: files whose content is expected to continually change during normal operation of the system |

Many of these folders are read + execute only for normal users and for the most part we don't need to touch them. 

For our specific lab build most of the DCC tools we use (Maya,Houdini, Nuke,Renderman) are in the /opt folder.

<asciinema-player src="/jmacey/sfdcc/labs/lab2/opt.cast" cols=120 rows=10></asciinema-player>


## NCCA Specific folders

We have a number of NCCA specific folders on the system, some of these are network shares / mounts and some are local to the machine.  The following is a list of the most important folders.

### ```/transfer```

The ```/transfer``` folder is a mounted 1Tb local hard drive. This is shared with the windows partition and should be use for local work.

This is specific to the machine and is not shared with other machines directly (more later). 

This should be used as a destination for local renders and caches.  It should be considered "volatile" so any data you want to keep should be copied to a more permanent location (home directory)/

### ```/public``` 

The ```/public``` folder is a network share when various things for teaching and learning are stored, in particular I use the ```/public/devel/23-24``` folder to store programming and development resources. I will refer to this folder a lot in the classes.

````/public/bin/2023```` is the folder where all the goScripts are stored. These scripts set up the environments for the various DCC tools to run. We will look at these in more detail later.

<asciinema-player src="/jmacey/sfdcc/labs/lab2/bin.cast" cols=120 rows=10></asciinema-player>


## ```/net```

The ```/net``` folder is connected to the network filesystem [NFS](https://en.wikipedia.org/wiki/Network_File_System) via [autofs](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/storage_administration_guide/nfs-autofs) and will attempt to automount any network shares of the ```/transfer``` drives of any Linux machines. It only mounts a given share when that share is being accessed and these are unmounted after a defined period of inactivity. Automounting NFS shares in this way conserves bandwidth and offers better performance.

{{% alert warning %}}
Unfortunately for this to work the machine needs to be booted into linux, also there is no equivalent for windows machines.
{{% /alert %}}

To make this work we can use ```cd /net/[machine-name]``` this will then mount the ```[machine-name]/transfer``` folder for us to access as shown below.

<asciinema-player src="/jmacey/sfdcc/labs/lab2/net.cast" cols=120 rows=10></asciinema-player>


## Environment Variables

Environment variables are a set of dynamic named values that can affect the way running processes will behave on a computer. 

All operating systems have ways of setting environment variables and running processes can read these variables to determine how they should behave. For example the TEMP environment variable specifies the location in which programs place temporary files.

When you login to the Linux labs a number of environment variables are created for you, for example the location of Renderman is set using the variable RMANTREE. 

In bash we refer to environment variables using the $ symbol, so to see the value of RMANTREE we would type ```echo $RMANTREE```

<asciinema-player src="/jmacey/sfdcc/labs/lab2/env1.cast" cols=120 rows=10></asciinema-player>


{{% alert note %}}
Note that convention is to use upper case for environment variables. But this is not a hard and fast rule.
{{% /alert %}}

To show all of the environment variables currently set we can use the [```env```](https://www.shell-tips.com/bash/environment-variables/#gsc.tab=0) command.

<asciinema-player src="/jmacey/sfdcc/labs/lab2/env2.cast" cols=120 rows=10></asciinema-player>

As you can see there are a lot of variables here, we can look at individual ones using the printenv command. 

<asciinema-player src="/jmacey/sfdcc/labs/lab2/env3.cast" cols=120 rows=10></asciinema-player>

To show how environment variables are used the following [awk](https://www.gnu.org/software/gawk/manual/gawk.html) script reads the ENVIRON array and prints out the name and value of each variable.

```awk
awk 'BEGIN{for(v in ENVIRON) print v}'
```

I feed this into the more command via a pipe to print them out.

<asciinema-player src="/jmacey/sfdcc/labs/lab2/env4.cast" cols=120 rows=10></asciinema-player>

To set an environment variable we use the ```export``` command.  For example to set the variable ```PROJ_DIR``` to the value ```~/Proj``` we would type ```export PROJ_DIR=~/Proj```

<asciinema-player src="/jmacey/sfdcc/labs/lab2/env5.cast" cols=120 rows=10></asciinema-player>

When you set an environment variable in a session it is only valid for this session. If you want to make it more permanent you need to add it to your ```.profile``` file.  

### common environment variables

| Variable | Purpose |
|----------|---------|
| HOME | The home directory of the current user |
| PATH | A list of directories to search for commands |
| PWD | The current working directory |
| SHELL | The current shell |
| USER | The current user |
| DISPLAY | The current X display |
| EDITOR | The current editor |
| HOSTNAME | The current hostname |
| PS1 | The primary prompt string |
| PS2 | The secondary prompt string |
| TERM | The current terminal type |


## ```$PATH```

This environment variable is used to specify a set of directories where executable programs are located.  When you type a command into the shell it will search the directories in the ```$PATH``` variable for the command.  If it finds it then it will execute it, if not it will return an error.

We can add custom locations to this PATH within our own folders. It is typically best to add these to the ```.profile``` file in your home directory as this will be set once when you login.  

There are two approaches to adding to an existing environment variable, you can either append to the existing variable or prepend to it.  Prepending is typically the best approach as it will ensure that your custom locations are searched first.

The prepend approach is shown below. We  add our custom path to the start of the existing PATH variable.

```bash
export PATH=/my/custom/path:$PATH
```

The append approach is shown below. We add our custom path to the end of the existing PATH variable.
```bash
export PATH=$PATH:/my/custom/path
```

We are now going to add a local scripts folder to our path, to do this we add

```bash
export PATH:~/scripts:$PATH
```

to our ```.profile``` file.  As this is only read when we login, we can either logout and back in again or we can type ```source ~/.profile``` to read the file and update the environment variables.

## Test Scripts

First we will make a folder to put our scripts in. 

```bash
mkdir ~/scripts
cd ~/scripts
touch hello.sh
```

Using an editor we can all the following to the file

```bash
#!/bin/bash
echo "Hello World"
```

<asciinema-player src="/jmacey/sfdcc/labs/lab2/scripts.cast" cols=120 rows=10></asciinema-player>

By default the touch command will generate a file with the following file permissions

```bash
-rw-r--r-- 1 jmacey ncca 0 Sep  9 10:44 hello.sh
```

This means that the file is read/write for the owner (jmacey) and read only for everyone else.  To make the file executable we need to use the chmod command.

```bash
chmod +x hello.sh
```

This will change the permissions to

```bash
-rwxr-xr-x 1 jmacey ncca 0 Sep  9 10:44 hello.sh
```

making it executable. We can now run the script by typing ```./hello.sh```

## Unix file permissions

Unix file permissions are a way to control who can read, write and execute a file.  There are three types of permissions for each file, these are read, write and execute.  These permissions are set for three groups of users, the owner, the group and everyone else.  The permissions are shown as a series of 10 characters, the first character is the file type, the next three are the permissions for the owner, the next three are the permissions for the group and the final three are the permissions for everyone else.

<asciinema-player src="/jmacey/sfdcc/labs/lab2/permissions.cast" cols=120 rows=10></asciinema-player>

## [````chmod```](https://en.wikipedia.org/wiki/Chmod)

```chmod``` has two main modes of usage, either the octal mode as shown in the table below or the symbolic mode.  

|	Sum|	rwx	|Permission|
|-------|-------|-----------|
|7|	4(r) + 2(w) + 1(x)	|rwx	read, write and execute|
|6|	4(r) + 2(w)	rw-	|read and write
|5|	4(r)        + 1(x)	r-x	|read and execute
|4|	4(r)	r--	|read only
|3|	       2(w) + 1(x)	-wx	|write and execute
|2|	       2(w)	-w-	|write only
|1|	              1(x)	--x	|execute only
|0|	0	--- |	none

octal mode takes an octal triple for the user, group and world permissions, for example 

```
chmod 755 hello.sh
```

will set the permissions to rwxr-xr-x which is typical for a script used by members of a group where the owner is the only one who can write to the file.

The symbolic mode uses a series of letters to set the permissions, for example

```
chmod u+x hello.sh
```

will add the execute permission to the owner of the file.  The following table shows the various letters and their meanings.

|Letter|	Meaning|  
|------|---------|
|w|	user/owner|
|g|	group|
|o|	other|
|a|	all|
|+|	add|
|-|	remove|
|=|	set|
|r|	read|
|w|	write|
|x|	execute|


## [```#!```](https://en.wikipedia.org/wiki/Shebang_(Unix))

The hashbang or shebang is the first two characters of a script file.  It is used to tell the shell what program to use to run the script.  For example if we want to run a python script we would use

```python
#!/usr/bin/env python
```

In this case we are using the env command to find the python executable.  This is useful as it will find the first python executable in the PATH variable.  This means that we can use different versions of python by changing the PATH variable (we will look at this later when we install pyenv in the next lab).

## Homework

create a simple python script in your scripts folder that prints out hello world. You can use the #!/usr/bin/env python to run the program. 



## References

