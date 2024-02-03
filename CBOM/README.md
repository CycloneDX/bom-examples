# Cryptography Bill of Materials (CBOM)

A Cryptography Bill of Materials (CBOM) is an object model to describe cryptographic assets and their dependencies.
Support for CBOM is included in CycloneDX v1.6 and higher. Discovering, managing, and reporting on cryptographic assets
is necessary as the first step on the migration journey to quantum-safe systems and applications.

- As of v1.6, CycloneDX supports `cryptographic-asset` as a first-class component type

## CBOM Design
The overall design goal of CBOM is to provide an abstraction that allows modeling and representing crypto assets in a
structured object format. This comprises the following points.

1. Modelling cryptographic assets
   Cryptographic assets occur in several forms. Algorithms and protocols are most commonly implemented in specialized cryptographic libraries. They may, however, also be 'hardcoded' in software components. Certificates and related cryptographic material like keys, tokens, secrets, or passwords are other cryptographic assets to be modeled.

2. Capturing cryptographic asset properties
   Cryptographic assets have properties that uniquely define them and that make them actionable for further reasoning. For example, it makes a difference if one knows the algorithm family (e.g. AES) or the specific variant or instantiation (e.g. AES-128-GCM). This is because the security level and the algorithm primitive (authenticated encryption) are only defined by the definition of the algorithm variant. The presence of a weak cryptographic algorithm like SHA1 vs. HMAC-SHA1 also makes a difference. Therefore, the goal of CBOM is to capture relevant cryptographic asset properties.

3. Capturing crypto asset dependencies
   To understand the impact of a cryptographic asset, it is important to capture its dependencies. Cryptographic libraries 'implement' certain algorithms and protocols, but their implementation alone does not reflect their usage by applications. CBOM, therefore, differentiates between 'implements' and 'uses' dependencies. It is possible to model algorithms or protocols that use other algorithms (e.g., TLS 1.3 uses ECDH/secp256r1), libraries that implement algorithms, and applications that 'use' algorithms from a library.

4. Applicability to various software components
   CycloneDX supports various components such as applications, frameworks, libraries, containers, operating systems, devices, firmware, and files. CBOM extends this model and can communicate a component's dependency on cryptographic assets.

5. High compatibility to CycloneDX SBOM and related tooling
   CBOM is native to the CycloneDX standard. It integrates cryptographic assets as an additional component type in the CycloneDX schema and further extends dependencies with the ability to specify dependency usage and implementation details. CBOM data can be present in existing SBOMs or externalized into dedicated CBOMs, thus creating modularity, which may optionally have varying authentication and authorization requirements.

6. Enable automatic reasoning
   CBOM enables tooling to reason about cryptographic assets and their dependencies automatically. This allows checking for compliance with policies that apply to cryptographic use and implementation.


## High Level Object Model
![CycloneDX Object Model Swimlane](https://cyclonedx.org/theme/assets/images/CycloneDX-Object-Model-Swimlane.svg)