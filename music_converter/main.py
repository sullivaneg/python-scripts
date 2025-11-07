from vid_to_audio import *

def main():
    flag = True
    while flag:
        name_path = input("Enter the path of your video file: ")
        if name_path == "":
            flag = False
            break
        else:
            convert_vid_to_audio(name_path)

if __name__ == "__main__":
    main()