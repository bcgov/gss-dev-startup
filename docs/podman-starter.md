# Install Podman into WSL
Inside  WSL(Ubuntu) -- update and upgrade your subsystem
```bash
sudo apt update
sudo apt upgrade -y
```

Install podman
```bash
sudo apt install -y podman
```

Verify your install
```
podman --version
```

Install podman-compose
```bash
sudo apt install podman-compose
```
Verify
```bash
podman
```

Break the world (this take less time than you would expect)(see below for retaining data with -v)
```bash
podman run \
  --name my-gss-postgis \
  -e POSTGRES_PASSWORD=fossrocks \
  -p 5432:5432 \
  -d postgis/postgis
```
Your data will not be retained when we stop this. If you want to keep it... add the added parameter
```bash
-v postgis_data:/var/lib/postgresql/data
```
---
**special note:**  
if you have an error where the image postgis/postgis can not be resolved you can do one of two things.
1. Add docker.io infront of the image 
```bash
podman run \
  --name my-gss-postgis \
  -e POSTGRES_PASSWORD=fossrocks \
  -p 5432:5432 \
  -d docker.io/postgis/postgis
```
2. or add docker.io to your podman configuration
- edit ```/etc/containers/registries.conf```
- find the line ```# # An array of host[:port] registries to try when pulling an unqualified image, in order.```
- add this below it ```unqualified-search-registries = ["docker.io"]```
---

Check your container named <b>my-gss-postgis</b> is running
```bash
podman container ps
```
At this point you can connect to the database with user postgres password fossrocks with pgsql, qgis, dbeaver, pgAdmin etc.   



Now stop the container
```bash
podman stop my-gss-postgis
```
Now Start it
```bash
podman start my-gss-postgis
```
Now Stop it and remove it (I am done with fun)

```bash
podman stop my-gss-postgis
podman rm my-gss-postgis
```
or 
```bash
podman rm -f my-gss-postgis
```
If you retained data you can remove that too
```bash
podman volume rm postgis_data
```