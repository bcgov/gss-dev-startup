#  🚀 GSS Dev Startup Materials
Quick guide for getting started with some basic dev tools common in creating geospatial analysis and automation workflows

## Part 1 [wsl starter](/docs/wsl-starter.md) 
Install WSL  
Python setup in WSL  
Virtual environments (venv)  
Basic Linux concepts (as needed), VS Code  
Basic Git startup workflows (feature branches, commits, PRs)  

## Part 2 [uv starter](/docs/uv-starter.md)  

Astral-UV (environment and package management)  
Installation  
Creating projects and virtual environments  
Working with others  
Running using uv  


## Part 3 [.env starter](/docs/env-starter.md)
What not to do  
Environment variables overview  
Terminal and Python dotenv  

## Part 4 Debug'n with VSCode
Debugging with VSCode  
UI, breakpoints, stepping, watchlist  
Debug console  
Code launch config  

Example Debug Config with args and env file
```json
        {
            "name": "Python Debugger: Demo args and envFile",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "args": ["1","2","3","4","5"],
            "envFile": "${workspaceFolder}/.env"
        }
```

## Part 5? [Podman](/docs/podman-starter.md)
Installation of Podman Podman Compose  
Starting big with PostGIS  
Run container  
Stop container  
Delete container  



Other Future Ideas
-----------------
S3 Object Storage, Cloud native data formats  
Fastapi, pydantic, duckdb  
Dockerfiles, Compose-files, Images, Containers Podman