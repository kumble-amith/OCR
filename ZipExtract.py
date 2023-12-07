import zipfile
import os
# https://www.kaggle.com/datasets/thomasqazwsxedc/alphabet-characters-fonts-dataset

ref = zipfile.ZipFile("Ignored/archive.zip")
ref.extractall(os.path.join(""))
ref.close()