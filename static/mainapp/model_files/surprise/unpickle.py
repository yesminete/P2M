import pickle

# Open the file containing the serialized data
with open('book_inner_id_to_raw.pickle', 'rb') as f:
    # Load the serialized data and reconstruct the Python object
    my_object = pickle.load(f)

# Now you can use the reconstructed object as normal
print(my_object)