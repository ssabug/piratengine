# piratengine

## Description

This repository aims to provide 'low' level open source tools for **Denon DJ** hardware, in particular those using **Engine DJ OS**.

The first objective is to have simple tools to backup database, and enable to export track and playlist data.

We then would like to add the ability to import/edit playlists (from text/m3u/json formats) to/from database.

## Features
 - [x] Database2/m.db  read track, playlist info, ...
 - [ ] Database2/m.db  track edit
 - [ ] Database2/m.db  track add
 - [x] Database2/m.db  playlist create
 - [ ] Database2/m.db  playlist add track

## Requirements
 - python 3.12.1

## Installation
 - `git clone` the repo
 - `cd piratengine`
 - (optional) you can create a python virtual environnement to avoid streambot python libraries to interfere with the ones already present on your system
 - (optional) to do so, run `python -m venv venv`
 - (optional) then `source /venv/bin/activate` (some IDEs can do this automatically) 
 - `pip install -r install/requirements.txt`

## Running
 - (optional) if you created a virtual environnement, run `source /venv/bin/activate` (some IDEs can do this automatically)
 - `python piratengine.py` 

## Compatibility
Linux, Mac, Windows (as in python)

Tested systems:
Fedora Linux

