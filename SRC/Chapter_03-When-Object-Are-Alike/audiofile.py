class AudioFile(object):
    ext = ""

    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid File Format")
        self.filename = filename

    # def play(self):
    #     print("Playing")


class MP3File(AudioFile):
    ext = "mp3"

    def play(self):
        print("playing {} as mp3".format(self.filename))


class WavFile(AudioFile):
    ext = "wav"

    def play(self):
        print("playing {} as wav".format(self.filename))


class OggFile(AudioFile):
    ext = "ogg"

    def play(self):
        print("playing {} as ogg".format(self.filename))


class FlacFile(object):
    def __init__(self, filename):
        if not filename.endswidth(".flac"):
            raise Exception("Invalid File Format")
        self.filename = filename

    def play(self):
        print("playing {} as flac".format(self.filename))

def AudioList(list):
    player = 

if __name__ == "__main__":
    ogg = OggFile("myfile.ogg")
    ogg.play()

    mp3 = MP3File("myFile.mp3")
    mp3.play()

    audiofile = []

    audiofile.append(ogg)
    audiofile.append(mp3)

    for myfile in audiofile:
        myfile.play()
