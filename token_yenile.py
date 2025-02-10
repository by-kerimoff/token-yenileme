import subprocess
import time

def get_youtube_stream_url(video_id):
    # yt-dlp ilə axın URL-sini əldə et
    command = f"yt-dlp -g https://www.youtube.com/watch?v={video_id}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def update_m3u_file(video_id, m3u_file_path):
    while True:
        try:
            # Yeni axın URL-sini əldə et
            stream_url = get_youtube_stream_url(video_id)
            print(f"Yeni URL: {stream_url}")

            # M3U faylını yenilə
            with open(m3u_file_path, "w") as m3u_file:
                m3u_file.write("#EXTM3U\n")
                m3u_file.write(f"#EXTINF:-1, YouTube Live\n")
                m3u_file.write(f"{stream_url}\n")

            print("M3U faylı yeniləndi!")
        except Exception as e:
            print(f"Xəta: {e}")

        # 60 saniyə gözlə (tokenin ömründən asılı olaraq intervalı tənzimləyin)
        time.sleep(60)

# YouTube video ID və m3u faylının yolu
youtube_video_id = "3g2EfhnmTkU"  # YouTube video ID-ni daxil edin
m3u_file_path = "youtube_live.m3u"  # M3U faylının yolu

# M3U faylını avtomatik yenilə
update_m3u_file(youtube_video_id, m3u_file_path)
