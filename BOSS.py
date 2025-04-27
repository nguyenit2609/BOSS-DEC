import os, random, string, requests, time, webbrowser
from rich.console import Console
from datetime import datetime, timedelta
from rich.text import Text

# Hàm xóa màn hình
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")  # Xóa màn hình tùy theo hệ điều hành

clear_screen()
console = Console()
text = Text("MENU", style="bold")
colors = ["red", "orange", "yellow", "green"]  # Không có màu trắng

for i, char in enumerate(text.plain):
    text.stylize(colors[i % len(colors)], i, i + 1)

# Hiển thị banner
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
console.print(f"[bold magenta]     ╔════════════╩═════════════════════[ [/bold magenta]", end="")
console.print(text, end="")
console.print("[bold yellow] ]═══════════════════╩═══════════╗")
console.print("[bold magenta]    ╙║ [/bold magenta]                                                                        [bold yellow]║╜")
# Nhập dữ liệu
console.print("[bold magenta]    ╙║ [bold magenta][1] Golike FB <antiband + đa luồng>  [/bold magenta][bold yellow]| PC[/bold yellow]                               [bold yellow]║╜")
console.print("[bold magenta]    ╙║ [bold magenta][2] TTC FB <antiband - crack>                [/bold magenta][bold yellow]| PC[/bold yellow]                               [bold yellow]║╜")
console.print("[bold magenta]    ╙║ [bold magenta][3] Golike Snapchat-Thread-Linkedin  [/bold magenta][bold yellow]| PC[/bold yellow]                               [bold yellow]║╜")
console.print("[bold magenta]    ╙║ [bold magenta][4] Golike FB <đa luồng>             [/bold magenta][bold yellow]| PC[/bold yellow]                               [bold yellow]║╜")
console.print("[bold magenta]    ╙║ [bold red][5] E[bold magenta]x[/bold magenta]i[bold magenta]t[/ bold magenta]                             [/bold magenta][bold yellow]    [/bold yellow]                               [bold yellow]║╜")
#console.print("[bold magenta]    ╙║ [/bold magenta]                                                                        [bold yellow]║╜")
console.print("[bold magenta]     ╚═══════════════════════════════════════[/bold magenta][bold yellow]══════════════════════════════════╝")
print("")
print("")

# Hàm rút gọn link bằng YeuMoney
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
        return "DCN-ADMIN"  # Key admin không có ngày hết hạn
    else:
        return f"DCN-{generate_random_key(6)}"  # Key user

# Hàm lưu key vào file (chỉ lưu 1 key)
def save_key_to_file(key):
    """Lưu key vào file, ghi đè để chỉ lưu 1 key."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Thời gian lưu key
    with open("key.txt", "w") as f:  # Dùng mode "w" để ghi đè
        f.write(f"{key} | {timestamp}\n")

# Hàm kiểm tra và xóa key nếu đã qua 00:00
def clean_expired_key():
    """Xóa key nếu đã qua 00:00 của ngày hôm sau."""
    if not os.path.exists("key.txt"):
        return
    
    updated_lines = []
    current_time = datetime.now()
    current_date = current_time.date()  # Ngày hiện tại
    
    with open("key.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            try:
                key, timestamp = line.strip().split(" | ")
                key_time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                key_date = key_time.date()  # Ngày tạo key
                # Nếu key không phải admin và đã qua ngày mới (00:00), bỏ qua
                if not key.startswith("DCN-ADMIN") and key_date == current_date:
                    updated_lines.append(line)
                elif key.startswith("DCN-ADMIN"):  # Giữ lại key admin
                    updated_lines.append(line)
            except:
                continue
    
    # Ghi lại key còn hiệu lực (nếu không còn key nào thì file sẽ trống)
    with open("key.txt", "w") as f:
        f.writelines(updated_lines)

# Hàm kiểm tra key hợp lệ
def is_valid_key(key, expected_key):
    """Kiểm tra key có hợp lệ không."""
    clean_expired_key()  # Dọn dẹp key hết hạn trước
    
    if key == "DCN-ADMIN":
        return True  # Key admin hợp lệ mọi lúc
    elif key == expected_key:  # So sánh với key đã tạo
        return True
    return False

# Hàm kiểm tra key đã lưu và còn hạn không
def check_stored_key():
    """Kiểm tra xem có key nào còn hạn trong file không, trả về key nếu hợp lệ."""
    clean_expired_key()  # Dọn dẹp key hết hạn trước
    
    if not os.path.exists("key.txt"):
        return None, None
    
    current_time = datetime.now()
    current_date = current_time.date()  # Ngày hiện tại
    with open("key.txt", "r") as f:
        for line in f:
            try:
                stored_key, timestamp = line.split(" | ")
                stored_key = stored_key.strip()
                key_time = datetime.strptime(timestamp.strip(), "%Y-%m-%d %H:%M:%S")
                key_date = key_time.date()  # Ngày tạo key
                if stored_key == "DCN-ADMIN":
                    return stored_key, stored_key  # Key admin luôn hợp lệ
                elif stored_key.startswith("DCN-"):
                    if key_date == current_date:  # Key chỉ hợp lệ trong cùng ngày
                        return stored_key, stored_key
            except:
                continue
    return None, None

# ======= Chạy Tool =======
try:
    admin_key = "DCN-ADMIN"
    
    # Kiểm tra xem có key nào còn hạn trong file không
    stored_key, user_key = check_stored_key()
    
    # Nếu không có key còn hạn, tạo key mới và yêu cầu người dùng vượt link
    if not stored_key:
        user_key = generate_key(is_admin=False)
        # Tạo link YeuMoney chứa key
        link_can_rut = f"https://www.webkey.x10.mx/?ma={user_key}"  # Thay bằng URL mới của bạn
        short_link = get_shortened_link_yeumoney(link_can_rut)
        console.print(f"[bold red][bold yellow]LINK[/bold yellow] [bold white]|[/bold white][bold magenta]VƯỢT LINK ĐỂ LẤY KEY[/bold magenta][/bold red][bold green]: {short_link}[/bold green]")
        
        while True:
            nhap_key = console.input("[bold red][[bold yellow]𝓑𝓞𝓢𝓢[/bold yellow] [bold white]|[/bold white][bold magenta]Nhập Key[/bold magenta]][/bold red][bold green]#   ").strip()
            
            if is_valid_key(nhap_key, user_key):
                # Lưu key vừa nhập thành công vào file (ghi đè key cũ)
                save_key_to_file(nhap_key)
                print("\n✅ Key hợp lệ! Đang xác nhận key...", end="\r")
                time.sleep(3)  # Chờ 3 giây trước khi vào tool
                print("\033[F\033[K" * 3, end="")  # Xóa 3 dòng vừa in
                break  
            else:
                print("\n❌ Key không hợp lệ. Vui lòng vượt link để lấy key!", end="\r")
                time.sleep(2)
                print("\033[F\033[K" * 2, end="")  # Xóa 2 dòng vừa in
    else:
        # Nếu có key còn hạn, hiển thị link YeuMoney nhưng không yêu cầu nhập lại
        link_can_rut = f"https://www.webkey.x10.mx/?ma={stored_key}"
        short_link = get_shortened_link_yeumoney(link_can_rut)
        console.print(f"[bold red][bold yellow]LINK[/bold yellow] [bold white]|[/bold white][bold magenta]VƯỢT LINK ĐỂ LẤY KEY[/bold magenta][/bold red][bold green]: {short_link}[/bold green]")
        console.print(f"[bold green]Key còn hạn: {stored_key}. Đang xác nhận key...[/bold green]")
        time.sleep(3)  # Chờ 3 giây trước khi vào tool
        print("\033[F\033[K" * 4, end="")

except Exception as e:
    console.print(f"[bold red]ErrolKey: {e}[/bold red]")

# Xử lý dữ liệu
while True:
    input_choice = console.input("[bold red][[bold yellow]𝓑𝓞𝓢𝓢[/bold yellow] [bold white]|[/bold white][bold magenta]Nhập số[/bold magenta]][/bold red][bold green]#   ")
    if input_choice == "1":
        url = "https://raw.githubusercontent.com/nguyenit2609/BOSS-DEC/refs/heads/main/FB_%C4%90A_LU%E1%BB%92NG_NO_LIKE" # Link github tool
        response = requests.get(url)
        response.raise_for_status()  # Gây lỗi nếu mã != 200
    # Chạy nội dung tool
        exec(response.text)
        console.print("[bold red]Đang vào tool...[/bold red]", end="\r")
        time.sleep(0.5)
        print("                                         ", end="\r")
        break
    if input_choice == "2":
        url = "https://raw.githubusercontent.com/nguyenit2609/BOSS-DEC/refs/heads/main/SP-TR-LD-IG" # Link github tool
        response = requests.get(url)
        response.raise_for_status()  # Gây lỗi nếu mã != 200
    # Chạy nội dung tool
        exec(response.text)
        console.print("[bold red]Đang vào tool...[/bold red]", end="\r")
        time.sleep(0.5)
        print("", end="\r")
        break
    if input_choice == "3":
        url = "https://raw.githubusercontent.com/nguyenit2609/BOSS-DEC/refs/heads/main/TTC-FB" # Link github tool
        webbrowser.open(url)
        print("")
        console.print("[bold red]Đang vào tool...[/bold red]", end="\r")
        time.sleep(0.5)
        print("", end="\r")
        break
    if input_choice == "4":
        url = "https://raw.githubusercontent.com/nguyenit2609/BOSS-DEC/refs/heads/main/FB_%C4%90A_LU%E1%BB%92NG_LIKE" # Link github tool
        webbrowser.open(url)
        print("")
        console.print("[bold red]Đang vào tool...[/bold red]", end="\r")
        time.sleep(0.5)
        print("", end="\r")
        break
    if input_choice == "5":
        exec(requests.get('https://raw.githubusercontent.com/nguyenit2609/BOSS-DEC/refs/heads/main/TT_V4.py').text)
        print("")
        console.print("[bold red]Đang vào tool...[/bold red]", end="\r")
        time.sleep(0.5)
        print("", end="\r")
        break
    if input_choice == "6":
        url = "" # Link github tool
        webbrowser.open(url)
        print("")
        console.print("[bold red]Đang vào tool...[/bold red]", end="\r")
        time.sleep(0.5)
        print("                                       ", end="\r")
        break
    if input_choice == "7":
        url = "" # Link github tool
        webbrowser.open(url)
        print("")
        console.print("[bold red]Đang vào tool...[/bold red]", end="\r")
        time.sleep(0.5)
        print("                                  ", end="\r")
        break
    if input_choice == "8":
        print("                                          ")
        console.print("[bold red]Đang thoát tool...[/bold red]", end="\r")
        time.sleep(0.5)
        print("                                                       ", end="\r")
        console.print("[bold red]═════════════════════════════════════════════════════════════════════════════════════[/bold red]")
        exit()
        break
    else:
        console.print("[bold red]Mày bị ngu à nhập sai rồi kia?[/bold red]")
        
console.print("[bold red]═════════════════════════════════════════════════════════════════════════════════════[/bold red]")
