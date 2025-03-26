import os
import pandas as pd
import matplotlib.pyplot as plt
import squarify

def get_file_info(folder_path):
    file_info = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path) / (1024 * 1024)  # Convert size to megabytes
            file_extension = os.path.splitext(file)[1].lower()
            file_info.append((file_extension, file_size))
    return file_info

def create_treemap(file_info):
    df = pd.DataFrame(file_info, columns=['File Type', 'Size (MB)'])
    df_grouped = df.groupby('File Type').sum().sort_values(by='Size (MB)', ascending=False).reset_index()
    
    # Remove any entries with zero size to avoid division by zero error
    df_grouped = df_grouped[df_grouped['Size (MB)'] > 0]
    
    plt.figure(figsize=(12, 8))
    squarify.plot(sizes=df_grouped['Size (MB)'], label=df_grouped['File Type'], alpha=.8)
    plt.title("Treemap of File Types Sorted by Size (MB)")
    plt.axis('off')
    plt.show()

folder_path = r"C:\Users"
file_info = get_file_info(folder_path)
create_treemap(file_info)
