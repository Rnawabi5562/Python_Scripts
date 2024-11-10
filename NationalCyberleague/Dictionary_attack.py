ciphertext = "37001e00070f001a1c0601071b01035d55371b1a500f1418114f03081918110b50131d0b54091909140254373f35552d1c0e1c0b1000130a51473a00541b1f47170713081515550f1a0b5005101a000a024701061d01171454" 
ciphertext_bytes = bytes.fromhex(ciphertext)

# Open the output file in write mode to save successful decryptions
with open("decryption_output.txt", "w") as output_file:
    with open("XOR_KeyBrute.txt", "r") as file:
        for line in file:
            print("Trying: " + line)
            key = line.strip().encode()
            decrypted = bytearray()

            for i in range(len(ciphertext_bytes)):
                decrypted.append(ciphertext_bytes[i] ^ key[i % len(key)])

            # Check if all decrypted bytes are printable ASCII characters
            if all(32 <= byte <= 126 for byte in decrypted):
                decrypted_text = decrypted.decode()  # Convert decrypted byte array to a string
                print("Decrypted (ASCII):", decrypted_text)
                
                # Write the successful decryption to the output file
                output_file.write(f"Key: {line.strip()} - Decrypted Text: {decrypted_text}\n")
