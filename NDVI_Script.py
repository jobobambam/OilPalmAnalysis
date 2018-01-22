##NDVI_Calculator=name
##Red_Band_layer=raster
##NIR_Band_layer=raster
##NDVI_Index_Name=output raster
outputs_GDALOGRRASTERCALCULATOR_1=processing.runalg('gdalogr:rastercalculator', NIR_Band_layer,'1',Red_Band_layer,'1',NIR_Band_layer,'1',Red_Band_layer,'1',None,'1',None,'1','(A-B)/(C+D)',None,5,None,NDVI_Index_Name)