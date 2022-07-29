# Hardware Bill of Materials (HBOM)

CycloneDX supports many types of components, including hardware devices, making it ideal for use with consumer electronics,
IoT, ICS, and other types of embedded devices. CycloneDX fills an important role in-between traditional eBOM and mBOM
use cases for hardware devices.

- Supports `device` as a first-class component type
- Utilizes a [formal and extensible taxonomy](https://github.com/CycloneDX/cyclonedx-property-taxonomy/blob/main/cdx/device.md) that defines a wide range of hardware devices and configurations

CycloneDX can represent any type of software component, service, and the firmware and hardware devices in an 'as-built'
product. A formal property taxonomy can be leveraged and extended to describe any type of hardware attribute or configuration.
CycloneDX can also reference documentation that may describe the 'recipe' for how the product is manufactured.  
Organizations, or entire industries, can also leverage multiple extension points to develop advanced models.

## PCIe SATA adapter board

This specific example is a PCIe SATA adapter board created by the [Computer Architecture Group, University of Cambridge 
Computer Laboratory](http://www.cl.cam.ac.uk/research/comparch/). The design and parts lists were derived from
https://github.com/ucam-comparch/pcie-sata-adaptor-board
