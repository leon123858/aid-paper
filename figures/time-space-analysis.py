import matplotlib.pyplot as plt
import numpy as np

def generate_data(multiplier):
    return [abs(i)**1.5 * multiplier for i in range(0, 11)]

# Generate data
time = list(range(-10, 1))  # Changed to range from -10 to 0
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
risk_levels = ['Minimal','Very Low','Low', 'Moderate', 'High', 'Very High', 'Extreme']
data = [generate_data(i*0.2) for i in range(len(colors))]

# Create the chart
plt.figure(figsize=(12, 8))

# Plot each curve
for color, values, risk in zip(colors, data, risk_levels):
    plt.plot(time, values, color=color, linewidth=2, label=f'{risk} Risk')

# Set chart title and axis labels
plt.title('Time Interval vs Space Difference (Risk Levels)', fontsize=16)
plt.xlabel('Time Interval', fontsize=12)
plt.ylabel('Space Difference', fontsize=12)

# Set x-axis range and ticks
plt.xlim(-10, 0)
plt.xticks(range(-10, 1, 2))  # Set ticks every 2 units for better readability

# Add grid lines
plt.grid(True, linestyle='--', alpha=0.7)

# Add legend
plt.legend(loc='upper left')

# Adjust layout
plt.tight_layout()

# Save the chart
plt.savefig('time_space_risk_chart_reversed.png', dpi=300)

# Display the chart (if running in an interactive environment)
plt.show()