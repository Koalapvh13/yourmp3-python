from DownloadMP3 import DownloadMP3
from VideoInfo import getVideoTitle
from os.path import dirname, realpath, join


def download(videoID, savePath):
    YTLINK = "https://www.youtube.com/watch?v=" + videoID
    title = getVideoTitle(YTLINK)
    if title != "":
        if DownloadMP3(videoID, title, savePath):
            print("Baixado com sucesso!")
        else:
            print("Falha ao baixar o video!")
    else:
        print("Falha procurar o Titulo do Vídeo!")


DIRECTORY = join(dirname(realpath(__file__)), "YourMP3-Downloads/")
#download("rWVjht-MIto", DIRECTORY)
