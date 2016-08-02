#!/usr/bin/python
# -*- encoding: utf-8 -*-
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


import sys
import numpy as np
from PIL import Image


def looponfiles():
    """
    Prend en paramètre les arguments passés en ligne de commande (fichiers à
    traiter) et lance la fonction de traitement
    """
    imext = ["jpg", "tif", "png", "JPG", "TIF", "PNG"]
    for filename in sys.argv[1:]:
        if len(filename.split('.')) >= 2 and filename.split('.')[1] in imext:
            process_im(filename)


def process_im(filename):
    """
    Prend en paramètre une chaine de caractère: le nom du fichier à traiter
    Redimensionne puis complète puis enregistre les images. Les images sont
    complétées par des arrays (tobestacked) représeantant des bandes blanches
    """
    # NOTATION GRAPHIQUE (largeur, hauteur)
    dim_req = (1920, 1280)
    img_pil = Image.open(filename)
    img_pil.thumbnail(dim_req)
    img_pil_arr = np.array(img_pil)
    # NOTATION MATRICIELLE: (ligne, colonne)
    dim_req = (1280, 1920)
    diff_dim = (abs(img_pil_arr.shape[0] - dim_req[0]),
                abs(img_pil_arr.shape[1] - dim_req[1]))
    # On complète
    # Si largeur bonne
    if diff_dim[0] == 0 and diff_dim[1] != 0:
        tobestacked = 255*np.ones((dim_req[0], diff_dim[1], 3),
                                  dtype="uint8")
        img_pil_arr = np.hstack((img_pil_arr, tobestacked)).copy()
    # Si hauteur bonne
    elif diff_dim[1] == 0 and diff_dim[0] != 0:
        tobestacked = 255*np.ones((diff_dim[0], dim_req[1], 3),
                                  dtype="uint8")
        img_pil_arr = np.vstack((img_pil_arr, tobestacked)).copy()
    img_pil = Image.fromarray(img_pil_arr)
    img_pil.save("{}.bmp".format(filename.split('.')[0]), "bmp")


if __name__ == "__main__":
    looponfiles()
