import requests
import shutil
# Nome del cimitero
nomecimitero = "cimitero2.zip"
# Download file from url
url = 'http://memoryp.org:3001/cimitero/get/'+nomecimitero
r = requests.get(url, allow_redirects=True)
open(nomecimitero, 'wb').write(r.content)
# Unzipping file
shutil.unpack_archive(nomecimitero, "./")
