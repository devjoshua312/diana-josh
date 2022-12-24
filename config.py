<<<<<<< HEAD
from cryptography.fernet import Fernet

key = b'TDhO_Q7myKtEY1cclhFm4VCFPSBpC27J7B7jlclsFeU='
fernet = Fernet(key)

encOaik = b'gAAAAABjprgZVkjW2K2hrf46e-Tar7xgnCAuzpN_KXJK3mq0clVZdRkGAK4kXzBEVnTaaMaM42l7gl7_2LqcurjVLC1Laqr-zAiuzR0dnxvCbVegzcRwPKs4EURVfvBwTlr0pmENhfXU7w678hZMePyw6Eqm6jp6mQ=='

oaik = fernet.decrypt(encOaik).decode()
print(oaik)

encFsaik = b'gAAAAABjprir-ihI8zNijW6zRv_FCwcBVKgVjL_oMQnZ5-OMd_t0mtqM4lBgmhYZCvinre-7Fh989B_zXFoagIT7o9FOI4diPixJxeEDyw6Oxe598WQKj1GzPOa6Hs-7kK9B2YQpoLmw'

fsaik = fernet.decrypt(encFsaik).decode()
=======
oaik = "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"
fsaik = "hlgisaiod7itygI87ghv6YUFvb8967yrfvbski"
>>>>>>> 89b8517e8be6e37e6b65ba18ec7f79a7ebf7c4dc
