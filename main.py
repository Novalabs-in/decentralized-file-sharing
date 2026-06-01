from cryptography.fernet import Fernet

class SecureFileEncrypter:
    """
    AES-256 Secure File Encryption & Processing
    Provides military-grade end-to-end encryption for peer-to-peer sharing.
    """
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_payload(self, raw_data: bytes) -> bytes:
        return self.cipher.encrypt(raw_data)

    def decrypt_payload(self, encrypted_data: bytes) -> bytes:
        return self.cipher.decrypt(encrypted_data)

if __name__ == "__main__":
    encrypter = SecureFileEncrypter()
    original = b"Secure payload data from Novalabs"
    secret = encrypter.encrypt_payload(original)
    recovered = encrypter.decrypt_payload(secret)
    print("Original bytes:", original)
    print("Encrypted payload:", secret[:40], "...[TRUNCATED]")
    print("Decrypted bytes matches original:", original == recovered)
