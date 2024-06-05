Hand Gesture Recognition System


## Project setup

- Install all the dependencies

```

pip install -r requirements. txt

```

- Provide an image buffer as parameter to  ``base64.b64decode()``

```

image_data = base64.b64decode(base64_image_buffer)

```

- Pass the image_data as a parameter to the recognizeHandGesture() method.

```

gesture = recognizeHandGesture(image_data)

```

- Execute the code

```
 
python .\start.py

```
