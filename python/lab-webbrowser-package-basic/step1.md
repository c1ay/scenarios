# Opening a URL in a New Tab

The `webbrowser` module makes it easy to open a URL in a new browser tab. Let's start by importing the webbrowser module and calling `the open_new_tab()` function to open a URL:

## Open the Python Shell

Open the Python shell by typing the following command in the terminal.

```bash
python3
```

Import the web browser module and use the `open_new_tab()` function to open the URL.

```python
import webbrowser
url = "https://www.google.com"
webbrowser.open_new_tab(url)
```

When you run this code, a new browser tab should open and navigate to Google's homepage.
