from flask import Flask, request, render_template
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

app = Flask(__name__)

# Load private key for decryption
# with open('keys/private_key.pem', 'rb') as key_file:
#     private_key = RSA.import_key(key_file.read())
#     decryptor = PKCS1_OAEP.new(private_key)

@app.route('/', methods=['GET', 'POST'])
def index():
    app.logger.info(f"Received request: {request.method} {request.url}")
    app.logger.info(f"Headers: {request.headers}")
    app.logger.info(f"Body: {request.get_data(as_text=True)}")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
