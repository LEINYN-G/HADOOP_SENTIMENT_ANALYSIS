# Copy and paste this code inside a Jupyter Notebook cell
import matplotlib.pyplot as plt
import seaborn as sns

# Insert the exact successful numbers fetched from HDFS part-00000 file
sentiment_categories = ['Negative', 'Neutral', 'Positive']
counts = [34645, 53514, 70440]

# Define custom styling configuration matrices
plt.figure(figsize=(8, 5))
sns.set_theme(style="whitegrid")

# Create the visual bar distribution
ax = sns.barplot(x=sentiment_categories, y=counts, palette=['#ff6b6b', '#ffd166', '#06d6a0'])

# Annotate title markers and formatting axis rules
plt.title('Distribution of Sentiments in Twitter Dataset (Processed via Hadoop MapReduce)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Sentiment Class', fontsize=12)
plt.ylabel('Total Count of Records', fontsize=12)

# Insert exact numeric data labels above the visual bars
for p in ax.patches:
    ax.annotate(f'{int(p.get_height()):,}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', 
                xytext=(0, 8), 
                textcoords='offset points', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('sentiment_distribution.png', dpi=300)
plt.show()
