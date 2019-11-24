from google.colab import auth
from google.colab import drive

class Colab():
    def mount(self):
        auth.authenticate_user()
        drive.mount('/content/gdrive/')
        baseDir = '/content/gdrive/My Drive/Colab/'

        return baseDir