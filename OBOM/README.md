# Operations Bill of Materials (OBOM)

CycloneDX is a full-stack bill of materials standard supporting entire runtime environments consisting of hardware, 
firmware, containers, operating systems, applications and their libraries. Coupled with the ability to specify 
configuration makes CycloneDX ideal for Operational Bill of Materials. OBOM is a security behavior defined in BSIMM and 
similar maturity models.

CycloneDX properties provide a mechanism to store configuration on a per-component and per-service basis inside a BOM. 
The specification also provides a mechanism to store URLs to documentation, including configuration management systems.

## Independent OBOM and SBOM
Inventory described in a SBOM will typically remain static until such time the inventory changes.
However, operational information may be dynamic and subject to change. Therefore, it is recommended to decouple
the OBOM from the SBOM. This allows OBOM information to be updated without having to create and track additional SBOMs.

<img src="https://cyclonedx.org/theme/assets/images/obom-sbom.svg" width="500" alt="Independent SBOM and OBOM Document">

## High Level Object Model
![CycloneDX Object Model Swimlane](https://cyclonedx.org/theme/assets/images/CycloneDX-Object-Model-Swimlane.svg)