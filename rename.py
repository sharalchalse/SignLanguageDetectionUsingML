import os

path = "Image/"

for folder in os.listdir(path):
    count = 0
    for image in os.listdir(os.path.join(path, folder)):
        os.rename(os.path.join(path, folder, image),
                  os.path.join(path, folder, str(count) + ".jpg"))
        count += 1
    print('Done with ' + folder) 