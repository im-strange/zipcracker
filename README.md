# ZipCracker
A powerful tool for unlocking zip file powered by Python.

## Installing ZipCracker
We need few python libraries
```
pip install zipfile
```

## Usage
> usage: python zipcracker.py [-h] [-d] [--randchar LENGTH RANGE]
                            [--randint START STOP] [--custom CUSTOM]
                            zipfile
## Options
> -h, --help            show this help message and exit
  -d, --default         1 million common passwords
  --randchar LENGTH RANGE
                        random letters of given length
  --randint START STOP  random numbers from 0 to given range
  --custom CUSTOM       custom txt file
