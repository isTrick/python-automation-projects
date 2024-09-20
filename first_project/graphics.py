import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('people.csv')

# First graphic
plt.figure(figsize=(10, 6))
df['Gender'] = df['Gender'].map({'M': 'Masculino', 'F': 'Feminino'})
df['Gender'].value_counts().plot(kind='bar', color='blue')
plt.title('Gênero das pessoas')
plt.xlabel('Gênero')
plt.ylabel('Contagem')

plt.show()

# Second graphic
plt.figure(figsize=(10, 6))
plt.hist(df['Age'], bins=10, color='skyblue', edgecolor='black')  # Ajuste o número de bins conforme necessário
plt.title('Distribuição de Idade')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.grid(axis='y', alpha=0.75)

plt.show()

# Third graphic
plt.figure(figsize=(10, 6))

df['State'].value_counts().plot(kind='pie', color='darkblue')
plt.title('Distribuição de idade')
plt.xlabel('')
plt.ylabel('')