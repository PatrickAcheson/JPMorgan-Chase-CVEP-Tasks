import pandas as pd
import matplotlib.pyplot as plt

def exercise_0(file):
    return pd.read_csv(file)

def exercise_1(df):
    return list(df.columns)

def exercise_2(df, k):
    return df.head(k)

def exercise_3(df, k):
    return df.sample(k)

def exercise_4(df):
    return df['type'].unique().tolist()

def exercise_5(df):
    return df['nameDest'].value_counts().head(10)

def exercise_6(df):
    return df[df['isFraud'] == 1]

def exercise_7(df):
    return df.groupby('nameOrig')['nameDest'].nunique().reset_index().sort_values(by='nameDest', ascending=False)

def visual_1(df):
    def transaction_counts(df):
        return df['type'].value_counts()

    def transaction_counts_split_by_fraud(df):
        return df.groupby(['type', 'isFraud']).size().unstack(fill_value=0)

    fig, axs = plt.subplots(2, figsize=(10, 10))
    transaction_counts(df).plot(ax=axs[0], kind='bar')
    axs[0].set_title('Transaction Types')
    axs[0].set_xlabel('Transaction Type')
    axs[0].set_ylabel('Count')

    transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar')
    axs[1].set_title('Transaction Types Split by Fraud')
    axs[1].set_xlabel('Transaction Type')
    axs[1].set_ylabel('Count')

    fig.suptitle('Transaction Type Analysis')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])

    for ax in axs:
        for p in ax.patches:
            ax.annotate(p.get_height(), (p.get_x() + p.get_width() / 2, p.get_height()))

    return "The first graph shows the count of each transaction type, providing an overview of the distribution of transaction types in the dataset. The second graph visualizes the count of transaction types split by fraud, highlighting the frequency of fraud for each transaction type."


def visual_2(df):
    def query(df):
        return df[df['type'] == 'CASH_OUT']

    plot = query(df).plot.scatter(x='oldbalanceOrg', y='oldbalanceDest')
    plot.set_title('Origin Account Balance vs. Destination Account Balance for Cash Out Transactions')
    plot.set_xlabel('Origin Account Balance')
    plot.set_ylabel('Destination Account Balance')
    return 'This scatter plot visualizes the relationship between the origin account balance and the destination account balance for Cash Out transactions.'

def exercise_custom(df):
    df['mean_amount'] = df.groupby('type')['amount'].transform('mean')
    return df

def visual_custom(df):
    df = exercise_custom(df)
    unique_df = df.drop_duplicates('type')
    plot = unique_df.plot(x='type', y='mean_amount', kind='bar', color='skyblue', edgecolor='black')
    plot.set_title('Average Transaction Amount by Type')
    plot.set_xlabel('Transaction Type')
    plot.set_ylabel('Average Amount')

    plt.tight_layout()
    plt.show()

    return 'This bar chart visualizes the average transaction amount for each type of transaction.'