from pytube import YouTube

def fetch_audio_from_yt(url):
  yt = YouTube(url)
  stream = yt.streams.first()
  video_path = stream.download(output_path = "audio")
  return video_path