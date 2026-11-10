import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:
    df = pd.read_csv('data/spam.csv', encoding='utf-8-sig')
    df.columns = df.columns.str.strip()


    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))


    sns.countplot(x='label', data=df, ax=axes[0], palette='viridis')
    axes[0].set_title('So luong Ham vs Spam')
    axes[0].set_xlabel('Loai tin nhan')
    axes[0].set_ylabel('So luong')

    counts = df['label'].value_counts()
    axes[1].pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140, colors=['#66b3ff','#ff9999'])
    axes[1].set_title('Ty le phan tram')

    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"Loi: {e}")