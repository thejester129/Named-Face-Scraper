# splits into training and testing folders, 80/20 split
import os
import shutil

if not os.path.isdir("train"):
    os.mkdir("train")

if not os.path.isdir("test"):
    os.mkdir("test")

names = os.listdir("faces")
names.remove(".gitignore")  # ;)
for name in names:
    files = os.listdir(os.path.join("faces", name))
    total = len(files)
    training_total = round(total * 0.8)
    training_files = files[0:training_total]
    testing_files = files[training_total:total]

    if not os.path.isdir(os.path.join("train", name)):
        os.mkdir(os.path.join("train", name))

    if not os.path.isdir(os.path.join("test", name)):
        os.mkdir(os.path.join("test", name))

    for train_file in training_files:
        shutil.copyfile(os.path.join("faces", name, train_file),
                        os.path.join("train", name, train_file))

    for testing_file in testing_files:
        shutil.copyfile(os.path.join("faces", name, testing_file),
                        os.path.join("test", name, testing_file))
