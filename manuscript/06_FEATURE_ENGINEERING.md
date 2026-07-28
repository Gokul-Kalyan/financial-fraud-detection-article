# Feature Engineering

After exploring the dataset, the next step was transforming the raw transaction data into features better suited for machine learning. Rather than relying solely on the original attributes, the preprocessing pipeline focused on preserving information that could improve the model's ability to distinguish between legitimate and fraudulent transactions.

Identifier columns that did not generalize to unseen customers were removed to prevent the model from learning account-specific patterns. Transaction categories were encoded into numerical values, and additional behavioural features were engineered using account balances and transaction amounts. These derived features captured characteristics such as balance changes, transaction-to-balance relationships, and unusually large transfers, providing richer information than the raw attributes alone.

![](../figures/4_feature_engineering_process.png)

*Figure 4. Feature engineering pipeline illustrating the transformation of raw transaction records into a model-ready dataset through data cleaning, categorical encoding, and the creation of engineered features that capture transaction behavior.*

The preprocessing pipeline was designed to be reusable, ensuring that identical feature transformations were applied during both model training and inference. This consistency helps prevent training-serving skew and supports reliable deployment of the final model.

With the data prepared, the next stage involved training and evaluating multiple machine learning models to identify the most effective approach for fraud detection.