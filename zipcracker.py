#!/usr/bin/python

red = "\033[0;1;31m"
bd = "\033[0;1;40m"
orn = "\033[1;38;5;208m"
gy = "\033[0;1;2m"
gr = "\033[1;32m"
n = "\x1B[0m"
ln = "\u2502"
t = "\u251C"

try: import argparse
except ModuleNotFoundError: print(f"{bd}[{rd}INFO{bd}] no module argparse.")

try: import zipfile
except ModuleNotFoundError: print(f"{bd}[{rd}INFO{bd}] no module zipfile.")

import time
import sys
import random

def is_exists(file):
  try:
    open(file, "r")
    return True
  except:
    return False

def open_zip(zip_file_name, password):
  status = 0
  parent_zip = zipfile.ZipFile(zip_file_name, "r")
  child_files = parent_zip.namelist()
  for child_zip in child_files:
    try:
      request = parent_zip.open(child_zip, pwd=password.encode('utf-8'))
      status += 1
    except RuntimeError:
      pass
  if status == 2: return 1
  else: return 0

examples = """examples:
  python zipcracker.py --default target.zip
  python zipcracker.py --randchar 5 1000 target.zip
  python zipcracker.py --randint 0 1000 target.zip
  python zipcracker.py --custom custom_list.txt target.zip
"""

parser = argparse.ArgumentParser(
	epilog = examples,
	prog = "python zipcracker.py",
	formatter_class = argparse.RawDescriptionHelpFormatter,
	add_help = True,
	usage = None
	)

with open("version.txt", "r") as version_file:
  version = version_file.readline()

parser.add_argument("zipfile", help=".zip file to crack")
parser.add_argument("--version", help="print version", action="version", version=version)
parser.add_argument("-d","--default", help="1 million common passwords", action="store_true")
parser.add_argument("--randchar", help="random letters of given length", type=int, nargs=2, metavar=("LENGTH","RANGE"))
parser.add_argument("--randint", help="random numbers from 0 to given range", type=int, nargs=2, metavar=("START","STOP"))
parser.add_argument("--custom", help="custom txt file")

try: args = parser.parse_args()
except: exit(0)
if is_exists(args.zipfile): pass
else: print(f"{bd}[{red}INFO{bd}] file `{args.zipfile}` not found"), exit(0)

if zipfile.is_zipfile(args.zipfile):
  pass
else:
  print(f"{bd}[{red}INFO{bd}] file `{args.zipfile}` is not a zip.")
  exit(0)

main_zip = args.zipfile

# <-- --default option -->
def default():
  print(f"\n {orn}{ln}—{n} {bd}TARGET : {main_zip}")
  time.sleep(0.3)
  fetched_passwords = []
  print(f" {orn}{ln}—{n} {bd}OPTION : --default")
  time.sleep(0.3)
  print(f" {orn}{ln}_{n}{gy} CTRL+C TO STOP")
  time.sleep(0.3)
  print(f"{bd} {ln} {orn}{ln}")
  password_list_file = "1m_pass.txt"
  password_list = open(password_list_file, "r").read().splitlines()
  counter = 1
  for password in password_list:
    try:
      phrase = f"{bd} {ln} {bd}{orn}{ln}—{n}{red}[{bd}{counter}{red}]{bd} Trying `{orn}{password}{bd}` : "
      trial = open_zip(main_zip, password)
      if trial == 1:
        print(f"{phrase}{gr}SUCCESS{n}\n", end="\r")
        fetched_passwords.append(password)
      else:
        print(f"{phrase}{red}BAD{n}", end="\r")
      counter += 1
    except KeyboardInterrupt:
      break
  time.sleep(0.3)
  print(f"\n{bd} {ln}{orn} {ln}_")
  time.sleep(0.3)
  print(f"{bd} {ln}  {orn} {ln}— {n}{bd}Possible password(s):")
  for key in fetched_passwords:
    print(f"{bd} {ln}  {orn} {ln}—{red}{n}{bd} {key}")
    time.sleep(0.1)
  print("")

def randint():
  start, stop = args.randint
  print(f"\n {orn}{ln}—{n} {bd}TARGET : {main_zip}")
  time.sleep(0.3)
  fetched_passwords = []
  print(f" {orn}{ln}—{n} {bd}OPTION : --randint")
  time.sleep(0.3)
  print(f" {orn}{ln}—{n} {bd}RANGE : {start}-{stop}")
  time.sleep(0.3)
  print(f" {orn}{ln}_{n} {gy}CTRL+C TO STOP")
  time.sleep(0.3)
  print(f"{bd} {ln} {orn}{ln}")
  time.sleep(0.3)
  for password in range(start, stop+1):
    try:
      phrase = f"{bd} {ln} {bd}{orn}{ln}—{n}{red}[{bd}{password}{red}]{bd} Trying `{orn}{password}{bd}` : "
      trial = open_zip(main_zip, str(password))
      if trial == 1:
        print(f"{phrase}{gr}SUCCESS{n}\n", end="\r")
        fetched_passwords.append(password)
      else:
        print(f"{phrase}{red}BAD{n}", end="\r")
    except KeyboardInterrupt:
      break
  time.sleep(0.3)
  print(f"\n{bd} {ln}{orn} {ln}_")
  time.sleep(0.3)
  print(f"{bd} {ln}  {orn} {ln}— {n}{bd}Possible password(s):")
  for key in fetched_passwords:
    print(f"{bd} {ln}  {orn} {ln}—{red}{n}{bd} {key}")
    time.sleep(0.1)
  print("")

def randchar():

  def random_pass(length):
    random_char = ""
    letters = "abcdefghijklmnopqrstuvwxys"
    for i in range(length):
      letter = random.choice(letters)
      random_char += letter
    return random_char

  given_length, stop_range = args.randchar
  print(f"\n {orn}{ln}—{n} {bd}TARGET : {main_zip}")
  time.sleep(0.3)
  fetched_passwords = []
  print(f" {orn}{ln}—{n} {bd}OPTION : --randchar")
  time.sleep(0.3)
  print(f" {orn}{ln}—{n} {bd}RANGE : {stop_range}")
  time.sleep(0.3)
  print(f" {orn}{ln}—{n} {bd}LENGTH : {given_length}")
  time.sleep(0.3)
  print(f" {orn}{ln}_{n} {gy}CTRL+C TO STOP")
  time.sleep(0.3)
  print(f"{bd} {ln} {orn}{ln}")
  time.sleep(0.3)
  fetched_passwords = []
  counter = 1

  for x in range(stop_range):
    generated_pass = random_pass(given_length)
    try:
      phrase = f"{bd} {ln} {bd}{orn}{ln}—{n}{red}[{bd}{counter}{red}]{bd} Trying `{generated_pass}` : "
      trial = open_zip(main_zip, generated_pass)
      if trial == 1:
        print(f"{phrase}{gr}SUCCESS{n}\n", end="\r")
        fetched_passwords.append(generated_pass)
      else:
        print(f"{phrase}{red}BAD{n}", end="\r")
      counter += 1
    except KeyboardInterrupt:
      break

  time.sleep(0.3)
  print(f"\n{bd} {ln}{orn} {ln}_")
  time.sleep(0.3)
  print(f"{bd} {ln}  {orn} {ln}— {n}{bd}Possible password(s):")
  for key in fetched_passwords:
    print(f"{bd} {ln}  {orn} {ln}—{red}{n}{bd} {key}")
    time.sleep(0.1)
  print("")

def custom():
  try: open(args.custom)
  except FileNotFoundError: print(f"{bd}[{red}INFO{bd}] file `args.custom` not found."), exit(1)

  print(f"\n {orn}{ln}—{n} {bd}TARGET : {main_zip}")
  time.sleep(0.3)
  print(f" {orn}{ln}—{n} {bd}REF : {args.custom}")
  time.sleep(0.3)
  fetched_passwords = []
  print(f" {orn}{ln}—{n} {bd}OPTION : --custom")
  time.sleep(0.3)
  print(f" {orn}{ln}_{n}{gy} CTRL+C TO STOP")
  time.sleep(0.3)
  print(f"{bd} {ln} {orn}{ln}")
  password_list_file = args.custom
  password_list = open(password_list_file, "r").read().splitlines()
  counter = 1

  for password in password_list:
    try:
      phrase = f"{bd} {ln} {bd}{orn}{ln}—{n}{red}[{bd}{counter}{red}]{bd} Trying `{orn}{password}{bd}` : "
      trial = open_zip(main_zip, password)
      if trial == 1:
        print(f"{phrase}{gr}SUCCESS{n}\n", end="\r")
        fetched_passwords.append(password)
      else:
        print(f"{phrase}{red}BAD{n}", end="\r")
      counter += 1
    except KeyboardInterrupt:
      break

  time.sleep(0.3)
  print(f"\n{bd} {ln}{orn} {ln}_")
  time.sleep(0.3)
  print(f"{bd} {ln}  {orn} {ln}— {n}{bd}Possible password(s):")
  for key in fetched_passwords:
    print(f"{bd} {ln}  {orn} {ln}—{red}{n}{bd} {key}")
    time.sleep(0.1)
  print("")

if args.randint:
  randint()
elif args.default:
  default()
elif args.randchar:
  randchar()
elif args.custom:
  custom()
