# Deployment

Building an accurate model was only part of the project. The final objective was to make it accessible through a production-oriented inference pipeline capable of processing new transactions consistently and reliably.

Each incoming transaction first undergoes **Pydantic validation** to ensure that the request contains valid and complete information. The validated data is then passed through the same feature preparation pipeline used during model training, ensuring that inference remains consistent with the training process.

The processed features are evaluated by the trained **CatBoost** model, which produces a fraud probability. Instead of returning only a binary prediction, the system applies a simple decision engine to classify the transaction into operational outcomes such as **Approve**, **Verify**, or **Block** based on predefined probability thresholds.

Every prediction is logged in a **PostgreSQL** database for traceability and future analysis before the API returns a structured JSON response to the client.

This deployment demonstrates how a trained machine learning model can be integrated into a complete inference workflow, transforming experimental results into a practical fraud detection service.
