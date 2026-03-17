# Getting started with environment variables and .env
This starter should help build routines that keep secrets and configurations out of your code. 

## What not to do
- Hardcoding secrets into code
- Committing .env or secrets to GitHub (see .gitignore and ensure .env is in there)
- Hardcoding configuration into code

## Environment Variables overview
Access environment variables through terminal 
- This will only remain for the life of your terminal session (runtime)
```bash
# Set an environment variable for this shell session
export API_KEY="123456"

# Read it back (note the $ is required)
echo $API_KEY
```
✅ Tip: export makes the variable available to child processes (like Python started from this shell). Without export, it remains a shell variable and won’t be inherited.  

Open Python
```bash
python #or python3
```
Then ... 
```python
import os
api_key = os.getenv("API_KEY")

# now set via python
os.environ["API_KEY"]="abcde"
print (os.getenv("API_KEY"))

# exit python ctrl-Z or
exit()
```
Now check in the shell
```bash
echo $API_KEY
# -> still 123456 (unchanged)
```
✅ Key concept: Changes to os.environ are local to the Python process and do not propagate back to the parent shell.


## Working with .env files

- local development with .env
- file structure -- include .env.example so configuration is transparent

Example .env
```
OBJ_STORE_URL=""
API_KEY=""
DB_USER=""
DB_PASSWORD=""
```
Hello dotenv
```python
from dotenv import load
```
Some additional topics to learn about
1. .env.local  -- local developement
2. .env.test -- automated test with isolated values
3. .env -- legacy or general configuration


# Where secrets should reside
- GitHub
- OpenShift
- 
