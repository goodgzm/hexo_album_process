import config
from funs import environment_check
from funs import deal_with_sub_json
from funs import image_compression_and_save



if __name__ =='__main__':
    
    src_image_root = config.Parameters.Image_Root_Path
    temp_image_root = config.Parameters.Uploading_Temp_Image_Path
    
    ## check config environment
    environment_check()
    
    ## compress and save images
    image_compression_and_save(src_image_root, temp_image_root)
    
    deal_with_sub_json(src_image_root, temp_image_root)