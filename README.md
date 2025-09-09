![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white&style=flat-square)
![HTML5](https://img.shields.io/badge/HTML5-orange?logo=html5&logoColor=white&style=flat-square)
![CSS3](https://img.shields.io/badge/CSS3-blue?logo=css3&logoColor=white&style=flat-square)
![JavaScript](https://img.shields.io/badge/JavaScript-yellow?logo=javascript&logoColor=black&style=flat-square)


# ZackDash - Setup Guide

This guide will help you step-by-step for setting up the ZackDash project including downloading the project files and running the project locally.

## ⚙️ Prerequisites

### 1. Install python

### Download, install python and create a venv (linux only)

For windows and macos: Download and install [python](https://www.python.org/downloads/) 👈

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

---
## 🧠 About ZackDash
**ZackDash** is a real time dashboard that can be configure in th config file (config.json). It obtains real time infos on the server/computer and create a local web server and display the infos in a configurable manner

---

## 🔧 Tech Stack

* Front end : **html**, **css**, **javascript**
* Back end : **python (flask)**

## 📁 Folder Structure

| Folder           | Description                          |
|------------------|--------------------------------------|
| `/templates`     | Web pages                            |
| `/static`        | Statics files (scripts, styles, ...) |
| `/static/assets` | Images, audio, video, ...            |
| `/static/styles` | Css style files                      |
| `/static/scripts`| JS scripts files                     |

## 🔒 License

ZackDash is released under **The Unlicense**. You can **use**, **modify**, and **distribute** it **freely**.