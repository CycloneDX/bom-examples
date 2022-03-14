# CISA VEX Use Case 3

### Single Product, Single Version, Multiple Vulnerabilities, Multiple Statuses

In this use case, Example Company has fielded product GHI. The company makes statements about each version of its product in a different VEX file.  For a given version of a given product, a particular vulnerability instance can only have a single status. However, other instances of the same or different vulnerabilities may have different statuses.

Product GHI’s TCP/IP-Stack is based on Treck’s stack, with some custom implementation and modifications. When Ripple20 was disclosed, Example Company’s PSIRT released a VEX file stating that product GHI’s version 17.4 is not affected by some of the Ripple20 vulnerabilities (namely CVE-2020-11897, CVE-2020-11902, CVE-2020-11899, CVE-2020-11905, CVE-2020-11906, CVE-2020-11913), but that it is affected by certain others (CVE-2020-11898, CVE-2020-11907, CVE-2020-11909, CVE-2020-11910, CVE-2020-11911). Moreover, others are still under investigation (CVE-2020-11896, CVE-2020-11900, CVE-2020-11904, CVE-2020-11903, CVE-2020-11908) and some are fixed already (CVE-2020-11901, CVE-2020-11912, CVE-2020-11914).
