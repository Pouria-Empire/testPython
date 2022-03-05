import sys

from past.builtins import execfile

someFile= open( "testing/Q1_in.txt", "r" )
someFile2= open( "testing/out.txt", "w" )
sys.stdin = someFile
sys.stdout = someFile2
execfile( "testing/main.py" )
someFile2.close()
