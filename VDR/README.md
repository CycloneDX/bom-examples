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

Below is a brief comparison between VDR and VEX.

|                         | VDR                                                                                                                                                                                   | VEX                                                                                                                                                                                                           |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| __Scope__               | Product or dependencies (components and services)                                                                                                                                     | Product, product family, or entire organization                                                                                                                                                               |
| __Expectation__             | Asserts all vulnerabilities affecting a product, component or service                                                                                                                 | Negative security advisory intended to state all vulnerabilities a product is not affected by                                                                                                                 |
| __Vulnerability types__     | Known and previously unknown vulnerabilities                                                                                                                                          | Known vulnerabilities                                                                                                                                                                                         |
| __Analysis decision__       | Describes the impact of the vulnerability (if any), vendor response, and expectations                                                                                                 | Describes the impact of the vulnerability (if any), vendor response, and expectations                                                                                                                         |
| __Publish lifecycle__       | &bull;&nbsp;Published alongside SBOM<br/>&bull;&nbsp;Continuously updated when new vulnerabilities <u>affecting the product</u> are discovered or when analysis decisions are updated | &bull;&nbsp;Published alongside SBOM (except CSAF)<br/>&bull;&nbsp;Continuously updated when new vulnerabilities are published or when analysis decisions are updated                                         | 
| __Agency support__          | [NIST SP 800-161](https://csrc.nist.gov/publications/detail/sp/800-161/rev-1/final) recommendation                                                                                    | CISA (pseudo specification)                                                                                                                                                                                   |
| __Limitations__             | Overarching statements (e.g. entire organization) are not permitted                                                                                                                   | Cannot describe vulnerabilities that do not already have an identifier (e.g. previously unknown vulnerabilities)                                                                                              |
| __Formats and standards__   | CycloneDX, SAG-PM VDR                                                                                                                                                                 | CycloneDX, CSAF, OpenVEX (in development)                                                                                                                                                                     |
| __Risk transparency__       | Communicates risk and modified severity (CVSS temporal and environmental metrics, OWASP risk rating, etc) as it relates to the product                                                | Does not communicate risk or modified severity                                                                                                                                                                |
| __Attestation support__     | VDR is an attestation that the vendor has checked product dependencies for vulnerabilities and has communicated them                                                                  | VEX is an attestation of what vulnerabilities do not affect a product, and optionally, the ones that do. VEX does not require a vendor to check product dependencies for vulnerabilities, or communicate them | 
| __Tool availability__       | Widespread                                                                                                                                                                            | Limited                                                                                                                                                                                                       |
| __Results__                 | Consumers have a clear understanding of the vulnerabilities affecting a product and the vulnerabilities that do not                                                                   | Consumers have a clear understanding of the vulnerabilities affecting a product and the vulnerabilities that do not                                                                                           |

For an in-depth comparison between VDR and VEX, refer to [Vulnerability and Exploitability Transparency - VDR & VEX](https://owasp.org/blog/2023/02/07/vdr-vex-comparison)

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
