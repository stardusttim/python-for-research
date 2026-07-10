import numpy as np
import matplotlib.pyplot as plt


# Line Plot Data
epochs = np.arange(1, 11)
train_acc = np.array([0.55, 0.68, 0.75, 0.82, 0.86, 0.89, 0.91, 0.93, 0.94, 0.95])
val_acc = np.array([0.52, 0.63, 0.70, 0.76, 0.80, 0.82, 0.83, 0.85, 0.85, 0.86])

# Line Plot
plt.figure(figsize=(6, 4), dpi=100)
plt.plot(epochs, train_acc, label='Training Accuracy', 
         color='blue', linewidth=2, marker='o')
plt.plot(epochs, val_acc, label='Validation Accuarcy',
         color='red', linewidth=2, linestyle='--', marker='s')
plt.title('Model Accuracy over Epochs', fontsize=12)
plt.xlabel('Epochs', fontsize=8)
plt.ylabel('Accuracy', fontsize=8)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='best')
plt.show()


# Bar Plot Data
models = ['Baseline', 'CNN', 'ResNet', 'Our Method']
scores = [72.5, 78.3, 85.0, 92.4]

# Bar Plot
plt.figure(figsize=(6, 4), dpi=100)
colors = ['#ced4da', '#adb5bd', '#6c757d', '#007bff']
bars = plt.bar(models, scores, color=colors, width=0.5, edgecolor="#000000")
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval+1, 
             f'{yval}%', 
             ha='center', va='bottom',
             fontsize=8)
plt.xlabel('Models')
plt.ylabel('Accuracy(%)')
plt.title('Performance Comparison')
plt.ylim(0, 110)
plt.show()


# Scatter Plot Data
np.random.seed(42)
feature_x = np.random.normal(50, 10, 50)
feature_y = feature_x * 1.5 + np.random.normal(0, 5, 50)

# Scatter Plot Data
plt.figure(figsize=(6, 4), dpi=100)
plt.scatter(feature_x, feature_y, color='blue', 
            alpha=0.7, edgecolor='black', s=30)
plt.title('Feature Correlation Analysis')
plt.xlabel('Feature X')
plt.ylabel('Feature Y')
plt.show()



# Subplot
fig, axes = plt.subplots(1, 3, figsize=(15, 4), dpi=120)

# Subplot 1: Line Plot
axes[0].plot(epochs, train_acc, label='Training Acc',
             color='blue', linewidth=2, marker='o')
axes[0].plot(epochs, val_acc, label='Validation Acc',
             color='red', linewidth=2, marker='s')
axes[0].set_title('(a)Model Accuracy over Epochs', fontsize=12)
axes[0].set_xlabel('Epochs', fontsize=8)
axes[0].set_ylabel('Accuracy', fontsize=8)
axes[0].grid(True, alpha=0.6, linestyle=':')
axes[0].legend(loc='best')

# Subplot 2: Bar Plot
axes[1].bar(models, scores, color='skyblue', edgecolor='black')
axes[1].set_title('(b) Model Comparison')
axes[1].set_ylabel('Score')

# Subplot 3: Scatter Plot
axes[2].scatter(feature_x, feature_y, color='green', alpha=0.6)
axes[2].set_title('(c) Distribution')

# Automatically adjust layout (extremely important)
plt.tight_layout()
# plt.show()  
# When saving figure, delete/comment the line above)

# Save figure
plt.savefig('Subplot.pdf', dpi=300, bbox_inches='tight')
plt.savefig('Subplot.png', dpi=300, bbox_inches='tight')