import os
import config

from funs import environment_check
from funs import deal_with_sub_json
from funs import json_integrate
from funs import image_compression_and_save
from funs import make_dir_json_md_of_album



if __name__ =='__main__':
    
    src_image_root = config.Parameters.Image_Root_Path
    temp_image_root = config.Parameters.Uploading_Temp_Image_Path
    hexo_photos_path = os.path.join(config.Parameters.Hexo_Root_Path,config.Parameters.Hexo_Sub_Dir_to_Photos)
    
    ## check config environment
    environment_check()
    
    ## compress and save images
    image_compression_and_save(src_image_root, temp_image_root)
    
    ## get info of images and save json of each dir
    deal_with_sub_json(src_image_root, temp_image_root)
    
    ## integrate jsons
    album_dict = json_integrate(temp_image_root)
    
    ## make folders and markdowns in dir of photos
    make_dir_json_md_of_album(temp_image_root, hexo_photos_path, album_dict)
    
    ## upload images with qshell
    if config.Parameters.Force_Upload:
        os.system("rm -rf ~/.qshell/qupload")
        
    cmd = "qshell qupload "+os.path.join(config.Parameters.Uploading_Temp_Image_Path,config.Parameters.Qshell_Config_File_Name)
    os.system(cmd)