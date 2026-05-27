# ML Model Handoff

This example shows a CycloneDX Manufacturing Bill of Materials (MBOM) for a
fictional application that uses one machine-learning model.

The BOM demonstrates:

- a `machine-learning-model` component with an inline `modelCard`
- two `data` components referenced from `modelCard.modelParameters.datasets[]`
- dependency links from the application to the model and from the model to the datasets
- a `formulation[]` workflow with training, evaluation, and handoff tasks
- workflow outputs for metrics and a handoff evidence artifact

Metric values, dataset names, workflow commands, and URLs are illustrative. They
are included to demonstrate CycloneDX structure, not to make claims about a real
model, dataset, performance result, safety posture, compliance status, or
deployment.
