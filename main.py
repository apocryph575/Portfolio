import moviepy.editor
import os


def main():
    directory = os.listdir(os.getcwd())
    for file in directory:
        if "mp4" in file:
            name = file.split(".mp4")[0]
            print(name)
            video = moviepy.editor.VideoFileClip(file)
            audio = video.audio
            audio.write_audiofile(f"{name}.mp3")

if __name__=="__main__":
    main()