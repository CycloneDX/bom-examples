# Model Card With Dataset References

This example shows a compact ML-BOM for an application that uses one fictional
machine-learning model and two fictional datasets.

The BOM demonstrates:

- a `machine-learning-model` component with an inline `modelCard`
- `modelCard.modelParameters.datasets[]` entries that reference dataset
  components by `bom-ref`
- `data` components that include the recommended `data` property
- top-level dependency links from the model to the referenced datasets

All names, URLs, and metric values are illustrative. They are not statements
about a real model, dataset, performance result, license, safety posture, or
deployment.
