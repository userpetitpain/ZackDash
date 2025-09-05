# ZackDash - Setup Guide

This guide will help you step-by-step for setting up the ZackDash project including downloading the project files, running the project locally and pushing changes to the remote server

## ⚙️ Prerequisites

### 1. Install python

### Download, install python and create a venv (linux only)

For windows : Download and install [python](https://www.python.org/downloads/) 👈

For macos : Download and install [python](https://www.python.org/downloads/) 👈

For Linux : 
```
#Debian/Ubutnu
sudo apt install python3
python3 -m venv venv
source venv/bin/activate
```

### 2. Install git

For windows : [git](https://git-scm.com/downloads)

For macos : [git](https://git-scm.com/downloads)

For linux :

```bash
#Debian/Ubuntu
sudo apt install git
```

## 🔁 Cloning the Repository

```bash
git clone https://github.com/userpetitpain/ZackDash.git
cd ZackDash
```

## 📦 Install modules

```bash
pip3 install -r requirements.txt
```

## ▶️ Run Dashboard

```bash
python3 server.py
```

Open your browser at :
👉 [http://localhost:52678](http://localhost:52678)

## 🚀Deployment via git !

### Create a new branch
```bash
git checkout -b my_branch # <- name of your branch
```

### Commit & Push
```bash
git add . # <- Files to commit
git commit -m "My commit" # <- Your commit message here
git push -u origin my_branch # <- Branch (main or master for main branch)
```
---
## 🧠 About ZackDash
**ZackDash** is a real time dashboard that can be configure in th config file (config.json). It obtains real time infos on the server/computer and create a local web server and display the infos in a configurable manner

---

## 🔧 Tech Stack

* Front end : **html**, **css**, **javascript**
* Back end : **python (flask)**

## 📁 Folder Structure

| Folder       | Description                          |
|--------------|--------------------------------------|
| `/templates` | Web pages                            |
| `/static`    | Statics files (scripts, styles, ...) |
| `/static/assets`| Images, audio, video, ...         |