# Reading an image

To read an image from a file, we use the `cv2.imread()` function. The function takes the file path as an argument and returns the image as a NumPy array.

Image path is `/home/labex/Desktop/Image.jpg`

## Detail

Input `python` to start the process of python interpreter. Then input the following code.

```python
# Read the image
image = cv2.imread('/home/labex/Desktop/Image.jpg')

# Check if the image is loaded correctly
if image is None:
    print('Error: Image not found.')
else:
    print('Image loaded successfully.')

```

## Note

The `cv2.imread()` function returns `None` if the image is not found. In this case, we print an error message. Otherwise, we print a success message.
