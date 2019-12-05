import pybitcointools

# Generate a random private key
valid_private_key = False
while not valid_private_key:
    private_key = pybitcointools.random_key()
    decoded_private_key = pybitcointools.decode_privkey(private_key, 'hex')
    valid_private_key = 0 < decoded_private_key < pybitcointools.N

print "Private Key (hex) is:", private_key
print "Private Key (decimal) is:", decoded_private_key

# Convert private key to WIF format
wif_encoded_private_key = pybitcointools.encode_privkey(decoded_private_key,
                                                        'wif')
print "Private Key (WIF) is:", wif_encoded_private_key

# Add suffix "01" to indicate a compressed private key
compressed_private_key = private_key + '01'
print "Private Key Compressed (hex) is:", compressed_private_key

# Generate a WIF format from the compressed private key (WIF-compressed)
wif_compressed_private_key = pybitcointools.encode_privkey(
    pybitcointools.decode_privkey(compressed_private_key, 'hex'), 'wif')
print "Private Key (WIF-Compressed) is:", wif_compressed_private_key

# Multiply the EC generator point G with the private key to get a public key
# point
public_key = pybitcointools.fast_multiply(pybitcointools.G,
                                          decoded_private_key)
print "Public Key (x,y) coordinates are:", public_key

# Encode as hex, prefix 04
hex_encoded_public_key = pybitcointools.encode_pubkey(public_key, 'hex')
print "Public Key (hex) is:", hex_encoded_public_key

# Compress public
