# Vulnerability Exploitability Exchange (VEX)

Known vulnerabilities inherited from the use of third-party and open source software and the exploitability of the vulnerabilities
can be communicated with CycloneDX. Previously unknown vulnerabilities affecting both components and services may also be disclosed
using CycloneDX, making it ideal for both VEX and security advisory use cases.
- VEX information can be represented inside an existing BOM, or in a dedicated VEX BOM
- Supports known and unknown vulnerabilities against components and services
- Communicates the vulnerability details, exploitability, and detailed analysis

## Independent BOM and VEX BOM
Inventory described in a BOM (SBOM, SaaSBOM, etc) will typically remain static until such time the inventory changes.
However, vulnerability information is much more dynamic and subject to change. Therefore, it is recommended to decouple
the VEX from the BOM. This allows VEX information to be updated without having to create and track additional BOMs.

VEX is an integral part of the CycloneDX specification providing the convenience of leveraging a single format and tool chain.

<img src="https://cyclonedx.org/theme/assets/images/vexbom.svg" width="500" alt="Independent BOM and VEX Document">

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

## BOM With Embedded VEX

<img src="https://cyclonedx.org/theme/assets/images/embedded-vex.svg" width="167" alt="BOM With Embedded VEX">

CycloneDX also supports embedding VEX information inside a BOM, thus having a single artifact that describes both
inventory and VEX data. There are several uses for embedding VEX data including:

* Audit use cases where inventory and vulnerability data need to be captured at a specific point in time
* Automated security tools may opt to create a single BOM with embedded vulnerability or VEX data for convenience and portability

## CycloneDX and Third-Party Advisory Formats

Every component or service defined in a CycloneDX BOM may optionally define external references to security advisory
feeds. CycloneDX is agnostic to the advisory format, however, the
[Common Security Advisory Framework (CSAF)](https://www.oasis-open.org/committees/csaf), an OASIS Open standard, is
recommended. Refer to the [Security Advisories Use Case](https://cyclonedx.org/use-cases/#security-advisories) for more information.

CSAF also supports an optional VEX profile which can be used with CycloneDX.

## High-Level Object Model
![CycloneDX Object Model Swimlane](https://cyclonedx.org/theme/assets/images/CycloneDX-Object-Model-Swimlane.svg)
