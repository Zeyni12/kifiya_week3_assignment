import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class InsuranceDataAnalysis:
    def __init__(self, data):
        self.data = data

    def descriptive_statistics(self):
        """Generate descriptive statistics grouped by province and gender."""
        return self.data.groupby(['Province', 'Gender']).agg(
            Avg_Total_Claim=('TotalClaims', 'mean'),
            Avg_Premium=('TotalPremium', 'mean'),
            Count=('TotalClaims', 'size')
        ).reset_index()

    def visualize_total_claims_by_province(self):
        """Bar chart for total claims by province."""
        grouped = self.data.groupby('Province')['TotalClaims'].mean().reset_index()
        grouped.plot(kind='bar', x='Province', y='TotalClaims', legend=False, figsize=(8, 5))
        plt.title('Average Total Claims by Province')
        plt.ylabel('Average Total Claims')
        plt.xlabel('Province')
        plt.show()

    def visualize_premiums_by_province(self):
        """Bar chart for premiums by province."""
        grouped = self.data.groupby('Province')['TotalPremium'].mean().reset_index()
        grouped.plot(kind='bar', x='Province', y='TotalPremium', legend=False, figsize=(8, 5))
        plt.title('Average Premiums by Province')
        plt.ylabel('Average Premiums')
        plt.xlabel('Province')
        plt.show()

    def visualize_premium_to_claim_ratio_by_gender(self):
        """Violin plot for premium-to-claim ratio by gender."""
        self.data['Premium_to_Claim_Ratio'] = self.data['TotalPremium'] / (self.data['TotalClaims'] + 1)
        sns.violinplot(x='Gender', y='Premium_to_Claim_Ratio', data=self.data)
        plt.title('Premium-to-Claim Ratio by Gender')
        plt.ylabel('Premium-to-Claim Ratio')
        plt.xlabel('Gender')
        plt.show()

    def visualize_premium_to_claim_ratio_by_zipcode(self):
        """Bar chart for premium-to-claim ratio by PostalCode."""
        self.data['Premium_to_Claim_Ratio'] = self.data['TotalPremium'] / (self.data['TotalClaims'] + 1)
        grouped = self.data.groupby('PostalCode')['Premium_to_Claim_Ratio'].mean().reset_index()
        grouped.plot(kind='bar', x='PostalCode', y='Premium_to_Claim_Ratio', legend=False, figsize=(8, 5))
        plt.title('Average Premium-to-Claim Ratio by PostalCode')
        plt.ylabel('Average Premium-to-Claim Ratio')
        plt.xlabel('PostalCode')
        plt.show()

    def highlight_profitable_segments(self):
        """Identify segments with high premium-to-claim ratios."""
        self.data['Premium_to_Claim_Ratio'] = self.data['TotalPremium'] / (self.data['TotalClaims'] + 1)
        grouped = self.data.groupby(['Province', 'Gender']).agg(
            Avg_Ratio=('Premium_to_Claim_Ratio', 'mean'),
            Count=('TotalClaims', 'size')
        ).reset_index()
        return grouped[grouped['Avg_Ratio'] > 1.5]

    def identify_low_risk_targets(self):
        """Identify segments with below-average total claims."""
        grouped = self.data.groupby(['Province', 'Gender']).agg(
            Avg_Total_Claim=('TotalClaims', 'mean')
        ).reset_index()
        avg_claim = grouped['Avg_Total_Claim'].mean()
        return grouped[grouped['Avg_Total_Claim'] < avg_claim]

# Example usage:
# df = pd.DataFrame({...})  # Load your data here
# analysis = InsuranceDataAnalysis(df)
# grouped_stats = analysis.descriptive_statistics()
# analysis.visualize_total_claims_by_province()
# analysis.visualize_premiums_by_province()
# analysis.visualize_premium_to_claim_ratio_by_gender()
# analysis.visualize_premium_to_claim_ratio_by_zipcode()
# profitable_segments = analysis.highlight_profitable_segments()
# low_risk_targets = analysis.identify_low_risk_targets()
