Author: Kaden Culp

A light, daily notebook that handles archival and compilation.

Running archive.py will do the following:

1. Move the contents of today's notebook to an archive subdirectory.

2. Move the contents of tomorrow's notebook to today's notebook.

3. Copy the template notebook to tomorrow's notebook.

4. Compile the contents of all the archived notebooks and write them to a directory.

Directories:

- archive compiled: Text compiled from text files of the same name in the daily archive.

- daily archive: A directory of subdirectories, each of which contains a single day's various text files.

- template: Directory which contains template texts files that will be copied over to the tomorrow directory when the script is ran.

- today: Contains txt files of the current day's notes, which will be moved to a subdirectory in the daily archive when the daily archive when the script is ran.

- tomorrow: Contains txt files of tomorrow's notes, which will be moved to the today directory when the script is ran.
