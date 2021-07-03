# Banking Behavioral Clustering
## Objective
Apply unsupervised learning strategies (PCA + K-means) to cluster customers by their demographics and behavior.

Determine:
1. Customer segmentation, by:
* Demographics (only twm_customer table)
* Banking behavior (after engineering useful features)

## Approach
1. Clean data and engineer features for clustering (numpy, pandas)
2. Use KMeans to find 3-5 clusters per category: demographics, banking behavior
3. Reduce dimensions for plotting with PCA

## TODO
4. Visualize results by plotting clusters in 2D [radar charts](https://plotly.com/python/radar-chart/)
5. Present findings and insights on clustered groups.

### Data
Financial transaction data from [here](https://drive.google.com/file/d/1zAjnf936aHkwVCq_BmA47p4lpRjyRzMf/view?usp=sharing).\
The data contains following tables:

- twm_customer - information about customers
- twm_accounts - information about accounts
- twm_checking_accounts - information about checking accounts (subset of twm_accounts)
- twm_credit_accounts - information about checking accounts (subset of twm_accounts)
- twm_savings_accounts - information about checking accounts (subset of twm_accounts)
- twm_transactions - information about financial transactions
- twm_savings_tran - information about savings transactions (subset of twm_transactions)
- twm_checking_tran - information about savings transactions (subset of twm_transactions)
- twm_credit_tran - information about credit checking (subset of twm_transactions)
