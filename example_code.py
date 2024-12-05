from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

# Your Python code to be highlighted
code = '''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset
data = pd.read_csv('your_dataset.csv')

# Calculate average purchase cost by age
age_costs = data.groupby('age')['purchase_cost'].mean().reset_index()

# Plot the results
plt.figure(figsize=(10, 6))
sns.lineplot(data=age_costs, x='age', y='purchase_cost')
plt.title('Average Purchase Cost by Age')
plt.xlabel('Age')
plt.ylabel('Average Purchase Cost')
plt.show()
'''

# Generate highlighted HTML code
formatter = HtmlFormatter(style='friendly')
html_code = highlight(code, PythonLexer(), formatter)

# Save the syntax-highlighted code to "example_code.html"
with open("example_code.html", "w") as f:
    f.write(f"<html><head><style>{formatter.get_style_defs()}</style></head><body>")
    f.write(html_code)
    f.write("</body></html>")

