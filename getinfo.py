import exifread
import requests
import config
import os

class PhotoExifInfo():
    
    def __init__(self):
        
        if os.path.exists('vvdkey.py'):
            from vvdkey import baidu_key
            self.baidu_map_ak = baidu_key
        else:
            ## set your baidu map key here
            self.baidu_map_ak = ""
            
        self.interested_keys = {
            # camera Model
            'Image Model':'相机型号',
            # Aperture 1/value
            'EXIF FNumber':'光圈',
            # Focal Length
            'EXIF FocalLength':'焦距',
            # Exposure Mode
            'EXIF ExposureMode':'曝光模式',
            # ExposureTime in seconds
            'EXIF ExposureTime':'曝光时间',
            # ISO
            'EXIF ISOSpeedRatings':'ISO',
            # date of photo
            'Image DateTime':'拍摄时间',
        }
        
        
    def get_image_info(self,image_path):
        """
        获取照片信息
        """
        image_info_dict={}
        
        with open(image_path, 'rb') as fp:
            tags = exifread.process_file(fp)
        
        for j in tags:
            print(f"{j} :{tags[j]}")
        
        for item in tuple(self.interested_keys):
            
            try:
                info = tags[item].printable
                if item == 'EXIF FNumber':
                    if '/' in info:
                        A,B = info.split('/')
                        info = 'f'+format(int(A)/int(B),'.1f')
                    else:
                        info = 'f'+info
                if item == 'EXIF FocalLength':
                    info = info+'mm'
                if item == 'EXIF ExposureTime':
                    info = info+'s'
                image_info_dict[self.interested_keys[item]] = info
                
            except:
                print(f'{image_path} has no attribute of {item}')                
                continue
            
        try:
            localcation = self._get_city_info(tags)
            if localcation != "":
                image_info_dict['positon'] = localcation
                
        except:
            print(f'{image_path} has no GPS info')    
            
        return image_info_dict
       
       
    def _get_lng_lat(self, tags):
        """
        经纬度转换
        """
        try:
            
            # 纬度
            LatRef = tags["GPS GPSLatitudeRef"].printable
            Lat = tags["GPS GPSLatitude"].printable[1:-1].replace(" ", "").replace("/", ",").split(",")
            Lat = float(Lat[0]) + float(Lat[1]) / 60 + float(Lat[2]) / 3600
            if LatRef != "N":
                Lat = Lat * (-1)
                
            # 经度
            LonRef = tags["GPS GPSLongitudeRef"].printable
            Lon = tags["GPS GPSLongitude"].printable[1:-1].replace(" ", "").replace("/", ",").split(",")
            Lon = float(Lon[0]) + float(Lon[1]) / 60 + float(Lon[2]) / 3600
            if LonRef != "E":
                Lon = Lon * (-1)
            return Lat,Lon
        except:
            print('Unable to get')



    def _get_city_info(self, tags):
        
        result = self._get_lng_lat(tags)
        if result:
            Lat, Lon = result
            url = "https://api.map.baidu.com/reverse_geocoding/v3/?ak="+self.baidu_map_ak+"&output=json&coordtype=wgs84ll&location=" + str(Lat) + ',' + str(Lon)
            #url = "https://api.map.baidu.com/reverse_geocoding/v3/?ak="+self.baidu_map_ak+"&output=json&coordtype=wgs84ll&location=31.225696563611,121.49884033194"
            response = requests.get(url).json()
            status = response['status']
            if status == 0:
                address = response['result']['formatted_address']
                if address != "":
                    return(address)
            else:
                print('baidu_map error')
        return ""

    
    
    
if __name__ == '__main__':
    instance = PhotoExifInfo()
    
