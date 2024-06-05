from app import recognizeHandGesture
import base64

# get base64 image buffer from browser
# with open('test.txt', 'r') as file:
#     # Read the entire contents of the file
#     base64_image_buffer = file.read()

# image_data = base64.b64decode(base64_image_buffer)
gesture = recognizeHandGesture(image_data)
print(gesture)