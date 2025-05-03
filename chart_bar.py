import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data for 2029 only
data = {
    'Year': [2029] * 9,
    'Role': ['Infra']*3 + ['DevOps']*3 + ['Architect']*3,
    'Provider': ['AWS', 'Azure', 'GCP'] * 3,
    'Demand_Supply_Gap': [
        # Infrastructure Engineer
        33, 26, 22,  # AWS, Azure, GCP
        # DevOps Engineer
        70, 68, 61,  # AWS, Azure, GCP
        # Cloud Architect
        47, 43, 45   # AWS, Azure, GCP
    ],
    'Salary': [
        # Infrastructure Engineer
        190333, 187405, 193261,  # AWS, Azure, GCP
        # DevOps Engineer
        251762, 248839, 254910,  # AWS, Azure, GCP
        # Cloud Architect
        278179, 270858, 285499   # AWS, Azure, GCP
    ]
}
df = pd.DataFrame(data)

# Define colors for each provider
colors = {
    'AWS': {'gap': 'blue', 'salary': 'cyan'},
    'Azure': {'gap': 'orange', 'salary': 'red'},
    'GCP': {'gap': 'green', 'salary': 'darkgreen'}
}

# Create one bar chart per role
roles = ['Infra', 'DevOps', 'Architect']
for role in roles:
    subset = df[df['Role'] == role]
    
    # Initialize plot
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    # Bar chart settings
    x = np.arange(len(subset['Provider']))
    bar_width = 0.35
    
    # Plot Demand/Supply Gap bars (left axis)
    ax1.bar(x - bar_width/2, subset['Demand_Supply_Gap'], 
            bar_width, label='Demand/Supply Gap', 
            color=[colors[p]['gap'] for p in subset['Provider']])
    
    # Configure left axis
    ax1.set_xlabel('Provider')
    ax1.set_ylabel('Demand/Supply Gap', color='black')
    ax1.set_xticks(x)
    ax1.set_xticklabels(subset['Provider'])
    ax1.tick_params(axis='y', labelcolor='black')
    ax1.grid(True, linestyle='--', alpha=0.7, axis='y')
    
    # Create right axis for Salary
    ax2 = ax1.twinx()
    ax2.bar(x + bar_width/2, subset['Salary'], 
            bar_width, label='Salary', 
            color=[colors[p]['salary'] for p in subset['Provider']])
    
    # Configure right axis
    ax2.set_ylabel('Salary (USD)', color='black')
    ax2.tick_params(axis='y', labelcolor='black')
    
    # Title and legend
    plt.title(f'Demand/Supply Gap and Salary for {role} Engineer (2029)')
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper center', 
               bbox_to_anchor=(0.5, -0.15), ncol=2)
    
    # Adjust layout
    plt.tight_layout()
    
    # Save chart as PNG
    plt.savefig(f'{role}_bar_demand_salary_2029.png', dpi=300, bbox_inches='tight')
    
    # Show chart
    plt.show()

