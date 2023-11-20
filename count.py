import os

def recursive_walking(entity):
    global count
    if os.path.isdir(entity):
        for ent in os.listdir(entity):
            new_dir = os.path.join(entity, ent)
            print(new_dir)
            recursive_walking(new_dir)
    else:
        print(entity + " - file found")
        if entity.split(".")[-1] == "mp4":
            count = count + 1
        

count = 0
path = os.path.abspath(os.getcwd())

recursive_walking(path)
print("There are " + str(count) + " mp4 files.")