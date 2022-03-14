# CISA VEX Use Case 9

### Multiple Product Lines, Multiple Vulnerabilities, Multiple Statuses

There are instances where vendors group products into product lines. For example, MicroLogix 1400 is a product line of programmable logic controllers offered by Rockwell Automation, Inc., that includes products such as 1766-L32BWA and 1766-L32BXBA. Rather than call out each of those product numbers individually, some Vendors may choose to state the exploitability of the entire product line, for one or more vulnerabilities

Example Company has a product line of Ethernet switches: PROD_ALPHA, which includes products MNO, PQR, and STU, as well as a product line of remote terminal units, PROD_BETA, which includes products VWX and YZA. When CVE-2021-44228 and CVE-2021-45105 are released for the Log4j vulnerabilities, Example Company produces a VEX document stating that these vulnerabilities are not exploitable (status: KNOWN_NOT_AFFECTED) in any of the products within product line PROD_ALPHA, but are exploitable (status: KNOWN_AFFECTED) in all products within PROD_BETA. Example Company decides to communicate that these entire product lines are affected/not-affected, as opposed to each product individually.

<hr>

CycloneDX Response:

While this is a valid use case that suppliers may want to do, it violates the objectives defined in the CISA document, specifically: "Second, VEX data can support more effective use of Software Bills of Materials (SBOM) data. The ultimate goal of VEX is to support greater automation across the vulnerability ecosystem, including disclosure, vulnerability tracking, and remediation."

SBOMs, as currently defined, do not support product families, which themselves are references to lists of products externalized and solely maintained by the vendor. Therefore it is not possible to achieve the automation objectives outlined in the introduction with this use case. Additionally, CycloneDX does not support this use case and there currently are no plans to do so.

This use case greatly expands the number of stakeholders necessary to create and maintain an accurate VEX. VEX would normally be created by technical security teams. However, if marketing changes product families, or new products are introduced, or M&A occurs which alters product families, all of these stakeholders would need to be part of an organizations process which would trigger updates to VEX.