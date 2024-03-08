# piratengine

## Description

This repository aims to provide 'low' level open source tools for **Denon DJ** hardware, in particular those using **Engine DJ OS**.

The first objective is to have simple tools to interact with m.db database.

Some features about StageLinQ will also be explored.

## Features

### Database2/m.db
 - [x] Qt GUI
 - [x] make a backup of the currently edited database
 - [x] read track, playlist info, ...
 - [ ] test database modified with all GUI features (v2 & v3)
 - [ ] track edit
 - [x] track add
 - [ ] track IDV3 fill
 - [ ] delete playlist/track/playlist track
 - [ ] change track position in playlist
 - [ ] change playlist index
 - [x] playlist create
 - [x] playlist to txt/json/m3u file
 - [x] playlist add track
 - [x] playlist add track from txt/json/m3u file
 - [x] scan files on engine dj music files storage
 - [x] update Track table from file scan
 - [x] support different database versions ( in 3.3.0 track table has 1 more parameter ) (to be tested  fully assessed )

 ### StageLinQ
 - [x] basic implementation of [PyStageLinQ](https://github.com/Jaxc/PyStageLinQ)
 - [x] grab stagelinq data 
 - [ ] use fileTransfer service
 - [ ] act as an instance of EngineDJ software

## Requirements
 - python 3
 - pip
 - Qt 6

## Installation
 - `git clone` the repo
 - `cd piratengine`
<details>
  <summary> (optional) you can create a python virtual environnement to avoid the project python libraries to interfere with the ones already present on your system </summary>

 - run `python -m venv venv`
 - then `source venv/bin/activate` (some IDEs can do this automatically) 
 </details>
 
 - `pip install -r install/requirements.txt`
 - in your installed library **PyStageLinQ.py** file, change the variable this way : `ANNOUNCE_IP = "224.0.0.251" `
`

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
WTFPL.

**This stuff is provided as is with no warranty at all, take your own precautions before using it (database backup ...)**.
