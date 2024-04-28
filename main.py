import os
import ctypes
from cv2 import VideoCapture, imwrite
from PIL import Image, ImageSequence
from tkinter import Tk, filedialog


def get_gif_path():
    root = Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Choose a file",
        filetypes=[("MP4", "*.mp4"), ("GIF", "*.gif")]
    )

    return file_path


def change_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)


def delete_files_in_frames(folder_path='frames'):
    files = os.listdir(folder_path)
    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)


def extract_frames(input_path):
    output_folder = 'frames'
    os.makedirs(output_folder, exist_ok=True)
    delete_files_in_frames()  # delete all files in 'frames' folder in case there's unwanted files

    if input_path.endswith('.gif'):
        with Image.open(input_path) as im:
            for i, frame in enumerate(ImageSequence.Iterator(im)):
                frame.save(os.path.join(output_folder, f"{i+100000}.png"))
    elif input_path.endswith('.mp4'):
        cap = VideoCapture(input_path)
        success, frame = cap.read()
        count = 0

        while success:
            imwrite(os.path.join(output_folder, f"{count + 100000}.png"), frame)
            success, frame = cap.read()
            count += 1

        cap.release()


def gif_wallpaper():
    path = get_gif_path()
    extract_frames(path)

    wallpaper_folder = os.path.join(os.getcwd(), 'frames')

    wallpaper_files = [f for f in os.listdir(wallpaper_folder) if f.endswith('.png')]

    if wallpaper_files:
        while True:
            for wallpaper in wallpaper_files:
                wallpaper_path = os.path.join(wallpaper_folder, wallpaper)
                # print(wallpaper_path)

                change_wallpaper(wallpaper_path)


if __name__ == "__main__":
    gif_wallpaper()
