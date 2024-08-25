# TODO

## v0.1.2
- [x] stagelinq : regression to 0.1.2 (announce IP patch automated)
- [x] test build & run powershell scripts
- [x] gui : add a console log output
- [x] gui : clean log undesired \r\n at first load and find a way to sanitize log files count
- [x] gui : clean GUI code structure
- [ ] gui : improve "Please wait" widget display refresh
- [ ] gui : No "Please Wait" menu while importing tracks to db and playlist
- [ ] gui : create icon & add it to Qt task icon
- [ ] gui : avoid multiple selections on same table lines to be considered
- [ ] gui : run long task as threads / async 
- [ ] gui : add menu to select columns to display [IN_PROGRESS] : isChecked() always return false
- [ ] stagelinq : data from one player overwrites some previously sent by another
- [ ] stagelinq : crashes program if one player is disconnected
- [ ] stagelinq : clean way of start/stop service (close connections,...)
- [ ] database : find a way to copy scan folder not database-referenced files to database root folder 
- [ ] database : shitty html characters in JSON exported playlists (for é,à,.. and so on)

## v0.1.1
- [x] stagelinq : add ip filter
- [x] implement proper EXE file generation [WINDOWS_TO_BE_TESTED]
- [x] stagelinq : implement stagelink 0.2.1 changes [TO_BE_TESTED] [KO]

## v0.1.0
- [x] implement import txt/json/m3u file to playlist
- [x] fix FilesTable not returning correct selected row indexes (**workaround using a cached array**)
- [x] Fix 3 first empty columns in track table
- [x] check if track not already in database before adding to  track /playlist 
- [x] add "loading..." popup while doing stuff
- [x] update lastEditTime playlist table each time operation done on playlist [TO_BE_TESTED]
- [x] main : implement proper CLI & no GUI option
- [x] main : improve exported json content
- [x] gui : automatic refresh of stagelinq data => segmentation fault => USE QTIMER
- [x] gui : modify mainGui structure to load additionnal code from another file
- [x] gui : add filter to tables
- [x] gui : disable push buttons when prior conditions not met (trigger when table element selection changed)
- [x] database : fordib to add files from a different root location as loaded database