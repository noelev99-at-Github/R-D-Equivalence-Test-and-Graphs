import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = 'C:/Users/noele/Documents/data analytics filesszzz/CompiledAISpeechVSNaturalFINAL.csv'

df = pd.read_csv(file_path)

# The Metrics
metrics = ['Intelligibility', 'Naturalness', 'Prosody', 'Social_Impression']

#S1 AND S2
# Calculate mean values for each metric for S1 and S2
s1_means = [df[f'S1{metric}'].mean() for metric in metrics]
s2_means = [df[f'S2{metric}'].mean() for metric in metrics]

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Width of the bars
bar_width = 0.35

# Positions of the bars on the x-axis
x = np.arange(len(metrics))

# Plot bars for S1 means
ax.bar(x - bar_width/2, s1_means, bar_width, label='S1 AI Generated Speech', color='red')

# Plot bars for S2 means
ax.bar(x + bar_width/2, s2_means, bar_width, label='S2 Natural Speech', color='blue')

# Mean scores on top of the bars
for i, (s1, s2) in enumerate(zip(s1_means, s2_means)):
    ax.text(i - bar_width/2, s1, round(s1, 2), ha='center', va='bottom', color='black')
    ax.text(i + bar_width/2, s2, round(s2, 2), ha='center', va='bottom', color='black')

# Labels and title
ax.set_xlabel('Metrics')
ax.set_ylabel('Mean')
ax.set_title('Comparison of Mean Scores between S1 AI Generated Speech and S2 Natural Speech', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(metrics)
ax.legend()

plt.tight_layout()
plt.show()


#S3 AND S4
s3_means = [df[f'S3{metric}'].mean() for metric in metrics]
s4_means = [df[f'S4{metric}'].mean() for metric in metrics]

fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.35

x = np.arange(len(metrics))

ax.bar(x - bar_width/2, s3_means, bar_width, label='S3 AI Generated Speech', color='green')

ax.bar(x + bar_width/2, s4_means, bar_width, label='S4 Natural Speech', color='pink')

for i, (s3, s4) in enumerate(zip(s3_means, s4_means)):
    ax.text(i - bar_width/2, s3, round(s3, 2), ha='center', va='bottom', color='black')
    ax.text(i + bar_width/2, s4, round(s4, 2), ha='center', va='bottom', color='black')

ax.set_xlabel('Metrics')
ax.set_ylabel('Mean')
ax.set_title('Comparison of Mean Scores Comparison between S3 AI Generated Speech and S4 Natural Speech', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(metrics)
ax.legend()

plt.tight_layout()
plt.show()


#S5 AND S6
s5_means = [df[f'S5{metric}'].mean() for metric in metrics]
s6_means = [df[f'S6{metric}'].mean() for metric in metrics]

fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.35

x = np.arange(len(metrics))

ax.bar(x - bar_width/2, s5_means, bar_width, label='S5 AI Generated Speech', color='teal')

ax.bar(x + bar_width/2, s6_means, bar_width, label='S6 Natural Speech', color='orange')

for i, (s5, s6) in enumerate(zip(s5_means, s6_means)):
    ax.text(i - bar_width/2, s5, round(s5, 2), ha='center', va='bottom', color='black')
    ax.text(i + bar_width/2, s6, round(s6, 2), ha='center', va='bottom', color='black')

ax.set_xlabel('Metrics')
ax.set_ylabel('Mean')
ax.set_title('Comparison of Mean Scores between S5 AI Generated Speech and S6 Natural Speech', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(metrics)
ax.legend()

plt.tight_layout()
plt.show()