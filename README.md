# MP4-Title-Changer

This is command-line-interface (cli) is written in Python3 and can change the titles of mp4-files. The titles of the mp4-files are the filenames without `.mp4` in camel case.

## Requirements & Install

To use the cli you must have installed Python3.

### Installation:

`pip3 install argparse mutagen`

## Usage

If no path is given with the parameter `-p PATH or --path PATH`, then the path is the current working directory.

You  can use the option `--change or -c` to change the titles of the mp4-files or the option `--get or -g` to get a list of all mp4-files with their title.

```
usage: mp4-title-changer.py [-h] [-p path] (-c | -g) [-r] [-v] [-d]

cli to change all titles of the mp4-files to the name of the file

optional arguments:

  -h, --help            show this help message and exit
  
  -p path, --path path  path of the directory of the mp4-files
  
  -c, --change          sets mode to change the titles of all mp4-files
  
  -g, --get             sets mode to get all mp4-files
  
  -r, --recursive       includes all subdirectories
  
  -v, --verbose         produces verbose output
  
  -d, --debug           shows debug messages
```
  
## Examples


### File & Folder structure
```
/home/user/videodirectory/video1.mp4 title: "wrong title 1"
/home/user/videodirectory/video2.mp4 title: "wrong title 2"
/home/user/videodirectory/sub1/video3.mp4 title: "wrong title 3"
/home/user/videodirectory/sub1/video4.mp4 title: "wrong title 4"
/home/user/videodirectory/sub2/video5.mp4 title: "wrong title 5"
/home/user/videodirectory/sub1/sub1/video6.mp4 title: "wrong title 6"
```

### Change the titles of the mp4-files
`python3 mp4-title-changer.py --path /home/user/videodirectory/ --change`

Output:
```
Testoutput
```

### Change the titles of the mp4-files recursively
`python3 mp4-title-changer.py --path /home/user/videodirectory/ --change --recursive`

Output:
```
Testoutput
```

### Get the titles of the mp4-files
`python3 mp4-title-changer.py --path /home/user/videodirectory/ --get`

Output:
```
Testoutput
```

### Get the titles of the mp4-files recursively
`python3 mp4-title-changer.py --path /home/user/videodirectory/ --get --recursive`

Output:
```
File: /home/user/videodirectory/video1.mp4 Title: wrong title 1
File: /home/user/videodirectory/video2.mp4 Title: wrong title 2
File: /home/user/videodirectory/sub1/video4.mp4 Title: wrong title 4
File: /home/user/videodirectory/sub1/video3.mp4 Title: wrong title 3
File: /home/user/videodirectory/sub1/sub1/video6.mp4 Title: wrong title 6
File: /home/user/videodirectory/sub2/video5.mp4 Title: wrong title 5
```


## License

See the [LICENSE](LICENSE.md) file for license rights and limitations (MIT).
