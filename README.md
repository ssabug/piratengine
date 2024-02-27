# piratengine

## Description

This repository aims to provide 'low' level open source tools for **Denon DJ** hardware, in particular those using **Engine DJ OS**.

The first objective is to have simple tools to interact with m.db database, and enable to export/import track and playlist data.

Maybe in the future some ethernet related stuff about the players will be investigated.

## Features
### Database2/m.db
 - [ ] make a backup of the currently edited database
 - [x] read track, playlist info, ...
 - [ ] track edit
 - [x] track add
 - [ ] track IDV3 fill
 - [x] test script-imported tracks
 - [x] playlist create
 - [x] playlist to txt file
 - [x] playlist add track
 - [x] playlist add track from txt file
 - [x] scan files on engine dj music files storage
 - [x] update Track table from file scan
 - [ ] support different database versions ( in 3.3.0 track table has 1 more parameter )

## Requirements
 - python 3
 - pip

## Installation
 - `git clone` the repo
 - `cd piratengine`
<details>
  <summary> (optional) you can create a python virtual environnement to avoid the project python libraries to interfere with the ones already present on your system </summary>

 - run `python -m venv venv`
 - then `source venv/bin/activate` (some IDEs can do this automatically) 
 </details>
 
 - `pip install -r install/requirements.txt`

## Running
 - (optional) if you created a virtual environnement, run `source venv/bin/activate` (some IDEs can do this automatically)
 - `python piratengine.py` 

## Utilities

Some useful ressources:

 - [SQL3 database editor](https://sqlitebrowser.org/dl/) to manually read/edit databases
 - [Denon stuff](https://support.denondj.com/en/support/solutions/articles/69000834165-engine-dj-v3-0-support-for-third-party-database-tools)
 - [Wireshark](https://www.wireshark.org/download.html) for network packet capture & analysis
 - [StageLinq python Implementation](https://github.com/Jaxc/PyStageLinQ) 
 - [StageLinq nodeJs Implementation](https://github.com/MarByteBeep/StageLinq)
 - [StageLinq Beatinfo](https://github.com/dzelionis/denon-stageLinQ-BeatInfo)
 
## Compatibility
Linux, Mac, Windows (as in python)

Tested systems:
Fedora Linux

## Licensing
WTFPL. But the authors keeps the right to trashtalk on anyone re-using this in a unlegitimate way.

**This stuff is provided as is with no warranty at all, take your own precautions before using it (database backup ...)**.
