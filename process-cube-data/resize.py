import Image
import os
import sys
import fnmatch
import shutil

def makeImageSquare(img):
    width,height = img.size

    squareSize = min(width, height)

    left = (width - squareSize)/2
    top = (height - squareSize)/2
    right = (width + squareSize)/2
    bottom = (height + squareSize)/2

    return img.crop((left, top, right, bottom))


path = sys.argv[1]
output = sys.argv[2]
newSize = int(sys.argv[3])

for dir in os.listdir(path):
    files = os.listdir(os.path.join(path, dir))
    imgFile = fnmatch.filter(files, "*.jpg")[0]
    data = fnmatch.filter(files, "*.txt")

    img = Image.open(os.path.join(path, dir, imgFile))
    img = makeImageSquare(img)
    img = img.resize((newSize, newSize))

    outPath = os.path.join(output, dir)

    if not os.path.exists(outPath):
        os.makedirs(outPath)

    img.save(os.path.join(outPath, imgFile.replace(".jpg", ".png")))

    for dataFile in data:
        shutil.copy(os.path.join(path, dir, dataFile), os.path.join(outPath, dataFile))
