class Songs:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for element in self.lyrics:
            print(element)


happy_bday = Songs(["May god bless you, ",
                   "Have a sunshine on you,",
                   "Happy Birthday to you !"])

happy_bday.sing_me_a_song()
