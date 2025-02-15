import numpy as np

# Generate a random encryption key (can be a string or a random array)
key = "random_encryption_key_1234"

# Save the encryption key to a .npy file
np.save("encryption_key.npy", np.array([key]))

print("Encryption key saved to 'encryption_key.npy'.")