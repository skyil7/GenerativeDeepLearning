from google.colab import auth
from google.colab import drive

def mount():
    auth.authenticate_user()
    drive.mount('/content/gdrive/')
    baseDir = 'My Drive/colab/'

    return baseDir