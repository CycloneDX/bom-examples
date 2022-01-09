# Software Bill of Materials (SBOM)

A complete and accurate inventory of all first-party and third-party components is essential for risk identification.
BOMs should ideally contain all direct and transitive components and the dependency relationships between them.

CycloneDX far exceeds the [Minimum Elements for Software Bill of Materials](https://www.ntia.gov/files/ntia/publications/sbom_minimum_elements_report.pdf)
as defined by the [National Telecommunications and Information Administration (NTIA)](https://www.ntia.gov/) in response
to [U.S. Executive Order 14028](https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/).

Adopting CycloneDX allows organizations to quickly meet these minimum requirements and mature into using more
sophisticated use cases over time. CycloneDX is capable of achieving all SBOM requirements defined in the
[OWASP Software Component Verification Standard (SCVS)](http://owasp.org/scvs).

CycloneDX can represent any type of software component along with services the software relies on. Refer to [Use Cases](https://cyclonedx.org/use-cases)
for details on the many possibilities that exist for beginner, intermediate, and advanced
SBOM use cases.

## High-Level Object Model
![CycloneDX Object Model Swimlane](https://cyclonedx.org/theme/assets/images/CycloneDX-Object-Model-Swimlane.svg)
