from pytube import YouTube
import pytube.request

pytube.request.default_range_size = 500000


def progress_func(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100
    print(f'Status: {round(pct_completed, 2)}%')


def download():
    video = YouTube(input('Entra el link del video '), on_progress_callback=progress_func)
    video = video.streams.get_highest_resolution()
    try:
        print('El titulo del video es: ' + video.title)
        video.download()
    except:
        print('Hubo un error en la descarga')
    print('Descarga completada')


finished = False
while not finished:
    download()
    option = input('Continuar(Y/N)')
    if option == 'N' or option == 'n':
        finished = True
