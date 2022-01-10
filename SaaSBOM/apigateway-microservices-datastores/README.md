# Software-as-a-Service BOM (SaaSBOM)

<img src="https://cyclonedx.org/theme/assets/images/dataflow-diagram-1.svg" width="500" alt="Dataflow Diagram" align="right">

Modern software often relies on external services, or is made up entirely of services. CycloneDX is capable of describing any type of service including:
- Microservice Architecture
- Service Orientated Architecture (SOA)
- Function as a Service (FaaS)
- n-Tier Architecture
- Actor model
- System of Systems

## Example with API Gateway, Microservices, and Datastores

This repository contains a SaaSBOM representing a very simple set of cloud services, including:
* API Gateway
* Three microservices
* A Postgres database
* A S3 bucket

## High Level Object Model
![CycloneDX Object Model Swimlane](https://cyclonedx.org/theme/assets/images/CycloneDX-Object-Model-Swimlane.svg)
