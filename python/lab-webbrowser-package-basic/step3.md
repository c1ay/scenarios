# Displaying Local HTML Files

The `webbrowser` module can also be used to display HTML files. A simple HTML file named "example.html" is provided here.

We can use the `open_new_tab()` function to display this HTML file in a new browser tab:

```python
file_path = "/home/labex/project/example.html"
webbrowser.open_new_tab(file_path)
```

When you run this code, a new browser tab should open and display the contents of example.html.
