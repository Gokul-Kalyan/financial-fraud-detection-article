# Deployment

Developing an accurate fraud detection model was only part of the project. To demonstrate how machine learning systems operate in production, the final solution was deployed as a RESTful API while incorporating practices that improve reproducibility, monitoring, and long-term maintainability.

Incoming transaction requests are first validated using Pydantic before undergoing the same preprocessing and feature engineering steps applied during training. The processed transaction is then evaluated by the production CatBoost model, which was configured with auto_class_weights="Balanced" to efficiently address class imbalance without requiring oversampled training data during deployment. Based on the predicted fraud probability, the API returns an appropriate decision while recording the transaction and prediction outcome for future analysis.

To ensure reproducible experimentation, MLflow was integrated into the training pipeline. Each training run records model parameters, evaluation metrics, and generated artifacts, allowing different experiments to be compared and reproduced. The selected production model is registered and versioned before being exported for deployment, separating experiment management from the inference service.

Beyond deployment, the platform incorporates data drift detection to monitor whether incoming transaction data continues to follow the statistical characteristics of the training dataset. Detecting distributional changes provides an early indication that model performance may degrade over time and that retraining could be required.

Together, automated deployment, experiment tracking, and continuous monitoring transform the project from a standalone machine learning model into a production-oriented fraud detection platform that follows modern MLOps practices.


![Figure 7: Production ML Lifecycle](../figures/7_MLflow_lifecycle.png)

*Figure 7. End-to-end machine learning lifecycle illustrating experiment tracking with MLflow, model registration, production deployment through FastAPI, and continuous monitoring using data drift detection to support reliable long-term operation.*