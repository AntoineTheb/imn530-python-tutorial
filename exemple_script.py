import argparse
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt


def afficher_image(image, tranche, titre='Image non bruitée'):
    # Afficher une image avec matplotlib

    fig, ax = plt.subplots()
    ax.set_title(titre)
    ax.imshow(image[..., tranche], cmap='gray')
    plt.show()


def bruiter_image(image, tranche):
    # Ajouter du bruit gaussien à une image

    image_bruitée = image + np.random.random(image.shape) * np.amax(image)
    afficher_image(image_bruitée, tranche, 'Image bruitée')

    return image_bruitée


def debruiter_image(image, tranche):
    # Appliquer un flou gaussien à une image

    image_debruitée = None  # TODO
    afficher_image(image_debruitée, tranche)
    return image_debruitée


def main():
    # Fonction principale

    parser = argparse.ArgumentParser(
        description='Bruiter et débruiter une image')
    parser.add_argument('image', type=str, help='Image à manipuler')
    parser.add_argument('--tranche', type=int, default=60,
                        help='Tranche à afficher')

    args = parser.parse_args()

    image = nib.load(args.image).get_fdata()
    tranche = args.tranche

    image_bruitée = bruiter_image(image, tranche)
    image_floue = debruiter_image(image_bruitée, tranche)


if __name__ == "__main__":
    main()
