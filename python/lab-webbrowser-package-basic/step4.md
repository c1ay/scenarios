# Searching Google from Python

The `webbrowser` module can even be used to execute a Google search directly from the Python console. Let's create a function that takes a search query as an argument and uses the `webbrowser` module to execute a Google search:

```python
def google_search(query):
    url = "https://www.google.com/search?q=" + query
    webbrowser.open_new_tab(url)
```

Now we can call the `google_search()` function with a search query:

```python
google_search("python web scraping")
```

When you run this code, a new browser tab should open and display the Google search results for "python web scraping".
