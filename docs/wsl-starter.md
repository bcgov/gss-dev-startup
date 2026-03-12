# Getting started with wsl (windows subsystem for linux)
Microsoft links  
[WSL troubleshooting](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting)  
[WSL install](https://learn.microsoft.com/en-us/windows/wsl/install)

## TLDR basic install
Open Powershell as admin
```
wsl --install
```

Once installed you can start it by searching for Ubuntu in windows search
- when you run it the first time you will need to make a username and password

Update your linux system -- update finds and prepares updates -- upgrade applies the update  

In your linux bash prompt
``` bash
sudo apt update
sudo apt upgrade
```

## Getting Python ready for venv
install venv
``` bash
sudo apt install python3-venv
```

## Working with a virtual environments
Make a project directory and make a venv
``` bash
mkdir project/myproject     # create directory
cd project/myproject
python3 -m venv venv        # create virtual environment named venv
source venv/bin/activate    # activate venv
```

Adding python packages to your virtual environment with pip
``` bash
python -m pip3 install geopandas   # install geopandas

```
Export the environment dependencies
``` bash
pip3 freeze > requirements.txt  # export dependencies to requirements.txt
```
Installing dependencies from file
```
python -m pip3 install -r requirements.txt
```

## Some basic useful linux commands
### WSL Specific
```
code .                      # open vscode in current directory
code projects/myproject/.   # open vscode in projects/myproject directory
explorer.exe .              # open file explorer in current directory
```

### Navigation
```
pwd          # Show current directory
ls           # List files
ls -la       # List all files with details
cd /path/to/dir
cd ..        # Up one directory
cd ~         # Home directory

```
### File and directory management
```
mkdir mydirectory
mkdir -p parent/child/grandchild

touch myfile.txt
cp source.txt destination.txt
mv oldname.txt newname.txt
rm myfile.txt
rm -r mydirectory   # Remove directory recursively (use with caution)

```
### Viewing and editing
```
cat file.txt
less file.txt
head file.txt
tail file.txt
tail -f /var/log/syslog   # Follow a log file
nano file.txt             # Simple text editor
```

### System package management

```

sudo apt update
sudo apt upgrade
sudo apt install <package>
sudo apt remove <package>

```


