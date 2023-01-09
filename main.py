import cv2
import argparse
import time

# Set up the argument parser
parser = argparse.ArgumentParser(description="Convert a video to ASCII art")
parser.add_argument("--height", type=int, default=60, help="Height of the ASCII video")
parser.add_argument("--width", type=int, default=80, help="Width of the ASCII video")
parser.add_argument("filename", help="Name of the video file")

# Parse the arguments
args = parser.parse_args()

# Open the AVI file using OpenCV
video = cv2.VideoCapture(args.filename)

# Set up the ASCII character set to use for the conversion
charset = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.  "
#charset = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^  "

start_time = time.time()

while True:

    current_time = time.time() - start_time

    # Get the frame corresponding of the current time
    video.set(cv2.CAP_PROP_POS_MSEC, current_time * 1000)
    # Read the frame
    ret, frame = video.read()
    # get total number of frames

    # Convert the frame to grayscale and resize it
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (args.width, args.height))

    # Iterate over the pixels in the frame and convert each one to ASCII
    ascii_frame = ""
    for row in gray:
        for pixel in row:
            ascii_frame += charset[int(pixel / 256 * len(charset))]
        ascii_frame += "\n"

    # Print the ASCII art to the console
    print(ascii_frame)
    time.sleep(1/30)

# Close the video file
video.release()

