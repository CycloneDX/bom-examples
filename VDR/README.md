# Vulnerability Disclosure Report (VDR)

Known vulnerabilities inherited from the use of third-party and open source software can be communicated with CycloneDX. 
Previously unknown vulnerabilities affecting both components and services may also be disclosed using CycloneDX, making 
it ideal for Vulnerability Disclosure Report (VDR) use cases.

[NIST SP 800-161: Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations](https://csrc.nist.gov/publications/detail/sp/800-161/rev-1/final) 
defines Vulnerability Disclosure Reports (VDR) as a best practice and recommends VDRs include:

- Analysis and findings describing the impact (or lack thereof) that a reported vulnerability has on a component or product
- Plans to address the vulnerability
- Signing the VDR with a trusted, verifiable, private key that includes a timestamp indicating the date and time of the VDR signature
- Publishing the VDR to a secure portal

## Distinction between Vulnerability Disclosure Report (VDR) and Vulnerability Exploitability eXchange (VEX)

|                         | VDR                                                                                                                                    | VEX                                                                                                                                                                                                                                                                                                                |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Scope                   | Product or dependencies (components and services)                                                                                      | Product, product family, or entire organization                                                                                                                                                                                                                                                                    |
| Expectation             | Asserts all vulnerabilities affecting a product, component or service                                                                  | Negative security advisory intended to state all vulnerabilities a product is not affected by                                                                                                                                                                                                                      |
| Analysis decision       | Describes impact of the vulnerability (if any), vendor response, and expectations                                                      | Describes impact of the vulnerability (if any), vendor response, and expectations                                                                                                                                                                                                                                  |
| Agency support          | [NIST SP 800-161](https://csrc.nist.gov/publications/detail/sp/800-161/rev-1/final) recommendation                                     | CISA (pseudo specification)                                                                                                                                                                                                                                                                                        |
| Vendor investment       | Moderate                                                                                                                               | High                                                                                                                                                                                                                                                                                                               |
| Consumer investment     | Low                                                                                                                                    | High                                                                                                                                                                                                                                                                                                               | 
| Limitations             | Overarching statements (e.g. entire organization) are not permitted                                                                    | Cannot describe previously unknown vulnerabilities affecting products or dependencies (components and services)                                                                                                                                                                                                    |
| Formats and standards   | CycloneDX, SAG-PM VDR                                                                                                                  | CycloneDX, CSAF                                                                                                                                                                                                                                                                                                    |
| Additional requirements | <li>SBOM and VDR must both be imported by consumer</li><li>SBOM and VDR analysis is optional</li>                                      | <li>SBOM and VEX must both be imported and analyzed by consumer.</li><li>Both vendor and consumer must either: <ol><li>Use the same sources of vulnerability intelligence</li><li>or agree on a least common denominator (NVD) thus limiting the breadth and accuracy of vulnerability intelligence</li></ol></li> |
| Risk transparency | Communicates risk and modified severity (CVSS temporal and environmental metrics, OWASP risk rating, etc) as it relates to the product | Does not communicate risk or modified severity                                                                                                                                                                                                                                                                     |
| Results                 | Consumers have a clear understanding of the vulnerabilities affecting a product and the vulnerabilities that do not                    | Consumers have a clear understanding of the vulnerabilities affecting a product and the vulnerabilities that do not                                                                                                                                                                                                |

## Independent BOM and VDR
Inventory described in a BOM (SBOM, SaaSBOM, etc) will typically remain static until such time the inventory changes.
However, vulnerability information is much more dynamic and subject to change. Therefore, it is recommended to decouple
the VDR from the BOM. This allows VDR information to be updated without having to create and track additional BOMs.

VDR is an integral part of the CycloneDX specification providing the convenience of leveraging a single format and tool chain.

<img src="https://cyclonedx.org/theme/assets/images/vdrbom.svg" width="500" alt="Independent BOM and VDR Document">

With CycloneDX, it is possible to reference a component, service, or vulnerability inside a BOM from other systems or
other BOMs. This deep-linking capability is referred to as BOM-Link.

**Syntax**:
```
urn:cdx:serialNumber/version#bom-ref
```

**Examples**:
```
urn:cdx:f08a6ccd-4dce-4759-bd84-c626675d60a7/1
urn:cdx:f08a6ccd-4dce-4759-bd84-c626675d60a7/1#componentA
```

| Field        | Description |
| ------------ | ----------- |
| serialNumber | The unique serial number of the BOM. The serial number MUST conform to RFC-4122. |
| version      | The version of the BOM. The default version is `1`. |
| bom-ref      | The unique identifier of the component, service, or vulnerability within the BOM. |


## High-Level Object Model
![CycloneDX Object Model Swimlane](https://cyclonedx.org/theme/assets/images/CycloneDX-Object-Model-Swimlane.svg)
