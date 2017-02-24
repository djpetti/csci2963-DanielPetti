"""
 Markdown.py
 0. just print whatever is passed in to stdin
 0. if filename passed in as a command line parameter, 
    then print file instead of stdin
 1. wrap input in paragraph tags
 2. convert single asterisk or underscore pairs to em tags
 3. convert double asterisk or underscore pairs to strong tags

"""

import fileinput
import re

class Buffer:
  def __init__(self):
    self.__buffer = ""

  def add(self, line):
    self.__buffer += line

  def get(self):
    return self.__buffer

  def clear(self):
    self.__buffer = None

  def empty(self):
    return self.__buffer == ""

def convertStrong(line):
  line = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', line)
  line = re.sub(r'__(.*)__', r'<strong>\1</strong>', line)
  return line

def convertEm(line):
  line = re.sub(r'\*(.*)\*', r'<em>\1</em>', line)
  line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
  return line

def convertH1(line):
  return re.sub(r'#(.*)', r'<h1>\1</h1>', line)

def convertH2(line):
  return re.sub(r'##(.*)', r'<h2>\1</h2>', line)

def convertH3(line):
  return re.sub(r'###(.*)', r'<h3>\1</h3>', line)

def convertBlockquote(line, line_buffer):
  if line.startswith(">"):
    line = line[1:]

    if line_buffer.empty():
      line_buffer.add("<blockquote>%s\n" % (line))
    else:
      line_buffer.add(line)

    return ""

  else:
    if not line_buffer.empty():
      ret = line_buffer.get() + "</blockquote>"
      line_buffer.clear()
      ret += line
      return ret

  return line

line_buffer = Buffer()
for line in fileinput.input():
  line = line.rstrip()
  line = convertBlockquote(line, line_buffer)
  line = convertStrong(line)
  line = convertEm(line)
  line = convertH3(line)
  line = convertH2(line)
  line = convertH1(line)

  if line:
    print '<p>' + line + '</p>'
