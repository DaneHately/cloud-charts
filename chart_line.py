import matplotlib.pyplot as plt
import pandas as pd

# Data for 2025-2029
data = {
    'Year': [2025, 2026, 2027, 2028, 2029] * 9,
    'Role': ['Infra']*15 + ['DevOps']*15 + ['Architect']*15,
    'Provider': (['AWS']*5 + ['Azure']*5 + ['GCP']*5) * 3,
    'Demand_Supply_Gap': [
        # Infrastructure Engineer
        0, 5, 12, 21, 33,    # AWS
        -3, 1, 7, 15, 26,     # Azure
        -5, -1, 5, 12, 22,    # GCP
        # DevOps Engineer
        0, 10, 24, 43, 70,    # AWS
        0, 9, 23, 42, 68,     # Azure
        -2, 7, 20, 37, 61,    # GCP
        # Cloud Architect
        0, 7, 17, 29, 47,     # AWS
        -1, 5, 14, 27, 43,    # Azure
        2, 8, 17, 29, 45      # GCP
    ],
    'Salary': [
        # Infrastructure Engineer
        130000, 143000, 157300, 173030, 190333,  # AWS
        128000, 140800, 154880, 170368, 187405,  # Azure
        132000, 145200, 159720, 175692, 193261,  # GCP
        # DevOps Engineer
        160000, 179200, 200704, 224788, 251762,  # AWS
        158000, 176960, 198195, 222178, 248839,  # Azure
        162000, 181440, 203213, 227598, 254910,  # GCP
        # Cloud Architect
        190000, 209000, 229900, 252890, 278179,  # AWS
        185000, 203500, 223850, 246235, 270858,  # Azure
        195000, 214500, 235950, 259545, 285499   # GCP
    ]
}
df = pd.DataFrame(data)

# Define colors for each provider
colors = {
    'AWS': {'gap': 'blue', 'salary': 'cyan'},
    'Azure': {'gap': 'orange', 'salary': 'red'},
    'GCP': {'gap': 'green', 'salary': 'darkgreen'}
}

# Create one chart per role
roles = ['Infra', 'DevOps', 'Architect']
for role in roles:
    subset = df[df['Role'] == role]
    
    # Initialize plot
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    # Plot Demand/Supply Gap (left axis)
    for provider in ['AWS', 'Azure', 'GCP']:
        provider_data = subset[subset['Provider'] == provider]
        ax1.plot(provider_data['Year'], provider_data['Demand_Supply_Gap'], 
                 label=f'{provider} Gap', color=colors[provider]['gap'], 
                 marker='o', linewidth=2)
    
    # Configure left axis
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Demand/Supply Gap', color='black')
    ax1.tick_params(axis='y', labelcolor='black')
    ax1.grid(True, linestyle='--', alpha=0.7)
    
    # Create right axis for Salary
    ax2 = ax1.twinx()
    for provider in ['AWS', 'Azure', 'GCP']:
        provider_data = subset[subset['Provider'] == provider]
        ax2.plot(provider_data['Year'], provider_data['Salary'], 
                 label=f'{provider} Salary', color=colors[provider]['salary'], 
                 linestyle='--', marker='s', linewidth=2)
    
    # Configure right axis
    ax2.set_ylabel('Salary (USD)', color='black')
    ax2.tick_params(axis='y', labelcolor='black')
    
    # Title and legend
    plt.title(f'Demand/Supply Gap and Salary for {role} Engineer (2025–2029)')
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper center', 
               bbox_to_anchor=(0.5, -0.15), ncol=3)
    
    # Adjust layout
    plt.tight_layout()
    
    # Save chart as PNG
    plt.savefig(f'{role}_demand_salary_2025_2029.png', dpi=300, bbox_inches='tight')
    
    # Show chart
    plt.show()
