#!/usr/bin/python  

import urllib.request, urllib.parse, sys, os, platform

def main(video_id):
    try:
        url = urllib.request.urlopen('https://www.youtube.com/get_video_info?video_id=' + video_id[32:])
        url_data = url.read()
    except:
        print('Can\'t read URL DATA!')
        return
    try:
        url_info = urllib.parse.parse_qs(url_data.decode('utf-8'))
        video_title = url_info['title'][0]
    except:
        reason = url_info['reason'][0]
        print('Can\'t parse URL! Reason:' + reason)
        return
    for symbol in ['\\','/',':','*','?','"','<','>','|']:
           video_title = video_title.replace(symbol,' ')  
    file_name = video_title + '.mp4'
    url_stream_map = url_info['url_encoded_fmt_stream_map'][0]
    video_info = url_stream_map.split(',')
    item = urllib.parse.parse_qs(video_info[0])
    item_url = item['url'][0]
   
    url = urllib.request.urlopen(item_url)
    length = int(url.headers['Content-Length'])
    buffer = url.read(1024)
    done = 0
    video_file = open(os.path.expanduser('~') + '\\Desktop\\' + file_name,'wb+')
    while buffer:
        done += 1024
        percent = done * 100 // length
        print('\r' + str(percent) + '%')
        video_file.write(buffer)
        buffer = url.read(1024)
    video_file.close()
    print('Download complited!')

if __name__ == '__main__':
    if len (sys.argv) > 1:
       main(sys.argv[1])
    else:
       print('Enter youtube video link as a parametr!')
