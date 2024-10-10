import os
import logging

# Function to download media (photos) and save in the folder
async def download_images(message, channel_name, client):
    try:
        # Create folder if it doesn't exist
        folder_path = 'photos/'
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # If message contains media and it's a photo, download it
        if message.media and 'image' in message.media.document.mime_type:
            file_path = os.path.join(folder_path, f"{message.id}.jpg")
            await client.download_media(message, file_path)
            logging.info(f"Downloaded image from message {message.id} in {channel_name}")
            return file_path
        return None
    except Exception as e:
        logging.error(f"Error downloading image from message {message.id}: {e}")
