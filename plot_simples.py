# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 13:52:10 2022

@author: jdebr
"""

'''plot simples de dados em netCDF'''

'''importando as bibliotecas necessarias'''

#ler arquivos em netCDF
import netCDF4 as nc
#criacao de plots
import matplotlib.pyplot as plt
import cartopy.crs as ccrs


'''abrindo o arquivo e definindo as variaveis'''
#abrindo o arquivo
fn = 'C:/Users/jdebr/Documents/clorofila_bahia/sst_ba.nc'
ds = nc.Dataset(fn)
#lendo as variaveis
for var in ds.variables.values():
    print(var)
#vendo as dimensoes das variaves
for dim in ds.dimensions.values():
    print(dim)
#definindo as variaveis
sst=ds['sst'][:]
lat=ds['lat'][:]
lon=ds['lon'][:]

#criando um mapa usando dados de sst de um mes aleatorio
ax = plt.axes(projection=ccrs.PlateCarree())
plt.contourf(lon, lat,sst[6],60,transform=ccrs.PlateCarree(),cmap='RdBu_r')
#adicionando um colorbar
cb=plt.colorbar()
#adicionando a linha de costa
ax.coastlines()
#adicionando latitude e longitude ao mapa
g = ax.gridlines(crs=ccrs.PlateCarree(), linestyle='-.', color='gray', draw_labels=True)
#deixando lat e lon em apenas dois lados(esquerda e baixo)
g.ylabels_right = False
g.xlabels_top = False
#adicionanto titulo do eixo x
cb.ax.set_xlabel('Temperature(°C)')
#adicionando titulo do mapa
plt.suptitle('Sea Surface Temperature (°C) ')
#ajustando a imagem
plt.subplots_adjust(top=0.94,bottom=0.041,left=0.0,right=0.8,hspace=0.195,wspace=0.2)
#salvando
plt.savefig('plot_simples.jpg')
