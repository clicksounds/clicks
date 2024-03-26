import shutil
import os
#shutil.rmtree("Meme")
shutil.copytree(".github/FileNamer/Output/Meme", "Meme")
#shutil.rmtree("Useful")
shutil.copytree(".github/FileNamer/Output/Useful", "Useful")
shutil.rmtree(".github/FileNamer/Output")
shutil.rmtree(".github/FileNamer/Update")