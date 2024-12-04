# Machine Learning Bill of Materials (ML-BOM)

Machine learning, particularly AI, often lacks transparency regarding models' usage, creation processes, and lifecycle within organizations. The Machine Learning Bill of Materials (ML-BOM) builds on CycloneDX to offer a detailed representation of machine learning models, datasets, and related artifacts. ML-BOM empowers organizations to document, manage, and secure their machine learning assets while enhancing visibility into model lineage and mitigating supply chain risks.

## Features of ML-BOM
- Captures machine learning models, datasets, libraries, and their interdependencies.
- Documents comprehensive metadata about models, including architecture, training datasets, performance metrics, and ethical considerations.
- Facilitates model lineage tracking, integrating it into the lifecycle management of ML components from design to decommission.
- Enhances transparency by illustrating how software incorporates ML/AI components and embedding them within the broader SBOM framework.
- Highlights critical details about model biases and ethical implications stemming from training datasets, while identifying and classifying the presence of sensitive data in datasets or trained models.

## Key Components

### 1. **Machine Learning Models**
ML-BOM can document models and their parameters, including Model Architecture and Performance Metrics, and Ethical and Fairness Considerations

### 2. **Datasets**
Datasets used for training, validation, and inference can be described with:
- **Data Classification**: Tags to specify sensitivity and value.
- **Data Governance**: Ownership, stewardship, and custodianship details.
- **Sensitive Data**: Annotations for datasets containing sensitive information.

### 3. **Libraries**
ML-BOM provides a detailed overview of the dependencies models have on specific ML/AI libraries, ensuring transparency and traceability in their usage, including their versioning, licenses, and security considerations


## High-Level Object Model
![CycloneDX Object Model Swimlane](https://cyclonedx.org/theme/assets/images/CycloneDX-Object-Model-Swimlane.svg)
