import os.path
from os import path

def main():
   a = input(" : ")
   print ("File exists:"+str(path.exists(a)))
   print ("File exists:" + str(path.exists('hlaa.txt')))
   print ("directory exists:" + str(path.exists('myDirectory')))

if __name__== "__main__":
   main()