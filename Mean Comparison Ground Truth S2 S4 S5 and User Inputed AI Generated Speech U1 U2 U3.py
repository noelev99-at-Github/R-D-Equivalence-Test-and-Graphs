import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = 'C:/Users/noele/Documents/data analytics filesszzz/Graphs/Updated Scripts and Graphs/S2S4S5U1U2U3.csv'

df = pd.read_csv(file_path)

# Metrics
metrics = ['Intelligibility', 'Naturalness', 'Prosody', 'Social_Impression']

# Columns for different speech types
speech_types = ['S2S4S5', 'U1U2U3']

# Mean values for each metric for different speech types
means = [[df[f'{st}{metric}'].mean() for metric in metrics] for st in speech_types]

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Width of the bars
bar_width = 0.1

# Positions of the bars on the x-axis
x = np.arange(len(metrics))

# Define colors for each metric
colors = {
    'Intelligibility': ['Red', 'Orange'],
    'Naturalness': ['Yellow', 'Green'],
    'Prosody': ['Blue', 'Indigo'],
    'Social_Impression': ['Violet', 'Pink']
}

# Plot bars for each speech type with different colors and alternate legend labels
for i, speech_type in enumerate(speech_types):
    for j, metric in enumerate(metrics):
        legend_label = f'{speech_type} {metric}'
        ax.bar(x[j] + (i - 1) * bar_width, means[i][j], bar_width, label=legend_label, alpha=0.8, color=colors[metric][i])

# Add mean scores on top of the bars
for i, mean_list in enumerate(means):
    for j, mean in enumerate(mean_list):
        ax.text(j + (i - 1) * bar_width, mean, round(mean, 2), ha='center', va='bottom', color='black')

# Add labels and title
ax.set_xlabel('Metrics')
ax.set_ylabel('Mean')
ax.set_title('Comparison of Mean Scores between S2S4S5 and U1U2U3 Audios (Natural Speech - Ground Truth and User Input AI Generated Speech)', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(metrics)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=2)

plt.tight_layout()
plt.show()
