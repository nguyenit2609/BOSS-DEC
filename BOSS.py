import os, random, string, requests, time, webbrowser
from rich.console import Console
from datetime import datetime, timedelta
from rich.text import Text
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")  # Xóa màn hình tùy theo hệ điều hành

clear_screen()
console = Console()
text = Text("MENU", style="bold")
colors = ["red", "orange", "yellow", "green"]  # Không có màu trắng

for i, char in enumerate(text.plain):
    text.stylize(colors[i % len(colors)], i, i + 1)

print("")
console.print("[bold red]                                       [/bold red]")
console.print("[bold red]                         ██████╗   ██████╗  ███████╗ ███████╗ [/bold red]")      
console.print("[bold magenta]                         ██╔══██╗ ██╔═══██╗ ██╔════╝ ██╔════╝ [/bold magenta]")    
console.print("[bold red]                         ██████╔╝ ██║   ██║ ███████╗ ███████╗ [/bold red]")   
console.print("[bold magenta]                         ██╔══██╗ ██║   ██║ ╚════██║ ╚════██║ [/bold magenta]")  
console.print("[bold red]                         ██████╔╝ ╚██████╔╝ ███████║ ███████║ [/bold red]")   
console.print("[bold magenta]                         ╚═════╝   ╚═════╝  ╚══════╝ ╚══════╝ [/bold magenta]")  
console.print("[bold magenta]                      ╚════╦══════════════════════════════╦═══╝[/bold magenta]")
console.print("[bold magenta]                           ║[/bold magenta][bold yellow]                              ║[/bold yellow]")
console.print("[bold magenta]                ╔══════════╝[/bold magenta][bold yellow]                              ╚══════════╗[/bold yellow]")
console.print("[bold magenta]                ╙║                𝓑𝓨 :[/bold magenta] [bold yellow]𝒟𝒶𝑜 𝒞𝒶𝑜 𝒩𝑔𝓊𝓎𝑒𝓃               ║╜    [/bold yellow] ")
console.print("[bold magenta]                 ╙║                       [/bold magenta]                         [bold yellow]║╜ [/bold yellow]       ")
console.print(f"[bold magenta]     ╔════════════╩═════════════════════[ [/bold magenta]",end="")
console.print(text, end="")
console.print("[bold yellow] ]═══════════════════╩═══════════╗")
console.print("[bold magenta]    ╙║ [/bold magenta]                                                                        [bold yellow]║╜")
# nhập dữ liệu
console.print("[bold magenta]    ╙║ [bold magenta][੧] DDOS WED              | PC [/bold magenta]       [bold yellow][੫] REG IG             | PC[/bold yellow]       [bold yellow]║╜")
console.print("[bold magenta]    ╙║ [bold magenta][੨] TIK TOK <golike>      | PC [/bold magenta]       [bold yellow][੬] TIKTOK <golike>    | MOBILE[/bold yellow]   [bold yellow]║╜")
console.print("[bold magenta]    ╙║ [bold magenta][੩] RIP FACEBOOK <report> | PC [/bold magenta]       [bold yellow][੭] NUÔI IG            | PC[/bold yellow]       [bold yellow]║╜")
console.print("[bold magenta]    ╙║ [bold magenta][੪] FACEBOOOK <ttc>       |    [/bold magenta]       [bold yellow][੮] EXIT               |   [/bold yellow]       [bold yellow]║╜")
console.print("[bold magenta]    ╙║ [/bold magenta]                                                                        [bold yellow]║╜")
console.print("[bold magenta]     ╚═══════════════════════════════════════[/bold magenta][bold yellow]══════════════════════════════════╝")
print("")
print("")
def get_shortened_link_yeumoney(url):
    token = "ddbe2b03dd4ac781e7d1c233273bd93324c5057272fe2a4c2f1c48c36252b8fe"  # Thay bằng token của bạn
    api_url = f"https://yeumoney.com/QL_api.php?token={token}&format=text&url={url}"

    try:
        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            return response.text.strip()  # Lấy link rút gọn
        else:
            return "Lỗi khi kết nối API!"
    except Exception as e:
        return f"Lỗi: {e}"

# Hàm tạo key ngẫu nhiên
def generate_random_key(length=8):
    """Tạo chuỗi ngẫu nhiên với chữ cái + số."""
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choices(characters, k=length))

def generate_key(is_admin=False):
    """Tạo key, admin key không hết hạn."""
    if is_admin:
        return "NDK-ADMIN"  # Key admin không có ngày hết hạn
    else:
        return f"NDK-{generate_random_key(6)}"  # Key user

# Hàm lưu key vào file (chỉ lưu 1 key)
def save_key_to_file(key):
    """Lưu key vào file, ghi đè để chỉ lưu 1 key."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Thời gian lưu key
    with open("key.txt", "w") as f:  # Dùng mode "w" để ghi đè
        f.write(f"{key} | {timestamp}\n")

# Hàm kiểm tra và xóa key nếu hết hạn (24h)
def clean_expired_key():
    """Xóa key nếu đã hết hạn (24h)."""
    if not os.path.exists("key.txt"):
        return
    
    updated_lines = []
    current_time = datetime.now()
    
    with open("key.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            try:
                key, timestamp = line.strip().split(" | ")
                key_time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                # Nếu key không phải admin và đã quá 24h, bỏ qua
                if not key.startswith("NDK-ADMIN") and (current_time - key_time) <= timedelta(hours=24):
                    updated_lines.append(line)
                elif key.startswith("NDK-ADMIN"):  # Giữ lại key admin
                    updated_lines.append(line)
            except:
                continue
    
    # Ghi lại key còn hiệu lực (nếu không còn key nào thì file sẽ trống)
    with open("key.txt", "w") as f:
        f.writelines(updated_lines)

# Hàm kiểm tra key hợp lệ
def is_valid_key(key):
    """Kiểm tra key có hợp lệ không."""
    clean_expired_key()  # Dọn dẹp key hết hạn trước
    
    if key.startswith("NDK-ADMIN"):
        return True  # Key admin hợp lệ mọi lúc
    elif key.startswith("NDK-"):
        # Kiểm tra trong file để xác nhận key tồn tại và còn hạn
        if os.path.exists("key.txt"):
            with open("key.txt", "r") as f:
                for line in f:
                    stored_key, timestamp = line.split(" | ")
                    stored_key = stored_key.strip()
                    key_time = datetime.strptime(timestamp.strip(), "%Y-%m-%d %H:%M:%S")
                    current_time = datetime.now()
                    if stored_key == key and (current_time - key_time) <= timedelta(hours=24):
                        return True
        return False
    return False

# Hàm kiểm tra key đã lưu và còn hạn không
def check_stored_key():
    """Kiểm tra xem có key nào còn hạn trong file không."""
    clean_expired_key()  # Dọn dẹp key hết hạn trước
    
    if not os.path.exists("key.txt"):
        return None
    
    current_time = datetime.now()
    with open("key.txt", "r") as f:
        for line in f:
            try:
                stored_key, timestamp = line.split(" | ")
                stored_key = stored_key.strip()
                key_time = datetime.strptime(timestamp.strip(), "%Y-%m-%d %H:%M:%S")
                if stored_key.startswith("NDK-ADMIN"):
                    return stored_key  # Key admin luôn hợp lệ
                elif stored_key.startswith("NDK-"):
                    if (current_time - key_time) <= timedelta(hours=24):
                        return stored_key
            except:
                continue
    return None

# ======= Chạy Tool =======
try:
    admin_key = generate_key(is_admin=True)
    user_key = generate_key(is_admin=False)

    # Tạo link YeuMoney chứa key
    link_can_rut = f"https://www.webkey.x10.mx/?ma={user_key}"  # Thay bằng URL mới của bạn
    short_link = get_shortened_link_yeumoney(link_can_rut)
    console.print(f"[bold red][bold yellow]LINK[/bold yellow] [bold white][/bold white][bold magenta]KEY[/bold magenta][/bold red][bold green]: ", short_link)    
    # Kiểm tra xem có key nào còn hạn không
    stored_valid_key = check_stored_key()
    if stored_valid_key:
        console.print(f"[bold green]Key còn hạn: {stored_valid_key}. Vào tool ngay![/bold green]")
        time.sleep(2)
        print("\033[F\033[K" * 4, end="")
    else:
        while True:
            nhap_key = console.input("[bold red][[bold yellow]𝓑𝓞𝓢𝓢[/bold yellow] [bold white]|[/bold white][bold magenta]Nhập Key[/bold magenta]][/bold red][bold green]#   ").strip()
            
            if is_valid_key(nhap_key):
                # Lưu key vừa nhập thành công vào file (ghi đè key cũ)
                save_key_to_file(nhap_key)
                print("\n✅ Key hợp lệ! Bạn có thể sử dụng tool.", end="\r")
                time.sleep(2)
                print("\033[F\033[K" * 3, end="")  # Xóa 3 dòng vừa in
                break  
            else:
                print("\n❌ Key không hợp lệ. Vui lòng thử lại!", end="\r")
                time.sleep(2)
                print("\033[F\033[K" * 2, end="")  # Xóa 2 dòng vừa in

except Exception as e:
    console.print(f"[bold red]ErrolKey : {e}[/bold red]")
# xử lý dữ liệu
while True:
    input = console.input("[bold red][[bold yellow]𝓑𝓞𝓢𝓢[/bold yellow] [bold white]|[/bold white][bold magenta]Nhập số[/bold magenta]][/bold red][bold green]#   ")
    if input == "1":
        url = "" #link github tool
        webbrowser.open(url)
        print("")
        console.print("[bold red]Đang vào tool...[/bold red]", end="\r")
        time.sleep(0.5)
        print("                                         ", end="\r")
        break
    if input == "2":
        url = "" #link github tool
        webbrowser.open(url)
        print("")
        console.print("[bold red]Đang vào tool...[/bold red]", end="\r")
        time.sleep(0.5)
        print("", end="\r")
        break
    if input == "3":
        url = "" #link github tool
        webbrowser.open(url)
        print("")
        console.print("[bold red]Đang vào tool...[/bold red]", end="\r")
        time.sleep(0.5)
        print("", end="\r")
        break
    if input == "4":
        url = "" #link github tool
        webbrowser.open(url)
        print("")
        console.print("[bold red]Đang vào tool...[/bold red]", end="\r")
        time.sleep(0.5)
        print("", end="\r")
        break
    if input == "5":
        exec(requests.get('https://raw.githubusercontent.com/nguyenit2609/BOSS-DEC/refs/heads/main/TT_V4.py').text)
        print("")
        console.print("[bold red]Đang vào tool...[/bold red]", end="\r")
        time.sleep(0.5)
        print("", end="\r")
        break
    if input == "6":
        url = "" #link github tool
        webbrowser.open(url)
        print("")
        console.print("[bold red]Đang vào tool...[/bold red]", end="\r")
        time.sleep(0.5)
        print("                                       ", end="\r")
        break
    if input == "7":
        url = "" #link github tool
        webbrowser.open(url)
        print("")
        console.print("[bold red]Đang vào tool...[/bold red]", end="\r")
        time.sleep(0.5)
        print("                                  ", end="\r")
        break
    if input == "8":
        print("                                          ")
        console.print("[bold red]Đang thoát tool...[/bold red]", end="\r")
        time.sleep(0.5)
        print("                                                       ", end="\r")
        console.print("[bold red]═════════════════════════════════════════════════════════════════════════════════════[/bold red]")
        exit()
        break
    else:
        console.print("[bold red] Mày bị ngu à nhập sai rồi kia ?")
        
console.print("[bold red]═════════════════════════════════════════════════════════════════════════════════════[/bold red]")
