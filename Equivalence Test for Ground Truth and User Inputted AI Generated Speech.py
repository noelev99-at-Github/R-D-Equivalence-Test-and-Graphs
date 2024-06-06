import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = 'C:/Users/noele/Documents/data analytics filesszzz/Graphs/Updated Scripts and Graphs/S2S4S5U1U2U3.csv'

df = pd.read_csv(file_path)

# S2S4S5 AND U1U2U3 INTELIGIBILITY EQUIVALENCE TEST
# Calculating mean values for Intelligibility scores of two groups, ignoring NaN or missing values
s2s4s5_mean = np.nanmean(df['S2S4S5Intelligibility'])
u1u2u3_mean = np.nanmean(df['U1U2U3Intelligibility'])

# Equivalence margin
equivalence_margin = 0.5 

# Boxplots for the two groups
plt.boxplot([df['S2S4S5Intelligibility'].dropna(), df['U1U2U3Intelligibility'].dropna()], labels=['S2S4S5 Audio Natural Speech', 'U1U2U3 Audio User Input AI Generated Speech'])

# Adding horizontal lines for equivalence margins
plt.axhline(y=s2s4s5_mean - equivalence_margin, color='red', linestyle='--', label=f'Equivalence Margin (S2 S4 S5 Audio Natural Speech) = {equivalence_margin}')
plt.axhline(y=s2s4s5_mean + equivalence_margin, color='red', linestyle='--')
plt.axhline(y=u1u2u3_mean - equivalence_margin, color='green', linestyle='--', label=f'Equivalence Margin (U1 U2 U3 Audio User Input AI Generated Speech) = {equivalence_margin}')
plt.axhline(y=u1u2u3_mean + equivalence_margin, color='green', linestyle='--')

# Adding mean scores for each group with thicker lines and black color
plt.text(1, s2s4s5_mean, f'Mean: {s2s4s5_mean:.2f}', ha='left', va='center', fontsize=10, color='black')
plt.text(2, u1u2u3_mean, f'Mean: {u1u2u3_mean:.2f}', ha='left', va='center', fontsize=10, color='black')
plt.axhline(y=s2s4s5_mean, color='orange', linestyle='-', linewidth=2, label=f'Mean (S2S4S5 Audio Natural Speech) = {s2s4s5_mean:.2f}')  # Mean line for S2S4S5 in orange
plt.axhline(y=u1u2u3_mean, color='blue', linestyle='-', linewidth=2, label=f'Mean (U1U2U3 Audio User Input AI Generated Speech) = {u1u2u3_mean:.2f}')  # Mean line for U1U2U3 in blue

# Labeling axes and adding title
plt.xlabel('Audio')
plt.ylabel('Intelligibility Ratings')
plt.title('Intelligibility Ratings Equivalence Test of S2 S4 S5 Audio Natural Speech and U1 U2 U3 Audio User Input AI Generated Speech', pad=20)
plt.legend()

plt.show()

# S2S4S5 AND U1U2U3 INTELIGIBILITY EQUIVALENCE TEST
s2s4s5_mean = np.nanmean(df['S2S4S5Naturalness'])
u1u2u3_mean = np.nanmean(df['U1U2U3Naturalness']) 

equivalence_margin = 0.5  # Example equivalence margin

plt.boxplot([df['S2S4S5Naturalness'].dropna(), df['U1U2U3Naturalness'].dropna()], labels=['S2S4S5 Audio Natural Speech', 'U1U2U3 Audio User Input AI Generated Speech'])

plt.axhline(y=s2s4s5_mean - equivalence_margin, color='red', linestyle='--', label=f'Equivalence Margin (S2 S4 S5 Naturalness) = {equivalence_margin}')
plt.axhline(y=s2s4s5_mean + equivalence_margin, color='red', linestyle='--')
plt.axhline(y=u1u2u3_mean - equivalence_margin, color='green', linestyle='--', label=f'Equivalence Margin (U1 U2 U3 Naturalness) = {equivalence_margin}')
plt.axhline(y=u1u2u3_mean + equivalence_margin, color='green', linestyle='--')

plt.text(1, s2s4s5_mean, f'Mean: {s2s4s5_mean:.2f}', ha='left', va='center', fontsize=10, color='black')
plt.text(2, u1u2u3_mean, f'Mean: {u1u2u3_mean:.2f}', ha='left', va='center', fontsize=10, color='black')
plt.axhline(y=s2s4s5_mean, color='orange', linestyle='-', linewidth=2, label=f'Mean (S2S4S5 Naturalness) = {s2s4s5_mean:.2f}')
plt.axhline(y=u1u2u3_mean, color='blue', linestyle='-', linewidth=2, label=f'Mean (U1U2U3 Naturalness) = {u1u2u3_mean:.2f}')

plt.xlabel('Audio')
plt.ylabel('Naturalness Ratings')
plt.title('Naturalness Ratings Equivalence Test of S2 S4 S5 Natural Speech and U1 U2 U3 User Input AI Generated Speech', pad=20)
plt.legend()

plt.show()

s2s4s5_mean = np.nanmean(df['S2S4S5Prosody'])
u1u2u3_mean = np.nanmean(df['U1U2U3Prosody']) 

equivalence_margin = 0.5  

plt.boxplot([df['S2S4S5Prosody'].dropna(), df['U1U2U3Prosody'].dropna()], labels=['S2S4S5 Audio Natural Speech', 'U1U2U3 Audio User Input AI Generated Speech'])

plt.axhline(y=s2s4s5_mean - equivalence_margin, color='red', linestyle='--', label=f'Equivalence Margin (S2 S4 S5 Prosody) = {equivalence_margin}')
plt.axhline(y=s2s4s5_mean + equivalence_margin, color='red', linestyle='--')
plt.axhline(y=u1u2u3_mean - equivalence_margin, color='green', linestyle='--', label=f'Equivalence Margin (U1 U2 U3 Prosody) = {equivalence_margin}')
plt.axhline(y=u1u2u3_mean + equivalence_margin, color='green', linestyle='--')

plt.text(1, s2s4s5_mean, f'Mean: {s2s4s5_mean:.2f}', ha='left', va='center', fontsize=10, color='black')
plt.text(2, u1u2u3_mean, f'Mean: {u1u2u3_mean:.2f}', ha='left', va='center', fontsize=10, color='black')
plt.axhline(y=s2s4s5_mean, color='orange', linestyle='-', linewidth=2, label=f'Mean (S2S4S5 Prosody) = {s2s4s5_mean:.2f}')
plt.axhline(y=u1u2u3_mean, color='blue', linestyle='-', linewidth=2, label=f'Mean (U1U2U3 Prosody) = {u1u2u3_mean:.2f}')

plt.xlabel('Audio')
plt.ylabel('Prosody Ratings')
plt.title('Prosody Ratings Equivalence Test of S2 S4 S5 Natural Speech and U1 U2 U3 User Input AI Generated Speech', pad=20)
plt.legend()

plt.show()

# S2S4S5 AND U1U2U3 SOCIAL IMPRESSION EQUIVALENCE TEST
s2s4s5_mean = np.nanmean(df['S2S4S5Social_Impression'])
u1u2u3_mean = np.nanmean(df['U1U2U3Social_Impression'])  

equivalence_margin = 0.5

plt.boxplot([df['S2S4S5Social_Impression'].dropna(), df['U1U2U3Social_Impression'].dropna()], labels=['S2S4S5 Audio Natural Speech', 'U1U2U3 Audio User Input AI Generated Speech'])

plt.axhline(y=s2s4s5_mean - equivalence_margin, color='red', linestyle='--', label=f'Equivalence Margin (S2 S4 S5 Social Impression) = {equivalence_margin}')
plt.axhline(y=s2s4s5_mean + equivalence_margin, color='red', linestyle='--')
plt.axhline(y=u1u2u3_mean - equivalence_margin, color='green', linestyle='--', label=f'Equivalence Margin (U1 U2 U3 Social Impression) = {equivalence_margin}')
plt.axhline(y=u1u2u3_mean + equivalence_margin, color='green', linestyle='--')

plt.text(1, s2s4s5_mean, f'Mean: {s2s4s5_mean:.2f}', ha='left', va='center', fontsize=10, color='black')
plt.text(2, u1u2u3_mean, f'Mean: {u1u2u3_mean:.2f}', ha='left', va='center', fontsize=10, color='black')
plt.axhline(y=s2s4s5_mean, color='orange', linestyle='-', linewidth=2, label=f'Mean (S2S4S5 Social Impression) = {s2s4s5_mean:.2f}')
plt.axhline(y=u1u2u3_mean, color='blue', linestyle='-', linewidth=2, label=f'Mean (U1U2U3 Social Impression) = {u1u2u3_mean:.2f}')

plt.xlabel('Audio')
plt.ylabel('Social Impression Ratings')
plt.title('Social Impression Ratings Equivalence Test of S2 S4 S5 Natural Speech and U1 U2 U3 User Input AI Generated Speech', pad=20)
plt.legend()

plt.show()


