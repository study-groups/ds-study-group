import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset (mock data for demonstration)
# Sample data structure: Sample ID, Taxon, Abundance, Health Status
data = {
    'Sample ID': np.arange(1, 11),
    'Taxon': ['Bacteroides', 'Firmicutes', 'Actinobacteria', 'Proteobacteria', 'Fusobacteria'] * 2,
    'Abundance': np.random.randint(100, 1000, size=10),
    'Health Status': ['Healthy', 'Disease'] * 5
}

df = pd.DataFrame(data)

# Step 2: Make a basic plot - Abundance of microbial taxa in samples
plt.figure(figsize=(10, 6))
sns.barplot(x='Taxon', y='Abundance', hue='Health Status', data=df)
plt.title('Microbial Taxa Abundance by Health Status')
plt.xlabel('Taxon')
plt.ylabel('Abundance')
plt.xticks(rotation=45)
plt.legend(title='Health Status')
plt.tight_layout()
plt.show()

# Data Science Investigation Suggestion:
"""
Given this dataset, a preliminary investigation could involve comparing the microbial diversity and abundance between healthy and diseased hosts. Using standard statistical tools and diversity indices (e.g., Shannon index, Simpson's diversity index), we can assess the impact of different health statuses on the gut microbiome's composition. Further, machine learning models like logistic regression or random forests could be employed to predict the health status of a host based on their gut microbiome profile. This analysis would provide insights into the microbiome's role in health and disease, serving as a foundation before exploring more complex analyses such as DNA-QAM coding.
"""
