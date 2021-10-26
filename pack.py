from os import mkdir
from os.path import isdir
from shutil import rmtree

if not isdir('./packages'):
  mkdir('./packages')

def installpackage(txt):
  txt=txt.replace('\r','')
  packname=txt.split('\n')[0]
  seperator=txt.split('\n')[1]
  tfiles=[(f.split('\n')[0],f.split('\n',1)[1]) for f in
          txt.split('\n',2)[2].split('\n'+seperator+'\n')]
  files={}
  for f in tfiles:
    files[f[0]]=f[1]
  try:
    try:
      mkdir('./packages/'+packname)
      print(' Created packages/'+packname)
    except:pass
    for f in files.keys():
      open('./packages/'+packname+'/'+f,'w').write(files[f])
      print(' Created packages/'+packname+'/'+f)
    return False
  except:
    return True
def uninstallpackage(pn):
  if input(' Are you sure you want to uninstall this package? (y/n)').lower()=='y':
    try:
      rmtree('./packages/'+pn)
      print(' Successfully uninstalled "'+pn+'"')
    except Exception as e:
      print(e)
      print(' No such package as "'+pn+'"')
