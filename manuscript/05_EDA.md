# Exploratory Data Analysis

Exploratory Data Analysis (EDA) was performed to better understand the dataset before developing machine learning models. The analysis focused on examining data quality, feature distributions, transaction characteristics, and the distribution of fraudulent and legitimate transactions.

The dataset contained **6,362,620 transaction records** across eleven features and showed no significant missing values, allowing the analysis to proceed without extensive data cleaning. One of the most important findings was the severe class imbalance, where fraudulent transactions represented only a small fraction of the dataset. This highlighted the need to evaluate models using precision, recall, and F1-score rather than accuracy alone.

The analysis also revealed variations in transaction types and a right-skewed distribution of transaction amounts, providing valuable insights for feature engineering and model development. These observations established a strong understanding of the data and guided the preprocessing decisions discussed in the next chapter.
