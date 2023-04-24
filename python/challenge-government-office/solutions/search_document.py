# define a function that takes two arguments, an inventory and document_name
def search_document(inventory, document_name):
    # check if the given document_name is present in the inventory
    # if yes, return the value of the document_name key from inventory
    if document_name in inventory:
        return inventory[document_name]
    # else, return a string value "document not found."
    else:
        return "Document not found."
