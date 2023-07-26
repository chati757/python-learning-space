import requests
import io
import pandas as pd

default_headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0"
}

def download_file(url, save_path):
    try:

        response = requests.get(url,headers=default_headers, stream=True)
        response.raise_for_status()

        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"File downloaded and saved at: {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

#แบบไม่ต้องเก็บลง disk ก่อนแต่ได้ Dataframe เลย
def download_and_convert_to_dataframe(url):
    try:
        response = requests.get(url,headers=default_headers)
        response.raise_for_status()

        # ใช้ io.BytesIO เพื่อเก็บข้อมูลใน buffer
        buffer = io.BytesIO(response.content)

        # อ่านไฟล์ Excel (.xlsx) จาก buffer และแปลงเป็น DataFrame
        df = pd.read_excel(buffer)

        return df
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None

if __name__ == "__main__":
    url = "https://www.thai-cac.com/system/export/?action=excel-company&kw=&status=all&type=&fchar=&order=&npage=1"
    
    #download file ธรรมดา
    '''
    save_path = "downloaded_file.xlsx"
    download_file(url, save_path)
    df = pd.read_excel(f'./{save_path}')
    print(df)
    '''

    #download แบบ fireless
    df = download_and_convert_to_dataframe(url)
    print(df)
    import pdb;pdb.set_trace()