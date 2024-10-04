import requests
import uuid
import time
import os

# Вставьте сюда ваши значения Authorization и второй tobitId
AUTHORIZATION = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsInZlciI6MSwia2lkIjoibnpkZW1kYmYifQ.eyJqdGkiOiJkNjZhNTZlZi00MzFhLTQ0OTYtYTNiZS02ZjU5NDMyOThlZDgiLCJzdWIiOiJYSUwtOU1CM0giLCJ0eXBlIjoxLCJleHAiOiIyMDI0LTA2LTIwVDE1OjI4OjI1WiIsImlhdCI6IjIwMjQtMDYtMTZUMTU6Mjg6MjVaIiwiTG9jYXRpb25JRCI6Mzc4LCJTaXRlSUQiOiI2MDAyMS0wODk4OSIsIklzQWRtaW4iOmZhbHNlLCJUb2JpdFVzZXJJRCI6NTE0MzM0OCwiUGVyc29uSUQiOiJYSUwtOU1CM0giLCJGaXJzdE5hbWUiOiJNdWhvIiwiTGFzdE5hbWUiOiJ0dWhvIiwiUm9sZXMiOlsic3dpdGNoX2xvY2F0aW9uIl19.dbNjCHHikxSJCyIJm4R4HH700_MK6fi_s1nO7Hyp6Bn3ItXf8I1RioFyzMqsWFc_5fRS1-zXAWO5uO_VBWx1FWFZdcTn_kAq-4PcN_PCtdJwaHfVd7J4ZNearXIv65eCzYD20enQZCgnuVrce4MtfoIRco3DUIX2JNjf79ltTulJdTmZXzYDS65JwjFhGbPRuUCsXwbLuSANKPr7HIU7P2XDHc9L2Wi9cEX0taMNEdZSMPIlwv5LgTIxxSpsycxdSUZdkqBT5vlF8cH1916TbEh3L7DSJGR8341P_yvMsJqjCdrg6n-e5XTCsOPdKWG8UOdHn9-dCRO1rydXwr-fIw"
SECOND_TOBIT_ID = 5143348
# По дефолту сейчас стоит GPT-4-Turbo
AI_TOBIT_ID = 5099960
AI_MODEL = 6

# Настройки для первого запроса на создание потока
create_thread_url = "https://intercom.tobit.cloud/api/thread"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
    "Accept": "*/*",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Authorization": AUTHORIZATION,
    "Content-Type": "application/json",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "Priority": "u=1"
}

data = {
    "forceCreate": True,
    "thread": {
        "aiModelType": AI_MODEL,
        "anonymizationForAI": False,
        "members": [
            {"tobitId": AI_TOBIT_ID},
            {"tobitId": SECOND_TOBIT_ID}
        ],
        "name": "Unbenannt",
        "priority": 0
    }
}

def fix_path(file_path):
    # Удаляем лишние кавычки
    file_path = file_path.strip('\"')
    # Заменяем одинарные обратные слэши на двойные
    file_path = file_path.replace("\\", "\\\\")
    return file_path

# Функции для работы с API
def create_thread():
    try:
        response = requests.post(create_thread_url, headers=headers, json=data)
        if response.status_code == 201:
            response_json = response.json()
            thread_id = response_json.get('thread', {}).get('id', 'ID not found')
            print(f"Thread ID: {thread_id}")
            return thread_id
        else:
            print(f"Failed to create thread. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Exception: {e}")
    return None

def send_message(thread_id, message_text, image_url=None):
    try:
        url = f"https://intercom.tobit.cloud/api/thread/{thread_id}/message"
        body = {
            "author": {"tobitId": SECOND_TOBIT_ID},
            "message": {
                "guid": str(uuid.uuid4()),
                "meta": {},
                "text": message_text,
                "typeId": 1
            }
        }
        if image_url:
            body["message"]["images"] = [{"url": image_url}]

        response = requests.post(url, headers=headers, json=body)
        if response.status_code == 201:
            data = response.json()
            creation_time = data.get('message', {}).get('creationTime', None)
            if creation_time:
                print("Message sent successfully.")
                return creation_time
        else:
            print(f"Failed to send message. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Exception: {e}")
    return None

def get_messages(thread_id, date):
    try:
        member_id = "0da73a5e-3741-42d5-92b9-bcc6da82c0f1"
        url = f"https://intercom.tobit.cloud/api/thread/{thread_id}/messages?memberId={member_id}&date={date}"

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            for message in data.get("messages", []):
                print(message.get("text", "No text"))
            return True
        elif response.status_code == 204:
            return False
        else:
            print(f"Failed to get messages. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Exception: {e}")
    return False

def upload_image(file_path):
    try:
        # Исправляем путь к файлу
        file_path = fix_path(file_path)
 
        url = "https://cube.tobit.cloud/image-service/v3/Images/ZBN-7LPIN"
        base_image_url = "https://tsimg.cloud/"

        headers = {
            "accept": "application/json",
            "accept-language": "ru,en;q=0.9",
            "authorization": AUTHORIZATION,
            "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"YaBrowser\";v=\"24.4\", \"Yowser\";v=\"2.5\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site"
        }

        files = {'File': (file_path, open(file_path, 'rb'), 'image/jpeg')}

        response = requests.post(url, headers=headers, files=files)
        if response.status_code == 201:
            image_path = response.json().get('image', {}).get('path')
            if image_path:
                full_image_url = base_image_url + image_path
                print(f"Image uploaded successfully: {full_image_url}")
                return full_image_url
        else:
            print(f"Failed to upload image. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Exception: {e}")
    return None

# Главная функция
def main():
    current_thread_id = None

    while True:
        if current_thread_id:
            choice = input("Продолжить с текущим Thread ID (1), начать заново (2) или выйти (3)? ")
        else:
            choice = '2'

        if choice == '1' and current_thread_id:
            message_text = input("Введите сообщение для отправки в API: ")
            upload_choice = input("Хотите загрузить фото? (да/нет): ").strip().lower()
            image_url = None
            if upload_choice == 'да':
                file_path = input("Введите путь или название файла фото: ")
                image_url = upload_image(file_path)
            creation_time = send_message(current_thread_id, message_text, image_url)

            if creation_time:
                print("Ваш запрос был успешно отправлен! Ожидайте ответа")
                while True:
                    if get_messages(current_thread_id, creation_time):
                        break
                    time.sleep(0.5)
        elif choice == '2':
            current_thread_id = create_thread()
            if current_thread_id:
                user_message = input("Введите сообщение для отправки в API: ")
                message_text = (
                    f"{user_message}"
                )
                upload_choice = input("Хотите загрузить фото? (да/нет): ").strip().lower()
                image_url = None
                if upload_choice == 'да':
                    file_path = input("Введите путь или название файла фото: ")
                    image_url = upload_image(file_path)
                creation_time = send_message(current_thread_id, message_text, image_url)

                if creation_time:
                    print("Ваш запрос был успешно отправлен! Ожидайте ответа")
                    while True:
                        if get_messages(current_thread_id, creation_time):
                            break
                        time.sleep(0.5)
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")

if __name__ == "__main__":
    main()