import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        file_path = file_path.replace('\\', '%2F')
        header = {'Content-Type': 'application/json',
                  'Accept': 'application/json',
                  'Authorization': f'OAuth {self.token}'}
        url_request = "https://cloud-api.yandex.net:443/v1/disk/resources/upload?path=" + file_path
        response = requests.get(url_request, headers=header)
        json_response = response.json()
        if response.status_code != 200:
            return "Wrong file's path!"
        url_request = json_response['href']
        response = requests.put(url_request)
        if response.status_code == 201:
            return 'OK!'
        else:
            return 'Error!'


if __name__ == '__main__':
    TOKEN = input()
    uploader = YaUploader(TOKEN)
    FILE_PATH = input()
    result = uploader.upload(FILE_PATH)
    print(result)