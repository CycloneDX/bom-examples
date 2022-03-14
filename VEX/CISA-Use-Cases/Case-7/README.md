# CISA VEX Use Case 7

### Multiple Products, Multiple Versions, Single Vulnerability, Multiple Statuses

In this use case, Example Company has fielded products ABC and JKL and provided updates over time, so that there are multiple versions software. The new Log4j vulnerability, with associated CVE-2021-44228, has been identified in components of products ABC and JKL.

To make it easier for its customers to download and distribute VEX material, Example Company decides to communicate the exploitability status of products ABC and JKL in a single VEX document, as opposed to creating two separate VEX documents. Example Company prepares a VEX document to communicate the exploitability of CVE-2021-44228 in product ABC as before (see Use Case 6).

The VEX document also includes the assertion that the vulnerability disclosed in CVE-2021-44228 is exploitable (status: KNOWN_AFFECTED) in versions 4.5 to 5.0 of product JKL. Moreover, CVE-2021-44228 is not exploitable (status: KNOWN_NOT_AFFECTED) in product JKL versions 1.0 to 4.4. The mitigation for all versions of product JKL is to upgrade to the new version 5.1, in which the status of CVE-2021-44228 is FIXED.
