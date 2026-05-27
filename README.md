Cloud Charts: Demand/Supply Gap and Salary Analysis (2025–2029)
Overview
This project analyzes the Demand/Supply Gap and Salary trends for three cloud computing roles—Infrastructure Engineer, DevOps Engineer, and Cloud Architect—across AWS, Azure, and GCP from 2025 to 2029. The charts were created using Python, Pandas, and Matplotlib in a Linux environment (WSL2 Ubuntu), showcasing my skills in cloud computing, data analysis, and Linux system administration.
Charts
Line Charts (2025–2029)
These charts show the trends over time for each role:

X-axis: Years (2025–2029).
Left Y-axis: Demand/Supply Gap (solid lines: blue for AWS, orange for Azure, green for GCP).
Right Y-axis: Salary (dashed lines: cyan for AWS, red for Azure, dark green for GCP).




Role
Chart File



Infrastructure Engineer
Infra_demand_salary_2025_2029.png


DevOps Engineer
DevOps_demand_salary_2025_2029.png


Cloud Architect
Architect_demand_salary_2025_2029.png


Bar Charts (2029)
These charts compare the metrics for 2029:

X-axis: Providers (AWS, Azure, GCP).
Left Y-axis: Demand/Supply Gap (bars: blue for AWS, orange for Azure, green for GCP).
Right Y-axis: Salary (bars: cyan for AWS, red for Azure, dark green for GCP).




Role
Chart File



Infrastructure Engineer
Infra_bar_demand_salary_2029.png


DevOps Engineer
DevOps_bar_demand_salary_2029.png


Cloud Architect
Architect_bar_demand_salary_2029.png


Key Insights

DevOps Engineer has the largest demand/supply gap (AWS: 70 in 2029), aligning with my focus on Terraform and Kubernetes (CKA) skills.
Cloud Architect on GCP offers the highest salary ($285,499 in 2029), supporting my goal of becoming a GCP Professional Cloud Architect.
AWS consistently shows the highest demand across roles, reflecting its market dominance.

Skills Highlighted
Cloud Computing

Data Analysis for Cloud Roles: Used Python to analyze demand and salary trends for cloud roles, providing insights into career opportunities in AWS, Azure, and GCP.
Cloud Technology Awareness: Focused on roles critical to cloud infrastructure (e.g., DevOps for CI/CD, Cloud Architect for multi-cloud design), aligning with my certifications in progress (AWS SAA, Terraform Associate, Google ACE).
Market Research: Leveraged data to identify high-demand areas, informing my career path in cloud computing.

Linux

Environment Setup: Configured a WSL2 Ubuntu environment to run Python scripts, demonstrating Linux system administration skills.
Package Management: Installed dependencies (Matplotlib, Pandas, NumPy) using pip in a virtual environment, showcasing Linux command-line proficiency.
X Server Configuration: Set up VcXsrv to display charts, requiring Linux environment variable configuration (DISPLAY) and troubleshooting.
Git Workflow: Used Git in Linux to version control and push the project to GitHub, highlighting version control skills in a Linux context.

How to Run

Set Up Environment:mkdir cloud_charts
cd cloud_charts
python3 -m venv venv
source venv/bin/activate
pip install matplotlib pandas numpy


Run Scripts:
Line charts:python chart_line.py


Bar charts:python chart_bar.py




View Charts: Generated PNG files will be saved in the directory.

Future Work

Add more years and roles to the dataset.
Explore interactive visualizations using Plotly.
Integrate real-time cloud market data via APIs.

About Me
I’m Dane Hately, founder of Ember Cloud, a cloud computing enthusiast with certifications in AWS, and GCP and deepening understanding in Terraform and Kubernetes. This project reflects my skills in data analysis, Python scripting, and Linux system administration, all of which are critical for my career goals as a DevOps Engineer and Cloud Architect.
