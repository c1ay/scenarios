# Displaying the image

To display the image, we use the `cv2.imshow()`function. The function takes two arguments: the window name and the image to display.

Also, we use the `cv2.waitKey()` function to wait for a key press. This is required to keep the window open until the user presses a key. The `cv2.waitKey()` function takes a single argument, which is the number of milliseconds to wait for a key press. If the user presses a key within the specified time, the function returns the key code. Otherwise, it returns `-1`. In this case, we pass `0` to wait indefinitely for a key press.
Finally, we use the `cv2.destroyAllWindows()` function to close all the windows. This is optional, but it is good practice to close all the windows before exiting the `Python interpreter`program.

## Detail

Input `python` to start the process of python interpreter. Then input the following code.

```python

window_name = 'Image'
# Display the image, image has been loaded in the previous steps
cv2.imshow(window_name, image)

# Wait for a key press and close the window
cv2.waitKey(0)

# destroy the window after you showing the image
cv2.destroyAllWindows()
```

## NOTE

1. You can change the `window_name` for your code and see the result.
2. You can change the parameter of `waitKey` for your code and see the result.
3. For your convenience, we removed the correctness detection of image loading in this step.
4. Note that you are using a _Python interpreter_, so the program does not end immediately after `imshow`, but if you are executing a _Python file_, you must use `waitKey` to ensure that the window does not close after `imshow`.
