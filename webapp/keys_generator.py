from Crypto.PublicKey import RSA

# Generate a 2048-bit RSA key pair (private + public key)
key = RSA.generate(2048)

# Save the private key to a file
private_key = key.export_key()
with open("private_key.pem", "wb") as private_file:
    private_file.write(private_key)

# Save the public key to a file
public_key = key.publickey().export_key()
with open("public_key.pem", "wb") as public_file:
    public_file.write(public_key)
