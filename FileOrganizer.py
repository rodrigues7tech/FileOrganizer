import os

user = os.getlogin()
download_path = rf'C:/Users\{user}\Downloads'


list_download_file = os.listdir(download_path)
list_file = ['.pdf', '.mp3', '.iso', '.mp4', '.png']

def organizer(file, file_type):
    path = os.path.join(download_path, file_type)
    origem = os.path.join(download_path, file)
    destino = os.path.join(path, file)
    if os.path.isdir(path):
        os.rename(origem, destino)
    else:
        os.mkdir(path)
        os.rename(origem, destino)

for item in list_download_file:
    if '.pdf' in item.lower():
        organizer(item, 'pdf')
    elif '.iso' in item.lower():
        organizer(item, 'iso')
    elif '.mp3' in item.lower():
        organizer(item, 'mp3')