#!/usr/bin/env python3
import re

frankenpath="./books/frankenstein.txt"

def get_text(path):
  with open(path) as f:
    file_contents = f.read()
  return(file_contents)
 
def count_words(input_string):
  word_array = input_string.split()
  length = len(word_array)
  #print(length)
  return(length)

def count_characters(input_string):
  chars = list(input_string.lower())
  char_dict = {}
  for c in chars:
    if c not in char_dict.keys():
       char_dict[c] = 0
    char_dict[c] = char_dict[c] + 1
  #print(char_dict)
  return(char_dict)

def print_report(file_path, word_count, char_dict):
  if re.match(r"^\.\/.*", file_path):
    file_path = file_path[2:]
  begin_str = "--- Begin report of {} ---".format(file_path)
  print(begin_str)
  count_str = "{} words found in the document".format(word_count)
  print(count_str)
  for c in char_dict.keys():
    if not re.match(r'(\s|\#|\.)', c):
      char_count_str = "The '{}' character was found {} times".format(c, char_dict[c])
      print(char_count_str)
  print("--- End report ---")
  
def main():
  file_contents = get_text(frankenpath)
  word_count = count_words(file_contents)
  char_dict = count_characters(file_contents)
  print_report(frankenpath, word_count, char_dict)

main()
