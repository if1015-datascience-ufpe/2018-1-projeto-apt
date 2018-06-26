# <markdowncell>
# # Dengue

# <codecell>
import os.path
import pandas as pd
import requests

# <codecell>
database_url = 'http://dados.recife.pe.gov.br/dataset/2a9b1c39-0700-4ddf-9a10-b3c8d5d9396c/resource/2a2ef847-7063-462e-bf76-a49ebc9a6d13/download/casos-dengue2016.csv'
database_file = 'casos-dengue2016.csv'

if os.path.exists(database_file):
    print('file already downloaded')
else:
    response = requests.get(database_url, stream=True)
    if response.status_code == 200:
        with open(database_file, 'wb') as file:
            file.write(response.content)
        print('file downloaded')
    else:
        raise Exception('could not download file')
