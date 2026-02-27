import os
import io
import re
import sys
import time
import json
import random
import string
import requests
import platform
import threading
import pytz
import datetime
import psutil
from datetime import datetime, timezone
from time import strftime
from threading import Timer
from faker import Faker
from gtts import gTTS
from telebot import TeleBot, types
from telebot.types import ChatPermissions, Message
from imgurpython import ImgurClient
from io import BytesIO
import yt_dlp
import telebot
import pycountry
os.system("cls" if os.name == "nt" else "clear")
ADMIN_ID = [6107281736]

    
def mtt_sendreaction(bot_token, chat_id, message_id, emoji, is_big):
        url = f"https://api.telegram.org/bot{bot_token}/setMessageReaction"
        payload = {
            "chat_id": chat_id,
            "message_id": message_id,
            "reaction": [
                {
                    "type": "emoji",
                    "emoji": emoji
                }
            ],
            "is_big": is_big
        }
        requests.post(url, json=payload)
        
    
bot = telebot.TeleBot('8713191831:AAF_6jOcpgW-vTzoiQyl0AwEppl9mx0P8zY', parse_mode='HTML')

# Ghi nhận thời gian bắt đầu bot
start_time = time.time()

# Hàm định dạng thời gian uptime
def format_uptime(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h} giờ {m} phút {s} giây"

# Lệnh /upt
@bot.message_handler(commands=['upt'])
def on_upt_command(message):
    try:
        uptime = format_uptime(time.time() - start_time)

        # RAM
        mem = psutil.virtual_memory()
        total_mem = mem.total / (1024 ** 3)
        used_mem = mem.used / (1024 ** 3)
        ram_percent = mem.percent

        # Ping (thời gian bot đã chạy)
        ping_real = int((time.time() - start_time) * 1000)
        bot_status = "✅ Mượt mà" if ping_real < 200 else "⚠️ Trung bình" if ping_real < 800 else "❌ Chậm"

        # Thông tin người dùng
        user_name = message.from_user.full_name

        # Tin nhắn phản hồi
        reply_msg = f"""
<blockquote expandable>
<b>📊 BÁO CÁO TRẠNG THÁI HỆ THỐNG</b>

<b>⏱ Thời gian</b>
  • <b>Hiện tại:</b> {time.strftime('%H:%M:%S')} | {time.strftime('%d/%m/%Y')}
  • <b>Thời gian hoạt động:</b> {uptime}

<b>🤖 Tình trạng Bot</b>
  • <b>Trạng thái:</b> {bot_status}
  • <b>Ping:</b> {ping_real} ms

<b>🖥 Thông tin hệ thống</b>
  • <b>Hệ điều hành:</b> {platform.system()} {platform.release()}
  • <b>CPU:</b> {os.cpu_count()} lõi
  • <b>RAM đã dùng:</b> {ram_percent}% ({used_mem:.2f} GB / {total_mem:.2f} GB)
  • <b>Python:</b> {platform.python_version()}

<b>👤 Yêu cầu từ</b>
  • <b>Người dùng:</b> {user_name}
</blockquote>
        """

        bot.send_message(message.chat.id, reply_msg.strip(), parse_mode="HTML")

    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")
    
    
# Hàm kiểm tra xem người dùng có phải admin hay không
def haha(chat_id, user_id):
    try:
        admins = bot.get_chat_administrators(chat_id)
        for admin in admins:
            if admin.user.id == user_id:
                return True
        return False
    except Exception as e:
        pass
        return False

# Xử lý tin nhắn chứa file
@bot.message_handler(content_types=['document'])
def handle_file(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    message_id = message.message_id

    # Kiểm tra nếu người dùng không phải admin thì xóa file
    if not haha(chat_id, user_id):
        try:
            bot.delete_message(chat_id, message_id)
        except Exception as e:
            pass
@bot.message_handler(commands=['taitool_adr'])
def taitool_adr(message):
    video = random.choice(["https://offvn.io.vn/bot.gif"])
    taitool_adr = (
        '<blockquote expandable>Tải ToolGopHerlysWar Trên Android Vào Đây Nhé: <a href="https://keyherlyswar.x10.mx/huongdan">Click Vào Đây</a></blockquote>'
    )
    bot.send_video(message.chat.id, video=video, caption=taitool_adr, reply_to_message_id=message.message_id, supports_streaming=True, parse_mode='HTML')

@bot.message_handler(commands=['taitool_ios'])
def taitool_ios(message):
    video = random.choice(["https://offvn.io.vn/bot.gif"])
    taitool_ios = (
        '<blockquote expandable>Tải ToolGopHerlysWar Trên Ios Vào Đây Nhé: <a href="https://www.mediafire.com/file/72dfs4b1gzwts0z/ToolGopHerlysWar.py/file">Click Vào Đây</a></blockquote>'
    )
    bot.send_video(message.chat.id, video=video, caption=taitool_ios, reply_to_message_id=message.message_id, supports_streaming=True, parse_mode='HTML')

@bot.message_handler(commands=['setuptool_adr'])
def setuptool_adr(message):
    video = random.choice(["https://offvn.io.vn/bot.gif"])
    setuptool_adr = (
        'B1: Tải Termux Bản Mới Nhất Tại: <a href="https://apkcombo.com/termux/com.termux/download/apk?from=cf&iat=1648037570&ref=https://download.apkcombo.com/com.termux/Termux_0.118.0_apkcombo.com.apk.html?ecp=Y29tLnRlcm11eC8wLjExOC4wLzExOC41MThkOGEwNDliMzFlZTI4ZTBkZjczZTVmYTIxZjM4NmZjNDY4ODg4LmFwaw%3D%3D&sig=d30b8e703fd3184ecaae3e2e0733885a&size=101739523&sj=1&utm_source=download-gone&version=latest">Click Vào Đây</a>\n'
        'B2: Sau Khi Tải Xong, Tiến Hành Cài Đặt Và Mở App Lên Rồi Copy Dán Dòng Lệnh Sau Vào Rồi Ấn Enter:\n'
        '<blockquote expandable><code>termux-setup-storage && pkg update && pkg upgrade && pkg install php && pkg install python && pip install requests && cd /sdcard/download && python ToolGopHerlysWar.py</code></blockquote>\n'
        'Từ Lần Sau Mỗi Khi Muốn Chạy Thì Nhập Lệnh:\n'
        '<blockquote expandable><code>cd /sdcard/download && python ToolGopHerlysWar.py</code></blockquote>'
    )
    bot.send_video(message.chat.id, video=video, caption=setuptool_adr, reply_to_message_id=message.message_id, supports_streaming=True, parse_mode='HTML')
    
    
@bot.message_handler(commands=['setuptool_ios'])
def setuptool_ios(message):
    video = random.choice(["https://offvn.io.vn/bot.gif"])
    setuptool_ios = (
        'B1: Tải Ish Shell Mới Nhất Tại : <a href="https://apps.apple.com/app/id1436902243">Click Vào Đây</a>\n'
        'B2: Sau Khi Cài Đặt Xong, Mở App Lên Rồi Copy Dán Dòng Lệnh Sau Vào Rồi Enter:\n'
        '<blockquote expandable><code>apk update && apk upgrade && apk add python3 && python3 --version && cat /dev/location > /dev/null &</code></blockquote>\n'
        'Từ Lần Sau Mỗi Khi Muốn Chạy Thì Nhập Lệnh:\n'
        '<blockquote expandable><code>python3 ToolGopHerlysWar.py</code></blockquote>'
    )
    bot.send_video(message.chat.id, video=video, caption=setuptool_ios, reply_to_message_id=message.message_id, supports_streaming=True, parse_mode='HTML')
    
@bot.message_handler(commands=['tv'])
def send_tv(message):
    full_name = message.from_user.full_name
    user_tag = f'<a href="tg://user?id={message.from_user.id}">{full_name}</a>'
    
    # Danh sách video hoặc GIF (có thể thay thế bằng file .mp4 nếu muốn dùng send_video)
    video = random.choice(["https://offvn.io.vn/bot.gif"])

    # Nội dung chú thích
    caption = (
        f"Xin chào {user_tag}!\n"
        '<blockquote expandable><a href="https://t.me/setlanguage/abcxyz">Đổi sang Tiếng Việt 🇻🇳</a></blockquote>\n'
        '<blockquote expandable><a href="https://t.me/setlanguage/vi-beta">Đổi sang Tiếng Việt (Beta) 🇻🇳</a></blockquote>'
    )

    # Gửi ảnh động (GIF)
    bot.send_animation(
        chat_id=message.chat.id,
        animation=video,
        caption=caption,
        reply_to_message_id=message.message_id
    )
@bot.message_handler(commands=['menu'])
def send_help(message):
    full_name = message.from_user.full_name
    user_tag = f'<a href="tg://user?id={message.from_user.id}">{full_name}</a>'
    menu = (
        f"Xin chào {user_tag}!\n\n"
        "Dưới đây là danh sách các lệnh mà bạn có thể sử dụng:\n"
        "<blockquote expandable>"
        "<b>• CHUNG</b>\n"
        "▫️ /menu - Hiển thị menu\n"
        "▫️ /muavip - Mua VIP để sử dụng chức năng\n"
        "▫️ /upt - Kiểm tra thời gian hoạt động bot\n"
        "▫️ /tv - Chuyển ngôn ngữ sang tiếng Việt\n\n"
        
        "<b>• ADMIN</b>\n"
        "▫️ /mad - Menu dành cho admin\n\n"

        "<b>• CÔNG CỤ & TIỆN ÍCH</b>\n"
        "▫️ /getid - Lấy ID Telegram\n"
        "▫️ /idbox - Lấy ID nhóm (box)\n"
        "▫️ /qrbank - Tạo mã QR chuyển khoản\n"
        "▫️ /qrcode - Tạo mã QR từ văn bản\n"
        "▫️ /cap - Chụp màn hình website\n"
        "▫️ /voice - Chuyển văn bản thành giọng nói\n"
        "▫️ /imgur - Tải ảnh lên Imgur\n\n"

        "<b>• THÔNG TIN</b>\n"
        "▫️ /weather - Dự báo thời tiết\n"
        "▫️ /thongtin - Thông tin tài khoản Telegram\n"
        "▫️ /contact - Liên hệ admin\n"
        "▫️ /dinhgiasdt - Định giá số điện thoại\n\n"

        "<b>• XÃ HỘI</b>\n"
        "▫️ /tt - Thông tin TikTok\n"
        "▫️ /fb - Thông tin Facebook\n"
        "▫️ /ff - Thông tin Free Fire\n"
        "▫️ /cc - Thông tin Capcut\n"
        "▫️ /zalo - Thông tin Zalo\n"
        "▫️ /avtfb - Lấy avatar Facebook\n\n"

        "<b>• GIẢI TRÍ</b>\n"
        "▫️ /gaitt - Video gái TikTok\n"
        "▫️ /videogai - Video gái ngẫu nhiên\n"
        "▫️ /anhgai - Ảnh gái xinh\n"
        "▫️ /anhdu - Ảnh dú\n"
        "▫️ /anhlon - Ảnh lon\n"
        "▫️ /anhnude - Ảnh nude\n\n"

        "<b>• TOOL HERLYS WAR</b>\n"
        "▫️ /taitool_adr - Link tải cho Android\n"
        "▫️ /taitool_ios - Link tải cho iOS\n"
        "▫️ /setuptool_adr - Hướng dẫn cài đặt Android\n"
        "▫️ /setuptool_ios - Hướng dẫn cài đặt iOS\n"
        "</blockquote>\n"
        "<i>💡 Mẹo:</i> Bấm vào lệnh để xem hướng dẫn sử dụng."
    )
    bot.send_message(message.chat.id, menu, parse_mode="HTML")


@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_member(message):
    for member in message.new_chat_members:
        full_name = member.full_name  # Lấy tên đầy đủ của thành viên mới
        user_tag = f'<a href="tg://user?id={member.id}">{full_name}</a>'
        chat_title = f'<b>{message.chat.title}</b>'  # Tag tên nhóm
        video = random.choice(["https://keyherlyswar.x10.mx/VID_20241009_190557_165.mp4"])
        welcome = (
            f"Xin Chào 👋! <b>{user_tag}</b>\n"
            f"<blockquote expandable>Đã Tham Gia Nhóm: {chat_title}\n"
            "Sử Dụng Lệnh /menu Để Xem Chi Tiết.</blockquote>"
        )
        bot.send_video(message.chat.id, video=video, caption=welcome, reply_to_message_id=message.message_id, supports_streaming=True, parse_mode='HTML')

@bot.message_handler(content_types=['left_chat_member'])
def goodbye_member(message):
    left_member = message.left_chat_member
    full_name = left_member.full_name  # Lấy tên đầy đủ của thành viên rời
    user_tag = f'<a href="tg://user?id={left_member.id}">{full_name}</a>'
    chat_title = f'<b>{message.chat.title}</b>'  # Tag tên nhóm

    goodbye_message = (
        f"Tạm Biệt, <b>{user_tag}</b>! 👋\n"
        f"<blockquote expandable>Chúng tôi rất tiếc khi bạn rời khỏi <b>{chat_title}</b>.\n"
        "Chúc bạn mọi điều tốt đẹp trong tương lai! 🌟\n"
        "Hy vọng bạn sẽ quay lại với chúng tôi một ngày không xa! 😊</blockquote>"
    )

    bot.send_message(message.chat.id, goodbye_message, parse_mode='HTML')
    
    # Lưu ID người dùng vào danh sách
    user_left_group.add(left_member.id)
    
@bot.message_handler(commands=['everyone'])
def notify_everyone(message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    # Kiểm tra nếu người dùng là admin
    if user_id not in ADMIN_ID:
        bot.reply_to(message, "<blockquote expandable>⚠️ Bạn không có quyền sử dụng lệnh này!</blockquote>", parse_mode='HTML')
        return

    # Kiểm tra nếu thông điệp có đủ thông tin
    if len(message.text.split()) < 2:
        bot.reply_to(message, "⚠️ Vui lòng nhập đúng lệnh: /everyone + tin nhắn cần báo.")
        return

    # Tạo thông điệp muốn gửi
    notification_message = "📢 THÔNG BÁO: " + " ".join(message.text.split()[1:])  # Thông điệp từ lệnh

    # Lấy danh sách thành viên trong nhóm
    members = bot.get_chat_administrators(chat_id)
    
    # Gửi thông báo đến từng thành viên không phải bot
    for member in members:
        try:
            user_id = member.user.id
            full_name = member.user.full_name
            
            # Tạo tag cho thành viên
            tag_message = f'<a href="tg://user?id={user_id}">{full_name}</a> đã nhận thông báo: {notification_message}'
            bot.send_message(user_id, tag_message, parse_mode='HTML')
        except Exception as e:
            print(f"Lỗi khi gửi thông báo cho {full_name}: {str(e)}")  # Ghi lại lỗi nếu có

    # Gửi tin nhắn tổng hợp đến nhóm
    bot.send_message(chat_id, notification_message, parse_mode='HTML')

@bot.message_handler(commands=['voice'])
def speak(message):
    tenlist = message.text.split()[1:]
    if len(tenlist) == 0:
        bot.reply_to(message, "<blockquote expandable>⚠️ Vui lòng nhập đúng lệnh: /voice + tin nhắn chuyển thành voice</blockquote>")
        return
    
    hahah = ' '.join(tenlist)
    noidung = f"{hahah}"
    
    tts = gTTS(text=noidung, lang='vi')
    audio = BytesIO()
    tts.write_to_fp(audio)
    audio.seek(0)
    
    bot.send_audio(message.chat.id, audio, caption=f"<blockquote expandable>Voice: {hahah}</blockquote>")

@bot.message_handler(commands=['ban'])
def ban_user(message):
    # Lấy ID người dùng và nhóm
    user_id = message.from_user.id
    chat_id = message.chat.id

    # Kiểm tra xem người gửi lệnh có phải là admin không
    admins = bot.get_chat_administrators(chat_id)
    admin_ids = [admin.user.id for admin in admins]
    
    if user_id not in admin_ids:
        bot.reply_to(message, "<blockquote expandable>⚠️ Bạn không có quyền sử dụng lệnh này!</blockquote>", parse_mode='HTML')
        return
    
    # Kiểm tra cú pháp lệnh và lấy ID người dùng cần ban
    if len(message.text.split()) == 2:
        try:
            user_to_ban_id = int(message.text.split()[1])
            bot.kick_chat_member(chat_id, user_to_ban_id)
            bot.reply_to(message, f"👤 Đã ban thành viên có ID: {user_to_ban_id}")
        except ValueError:
            bot.reply_to(message, "⚠️ Vui lòng nhập ID người dùng hợp lệ!")
    else:
        bot.reply_to(message, "⚠️ Cú pháp sai! Sử dụng: /ban [ID người dùng]")
@bot.message_handler(commands=['mute'])
def mute_user(message):
    # Lấy ID người dùng và nhóm
    user_id = message.from_user.id
    chat_id = message.chat.id

    # Kiểm tra xem người gửi lệnh có phải là admin không
    admins = bot.get_chat_administrators(chat_id)
    admin_ids = [admin.user.id for admin in admins]
    
    if user_id not in admin_ids:
        bot.reply_to(message, "<blockquote expandable>⚠️ Bạn không có quyền sử dụng lệnh này!</blockquote>", parse_mode='HTML')
        return
    
    # Kiểm tra cú pháp lệnh và lấy ID người dùng cần mute và thời gian
    if len(message.text.split()) == 3:
        try:
            user_to_mute_id = int(message.text.split()[1])  # ID của người dùng cần mute
            mute_time_in_hours = int(message.text.split()[2])  # Thời gian tắt tiếng (giờ)

            # Tính thời gian tắt tiếng (seconds)
            mute_until_timestamp = int(time.time()) + (mute_time_in_hours * 3600)
            
            # Mute người dùng
            bot.restrict_chat_member(
                chat_id, 
                user_to_mute_id, 
                can_send_messages=False, 
                until_date=mute_until_timestamp
            )

            bot.reply_to(message, f"🔇 Đã mute thành viên có ID: {user_to_mute_id} trong {mute_time_in_hours} giờ.")
        except ValueError:
            bot.reply_to(message, "⚠️ Vui lòng nhập ID người dùng và thời gian hợp lệ!")
    else:
        bot.reply_to(message, "⚠️ Cú pháp sai! Sử dụng: /mute [ID người dùng] [số giờ]")
@bot.message_handler(commands=['unmute'])
def unmute_user(message):
    # Lấy ID người dùng và nhóm
    user_id = message.from_user.id
    chat_id = message.chat.id

    # Kiểm tra xem người gửi lệnh có phải là admin không
    admins = bot.get_chat_administrators(chat_id)
    admin_ids = [admin.user.id for admin in admins]
    
    if user_id not in admin_ids:
        bot.reply_to(message, "<blockquote expandable>⚠️ Bạn không có quyền sử dụng lệnh này!</blockquote>", parse_mode='HTML')
        return
    
    # Kiểm tra cú pháp lệnh và lấy ID người dùng cần mở lại tiếng
    if len(message.text.split()) == 2:
        try:
            user_to_unmute_id = int(message.text.split()[1])  # ID của người dùng cần unmute

            # Mở lại quyền gửi tin nhắn cho người dùng
            bot.restrict_chat_member(
                chat_id, 
                user_to_unmute_id, 
                can_send_messages=True, 
                can_send_media_messages=True, 
                can_send_polls=True, 
                can_send_other_messages=True, 
                can_add_web_page_previews=True, 
                can_invite_users=True
            )

            bot.reply_to(message, f"🔊 Đã mở lại tiếng cho thành viên có ID: {user_to_unmute_id}.")
        except ValueError:
            bot.reply_to(message, "⚠️ Vui lòng nhập ID người dùng hợp lệ!")
    else:
        bot.reply_to(message, "⚠️ Cú pháp sai! Sử dụng: /unmute [ID người dùng]")
@bot.message_handler(commands=['getid'])
def get_user_id(message):
    chat_id = message.chat.id

    # Nếu người dùng trả lời tin nhắn
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        full_name = message.reply_to_message.from_user.full_name
        bot.send_message(chat_id, f"<blockquote expandable>ID của {full_name} là: <code>{user_id}</code>.</blockquote>", parse_mode='html')

    # Nếu người dùng tag bằng cú pháp @username
    elif message.entities:
        for entity in message.entities:
            if entity.type == 'mention':
                username = message.text[entity.offset:entity.offset + entity.length]
                try:
                    user_info = bot.get_chat(username)  # Lấy thông tin của người dùng được tag
                    user_id = user_info.id
                    full_name = user_info.full_name
                    bot.send_message(chat_id, f"<blockquote expandable>ID của {full_name} là: <code>{user_id}</code>.</blockquote>", parse_mode='html')
                except Exception as e:
                    bot.reply_to(message, "⚠️ Không thể lấy ID người dùng. Vui lòng kiểm tra lại cú pháp tag.")

    # Nếu không trả lời hoặc tag ai
    else:
        bot.reply_to(message, "⚠️ Vui lòng trả lời tin nhắn hoặc tag người dùng để lấy ID.")
      
        
@bot.message_handler(commands=['ff'])
def get_ff_info(message):
    try:
        args = message.text.split()
        if len(args) < 2:
            bot.reply_to(message, "Vui lòng nhập ID người chơi.\nVí dụ: <code>/ff 12345678</code>", parse_mode="HTML")
            return
        
        player_id = args[1]
        url = f"https://keyherlyswar.x10.mx/Apidocs/getinfoff.php?id={player_id}"
        response = requests.get(url)
        data = response.json()
        
        # Accessing the correct part of the data
        cay = data["rapidapi_info"]["data"]["basicInfo"]

        if not cay.get("accountId"):
            bot.reply_to(message, "Không tìm thấy người chơi với ID này.")
            return

        msg = f"""
<blockquote expandable><b>THÔNG TIN CƠ BẢN</b>
👤 Người Chơi: {cay["nickname"]}
🔢 UID: {cay["accountId"]}
📈 Level: {cay["level"]} | EXP: {cay["exp"]}
🌍 Khu Vực: {cay["region"]}
👍 Likes: {cay["liked"]}
📝 Tiểu Sử: {data["rapidapi_info"]["data"]["socialInfo"]["signature"]}
🏆 ST Rank: {cay["rank"]}
🥇 TC Rank: {cay["csRank"]}
📅 Ngày Tạo: {cay["createAt"]}
🕒 Login Lần Cuối: {cay["lastLoginAt"]}
🛠 Kĩ Năng: {', '.join(map(str, cay.get("weaponSkinShows", [])))}
🖼Ảnh Avatar: <a href="{data["rapidapi_info"]["data"]["basicInfo"]["avatars"][0]}">Click vào để xem ảnh</a>

<b>THÔNG TIN PET</b>
🐾 Tên Pet: {data["rapidapi_info"]["data"]["petInfo"]["name"]}
📈 Level: {data["rapidapi_info"]["data"]["petInfo"]["level"]} | EXP: {data["rapidapi_info"]["data"]["petInfo"]["exp"]}
✅ Được Chọn: {data["rapidapi_info"]["data"]["petInfo"]["isSelected"]}

<b>THÔNG TIN QUÂN ĐOÀN</b>
🏰 Tên Quân Đoàn: {data["rapidapi_info"]["data"]["clanBasicInfo"]["clanName"]}
🆔 ID: {data["rapidapi_info"]["data"]["clanBasicInfo"]["clanId"]}
📈 Level: {data["rapidapi_info"]["data"]["clanBasicInfo"]["clanLevel"]}
👥 Thành Viên: {data["rapidapi_info"]["data"]["clanBasicInfo"]["memberNum"]}

<b>CHỦ QUÂN ĐOÀN</b>
👑 Người Chơi: {data["rapidapi_info"]["data"]["captainBasicInfo"]["nickname"]}
🔢 UID: {data["rapidapi_info"]["data"]["captainBasicInfo"]["accountId"]}
📈 Level: {data["rapidapi_info"]["data"]["captainBasicInfo"]["level"]} | EXP: {data["rapidapi_info"]["data"]["captainBasicInfo"]["exp"]}
🌍 Khu Vực: {data["rapidapi_info"]["data"]["captainBasicInfo"]["region"]}
🏆 BR Rank: {data["rapidapi_info"]["data"]["captainBasicInfo"]["rank"]}
🥇 CS Rank: {data["rapidapi_info"]["data"]["captainBasicInfo"]["csRank"]}</blockquote>
"""

        bot.send_message(message.chat.id, msg, parse_mode="HTML")
    except Exception as e:
        bot.reply_to(message, f"Đã xảy ra lỗi: {e}")
        
@bot.message_handler(commands=['addid'])
def add_user_to_group(message):
    try:
        chat_id = message.chat.id
        # Kiểm tra quyền của admin
        if message.from_user.id not in [admin.user.id for admin in bot.get_chat_administrators(chat_id)]:
            bot.reply_to(message, "<blockquote expandable>⚠️ Bạn không có quyền sử dụng lệnh này!</blockquote>", parse_mode='HTML')
            return

        # Kiểm tra nếu người dùng trả lời tin nhắn
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
        else:
            # Tách ID người dùng từ tin nhắn, ví dụ: /addid <user_id>
            user_id = int(message.text.split()[1])

        # Tạo link mời vào nhóm
        invite_link = bot.create_chat_invite_link(chat_id)

        # Gửi link mời đến người dùng qua tin nhắn riêng
        bot.send_message(user_id, f"Bạn đã được mời vào nhóm. Nhấn vào link để tham gia: {invite_link.invite_link}")
        bot.reply_to(message, "✅ Đã gửi link mời cho người dùng.")

    except IndexError:
        bot.reply_to(message, "⚠️ Vui lòng cung cấp ID người dùng hoặc trả lời tin nhắn người dùng. Ví dụ: /addid <user_id> hoặc trả lời tin nhắn.")
    except Exception as e:
        bot.reply_to(message, f"⚠️ Không thể gửi link mời. Lỗi: {str(e)}")
      
@bot.message_handler(commands=['idbox'])
def get_group_id(message):
    chat_id = message.chat.id
    bot.reply_to(message, f"<blockquote expandable>ID của nhóm này là: <code>{chat_id}</code></blockquote>", parse_mode='HTML')
 
@bot.message_handler(commands=['contact'])
def contact(message):
    contact = (
        'Thông Tin Của Admin :\n'
        '<blockquote expandable>Facebook : <a href="https://www.facebook.com/Quanhau210">Quan Hậu</a>\n'
        'Zalo :  <a href="https://zalo.me/0794268460">Quan Hậu - 0794268460</a>\n'
        'Telegram : <a href="https://t.me/Quanhau2010">Herlys War</a>\n'
        'Nhóm : <a href="https://t.me/herlyswartool">Nhóm</a></blockquote>'
    )
    bot.send_message(message.chat.id, contact, parse_mode="HTML")

@bot.message_handler(commands=['unban'])
def unban_user(message):
    # Kiểm tra quyền admin
    chat_member = bot.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status not in ['administrator', 'creator']:
        bot.reply_to(message, "Bạn không có quyền để thực hiện lệnh này.")
        return

    # Tách user_id từ lệnh
    try:
        user_id = int(message.text.split()[1])
        bot.unban_chat_member(message.chat.id, user_id)
        bot.reply_to(message, f"Đã bỏ cấm người dùng với ID {user_id}.")
    except (IndexError, ValueError):
        bot.reply_to(message, "Vui lòng nhập ID người dùng cần unban sau lệnh.")
    except Exception as e:
        bot.reply_to(message, f"Đã xảy ra lỗi: {str(e)}")
        

        
@bot.message_handler(commands=['gaitt'])
def handle_gaitt(message):
    # Kiểm tra xem ID nhóm hiện tại có phải là nhóm cho phép không
    

    try:
        response = requests.get("https://gaitiktok.onrender.com/random?apikey=randomtnt")
        
        # Kiểm tra phản hồi từ API
        if response.status_code != 200:
            bot.send_message(message.chat.id, "<blockquote expandable>⚠️Bot Lỗi Vui Lòng Thử Lại Sau!</blockquote>", parse_mode='HTML')
            return
        
        data = response.json()["data"]
        
        play = data['play']
        author = data['author']
        digg_count = data['digg_count']
        comment_count = data['comment_count']
        play_count = data['play_count']
        share_count = data['share_count']
        download_count = data['download_count']
        title = data['title']
        duration = data['duration']
        region = data['region']

        video_path = 'tkvd.mp4'
        video_data = requests.get(play)
        with open(video_path, 'wb') as video_file:
            video_file.write(video_data.content)
        
        # Tạo nội dung tin nhắn
        gaitt = (
            "<blockquote expandable>"
            f"┏━━━━━━━━━━━━━━━━━━━━┓\n"
            f"┣➤📺 Random gái tiktok\n"
            f"┣➤🌐 Quốc gia: {region}\n"
            f"┣➤📝 Tiêu đề: {title}\n"
            f"┣➤🔍 Tên kênh: {author['nickname']}\n"
            f"┣➤😽 ID người dùng: {author['unique_id']}\n"
            f"┣➤❤ Lượt tim: {digg_count}\n"
            f"┣➤💬 Lượt bình luận: {comment_count}\n"
            f"┣➤👁‍🗨 Lượt xem: {play_count}\n"
            f"┣➤📎 Lượt share: {share_count}\n"
            f"┣➤👉 Lượt tải: {download_count}\n"
            f"┣➤⏰ Thời gian: {duration} s\n"
            f"┗━━━━━━━━━━━━━━━━━━━━┛\n"
            "</blockquote>"
        )

        # Gửi video với caption và reply_to_message_id
        with open(video_path, 'rb') as video:
            bot.send_video(
                message.chat.id,
                video=video,
                caption=gaitt,
                reply_to_message_id=message.message_id,
                supports_streaming=True,
                parse_mode='HTML'
            )
        
        # Xóa file video sau khi gửi
        os.remove(video_path)
    
    except Exception as e:
        bot.send_message(message.chat.id, "<blockquote expandable>⚠️Không Thể Gửi Video, Vui Lòng Thử Lại Sau!.</blockquote>", parse_mode='HTML')

@bot.message_handler(commands=['anhdu'])
def send_image(message):
    # Gửi tin nhắn tạm thời yêu cầu đợi
    processing_message = bot.reply_to(message, "<blockquote expandable>Vui lòng đợi 1 chút để ảnh được tải lên...</blockquote>", parse_mode='HTML')
    try:
        response = requests.get("https://keyherlyswar.x10.mx/Apidocs/anhgirl.php")
        
        if response.status_code == 200:
            data = response.json()

            if 'url' in data:
                image_url = data['url']

                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
                }
                image_data = requests.get(image_url, headers=headers)

                if image_data.status_code == 200 and image_data.content:
                    image_file = BytesIO(image_data.content)
                    image_file.name = "image.jpg"  
                    username = message.from_user.username
                    caption = f"<blockquote expandable>Ảnh Dú Mà @{username} Yêu Cầu:</blockquote>"
                    sent_message = bot.send_photo(message.chat.id, image_file, caption=caption, parse_mode="HTML")
                    
                    # Schedule deletion of the image after 1 minute
                    threading.Thread(target=delete_message_after_delay, args=(message.chat.id, sent_message.message_id, 60)).start()
                else:
                    bot.reply_to(message, "Không thể tải ảnh.")
            else:
                bot.reply_to(message, "Không gửi được ảnh")
        else:
            bot.reply_to(message, f"Yêu cầu thất bại với mã lỗi {response.status_code}")
    except Exception as e:
        bot.reply_to(message, f"Đã xảy ra lỗi: {e}")
    finally:
        # Xóa tin nhắn tạm thời yêu cầu đợi
        bot.delete_message(message.chat.id, processing_message.message_id)

def delete_message_after_delay(chat_id, message_id, delay):
    time.sleep(delay)
    bot.delete_message(chat_id, message_id)


@bot.message_handler(commands=['anhgai'])
def send_image(message):
    # Gửi tin nhắn tạm thời yêu cầu đợi
    processing_message = bot.reply_to(message, "<blockquote expandable>Vui lòng đợi 1 chút để ảnh được tải lên...</blockquote>", parse_mode='HTML')
    try:
        response = requests.get("https://keyherlyswar.x10.mx/Apidocs/anhgirl.php")
        
        if response.status_code == 200:
            data = response.json()

            if 'url' in data:
                image_url = data['url']

                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
                }
                image_data = requests.get(image_url, headers=headers)

                if image_data.status_code == 200 and image_data.content:
                    image_file = BytesIO(image_data.content)
                    image_file.name = "image.jpg"  
                    username = message.from_user.username
                    caption = f"<blockquote expandable>Ảnh Gái Mà @{username} Yêu Cầu:</blockquote>"
                    sent_message = bot.send_photo(message.chat.id, image_file, caption=caption, parse_mode="HTML")
                    
                    # Schedule deletion of the image after 1 minute
                    threading.Thread(target=delete_message_after_delay, args=(message.chat.id, sent_message.message_id, 60)).start()
                else:
                    bot.reply_to(message, "Không thể tải ảnh.")
            else:
                bot.reply_to(message, "Không gửi được ảnh")
        else:
            bot.reply_to(message, f"Yêu cầu thất bại với mã lỗi {response.status_code}")
    except Exception as e:
        bot.reply_to(message, f"Đã xảy ra lỗi: {e}")
    finally:
        # Xóa tin nhắn tạm thời yêu cầu đợi
        bot.delete_message(message.chat.id, processing_message.message_id)

def delete_message_after_delay(chat_id, message_id, delay):
    time.sleep(delay)
    bot.delete_message(chat_id, message_id)
    
    
@bot.message_handler(commands=['anhlon'])
def send_image(message):
    # Gửi tin nhắn tạm thời yêu cầu đợi
    processing_message = bot.reply_to(message, "<blockquote expandable>Vui lòng đợi 1 chút để ảnh được tải lên...</blockquote>", parse_mode='HTML')
    try:
        response = requests.get("https://keyherlyswar.x10.mx/Apidocs/anhlon.php")
        
        if response.status_code == 200:
            data = response.json()

            if 'url' in data:
                image_url = data['url']

                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
                }
                image_data = requests.get(image_url, headers=headers)

                if image_data.status_code == 200 and image_data.content:
                    image_file = BytesIO(image_data.content)
                    image_file.name = "image.jpg"  
                    username = message.from_user.username
                    caption = f"<blockquote expandable>Ảnh Lồn Mà @{username} Yêu Cầu:</blockquote>"
                    sent_message = bot.send_photo(message.chat.id, image_file, caption=caption, parse_mode="HTML")
                    
                    # Schedule deletion of the image after 1 minute
                    threading.Thread(target=delete_message_after_delay, args=(message.chat.id, sent_message.message_id, 60)).start()
                else:
                    bot.reply_to(message, "Không thể tải ảnh.")
            else:
                bot.reply_to(message, "Không gửi được ảnh")
        else:
            bot.reply_to(message, f"Yêu cầu thất bại với mã lỗi {response.status_code}")
    except Exception as e:
        bot.reply_to(message, f"Đã xảy ra lỗi: {e}")
    finally:
        # Xóa tin nhắn tạm thời yêu cầu đợi
        bot.delete_message(message.chat.id, processing_message.message_id)

def delete_message_after_delay(chat_id, message_id, delay):
    time.sleep(delay)
    bot.delete_message(chat_id, message_id)
    
@bot.message_handler(commands=['anhnude'])
def send_image(message):
    # Gửi tin nhắn tạm thời yêu cầu đợi
    processing_message = bot.reply_to(message, "<blockquote expandable>Vui lòng đợi 1 chút để ảnh được tải lên...</blockquote>", parse_mode='HTML')
    try:
        response = requests.get("https://keyherlyswar.x10.mx/Apidocs/anhnude.php")
        
        if response.status_code == 200:
            data = response.json()

            if 'url' in data:
                image_url = data['url']

                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
                }
                image_data = requests.get(image_url, headers=headers)

                if image_data.status_code == 200 and image_data.content:
                    image_file = BytesIO(image_data.content)
                    image_file.name = "image.jpg"  
                    username = message.from_user.username
                    caption = f"<blockquote expandable>Ảnh Nude Mà @{username} Yêu Cầu:</blockquote>"
                    sent_message = bot.send_photo(message.chat.id, image_file, caption=caption, parse_mode="HTML")
                    
                    # Schedule deletion of the image after 1 minute
                    threading.Thread(target=delete_message_after_delay, args=(message.chat.id, sent_message.message_id, 60)).start()
                else:
                    bot.reply_to(message, "Không thể tải ảnh.")
            else:
                bot.reply_to(message, "Không gửi được ảnh")
        else:
            bot.reply_to(message, f"Yêu cầu thất bại với mã lỗi {response.status_code}")
    except Exception as e:
        bot.reply_to(message, f"Đã xảy ra lỗi: {e}")
    finally:
        # Xóa tin nhắn tạm thời yêu cầu đợi
        bot.delete_message(message.chat.id, processing_message.message_id)

def delete_message_after_delay(chat_id, message_id, delay):
    time.sleep(delay)
    bot.delete_message(chat_id, message_id)
    
@bot.message_handler(commands=['muavip'])
def handle_muavip(message):
    chat_id = message.chat.id
    message_id = message.message_id
    from_id = message.from_user.id

    caption = (
        "<blockquote expandable>┌ Thông Tin Thanh Toán 💳\n"
        "├ Ngân Hàng : TechcomBank 🏦\n"
        "├ STK : <code>311220044444</code>\n"
        "├ Chủ TK: NGUYEN THI ANH\n"
        f"├ ND : <code>muavip_{from_id}</code>\n"
        "├ Số Tiền : 50.000đ\n"
        "├ HSD : 30 Ngày !\n"
        "└ 💬 Liên Hệ : @quanhau2010</blockquote>"
    )

    # Gửi ảnh cùng thông tin thanh toán
    bot.send_photo(chat_id, "https://files.catbox.moe/rkvxsm.jpg", caption, parse_mode="HTML", reply_to_message_id=message_id)

    # Xóa tin nhắn gốc
    
@bot.message_handler(commands=['qrbank'])
def handle_qrbank(message):
    
    chat_id = message.chat.id
    message_id = message.message_id
    args = message.text.split()

    if len(args) < 3:
        bot.send_message(chat_id, "⚠️ Vui Lòng Sử Dụng Lệnh /qrbank {STK} {Ngân hàng}\n💬 Ví Dụ: /qrbank 444888365 MBbank.", reply_to_message_id=message_id)
        return

    STK = args[1]
    BANK = args[2]

    # Kiểm tra mã QR
    qr_url = f"https://img.vietqr.io/image/{BANK}-{STK}-compact.png"
    try:
        response = requests.get(qr_url)

        if response.status_code == 200:
            # Gửi ảnh mã QR và thông tin
            caption = f"<blockquote expandable>STK: <code>{STK}</code>\nNgân Hàng: {BANK}</blockquote>"
            bot.send_photo(chat_id, qr_url, caption, parse_mode="HTML", reply_to_message_id=message_id)

            # Xóa tin nhắn gốc
            
        else:
            bot.send_message(chat_id, "Bạn nhập sai gì đó không thể tạo mã qr!", reply_to_message_id=message_id)

    except Exception as e:
        pass
@bot.message_handler(commands=['qrcode'])
def handle_qrcode(message):
    
    chat_id = message.chat.id
    message_id = message.message_id
    noidung = ' '.join(message.text.split()[1:])  # Lấy nội dung sau lệnh

    if noidung:
        # Tạo mã QR từ nội dung
        qr_code_url = f"https://api.qrserver.com/v1/create-qr-code/?data={noidung}"
        caption = f"<blockquote expandable>Nội dung QR: <code>{noidung}</code></blockquote>"
        
        # Gửi ảnh mã QR
        bot.send_photo(chat_id, qr_code_url, caption, parse_mode="HTML", reply_to_message_id=message_id)

        # Xóa tin nhắn gốc
        
    else:
        bot.send_message(chat_id, "⚠️ Vui Lòng Sử Dụng Lệnh /qrcode {nội dung}\n💬 Ví Dụ: /qrcode Hello.", reply_to_message_id=message_id)
       

@bot.message_handler(commands=['tt'])
def send_python_code(message):
    
    if len(message.text.split()) == 1:
        bot.reply_to(message, "<blockquote expandable>⚠️ Vui lòng nhập username sau lệnh /tt.\n\n💭 Ví dụ: /tt capyboiii_7</blockquote>", parse_mode='HTML')
        time.sleep(1)
        threading.Thread(target=xoatn, args=(message, 0)).start()
        return
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }
    acc = message.text.split()[1]
    gio = datetime.now().strftime('%d/%m/%Y %H:%M:%S') 
    video = random.choice(["https://offvn.io.vn/bot.gif"])
    
    try:
        home = requests.get(f"https://tiktok.com/@{acc}", headers=headers).text
        nickname = home.split('"nickname":"')[1].split('"')[0]
        username = home.split('"uniqueId":"')[1].split('"')[0]
        linkacc = "https://tiktok.com/@"+username
        tieusu = home.split('"signature":"')[1].split('"')[0]
        idacc = home.split('"id":"')[1].split('"')[0]
        dangfollow = home.split('"followingCount":')[1].split(',')[0]
        follow = home.split('"followerCount":')[1].split(',')[0]
        video_count = home.split('"videoCount":')[1].split(',')[0]
        friends = home.split('"friendCount":')[1].split('}')[0]
        heart = home.split('"heart":')[1].split(',')[0]
        xacminh = home.split('"verified":')[1].split(',')[0]
        ngonngu = home.split('"language":"')[1].split('"')[0]
        avatar_url = home.split('"avatarLarger":"')[1].split('"')[0].replace('\\u002F', '/')
        
        tiktok = (
        f'THONG TIN INFO TIKTOK\n<blockquote expandable>┌<b>Name</b>: {nickname}\n├<b>username</b>: {username}\n├<b>Link</b>: {linkacc}\n├<b>Bio</b>: {tieusu}\n├<b>ID</b>: {idacc}\n├<b>Following</b>: {dangfollow} <b>Người</b>\n├<b>Follows</b>: {follow} <b>Follow</b>\n├<b>Videos</b>: {video_count}\n├<b>Friends</b>: {friends} <b>Bạn Bè</b>\n├<b>Likes</b>: {heart}\n├<b>Verified</b>: {xacminh}\n└<b>Language</b>: {ngonngu}</blockquote>')

        bot.send_photo(message.chat.id, photo=avatar_url, caption=tiktok, reply_to_message_id=message.message_id, parse_mode='HTML')
        
        threading.Thread(target=xoatn, args=(message, 0)).start()
    except Exception as e:
        pass

# Handle the /thongtin command
@bot.message_handler(commands=['thongtin'])
def handle_check(message):
    
    # Check if the message is a reply to another user's message
    user = message.reply_to_message.from_user if message.reply_to_message else message.from_user

    # Get user profile photos and bio
    user_photos = bot.get_user_profile_photos(user.id)
    bio = bot.get_chat(user.id).bio or "Không có bio"
    
    # Get user details
    user_first_name = user.first_name
    user_last_name = user.last_name or ""
    user_username = ("@" + user.username) if user.username else "Không có username"
    user_language = user.language_code or 'Không xác định'

    # Get user's status in the chat
    status_dict = {
        "creator": "Admin chính",
        "administrator": "Admin",
        "member": "Thành viên",
        "restricted": "Bị hạn chế",
        "left": "Rời nhóm",
        "kicked": "Bị đuổi khỏi nhóm"
    }
    status = status_dict.get(bot.get_chat_member(message.chat.id, user.id).status, "Không xác định")

    # Prepare and send user information as a photo message if an avatar exists
    if user_photos.total_count > 0:
        avatar_file_id = user_photos.photos[0][-1].file_id
        caption = (
            f"👤 Thông Tin Của {'Bạn' if user.id == message.from_user.id else 'Người Dùng'}\n"
            f"<blockquote expandable>┌ ID: <code>{user.id}</code>\n"
            f"├ Tên: {user_first_name} {user_last_name}\n"
            f"├ Username: {user_username}\n"
            f"├ Ngôn ngữ: {user_language}\n"
            f"├ Trạng thái: {status}\n"
            f"├ Bio: {bio}\n"
            f"└ Avatar: Đã có avatar</blockquote>"
        )
        bot.send_photo(message.chat.id, avatar_file_id, caption=caption, parse_mode='HTML', reply_to_message_id=message.message_id)
    else:
        # Send message without avatar if user has no profile photo
        caption = (
            f"👤 Thông Tin Của {'Bạn' if user.id == message.from_user.id else 'Người Dùng'}\n"
            f"<blockquote expandable>┌ ID: <code>{user.id}</code>\n"
            f"├ Tên: {user_first_name} {user_last_name}\n"
            f"├ Username: {user_username}\n"
            f"├ Ngôn ngữ: {user_language}\n"
            f"├ Trạng thái: {status}\n"
            f"├ Bio: {bio}\n"
            f"└ Avatar: Chưa có avatar</blockquote>"
        )
        bot.reply_to(message, caption, parse_mode='HTML')

    # Delete the waiting message and remove the command message after handling
    threading.Thread(target=delete_message, args=(message, 0)).start()
    bot.delete_message(message.chat.id, waiting.message_id)

# Function to handle message deletion after a delay (optional implementation)
def delete_message(message, delay):
    import time
    time.sleep(delay)
    bot.delete_message(message.chat.id, message.message_id)

        
@bot.message_handler(commands=['cap'])
def cap(message):
    args = message.text.split()[1:]  # Lấy các tham số sau lệnh
    if not args:
        bot.reply_to(message, "Bạn phải nhập tên trang web phía sau lệnh /cap.")
        return
    
    website = args[0]  # Lấy tên trang web

    # URL để chụp ảnh trang web
    url = f"https://keyherlyswar.x10.mx/Apidocs/cap.php?url={website}"

    # Tải ảnh
    response = requests.get(url)
    if response.status_code == 200:
        file_path = f"cap_{message.from_user.id}.png"
        with open(file_path, 'wb') as file:
            file.write(response.content)

        # Gửi ảnh cho người dùng
        with open(file_path, 'rb') as file:
            bot.send_photo(message.chat.id, file, f"<blockquote expandable>Ảnh Chụp Màn Hình Web Của Bạn Nè : </blockquote>", parse_mode='html')

        # Xóa file sau khi gửi
        os.remove(file_path)
    else:
        bot.reply_to(message, "Có lỗi xảy ra khi chụp ảnh.")

# Function to generate a random strin
       

API_URL = "https://keyherlyswar.x10.mx/Apidocs/getinfofb.php?uid={facebook_id}&apikey=31122010"
def shorten_url(url):
    # Implement URL shortening or use an API for shortening URLs
    # Example: you can use a shortening service here or skip it if unnecessary.
    return url

@bot.message_handler(commands=['fb'])
def get_facebook_info(message):
    parameter = message.text.split(' ')[1] if len(message.text.split(' ')) > 1 else None
    
    if parameter is None:
        bot.send_message(message.chat.id, "❌ Vui lòng cung cấp ID Facebook sau lệnh <b>/fb</b>.", parse_mode="HTML")
        return
        
    # Determine if it's a Facebook ID or a link
    if parameter.isdigit():  # If it's a Facebook ID
        facebook_id = parameter
    else:  # If it's a Facebook link
        if 'facebook.com' not in parameter:
            bot.send_message(message.chat.id, "❌ Liên kết không hợp lệ. Vui lòng cung cấp một liên kết Facebook.", parse_mode="HTML")
            return

        # Use the API to get the Facebook ID from the URL
        api_url = f"https://offvn.x10.mx/Fb/convertID.php?url={parameter}"
        try:
            api_response = requests.get(api_url)
            api_response.raise_for_status()
            json_response = api_response.json()

            if 'id' in json_response:
                facebook_id = json_response['id']
            else:
                bot.send_message(
                    message.chat.id,
                    "❌ Không thể lấy ID từ liên kết Facebook. Vui lòng thử lại với một liên kết khác.",
                    parse_mode="HTML"
                )
                return

        except requests.RequestException as e:
            bot.send_message(
                message.chat.id,
                f"❌ Có lỗi xảy ra khi truy cập API: {e}",
                parse_mode="HTML"
            )
            return
        except Exception as e:
            bot.send_message(
                message.chat.id,
                f"❌ Có lỗi xảy ra: {e}",
                parse_mode="HTML"
            )
            return

    # Construct the URL for the avatar image
    avatar_url = f"https://graph.facebook.com/{facebook_id}/picture?width=1500&height=1500&access_token=2712477385668128%7Cb429aeb53369951d411e1cae8e810640"
    try:
        response = requests.get(avatar_url)
        response.raise_for_status()

        # Rút gọn URL ảnh
        short_url = shorten_url(response.url)
    except requests.exceptions.RequestException as e:
        bot.send_message(message.chat.id, "❌ Lỗi khi lấy ảnh đại diện: " + str(e))
        return

    # Fetch Facebook data
    response = requests.get(API_URL.format(facebook_id=facebook_id))
    if response.status_code == 200:
        data = response.json()

        # Create the message text with the Facebook info
        message_text = "<blockquote expandable>╭──────Facebook Info───────⭓\n"
        message_text += "┌ 👤 Người Dùng\n"

        # Danh sách các trường thông tin cần hiển thị
        fields = {
            "Tên": data.get('name'),
            "ID": data.get('id'),
            "Tên người dùng": data.get('username'),
            "Ngôn ngữ": data.get('language'),
            "Đến từ": data.get('hometown', {}).get('name'),
            f"Avatar: <a href=\"{short_url}\">Nhấn Vào Để Xem</a>\n"
            "├ Link FB": data.get('link'),
            "Ngày tạo tài khoản": data.get('created_time', '').split('T')[0],
            "Người theo dõi": "{:,.0f}".format(data.get('subscribers', {}).get('summary', {}).get('total_count', 0)).replace(",", "."),  # Định dạng người theo dõi
            "Giới thiệu": data.get('about'),  # Lấy giới thiệu từ trường about
            "Ngày sinh": data.get('birthday'),
            "Giới tính": data.get('gender'),
            "Tình trạng quan hệ": data.get('relationship_status'),
            "Người quan trọng": data.get('significant_other', {}).get('name'),  # Lấy tên người quan trọng
            "ID người quan trọng": data.get('significant_other', {}).get('id'),  # Lấy ID người quan trọng
            "Xác thực": '✅' if data.get('is_verified') else '❌',
        }

        # Thêm từng trường vào tin nhắn nếu có
        for field_name, field_value in fields.items():
            if field_value:  # Chỉ thêm nếu có giá trị
                message_text += f"├ {field_name}: {field_value}\n"

        # Lấy trích dẫn yêu thích từ trường "quotes"
        quotes_string = data.get('quotes', "")
        
        # Phân tách và định dạng trích dẫn
        if quotes_string:
            quotes = quotes_string.split('\r\n\r\n')
            message_text += "├ Trích dẫn yêu thích:\n"
            for quote in quotes:
                message_text += f"│   - {quote.strip()}\n"

        message_text += "╰─────────────⭓\n\n┌ 💼 Công Việc\n"
        work = data.get('work', [])
        for idx, job in enumerate(work):
            company_name = job.get('employer', {}).get('name')
            position = job.get('position', {}).get('name')
            start_date = job.get('start_date')
            description = job.get('description')
            location = job.get('location', {}).get('name')

            if company_name or position or start_date or description or location:
                message_text += f"├ Công việc {idx + 1}:\n"
                if company_name:
                    message_text += f"│ ├ Công ty: {company_name}\n"
                if position:
                    message_text += f"│ ├ Vị trí: {position}\n"
                if location:
                    message_text += f"│ ├ Địa điểm: {location}\n"
                if start_date:
                    message_text += f"│ ├ Bắt đầu: {start_date}\n"
                if description:
                    message_text += f"│ └ Mô tả: {description}\n"

        message_text += "╰─────────────⭓\n\n┌ 🎓 Học Vấn\n"
        education = data.get('education', [])
        for idx, school in enumerate(education):
            school_name = school.get('school', {}).get('name')
            degree = school.get('type')
            major = ', '.join([conc.get('name') for conc in school.get('concentration', [])])
            year = school.get('year', {}).get('name')

            if school_name or degree or major or year:
                message_text += f"├ Học vấn {idx + 1}:\n"
                if school_name:
                    message_text += f"│ ├ Trường: {school_name}\n"
                if degree:
                    message_text += f"│ ├ Loại: {degree}\n"
                if major:
                    message_text += f"│ ├ Chuyên ngành: {major}\n"
                if year:
                    message_text += f"│ └ Năm: {year}\n"

        message_text += "╰─────────────⭓\n\n┌ 🛡️ Quyền Riêng Tư\n"
        privacy = data.get('privacy', {})
        message_text += f"├ Nội dung: {privacy.get('content', 'Không rõ')}\n"
        message_text += f"├ Ai có thể xem: {privacy.get('who_can_see', 'Không rõ')}\n"
        message_text += "╰─────────────⭓</blockquote>"

        # Then send the caption as a separate message in HTML format
        bot.send_message(message.chat.id, message_text, parse_mode='HTML')
    else:
        bot.send_message(message.chat.id, "❌ Không thể lấy thông tin. Vui lòng kiểm tra lại.", parse_mode="HTML")
        
        
@bot.message_handler(commands=['dinhgiasdt'])
def handle_dinhgiasdt(message):
    # Lấy số điện thoại từ lệnh
    sdt = message.text.split()[1] if len(message.text.split()) > 1 else None
    
    if sdt:
        # Giả định bạn có một API trả về dữ liệu JSON như bạn đã cung cấp
        url = f'https://api.sumiproject.net/valuation?sdt={sdt}'
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            # Kiểm tra dữ liệu trong response
            valuation = data.get('data', {}).get('valuation', {}).get(sdt)
            
            if valuation:
                # Gửi thông điệp định giá với blockquote
                message_text = f'<blockquote expandable>Số {sdt} của bạn được định giá là: {valuation}vnđ</blockquote>'
                bot.send_message(message.chat.id, message_text, parse_mode='HTML')
            else:
                bot.send_message(message.chat.id, 'Không tìm thấy giá trị định giá cho số điện thoại này.')
        else:
            bot.send_message(message.chat.id, 'Đã xảy ra lỗi khi lấy thông tin định giá.')
    else:
        bot.send_message(message.chat.id, 'Vui lòng nhập số điện thoại sau lệnh: /dinhgiasdt {sdt}')
        
@bot.message_handler(commands=['countryinfo'])
def country_info(message):
    args = message.text.split()[1:]
    if not args:
        bot.reply_to(message, "Vui lòng cung cấp tên quốc gia!")
        return

    country_name = " ".join(args)
    api_endpoint = f"https://restcountries.com/v3.1/name/{country_name}"

    try:
        response = requests.get(api_endpoint)
        response.raise_for_status()
        country_data = response.json()

        if not country_data:
            bot.reply_to(message, f"Không tìm thấy thông tin cho quốc gia '{country_name}'.")
            return

        country_info = country_data[0]
        name = country_info.get("name", {}).get("common", "N/A")
        official_name = country_info.get("name", {}).get("official", "N/A")
        capital = country_info.get("capital", ["N/A"])[0]
        region = country_info.get("region", "N/A")
        population = country_info.get("population", "N/A")
        languages = ", ".join(country_info.get("languages", {}).values())
        timezones = ", ".join(country_info.get("timezones", []))
        continents = ", ".join(country_info.get("continents", []))
        google_maps = country_info.get("maps", {}).get("googleMaps", "N/A")
        open_street_maps = country_info.get("maps", {}).get("openStreetMaps", "N/A")
        flags_png = country_info.get("flags", {}).get("png", "N/A")
        flags_svg = country_info.get("flags", {}).get("svg", "N/A")
        video = random.choice(["https://offvn.io.vn/bot.gif"])
        message_text = (
            "<blockquote expandable>"
            f"🌎 Quốc Gia: {name} ({official_name})\n"
            f"⛩️ Thủ Đô: {capital}\n"
            f"🧭 Vùng Đất: {region}\n"
            f"👥 Dân Số: {population}\n"
            f"📝 Ngôn Ngữ: {languages}\n"
            f"⏳ Múi giờ: {timezones}\n"
            f"🗺️ Lục Địa: {continents}\n"
            f"📍 Google Map: {google_maps}\n"
            f"🗾 Bản Đồ: {open_street_maps}\n\n"
            f"🔱 Cờ:\n{flags_png}\n{flags_svg}"
            "</blockquote>"
        )
        
        bot.send_video(message.chat.id, video=video, caption=message_text, reply_to_message_id=message.message_id, supports_streaming=True, parse_mode='HTML')
    except requests.exceptions.RequestException as e:
        bot.reply_to(message, "<blockquote expandable>Đã xảy ra lỗi khi tìm thông tin quốc gia. Vui lòng thử lại sau.</blockquote>", parse_mode='html')


# Translate weather conditions
def translate_condition(condition):
    translations = {
        'Sunny': 'Trời Nắng',
        'Mostly sunny': 'Nhiều Nắng',
        'Partly sunny': 'Nắng Vài Nơi',
        'Rain showers': 'Mưa Rào',
        'T-Storms': 'Có Bão',
        'Light rain': 'Mưa Nhỏ',
        'Mostly cloudy': 'Trời Nhiều Mây',
        'Rain': 'Trời Mưa',
        'Heavy T-Storms': 'Bão Lớn',
        'Partly cloudy': 'Mây Rải Rác',
        'Mostly clear': 'Trời Trong Xanh',
        'Cloudy': 'Trời Nhiều Mây',
        'Clear': 'Trời Trong Xanh, Không Mây'
    }
    return translations.get(condition, condition)

@bot.message_handler(commands=['weather'])
def send_weather(message):
    args = message.text.split()[1:]
    if not args:
        bot.reply_to(message, "Vui lòng cung cấp tên thành phố!")
        return
    
    city = " ".join(args)
    api_url = f"http://api.weatherapi.com/v1/current.json?key=deae5206758c44f38b0184151232208&q={city}"
    
    try:
        response = requests.get(api_url, timeout=5)
        data = response.json()

        if 'error' in data:
            bot.reply_to(message, "Không tìm thấy thành phố hoặc xảy ra lỗi.")
            return
        
        weather_info = data['current']
        location_info = data['location']
        condition = translate_condition(weather_info['condition']['text'])
        
        # Format date and time based on location's timezone
        timezone = pytz.timezone(location_info['tz_id'])
        current_time = datetime.now(timezone).strftime('%H:%M:%S - %d/%m/%Y')

        # Prepare weather information message
        weather_message = (
            f"<blockquote expandable>Thời tiết của {city} (tính đến {current_time}):\n"
            f"🌡 Nhiệt độ: {weather_info['temp_c']}°C ({weather_info['temp_f']}°F)\n"
            f"✨ Cảm giác như: {weather_info['feelslike_c']}°C ({weather_info['feelslike_f']}°F)\n"
            f"📌 Dự báo: {condition}\n"
            f"🌪️ Gió: {weather_info['wind_kph']} km/h, {weather_info['wind_dir']}\n"
            f"🌀 Ấp suất: {weather_info['pressure_mb']} mb\n"
            f"💧 Độ ẩm: {weather_info['humidity']}%\n"
            f"🧬 Chỉ số tia cực tím: {weather_info['uv']}\n"
        )
        
        additional_info = (
            f"☁️ Mây che phủ: {weather_info['cloud']}%\n"
            f"🌧️ Lượng mưa: {weather_info['precip_mm']} mm ({weather_info['precip_in']} in)\n"
            f"🌬️ Gió giật: {weather_info['gust_kph']} km/h</blockquote>\n"
        )

        # Send the message with weather information
        bot.reply_to(message, weather_message + additional_info, parse_mode='html')
    except requests.exceptions.RequestException as e:
        bot.reply_to(message, "Đã xảy ra lỗi khi tìm kiếm dữ liệu.")
        print(f"Error fetching data: {e}")
        

        
@bot.message_handler(commands=['avtfb'])
def get_facebook_avatar(message):
    
    user_id = message.from_user.id

    # Check command format
    if len(message.text.split()) != 2:
        bot.reply_to(message, 'Vui lòng nhập đúng định dạng\nExample: /avtfb [link hoặc id]')
        return

    # Get parameter from the message
    parameter = message.text.split()[1]

    # Determine if it's a Facebook ID or a link
    if parameter.isdigit():  # If it's a Facebook ID
        facebook_id = parameter
    else:  # If it's a Facebook link
        if 'facebook.com' not in parameter:
            bot.edit_message_text('Liên kết không phải từ Facebook', message.chat.id, waiting_message.message_id)
            return

        # Use the API to get the Facebook ID from the URL
        api_url = f"https://offvn.x10.mx/Fb/convertID.php?url={parameter}"
        try:
            api_response = requests.get(api_url)
            api_response.raise_for_status()
            json_response = api_response.json()

            if 'id' in json_response:
                facebook_id = json_response['id']
            else:
                bot.edit_message_text('Không thể lấy ID từ liên kết Facebook. Vui lòng thử lại với một liên kết khác.', message.chat.id, waiting_message.message_id)
                return

        except requests.RequestException as e:
            bot.edit_message_text(f'Có lỗi xảy ra khi truy cập API: {e}', message.chat.id, waiting_message.message_id)
            return
        except Exception as e:
            bot.edit_message_text(f'Có lỗi xảy ra: {e}', message.chat.id, waiting_message.message_id)
            return

    # Use the provided Facebook URL for the profile picture
    graph_url = f"https://graph.facebook.com/{facebook_id}/picture?width=1500&height=1500&access_token=2712477385668128%7Cb429aeb53369951d411e1cae8e810640"
    
    try:
        response = requests.get(graph_url)
        response.raise_for_status()

        # Send the avatar image to the user with a caption
        caption = f"<blockquote expandable>Avatar cho Facebook ID hoặc link: <code>{facebook_id}</code></blockquote>"
        bot.send_photo(message.chat.id, response.url, caption=caption, parse_mode='html')

    except requests.RequestException as e:
        bot.edit_message_text(f'Có lỗi xảy ra khi truy cập Facebook: {e}', message.chat.id, waiting_message.message_id)
    except Exception as e:
        bot.edit_message_text(f'Có lỗi xảy ra: {e}', message.chat.id, waiting_message.message_id)
        
     
        
# Lưu thời gian khởi động bot
start_time = time.time()

# Múi giờ bạn muốn (ví dụ múi giờ Hà Nội)
timezone = pytz.timezone('Asia/Ho_Chi_Minh')

# Biến đếm số lệnh đã được bot xử lý
command_count = 0

@bot.message_handler(commands=['reset'])
def handle_reset(message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    # Kiểm tra nếu người dùng là admin
    if user_id not in ADMIN_ID:
        bot.reply_to(message, "<blockquote expandable>⚠️ Bạn không có quyền sử dụng lệnh này!</blockquote>", parse_mode='HTML')
        return

    # Tính thời gian hoạt động của bot
    uptime = time.time() - start_time
    hours, remainder = divmod(int(uptime), 3600)
    minutes, seconds = divmod(remainder, 60)

    # Tính thời gian hiện tại theo múi giờ đã chọn
    current_time = datetime.now(timezone).strftime("%H:%M:%S, %d-%m-%Y")

    # Thông tin hệ thống
    system_info = platform.system() + " " + platform.release()  # Hệ điều hành
    bot_version = "1.0.0"  # Phiên bản bot

    # Thông tin tài nguyên hệ thống (CPU, RAM)
    memory = psutil.virtual_memory()  # Bộ nhớ RAM
    memory_percent = memory.percent  # Tỷ lệ sử dụng bộ nhớ

    # Dung lượng ổ cứng
    disk = psutil.disk_usage('/')  # Thông tin về ổ cứng chính
    disk_percent = disk.percent  # Tỷ lệ sử dụng ổ cứng

    # Chuẩn bị thông báo
    message_text = (
        f"<blockquote expandable><b>🔄 Khởi động lại tool</b>\n\n"
        f"<b>🕒 Thời gian hiện tại (Múi giờ {timezone.zone})</b>: {current_time}\n\n"
        f"<b>🔹 Thời gian bot hoạt động</b>: {hours} giờ {minutes} phút {seconds} giây\n\n"
        f"<b>📋 Thông tin hệ thống:</b>\n"
        f"- <b>Hệ điều hành:</b> {system_info}\n"
        f"- <b>Phiên bản bot:</b> {bot_version}\n\n"
        f"<b>🔧 Tình trạng tài nguyên hệ thống:</b>\n"
        f"- <b>RAM sử dụng:</b> {memory_percent}%\n"
        f"- <b>Ổ cứng sử dụng:</b> {disk_percent}%\n\n"
        f"<i>--- Kết thúc thông báo ---</i>\n\n"
        f"<b>⚙️ Đang khởi động lại tool...</b>\n"
        f"<b>⏳ Vui lòng chờ trong giây lát...</b></blockquote>"
    )

    # Gửi tin nhắn xác nhận với parse_mode='html'
    bot.reply_to(message, message_text, parse_mode='html')

    # Tắt bot hiện tại và chạy lại file tool
    time.sleep(1)  # Thời gian nghỉ trước khi khởi động lại
    bot.send_message(message.chat.id, "<blockquote expandable><b>🔄 Reset hoàn tất!</b>\n<b>Bot đã được khởi động lại thành công.</b></blockquote>", parse_mode='html')
    os.execv(sys.executable, ['python'] + ['bot1.py'])  # Chạy lại file tool.py
    
@bot.message_handler(commands=['mad'])
def admin_menu(message):
    full_name = message.from_user.full_name
    user_tag = f'<a href="tg://user?id={message.from_user.id}">{full_name}</a>'
    menu = (
        f"XIN CHÀO ADMIN {user_tag}\n\n"
        "DƯỚI ĐÂY LÀ DANH SÁCH LỆNH DÀNH CHO QUẢN TRỊ VIÊN:\n"
        "<blockquote expandable>"
        "• /everyone - Gửi tin nhắn đến tất cả thành viên\n"
        "• /ban - Cấm người dùng\n"
        "• /unban - Gỡ cấm người dùng\n"
        "• /mute - Tắt quyền nhắn tin của người dùng\n"
        "• /unmute - Bỏ tắt quyền nhắn tin\n"
        "</blockquote>\n"
        "⚠️ LƯU Ý: Các lệnh này chỉ sử dụng được bởi quản trị viên."
    )
    bot.send_message(message.chat.id, menu, parse_mode="HTML")
@bot.message_handler(commands=['videogai'])
def send_video(message):
    # Gửi tin nhắn tạm thời yêu cầu đợi
    processing_message = bot.reply_to(message, "<blockquote expandable>Vui lòng đợi 1 chút để video được tải lên...</blockquote>", parse_mode='HTML')
    try:
        response = requests.get("https://keyherlyswar.x10.mx/Apidocs/videogai.php")
        
        if response.status_code == 200:
            data = response.json()

            if 'url' in data:
                video_url = data['url']

                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
                }
                video_data = requests.get(video_url, headers=headers)

                if video_data.status_code == 200 and video_data.content:
                    video_file = BytesIO(video_data.content)
                    video_file.name = "video.mp4"  
                    username = message.from_user.username
                    caption = f"<blockquote expandable>Video Gái Mà @{username} Yêu Cầu:</blockquote>"
                    bot.send_video(message.chat.id, video_file, caption=caption, parse_mode='HTML')
                else:
                    bot.reply_to(message, "Không thể tải video.")
            else:
                bot.reply_to(message, "Không gửi được Video")
        else:
            bot.reply_to(message, f"Yêu cầu thất bại với mã lỗi {response.status_code}")
    except Exception as e:
        bot.reply_to(message, f"Đã xảy ra lỗi: {e}")
    finally:
        # Xóa tin nhắn tạm thời yêu cầu đợi
        bot.delete_message(message.chat.id, processing_message.message_id)




    
# Hàm lấy thông tin từ URL với tham số {link}
def get_capcut_info(link):
    url = f'https://subhatde.id.vn/capcut/info?url={link}'
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Hàm gửi thông tin tới người dùng
@bot.message_handler(commands=['cc'])
def send_capcut_info(message):
    try:
        # Lấy link từ tin nhắn
        link = message.text.split()[1]
        
        # Lấy thông tin từ URL
        data = get_capcut_info(link)
        
        if data:
            user_info = data['user']
            user_stats = data['user_statistics']
            tiktok_info = user_info['tiktok_user_info']
            vip_info = data['vip_info']
            
            # Lấy avatar và mô tả
            avatar_url = user_info['avatar_url']
            description = user_info['description'].replace("\n", "\\n")
            
            # Lấy mã giới thiệu từ mô tả nếu có
            referral_code = ""
            if "Mã giới thiệu" in description:
                referral_code = description.split("Mã giới thiệu: ")[1].split("\\n")[0]
            
            # Tạo thông điệp chi tiết với tất cả thông tin
            msg = f"""
<blockquote expandable>
╭─────────────⭓
│Thông tin người dùng CapCut:
├─────────────⭔
│- UID: {user_info['uid']}
│- Tên: {user_info['name']}
│- ID CapCut: {user_info['unique_id']}
│- Mô Tả: {description}
│- Giới tính: {"Nam" if user_info['gender'] == 1 else "Nữ"}
│- Follower CapCut: {user_info['relation_info']['statistics']['follower_count']}
├─────────────⭔
│Thông tin TikTok:
├─────────────⭔
│- Tên TikTok: {tiktok_info['name']}
│- Link TikTok: {tiktok_info['deeplink']}
├─────────────⭔
│Thống kê CapCut:
├─────────────⭔
│- Số mẫu: {user_stats['template_count']}
│- Số lượng tác phẩm: {user_stats['work_count']}
│- Tổng lượt thích: {user_stats['like_count']}
│- Số lượng mẫu yêu thích: {user_stats['favorite_count']}
├─────────────⭔
│Thông tin VIP:
├─────────────⭔
│- VIP: {"Có" if vip_info['flag'] == 1 else "Không"}
│- Thời gian bắt đầu: {vip_info['start_time']}
│- Thời gian kết thúc: {vip_info['end_time']}
│- Lợi ích hiện tại: {vip_info['benefits_info'] or "Không có"}
├─────────────⭔
│Mã giới thiệu: {referral_code or "Không có"}
╰─────────────⭓</blockquote>
"""
            # Gửi ảnh avatar và thông điệp cùng nhau
            bot.send_photo(message.chat.id, avatar_url, caption=msg, parse_mode='html')
        else:
            bot.reply_to(message, "Không thể lấy thông tin từ URL.")
    
    except IndexError:
        bot.reply_to(message, "Vui lòng nhập link CapCut theo cú pháp: /capcutinfo <link>")
        

        
        
# Cấu hình Imgur
IMGUR_CLIENT_ID = "c76eb7edd1459f3"
imgur_client = ImgurClient(IMGUR_CLIENT_ID, None)

# URL video (đảm bảo đường dẫn hợp lệ)
VIDEO_URL = "https://offvn.io.vn/bot.gif"

# Lấy thời gian hiện tại theo múi giờ
def get_current_time():
    tz = pytz.timezone("Asia/Ho_Chi_Minh")
    now = datetime.now(tz)
    return now.strftime("%H:%M:%S")

# Tải file từ URL
def download_file(url, save_path):
    response = requests.get(url, stream=True)
    with open(save_path, "wb") as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)

# Xử lý khi người dùng gửi tin nhắn
@bot.message_handler(commands=["imgur"])
def handle_imgur_command(message: Message):
    if not message.reply_to_message or not message.reply_to_message.photo:
        bot.reply_to(message, "Bạn phải reply một ảnh nào đó!")
        return
    
    start_time = time.time()

    # Tải file ảnh được reply
    attachment_urls = []
    for photo in message.reply_to_message.photo:
        file_id = photo.file_id
        file_info = bot.get_file(file_id)
        file_url = f"https://api.telegram.org/file/bot{bot.token}/{file_info.file_path}"
        attachment_urls.append(file_url)

    uploaded_links = []
    failed_files = []

    for index, url in enumerate(attachment_urls):
        save_path = f"cache_{index}.jpg"
        try:
            # Tải file về máy
            download_file(url, save_path)

            # Upload lên Imgur
            uploaded_image = imgur_client.upload_from_path(save_path, anon=True)
            uploaded_links.append(uploaded_image["link"])

            # Xóa file đã tải
            os.remove(save_path)
        except Exception as e:
            failed_files.append(url)
            print(f"Lỗi khi xử lý {url}: {e}")

    # Tổng hợp kết quả
    success_count = len(uploaded_links)
    failed_count = len(failed_files)
    current_time = get_current_time()

    result_message = (
        "<blockquote expandable>\n"
        "=== [ 𝗜𝗠𝗚𝗨𝗥 𝗨𝗣𝗟𝗢𝗔𝗗 ] ===\n"
        "━━━━━━━━━━━━━━━━━━\n"
        f"[🍑] → 𝗡𝗴𝘂𝗼𝗶 𝗗𝘂𝗻𝗴: {message.from_user.first_name}\n"
        f"[🥨] → 𝗩𝗮𝗼 𝗟𝘂𝗰: {current_time}\n"
        f"[🍒] → 𝗧𝗵𝗮𝗻𝗵 𝗰𝗼𝗻𝗴: {success_count}\n"
        f"[🫐] → 𝗧𝗵𝗮𝘁 𝗯𝗮𝗶: {failed_count}\n"
        "━━━━━━━━━━━━━━━━━━\n"
    )

    for idx, link in enumerate(uploaded_links, 1):
        result_message += f"[{idx}] {link}\n"

    result_message += "</blockquote>"

    # Gửi video và kết quả về Telegram
    bot.send_video(message.chat.id, video=VIDEO_URL, caption=result_message, reply_to_message_id=message.message_id, supports_streaming=True, parse_mode='HTML')
    
# Hàm lấy thông tin từ API
def get_info_from_zalo(phone):
    url = f"https://keyherlyswar.x10.mx/Apidocs/getinfozalo.php?phone={phone}&apikey=offvn"
    response = requests.get(url)
    
    try:
        data = response.json()  # Phân tích dữ liệu JSON
        if data.get('error') == False:
            # Trích xuất tất cả các dữ liệu từ JSON và bao bọc tất cả trong một blockquote
            user_info = f"<blockquote expandable>Họ và tên: {data['name']}\n" \
                        f"Tên Zalo: {data['zalo_name']}\n" \
                        f"Loại tài khoản: {data['acc_type']}\n" \
                        f"Ảnh đại diện: {data['avatar']}\n" \
                        f"Mã QR: {data['qrCodeUrl']}\n" \
                        f"Số điện thoại: {data['messageInfo']['argv']}\n" \
                        f"Tài khoản doanh nghiệp: {data['user']['isBusiness']}\n" \
                        f"Hiển thị Banner: {data['user']['showBanner']}\n" \
                        f"Thông tin người dùng:\n" \
                        f"  - Loại thông điệp: {data['messageInfo']['type']}\n" \
                        f"  - ID cuộc trò chuyện: {data['messageInfo']['convId']}\n" \
                        f"  - Có phiên ZWeb: {data['messageInfo']['hasZWebSession']}\n" \
                        f"Thông tin QR:\n" \
                        f"  - Link ảnh đại diện: {data['thumbnail']}\n" \
                        f"  - QR Code: {data['qrCodeUrl']}\n" \
                        f"Thông tin thêm:\n" \
                        f"  - Loại tài khoản Zalo: {data['type']}\n" \
                        f"  - Avatar URL: {data['avatar']}\n" \
                        f"  - Banner hiển thị: {data['user']['showBanner']}</blockquote>"
            return user_info
        else:
            return "<blockquote expandable>Lỗi khi lấy dữ liệu cho số điện thoại đã cung cấp.</blockquote>"
    except Exception as e:
        return f"<blockquote expandable>Đã xảy ra lỗi: {e}</blockquote>"

# Xử lý lệnh /zalo
@bot.message_handler(commands=['zalo'])
def handle_zalo(message):
    # Lấy số điện thoại (sau lệnh, tách ra theo khoảng trắng)
    try:
        phone_number = message.text.split()[1]  # Lấy số điện thoại
        info = get_info_from_zalo(phone_number)
        
        # Gửi lại kết quả cho người dùng với parse_mode='html'
        bot.send_message(message.chat.id, info, parse_mode='html')
    except IndexError:
        # Xử lý trường hợp không cung cấp số điện thoại
        bot.send_message(message.chat.id, "<blockquote expandable>Vui lòng cung cấp số điện thoại sau lệnh. Ví dụ: /zalo 1234567890</blockquote>", parse_mode='html')
        
while True:
    try:
        bot.infinity_polling()
    except Exception as e:
        print(f"Lỗi đã xảy ra: {e}")
        time.sleep(5)  # Đợi 5 giây trước khi khởi động lại bot
