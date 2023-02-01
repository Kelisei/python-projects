from pytube import YouTube
def Descarga():
    video = YouTube(input('Entra el link del video '))
    video = video.streams.get_highest_resolution()
    try:
        print('El titulo del video es: ' + video.title)
        video.download()
    except:
        print('Hubo un error en la descarga')
    print('Descarga completada')

Descarga()
