"""EDA script"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def main(ab):
    """Run EDA"""
    # plot dist
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    sns.countplot(data=ab, x='marketing_strategy', ax=axes[0])
    axes[0].set_title('Contact Method Distribution')
    axes[0].tick_params(axis='x', rotation=45)

    sns.countplot(data=ab, x='group', ax=axes[1])
    axes[1].set_title('Group Distribution')

    sns.countplot(data=ab, x='outcome', ax=axes[2])
    axes[2].set_title('Outcome Distribution')

    plt.tight_layout()
    plt.show()

    # by group
    palette = {'treatment': 'blue', 'control': 'navy'}

    plt.figure(figsize=(6, 5))
    sns.countplot(data=ab, x='marketing_strategy', hue='group', palette=palette)
    plt.title('Contact Method Distribution by Group')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(6, 5))
    sns.countplot(data=ab, x='group', palette=palette)
    plt.title('Group Distribution')
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(6, 5))
    sns.countplot(data=ab, x='outcome', hue='group', palette=palette)
    plt.title('Outcome Distribution by Group')
    plt.tight_layout()
    plt.show()

    # correlation
    df_encoded = pd.get_dummies(ab, columns=['group', 'marketing_strategy'], drop_first=True)
    corr = df_encoded.corr()
    corr_outcome = corr['outcome'].sort_values(ascending=False)
    print(corr_outcome)

    plt.figure(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix')
    plt.show()

    # basic stats
    print(ab['group'].value_counts())
    print(ab.groupby('group')['outcome'].mean())

    control = ab[ab['group'] == 'control']


if __name__ == "__main__":
    # load data
 
    main(ab)
