import pandas as pd
import re
import PySimpleGUI as psg
import subprocess

fhandle = open(r'C:\temp\update.txt', 'w')
subprocess.run('pip list --outdated', shell = True, stdout = fhandle)
fhandle.close()

df1 = pd.DataFrame(columns=['Package', 'Version', 'Latest', 'Type'])
fhandle = open(r'C:\temp\update.txt', 'r')
AnyPackagesToUpgrade = 0
