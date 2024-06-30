import random
from PIL import Image
import matplotlib.pyplot as plt

def plot_transformed_images(image_paths, transform, n=3, seed=42):

    if seed:
        random.seed(seed)
    random_image_path = random.sample(image_paths, k=n)
    for img in random_image_path:
        with Image.open(img) as f:
            fig, ax = plt.subplots(nrows = 1, ncols = 2)
            ax[0].imshow(f)
            ax[0].set_title(f'Original\nsize {f.size}')
            ax[0].axis(False)

            transformed_image = transform(f).permute(1, 2, 0)
            ax[1].imshow(transformed_image)
            ax[1].set_title(f'transformed image\nsize {transformed_image.shape}')
            ax[1].axis(False)
            
            fig.suptitle(f'Class : {img.parent.stem}', fontsize = 16)