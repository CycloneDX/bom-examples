# Operations Bill of Materials (OBOM)

CycloneDX is a full-stack bill of materials standard supporting entire runtime environments consisting of hardware,
firmware, containers, operating systems, applications and their libraries. Coupled with the ability to specify
configuration makes CycloneDX ideal for Operational Bill of Materials. OBOM is a security behavior defined in BSIMM and
similar maturity models.

CycloneDX properties provide a mechanism to store configuration on a per-component and per-service basis inside a BOM.
The specification also provides a mechanism to store URLs to documentation, including configuration management systems.

## Example-1 Decoupled

This example describes an application called Keycloak, its software inventory and the runtime and environmental 
configuration. Inventory described in an SBOM will typically remain static until such time the inventory changes. 
However, operational information is much more dynamic and subject to change. Therefore, it is recommended to decouple 
the OBOM from the SBOM as this example illustrates. This allows operational information to be updated without having to 
create and track additional SBOMs.

The example is not complete, but does attempt to show the types of data that can be captured for operational concerns. 
The example uses CycloneDX properties to store this data. All properties start with `internal`, 
which is a reserved namespace defined in the [CycloneDX Property Taxonomy](https://github.com/CycloneDX/cyclonedx-property-taxonomy).

### Referencing BOMs

| BOM Type | Filename |
| -------- | -------- |
| Software Bill of Materials (SBOM) | [bom.json](bom.json) |
| Operations Bill of Materials (OBOM) | [obom.json](obom.json) |

The OBOM references the SBOM by the SBOMs serial number and version. The syntax is:

```
urn:cdx:serialNumber/version#bom-ref
```

| Field        | Description |
| ------------ | ----------- |
| serialNumber | The unique serial number of the BOM. The serial number MUST conform to RFC-4122. |
| version      | The version of the BOM. The default version is `1`. |
| bom-ref      | The unique identifier of the component, service, or vulnerability within the BOM. |

Because this example is referencing a BOM, and not a component within a BOM, the `bom-ref` is omitted.
