import requests
import os
import re
import zipfile
import wget

class download_chromedriver():
    def __init__(self, pathToDownload):
        self.path = pathToDownload

        if os.name == 'nt':
            replies = os.popen(r'reg query "HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon" /v version').read()
            replies = replies.split('\n')
            for reply in replies:
                if 'version' in reply:
                    reply = reply.rstrip()
                    reply = reply.lstrip()
                    tokens = re.split(r"\s+", reply)
                    fullversion = tokens[len(tokens) - 1]
                    tokens = fullversion.split('.')
                    self.version = tokens[0]
                    break
        url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE_' + str(self.version)
        print(url)
        response = requests.get(url)
        self.version_number  = response.text
        if 'NoSuchKey' in str(self.version_number):
            url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE_' + str(int(self.version)-1)
            print(url)
            response = requests.get(url)
            self.version_number = response.text

    def download(self):
        self.download_url = "https://chromedriver.storage.googleapis.com/" + self.version_number + "/chromedriver_win32.zip"
        print(self.download_url)

        # download the zip file using the url built above
        latest_driver_zip = wget.download(self.download_url, out='./files/chromedriver.zip')

        # extract the zip file
        with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
            zip_ref.extractall(path = './files/') # you can specify the destination folder path here
        # delete the zip file downloaded above
        os.remove(latest_driver_zip)
        # os.rename(driver_binaryname, target_name)
        # os.chmod(target_name, 755)



    # elif os.name == 'posix':
    #     reply = os.popen(r'chromium --version').read()
    #
    #     if reply != '':
    #         reply = reply.rstrip()
    #         reply = reply.lstrip()
    #         tokens = re.split(r"\s+", reply)
    #         fullversion = tokens[1]
    #         tokens = fullversion.split('.')
    #         version = tokens[0]
    #     else:
    #         reply = os.popen(r'google-chrome --version').read()
    #         reply = reply.rstrip()
    #         reply = reply.lstrip()
    #         tokens = re.split(r"\s+", reply)
    #         fullversion = tokens[2]
    #         tokens = fullversion.split('.')
    #         version = tokens[0]
    #
    #     target_name = './bin/chromedriver-linux-' + version
    #     print('new chrome driver at ' + target_name)
    #     found = os.path.exists(target_name)
    #     if not found:
    #         version_number = get_latestversion(version)
    #         download_url = "https://chromedriver.storage.googleapis.com/" + version_number +"/chromedriver_linux64.zip"
    #         download(download_url, './temp/chromedriver', target_name)

