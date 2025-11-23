import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def run_analysis():
    try:
        # 1. Load CSV
        df = pd.read_csv("./banggood_clean.csv")
        print("CSV loaded successfully.")
    except FileNotFoundError:
        print("Error: './banggood_clean.csv' file not found.")
        return
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return

    # Required columns
    required_cols = ['category', 'price', 'rating', 'reviews', 'value_score', 'popularity']
    for col in required_cols:
        if col not in df.columns:
            print(f"Error: Missing required column '{col}' in CSV.")
            return

    # Convert numeric columns safely
    for col in ['price', 'rating', 'reviews', 'value_score', 'popularity']:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Drop rows with missing essential values
    df = df.dropna(subset=['category', 'price', 'rating', 'reviews', 'value_score', 'popularity'])

    # Create output folder if not exists
    output_folder = "../"
    os.makedirs(output_folder, exist_ok=True)

    # 1. Price distribution per category
    plt.figure(figsize=(10,6))
    sns.boxplot(x="category", y="price", data=df)
    plt.title("Price Distribution per Category")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(output_folder, "plots_price_distribution.png"))
    plt.close()

    # 2. Rating vs Price
    plt.figure(figsize=(7,5))
    sns.scatterplot(x="price", y="rating", hue="category", data=df)
    plt.title("Rating vs Price")
    plt.tight_layout()
    plt.savefig(os.path.join(output_folder, "plots_rating_vs_price.png"))
    plt.close()

    # 3. Top reviewed products
    print("\nTop 10 Reviewed Products:")
    print(df.sort_values("reviews", ascending=False).head(10))

    # 4. Best Value Items per category
    print("\nTop 5 Best Value Items per Category:")
    print(df.sort_values("value_score", ascending=False).groupby("category").head(5))

    # 5. Popularity vs Price
    plt.figure(figsize=(7,5))
    sns.scatterplot(x="price", y="popularity", data=df)
    plt.title("Popularity vs Price")
    plt.tight_layout()
    plt.savefig(os.path.join(output_folder, "plots_popularity.png"))
    plt.close()

    print("\nAnalysis Completed. Plots saved successfully.")

if __name__ == "__main__":
    run_analysis()
