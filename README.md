# ZipCracker
A powerful tool for unlocking zip file powered by Python.

## Installing ZipCracker
Prerequisite python module
```
pip install zipfile
```

Installing through terminal
```
git clone https://github.com/im-strange/zipcracker
```

To use `zipcracker` command instead of `python zipcracker.py`
```
cd zipcracker
chmod +x setup.sh
./setup.sh
source ~/.bashrc
```

## Usage
```
zipcracker [-h] [--version] [-d] [--randchar LENGTH RANGE]
                            [--randint START STOP] [--custom CUSTOM]
                            zipfile
```

## Options
```
-h, --help            show this help message and exit
--version             print version
-d, --default         1 million common passwords
--randchar LENGTH RANGE
                      random letters of given length
--randint START STOP  random numbers from 0 to given range
--custom CUSTOM       custom txt file
```

## Examples
- Try with 1 million common passwords. 
> `zipcracker --default target.zip`
- Random letters with 5 characters and try 1000 times. 
>`zipcracker --randchar 5 1000 target.zip`
- Numbers from 0 to 1000.
> `zipcracker --randint 0 1000 target.zip`
- Try with custom .txt file.
> `zipcracker --custom custom_list.txt target.zip`



