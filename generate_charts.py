import matplotlib.pyplot as plt
import numpy as np

# Data from ISTAT and Industry Reports (2024-2026 Forecast)
years = ['2023', '2024', '2025', '2026 (F)']
large_ent = [25.0, 32.5, 53.1, 65.0]  # Large Enterprises
national_avg = [5.0, 8.2, 16.4, 25.0] # National Average
smes = [4.0, 7.7, 15.7, 23.0]         # SMEs

# Plot 1: The Adoption S-Curve
plt.figure(figsize=(10, 7))
plt.plot(years, large_ent, marker='o', linewidth=2, label='Large Enterprises (>250)')
plt.plot(years, national_avg, marker='s', linewidth=2, label='National Average', linestyle='--')
plt.plot(years, smes, marker='^', linewidth=2, label='SMEs (10-249)')

plt.title('AI Adoption S-Curve in Italy (2023-2026)', fontsize=14, fontweight='bold')
plt.ylabel('Adoption Rate (%)', fontsize=12)
plt.xlabel('Year', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.annotate('Tipping Point', xy=('2025', 16.4), xytext=('2024', 40),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)

# Add Source Citation
plt.figtext(0.5, 0.01, 'Source: ISTAT "Imprese e ICT" (2024-2025); Politecnico di Milano AI Index (2026 Forecast)', 
            ha='center', fontsize=8, style='italic', alpha=0.7)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('ai_adoption_scurve.png')
plt.close()

# Plot 2: Technology Distribution Radar Chart
labels = np.array(['Text Mining', 'GenAI', 'Speech Recog.', 'Computer Vision', 'ML', 'Robotics'])
# Industry average vs Manufacturing
industry_avg = [70, 59, 41, 25, 30, 15]
manufacturing = [40, 45, 30, 65, 55, 50]

angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
industry_avg += industry_avg[:1]
manufacturing += manufacturing[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))
ax.fill(angles, industry_avg, color='blue', alpha=0.25, label='National Average')
ax.plot(angles, industry_avg, color='blue', linewidth=2)
ax.fill(angles, manufacturing, color='red', alpha=0.25, label='Manufacturing Sector')
ax.plot(angles, manufacturing, color='red', linewidth=2)

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)
plt.title('Technology Focus: Manufacturing vs National Average (2025)', fontsize=14, fontweight='bold', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# Add Source Citation
plt.figtext(0.5, 0.05, 'Source: ISTAT Report "Imprese e ICT" (Dec 2025); Sectoral Manufacturing Index', 
            ha='center', fontsize=8, style='italic', alpha=0.7)

plt.savefig('ai_tech_radar.png')
plt.close()

# Plot 3: Heatmap of Application Maturity
applications = ['Admin', 'Marketing', 'Production', 'R&D', 'Logistics']
sectors = ['Manufacturing', 'Chemicals', 'Plastic/Rubber']
# 3: High/Saturated, 2: Growing, 1: Experimental/Low
data = np.array([
    [3, 3, 2, 1, 1], # Manufacturing
    [3, 3, 1, 3, 1], # Chemicals
    [2, 2, 2, 1, 2]  # Plastic/Rubber
])

fig, ax = plt.subplots(figsize=(10, 5))
im = ax.imshow(data, cmap='YlGn')

ax.set_xticks(np.arange(len(applications)))
ax.set_yticks(np.arange(len(sectors)))
ax.set_xticklabels(applications)
ax.set_yticklabels(sectors)

plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Add text annotations
for i in range(len(sectors)):
    for j in range(len(applications)):
        val = data[i, j]
        label = "High" if val == 3 else "Growing" if val == 2 else "Low"
        text = ax.text(j, i, label, ha="center", va="center", color="black")

ax.set_title("AI Application Maturity Heatmap (2025-2026)", fontsize=14, fontweight='bold', pad=20)

# Add Source Citation
plt.figtext(0.5, 0.01, 'Source: Federchimica 31st Report (2025); Smart Manufacturing Survey (Gomma-Plastica, 2026)', 
            ha='center', fontsize=8, style='italic', alpha=0.7)

fig.tight_layout(rect=[0, 0.05, 1, 0.95])
plt.savefig('ai_application_heatmap.png')
plt.close()

print("Charts generated successfully: scurve, radar, and heatmap.")
