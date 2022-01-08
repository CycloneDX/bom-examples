# Operations Bill of Materials (OBOM)

CycloneDX is a full-stack bill of materials standard supporting entire runtime environments consisting of hardware,
firmware, containers, operating systems, applications and their libraries. Coupled with the ability to specify
configuration makes CycloneDX ideal for Operational Bill of Materials. OBOM is a security behavior defined in BSIMM and
similar maturity models.

CycloneDX properties provide a mechanism to store configuration on a per-component and per-service basis inside a BOM.
The specification also provides a mechanism to store URLs to documentation, including configuration management systems.

## Example-1 Standalone

This example describes an application called Keycloak, its software inventory and the runtime and environmental
configuration. Inventory described in an SBOM will typically remain static until such time the inventory changes.
However, operational information is much more dynamic and subject to change. Therefore, it is recommended to decouple
the OBOM from the SBOM. This allows operational information to be updated without having to create and track additional SBOMs.

This example however, contains both SBOM and OBOM data within a single BOM.

The example is not complete, but does attempt to show the types of data that can be captured for operational concerns.
The example uses CycloneDX properties to store this data. All properties start with `internal`,
which is a reserved namespace defined in the [CycloneDX Property Taxonomy](https://github.com/CycloneDX/cyclonedx-property-taxonomy).
