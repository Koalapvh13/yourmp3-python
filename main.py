from DownloadMP3 import DownloadMP3
from VideoInfo import getVideoTitle


def download(videoID, savePath):
    YTLINK = "https://www.youtube.com/watch?v=" + videoID
    title = getVideoTitle(YTLINK)
    if title is not "":
        if DownloadMP3(videoID, title, savePath):
            print("Baixado com sucesso!")
        else:
            print("Falha ao baixar o video!")
    else:
        print("Falha procurar o Titulo do Vídeo!")


DIRECTORY = "./YourMP3-Downloads/"