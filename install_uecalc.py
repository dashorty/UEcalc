import requests

raw_file_list = ['https://raw.githubusercontent.com/dashorty/UEcalc/master/UEcalc.py',
                 'https://raw.githubusercontent.com/dashorty/UEcalc/master/uecalc.pyui']

for df in raw_file_list:
    filename = df[df.rfind('/')+1:]
    r = requests.get(df, allow_redirects=True)
    open(filename, 'wb').write(r.content)
