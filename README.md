# ZipCracker
A powerful tool for unlocking zip file powered by Python.

## Installing ZipCracker
We need few python libraries
```
pip install zipfile
```

## Usage
```
python zipcracker.py [-h] [-d] [--randchar LENGTH RANGE]
                            [--randint START STOP] [--custom CUSTOM]
                            zipfile
```

## Options
```
-h, --help            show this help message and exit
-d, --default         1 million common passwords
--randchar LENGTH RANGE
                      random letters of given length
--randint START STOP  random numbers from 0 to given range
--custom CUSTOM       custom txt file
```

## Examples
>try with 1 million common passwords. 
```
python zipcracker.py --default target.zip
```
>random letters with 5 characters and try 1000 times. 
```
python zipcracker.py --randchar 5 1000 target.zip
```
>numbers from 0 to 1000.
```
python zipcracker.py --randint 0 1000 target.zip
```
>try with custom .txt file.
```
python zipcracker.py --custom custom_list.txt target.zip
```



