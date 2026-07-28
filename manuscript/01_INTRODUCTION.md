# Introduction

A few months ago, I came across an online store advertising premium shirts at an unbelievably low price. The website looked convincing, the offer seemed genuine, and I completed the purchase without giving it much thought. Days passed with no order confirmation, no shipment updates, and eventually, I realized I had fallen victim to an online shopping scam.

Fortunately, the financial loss was small. What stayed with me, however, was not the ₹200 I lost but the question it raised: **How do financial systems identify and stop fraudulent transactions?** That curiosity became the starting point of this project.

That question led me down a path I hadn't expected. I began exploring how banks and payment platforms detect fraudulent transactions, the challenges they face, and the role machine learning plays in identifying suspicious patterns hidden within millions of legitimate transactions. The more I learned, the more I realized that building an effective fraud detection system involves far more than training a machine learning model.

Driven by that curiosity, I decided to build an end-to-end machine learning pipeline using a large-scale financial transaction dataset. The goal was not simply to achieve high predictive performance, but to understand every stage of the development process—from exploring the data and engineering meaningful features to comparing machine learning models, evaluating their performance, deploying the final solution with Streamlit, and documenting the project in a structured and reproducible manner.

This article documents that engineering journey. Rather than presenting only the final results, I will walk through the decisions, challenges, and lessons that shaped the project from start to finish. Whether you're a machine learning enthusiast, a student building your first end-to-end project, or an aspiring ML engineer looking to strengthen your portfolio, I hope this article provides practical insights into building a complete machine learning solution.

Let's begin by understanding the problem of financial transaction fraud and why it remains one of the most challenging applications of machine learning.

