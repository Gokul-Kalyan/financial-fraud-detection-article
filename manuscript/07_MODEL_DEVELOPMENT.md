# Model Development

With the data prepared, the next step was to train machine learning models capable of distinguishing legitimate transactions from fraudulent ones. Rather than selecting a single algorithm from the outset, multiple classification models were trained and evaluated to understand their strengths and limitations on the dataset.

The initial experiments included widely used supervised learning algorithms, providing a baseline for comparison. Each model was trained using the same preprocessing pipeline and evaluated under identical conditions to ensure a fair comparison.

Given the highly imbalanced nature of the dataset, overall accuracy was not considered a sufficient measure of performance. Instead, greater emphasis was placed on precision, recall, and the F1-score, as these metrics better reflect a model's ability to identify fraudulent transactions while minimizing false positives.

Among the evaluated models, **CatBoost** consistently delivered the strongest overall performance. Its ability to capture complex relationships within the engineered features, combined with efficient handling of structured tabular data, resulted in a better balance between fraud detection capability and prediction reliability.

The selected CatBoost model was then saved and integrated into the deployment pipeline, forming the core of the fraud detection system presented in this project.

![Figure 5: Model Evolution](../figures/5_model_evolution.png)

*Figure 5. Evolution of the model development process, from addressing class imbalance with SMOTE during experimentation to selecting a production-ready CatBoost model using built-in balanced class weights for a simpler and more memory-efficient deployment pipeline.*

The following chapter evaluates the performance of the selected model in greater detail and compares its results against the alternative approaches considered during development.
