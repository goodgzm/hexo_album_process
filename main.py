import os
import config

from funs import environment_check
from funs import deal_with_sub_json
from funs import json_integrate
from funs import image_compression_and_save



if __name__ =='__main__':
    
    src_image_root = config.Parameters.Image_Root_Path
    temp_image_root = config.Parameters.Uploading_Temp_Image_Path
    hexo_photos_path = os.p
    
    ## check config environment
    environment_check()
    
    ## compress and save images
    image_compression_and_save(src_image_root, temp_image_root)
    
    ## get info of images and save json of each dir
    deal_with_sub_json(src_image_root, temp_image_root)
    
    ## integrate jsons
    json_integrate(temp_image_root)
    
    ## make folders and markdowns in dir of photos
    