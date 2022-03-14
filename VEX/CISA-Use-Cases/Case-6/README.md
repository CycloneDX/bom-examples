# CISA VEX Use Case 6

### Single Product, Multiple versions, Single Vulnerability, Multiple Statuses

In this use case, Example Company has fielded product ABC and provided updates or otherwise updated it over time, so that there are multiple versions of the software. The new Log4j vulnerability, with associated CVE-2021-44228, has been identified in a component of product ABC.

Example Company concludes that some versions of product ABC are affected by CVE-2021-44228 (see Use Case 4). Example Company also concludes that there are some versions of product ABC that are not impacted by CVE-2021-44228. Example Company prepares a VEX document to communicate that the vulnerability is exploitable (status: KNOWN_AFFECTED) in versions 2.4, 2.6, and all versions from and including 2.9 to 4.1, but also not exploitable (status: KNOWN_NOT_AFFECTED) in versions 1.0 to 2.3, 2.5, and 2.7 to 2.8.
