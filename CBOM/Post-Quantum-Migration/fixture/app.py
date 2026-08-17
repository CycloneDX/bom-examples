"""Static discovery fixture for a staged post-quantum migration inventory."""

POST_QUANTUM_KEY_ESTABLISHMENT = "ML-KEM-768"
POST_QUANTUM_SIGNATURE = "ML-DSA-65"

# Classical algorithms remain visible during the transition period.
CLASSICAL_KEY_ESTABLISHMENT = "ECDH-P-256"
CLASSICAL_SIGNATURE = "ECDSA-P-256-SHA-256"

CRYPTOGRAPHIC_OPERATIONS = {
    POST_QUANTUM_KEY_ESTABLISHMENT: ("keygen", "keyderive"),
    POST_QUANTUM_SIGNATURE: ("keygen", "sign", "verify"),
    CLASSICAL_KEY_ESTABLISHMENT: ("keygen", "keyderive"),
    CLASSICAL_SIGNATURE: ("keygen", "sign", "verify"),
}
