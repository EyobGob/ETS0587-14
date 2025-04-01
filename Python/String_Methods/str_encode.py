text = "Hello, world!"

# Encode the string to bytes using UTF-8 (the default)
encoded_bytes = text.encode()

print(f"Original string: {text}")  # Output: Original string: Hello, world!
print(f"Encoded bytes: {encoded_bytes}") # Output: Encoded bytes: b'Hello, world!'

# Decode the bytes back to a string
decoded_string = encoded_bytes.decode()

print(f"Decoded string: {decoded_string}") # Output: Decoded string: Hello, world!  