import secp256k1
from solana.account import PrivateKey
from solana.client import Client

# Generate a new private key
private_key_bytes = secp256k1.PrivateKey()

# Create a PrivateKey object from the private key bytes
private_key = PrivateKey.from_bytes(private_key_bytes)

# Get the public key and address for the Solana account
public_key = private_key.public_key
address = private_key.public_key.to_string()

# Create a client instance
client = Client()

# Check the balance of the Solana account
response = client.get_balance(address)
balance = response['result']['balance']

# Print the balance of the Solana account
print(f'The balance of the Solana account is: {balance}')
