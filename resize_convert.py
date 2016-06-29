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


import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image


def main():
    pass


def resize(ims_path):
    for filename in os.listdir(ims_path):
        if filename.endswith(".JPG"):
            img = mpimg.imread(filename)

            # Redimnesionnement
            dim_req = (1080, 1920)  # Hauteur en première coordonnée
#            diff_dim = (img.shape[0] - dim_req[0], img.shape[1] - dim_req[1])
#
#            # Détermination du côté à redimensionner en premier
#            car = None
#            if diff_dim[0] > diff_dim[1]:
#                car = 0  # 0 pour la hauteur
#            elif diff_dim[1] > diff_dim[0]:
#                car = 1  # 1 pour la largeur
#
#            # Nouvelle image
#            ratio = float(diff_dim[1])/float(dif_dim[0])  # Largeur sur hauteur
#            if car:
#                dim_prov = (int(dim_req[1]/ratio), dim_req[1]) 
#            elif not car:
#                dim_prov = (dim_req[0], int(ratio*dim_req[0]))
            img_pil = Image.open(filename)
            img_pil.thumbnail(dim_req)
            img_pil_arr = np.array(img_pil)
            # L'image est retournée: shape donne (606, 1080, 3)
            img_pil_arr = np.transpose(img_pil_arr, (1, 0, 2))
            diff_dim = (abs(img_pil_arr.shape[0] - dim_req[0]),
                        abs(img_pil_arr.shape[1] - dim_req[1]))
            # On complète
            if diff_dim[0] == 0:  # Si hauteur bonne
                tobestacked = np.zeros((dim_req[0], 1, 3))
                for i in range(diff_dim[1]):
                    img_pil_arr = np.hstack((img_pil_arr, tobestacked)).copy()
            elif diff_dim[1] == 0:  # Si largeur bonne
                tobestacked = np.zeros((1, dim_req[1], 3))
                for i in range(diff_dim[0]):
                    img_pil_arr = np.vstack((img_pil_arr, tobestacked)).copy()
            img_pil = Image.fromarray(img_pil_arr)
            img_pil.save(filename, "bmp")



if __name__ == "__main__":
    main()
