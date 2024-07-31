total_items = 100  # Total number of items to process
for i in range(total_items):
    # Process the item
    # Update the progress bar
    progress = (i + 1) / total_items  # Calculate the progress percentage
    print(f'Progress: {"#" * int(progress * 20)} {int(progress * 100)}%', end='\r')  # Update the progress bar
    # Perform the processing for the current item
    # ...
