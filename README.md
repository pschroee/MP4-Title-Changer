# MP4-Title-Changer

This

## Install

`pip3 install argparse glob mutagen`

## Usage
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


### Folder structure
```
/home/user/videodirectory
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
Testoutput
```


## License

See the [LICENSE](LICENSE.md) file for license rights and limitations (MIT).
