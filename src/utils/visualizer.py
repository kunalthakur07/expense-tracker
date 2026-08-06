import matplotlib.pyplot as plt
from src.controllers.report_generator import ReportGenerator

def plot_category_spending():
    data = ReportGenerator.category_summary()
    cats = list(data.keys())
    values = list(data.values())
    plt.figure(figsize=(6,4))
    plt.bar(cats, values)
    plt.title("Spending by Category")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
