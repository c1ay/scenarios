# Government Office

Your task is to write a Python function called `search_document` that takes in two parameters:

- `inventory` (a dictionary): represents the current inventory of the office where the keys are the document names and the values are the locations where the documents are stored.
- `document_name` (a string): represents the name of the document that needs to be searched.

## Example Usage

```python
inventory = {"document1": "A1", "document2": "B2", "document3": "C3"}
document_name = "document2"

location = search_document(inventory, document_name)
print(location)
```

Output:

```python
B2
```

```python
inventory = {"document1": "A1", "document2": "B2", "document3": "C3"}
document_name = "document4"

location = search_document(inventory, document_name)
print(location)
```

Output:

```python
Document not found.
```

## TODO

- Complete `search_document.py`

## Requirements

- The function should return the location where the document is stored if it is found in the inventory.
- If the document is not found in the inventory, the function should return a message indicating that the document was not found.
