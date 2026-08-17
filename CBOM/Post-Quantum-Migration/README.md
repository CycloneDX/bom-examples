# Post-Quantum Migration CBOM Example

This example models an application during a staged migration from classical public-key cryptography to post-quantum cryptography. The inventory contains ML-KEM-768 and ML-DSA-65 alongside ECDH P-256 and ECDSA P-256, reflecting a period in which compatibility or migration constraints require both algorithm families to remain present.

The application depends on an illustrative cryptographic library, and the library provides the four algorithm assets. This separation allows consumers to distinguish the application that uses a cryptographic implementation from the implementation boundary and the algorithms it provides.

## Interpreting the inventory

`nistQuantumSecurityLevel` records the NIST security category associated with the parameter set. A value of `0` on the classical ECDH and ECDSA assets means that they do not provide security against a cryptographically relevant quantum computer. It does not mean that they provide no classical security.

The presence of an algorithm in a CBOM does not establish that:

- the implementation is correct or side-channel resistant;
- the application negotiates or combines algorithms securely;
- keys and other cryptographic material are managed securely;
- every runtime-selected algorithm was discovered; or
- migration to post-quantum cryptography is complete.

Inventory consumers should retain unresolved or dynamically selected algorithms as explicit unknowns rather than classifying them as quantum-safe. Migration decisions also require deployment context, protected-data lifetime, protocol behavior, interoperability testing, and implementation validation.

## Source fixture

[`fixture/app.py`](fixture/app.py) is a deliberately small, non-executable discovery fixture. It identifies the algorithm selections and operations represented by the CBOM without including keys, ciphertexts, signatures, or generated cryptographic material. It was reduced from the open-source [`AAH_PostQuantum_Cryptography`](https://github.com/AAH20/AAH_PostQuantum_Cryptography) implementation for use as a stable inventory example.
