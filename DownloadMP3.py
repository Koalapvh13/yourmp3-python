def DownloadMP3(videoID, filename, path="./"):
    from win10toast import ToastNotifier
    from youtube_dl import YoutubeDL
    import youtube_dl

    toaster = ToastNotifier()
    toaster.show_toast(filename,
    "Baixando música em MP3",
    duration=10)
    # from VideoInfo import getVideoTitle

    videoURL = "https://www.youtube.com/watch?v=" + videoID
    saveIn = path + filename
    try:
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": saveIn + ".%(ext)s",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([videoURL])
        return True
    except Exception as e:
        return False


#print(DownloadMP3("rWVjht-MIto", "Specktrem - Shine", "./YourMP3-Downloads/"))
