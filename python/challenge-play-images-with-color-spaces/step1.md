# Color Space Transformations

In this sub-challenge, you will implement a function that can convert an input image into different color spaces (**RGB**, **HSV**, and **LAB**).

## Requirements:

Please complete the `convert_color_space` function in the file `/home/labex/project/convert_color_space.py`.
And we provide an image file `images/img1.jpg` for you to test.

The function should have the following signature:

1. Reads an input image, and an input string, which can be **"RGB"**, **"HSV"** or **"LAB"**. Each of these three strings corresponds to a different color space.
2. Convert the input image into various color spaces.
3. The function outputs the numpy array of the original image, and the numpy array of the image in different color spaces.
4. The numpy array of the original image, referring to what you read through the `cv2.imread()` method. This array is not an **“RGB”** array, but a **"BGR"** array.
