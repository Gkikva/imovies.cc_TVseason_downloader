import requests


class Imovie:
    def __init__(self, name_season, name_of_season, url_of_season):
        self.name_season = name_season
        self.number_of_season = name_of_season
        self.url_of_season = url_of_season
        self.splitted_url = self.url_of_season.split("/")
        self.url = f"https://api.imovies.cc/api/v1/movies/{self.splitted_url[5]}/season-files/{self.number_of_season}"
        self.data_data=requests.get(self.url)

        self.json_data = self.data_data.json()
        self.file_name = 0
        self.path = self.json_data['data']

    def download(self, language):
        user_language = language
        for x in self.path:
            self.file_name += 1
            print('proccessing ' + str(self.file_name))
            for language in x['files']:
                if language["lang"] == user_language.lower() or language["lang"] == user_language.upper():
                    z = language['files'][0]['src']
                    video_path = requests.get(z,stream = True)
                    video_file = str(self.name_season) + " " + str(self.file_name) + ".mp4"
                    with open(video_file, 'wb') as f:
                        for chunk in video_path.iter_content(chunk_size= 1024):
                            if chunk:
                                f.write(chunk)
                    print("Video was downloaded")
        print("all video was downloaded")
        #

name_season = str(input("enter season name:  "))
number_of_season = int(input('enter which season you want to download:  '))
user_language = str(input("enter which language you want? GEO / RUS / ENG   "))
url_of_season = str(input("input the URL of the season:   "))


download_video = Imovie(name_season, number_of_season , url_of_season)
download_video.download(user_language)

