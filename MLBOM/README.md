# Machine Learning Bill of Materials (ML-BOM)

A Machine Learning Bill of Materials (ML-BOM) describes AI/ML inventory such as
models, datasets, and related artifacts. CycloneDX supports ML-BOM use cases with
component types such as `machine-learning-model` and `data`, plus `modelCard`
metadata for model transparency.

This directory contains compact examples that are intended to be easy to inspect,
validate, and reuse as starting points.

| Example | Description |
|---------|-------------|
| [Model Card With Dataset References](Model-Card-With-Dataset) | A schema-valid ML-BOM showing one application, one model component, two dataset components, an inline model card, dataset references, and dependency links. |
