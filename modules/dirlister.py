import os 
def run(**run):
    print("[*] In dirlister module.")
    files = os.listdir(".")
    return str(files)
