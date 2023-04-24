# Writing an image to a file

To save an image in a different format, we use the `cv2.imwrite()` function. The function takes two arguments: the file path and the image to save.

## Detail

Input `python` to start the process of python interpreter. Then input the following code.

```python

# Save the image in a different format, image has been loaded in the previous steps
cv2.imwrite('/home/labex/Desktop/Image.png', image)
```

## Note

1. In this case, we save the image **in the PNG format** (Image.png). The image is saved **in the same directory** (/home/labex/Desktop/) as the Python script.
2. For your convenience, we removed the correctness detection of image loading in this step.
