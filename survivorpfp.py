"""
Time In Profile Pic.....
Command: `.surpfp`

Custom / Modified Plugin for some magical effects by this Legendary Guy @Sur_vivor


#curse: who ever edits this credit section will goto hell

⚠️DISCLAIMER⚠️

USING THIS PLUGIN CAN RESULT IN ACCOUNT BAN + CAS BAN + SPAM BAN + ACCOUNT SUSPENSION . WE DONT CARE ABOUT BAN, SO WE ARR USING THIS.
"""
import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions
from userbot.utils import admin_cmd
import asyncio
import shutil 
import random, re


FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

#Add telegraph media links of profile pics that are to be used
TELEGRAPH_MEDIA_LINKS = ["https://telegra.ph/file/2eab4f64ead6fbf41bf87.jpg",
                         "https://telegra.ph/file/6bef1ffbaddc5230c2ae1.jpg",
                         "https://telegra.ph/file/a03f035e83098a7c5bded.jpg",
                         "https://telegra.ph/file/f0a230a30b9952f56d2cd.jpg",
                         "https://telegra.ph/file/d00e6bb4b4a483099c992.jpg",
                         "https://telegra.ph/file/1270ed675db61e6c84eea.jpg",
                         "https://telegra.ph/file/32743c9389915b02fdea7.jpg",
                         "https://telegra.ph/file/8c02a1430502bea931ff7.jpg",
                         "https://telegra.ph/file/28c242ea9f8cf32db4c21.jpg",
                         "https://telegra.ph/file/c089426ca031d1f6297b0.jpg",
                         "https://telegra.ph/file/a196b6c07f0a659daf058.jpg",
                         "https://telegra.ph/file/69f19acd13b1eaf3fc120.jpg",
                         "https://telegra.ph/file/9478a8a10a5457201b9bd.jpg",
                         "https://telegra.ph/file/2765633721f6e21a0df9e.jpg",
                         "https://telegra.ph/file/b371ebcd42849d093bfc2.jpg",
                         "https://telegra.ph/file/19b004330bf89c13f0d1d.jpg",
                        ]
@borg.on(admin_cmd(pattern="surpfp ?(.*)"))
async def autopic(event):
    while True:
        piclink = random.randint(0, len(TELEGRAPH_MEDIA_LINKS) - 1)
        AUTOPP = TELEGRAPH_MEDIA_LINKS[piclink]
        downloaded_file_name = "./userbot/original_pic.png"
        downloader = SmartDL(AUTOPP, downloaded_file_name, progress_bar=True)
        downloader.start(blocking=False)
        photo = "photo_pfp.png"
        while not downloader.isFinished():
            place_holder = None
    
    
        shutil.copy(downloaded_file_name, photo)
        im = Image.open(photo)
        current_time = datetime.now().strftime("@peru_monster \n \nTime: %H:%M:%S \nDate: %d/%m/%y")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 23)
        drawn_text.text((350, 400), current_time, font=fnt, fill=(230,230,250))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                file
            ))
            os.remove(photo)
            
            await asyncio.sleep(30)
        except:
            return
