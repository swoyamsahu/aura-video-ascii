import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
import time
import sys
import os

# Configuration
VIDEO_PATH = "aura.mp4"
WIDTH = 48
HEIGHT = 42
FPS = 10
MAX_DURATION = 12
ASCII_CHARS = " `'.,-~:;+=*!#%@█"

def auto_contrast(img):
    hist = img.histogram()
    min_gray = next(i for i, v in enumerate(hist) if v > 0)
    max_gray = next(i for i in reversed(range(256)) if hist[i] > 0)
    scale = 255 / (max_gray - min_gray + 1e-5)
    lut = [max(0, min(255, int((i - min_gray) * scale))) for i in range(256)]
    return img.point(lut)

def enhance_image(img):
    img = auto_contrast(img)
    img = ImageEnhance.Contrast(img).enhance(2.6)
    img = ImageEnhance.Brightness(img).enhance(1.15)
    edge = img.filter(ImageFilter.FIND_EDGES)
    sharp = img.filter(ImageFilter.SHARPEN)
    return Image.blend(sharp, edge, 0.5)

def frame_to_ascii(frame):
    img = Image.fromarray(frame).convert("L")
    img = enhance_image(img)
    img = img.resize((WIDTH, HEIGHT))
    pixels = np.array(img)
    
    ascii_img = []
    for row in pixels:
        line = ''.join(ASCII_CHARS[int(p / 256 * len(ASCII_CHARS))] * 2 for p in row)
        ascii_img.append(" " + line)
    return '\n'.join(ascii_img)

def extract_frames():
    cap = cv2.VideoCapture(VIDEO_PATH)
    video_fps = cap.get(cv2.CAP_PROP_FPS) or 25
    interval = max(1, int(video_fps // FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    max_frames = total_frames
    if MAX_DURATION:
        max_frames = min(total_frames, int(FPS * MAX_DURATION))
    
    ascii_frames = []
    count = 0
    
    while cap.isOpened() and len(ascii_frames) < max_frames:
        ret, frame = cap.read()
        if not ret:
            break
        if count % interval == 0:
            ascii_frames.append(frame_to_ascii(frame))
        count += 1
    
    cap.release()
    return ascii_frames

def play_ascii_video(ascii_frames):
    os.system('cls' if os.name == 'nt' else 'clear')
    delay = 1 / FPS
    
    try:
        while True:
            for frame in ascii_frames:
                sys.stdout.write("\033c")
                sys.stdout.write(frame + "\n")
                sys.stdout.flush()
                time.sleep(delay)
    except KeyboardInterrupt:
        print("\n\033[1;32mThank you for cloning the Aura Farming ASCII video player! 😂\033[0m")
        print("If you enjoyed this project, please give the repo a star:")
        print("https://github.com/iamnaheem/aura-video-ascii\n")

def main():
    ascii_frames = extract_frames()
    play_ascii_video(ascii_frames)

if __name__ == "__main__":
    main()
