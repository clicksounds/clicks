import shutil
import os
shutil.rmtree("MultipleClick")
shutil.copytree(".github/FileNamer/Output", "MultipleClick")
shutil.rmtree(".github/FileNamer/Output")
shutil.rmtree(".github/FileNamer/Update")