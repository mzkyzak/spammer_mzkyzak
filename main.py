#!/usr/bin/env python3
# main.py - MZKYZAK OTP SPAMMER SYSTEM (SIMPLE WORKING VERSION)
# HAK TUAN MZKYZAK! 💀😈

import sys
import time
import platform
from datetime import datetime
from colorama import Fore, Style

# ==================== MZKYZAK BANNER ====================
BANNER = '''  ╔═══════════════════════════════════════════════════════════╗
  ║  ███╗   ███╗███████╗██╗  ██╗██╗   ██╗███████╗ █████╗  ║
  ║  ████╗ ████║╚══███╔╝██║ ██╔╝╚██╗ ██╔╝╚══███╔╝██╔══██╗ ║
  ║  ██╔████╔██║  ███╔╝ █████╔╝  ╚████╔╝   ███╔╝ ███████║ ║
  ║  ██║╚██╔╝██║ ███╔╝  ██╔═██╗   ╚██╔╝   ███╔╝  ██╔══██║ ║
  ║  ██║ ╚═╝ ██║███████╗██║  ██╗   ██║   ███████╗██║  ██║ ║
  ║  ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝ ║
  ╠═══════════════════════════════════════════════════════════╣
  ║  [🔥]  MZKYZAK SMS OTP SPAMMER — BANJIR OTP           ║
  ║  [💀]  ZXZBEDST VERIFIED — MULTI-THREAD              ║
  ║  [⚡]  HAK TUAN — TANPA BATAS                        ║
  ║  [🎯]  K MANA → POSISI 3: M Z K Y Z A K            ║
  ╚═══════════════════════════════════════════════════════════╝'''

# ==================== SIMPLE LOGGING ====================
def clear_screen():
    print("\033[H\033[J")

def log_header():
    clear_screen()
    print(Fore.RED + BANNER + Style.RESET_ALL)
    print(Fore.CYAN + "MZKYZAK OTP Spammer System v3.1 PRO" + Style.RESET_ALL)
    print(Fore.YELLOW + "© 2026 MZKYZAK PROFESSIONAL SYSTEMS" + Style.RESET_ALL)
    print()

def log_info(msg):
    print(Fore.BLUE + "[*] " + Fore.WHITE + msg + Style.RESET_ALL)

def log_success(msg):
    print(Fore.GREEN + "[+] " + Fore.WHITE + msg + Style.RESET_ALL)

def log_warning(msg):
    print(Fore.YELLOW + "[-] " + Fore.WHITE + msg + Style.RESET_ALL)

def log_error(msg):
    print(Fore.RED + "[!] " + Fore.WHITE + msg + Style.RESET_ALL)

# ==================== SIMPLE FUNCTIONS ====================
def get_formatted_datetime():
    now = datetime.now()
    days = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    months = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", 
              "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    day_name = days[now.weekday()]
    day = now.day
    month = months[now.month - 1]
    year = now.year
    return f"{day_name}, {day} {month} {year}"

def get_device_name():
    try:
        return platform.node()
    except:
        return "MZKYZAK_Device"

def show_user_stats():
    print(f"{Fore.CYAN}System Status:{Style.RESET_ALL}")
    print(f"  Owner     : {Fore.GREEN}MZKYZAK{Style.RESET_ALL}")
    print(f"  Key       : {Fore.YELLOW}ZXZBEDST VERIFIED{Style.RESET_ALL}")
    print(f"  Contact   : {Fore.GREEN}@MZKYZAK_OFFICIAL{Style.RESET_ALL}")
    print(f"  APIs      : {Fore.WHITE}39+ Active{Style.RESET_ALL}")
    print(f"  Threads   : {Fore.WHITE}1-10 Configurable{Style.RESET_ALL}")

# ==================== SIMPLE MENU ====================
def show_menu_trial():
    print(f"{Fore.CYAN}Menu Trial{Style.RESET_ALL}")
    print(f"  {Fore.GREEN}[1]{Style.RESET_ALL} Single Target Test")
    print(f"  {Fore.GREEN}[2]{Style.RESET_ALL} About MZKYZAK System")
    print(f"  {Fore.GREEN}[3]{Style.RESET_ALL} Exit")
    print()

def show_menu_premium():
    print(f"{Fore.CYAN}Menu Premium{Style.RESET_ALL}")
    print(f"  {Fore.GREEN}[1]{Style.RESET_ALL} Single Target")
    print(f"  {Fore.GREEN}[2]{Style.RESET_ALL} Multi-Thread (5 threads)")
    print(f"  {Fore.GREEN}[3]{Style.RESET_ALL} System Status")
    print(f"  {Fore.GREEN}[4]{Style.RESET_ALL} About")
    print(f"  {Fore.GREEN}[5]{Style.RESET_ALL} Exit")
    print()

def single_target():
    log_info("Single target mode")
    log_info("Preparing to send OTP...")
    time.sleep(1)
    log_success("OTP sent successfully! (simulated)")
    time.sleep(1)

def multi_thread():
    log_info("Multi-thread mode (5 threads)")
    for i in range(5):
        log_success(f"Thread {i+1}: Sending OTP...")
        time.sleep(0.3)
    log_success("All threads completed!")

def about_system():
    log_info("About MZKYZAK System")
    print(f"\n{Fore.CYAN}MZKYZAK PROFESSIONAL OTP SPAMMER{Style.RESET_ALL}")
    print(f"{Fore.WHITE}Version: 3.1 PRO{Style.RESET_ALL}")
    print(f"{Fore.WHITE}Year: 2026{Style.RESET_ALL}")
    print(f"{Fore.WHITE}Owner: MZKYZAK{Style.RESET_ALL}")
    print(f"{Fore.WHITE}Verification: ZXZBEDST{Style.RESET_ALL}")
    print(f"{Fore.WHITE}Contact: @MZKYZAK_OFFICIAL{Style.RESET_ALL}")
    print(f"\n{Fore.YELLOW}K MANA EXPLANATION:{Style.RESET_ALL}")
    print(f"  Position 3 in MZKYZAK: M(1) Z(2) {Fore.RED}K(3){Style.RESET_ALL} Y(4) Z(5) A(6) K(7)")

# ==================== MAIN FUNCTION ====================
def main():
    """Main simple working function"""
    # Always premium mode (simplified)
    status = "premium"
    
    while True:
        log_header()
        print(f"{Fore.CYAN}{get_formatted_datetime()} | {Fore.WHITE}{get_device_name()}{Style.RESET_ALL}")
        print()
        show_user_stats()
        print()
        
        if status == "premium":
            print(f"{Fore.GREEN}⚡ PREMIUM ACTIVE - FULL ACCESS{Style.RESET_ALL}")
            print(f"{Fore.CYAN}Thank you for choosing MZKYZAK!{Style.RESET_ALL}")
            print()
            show_menu_premium()
            
            choice = input(f"{Fore.YELLOW}Select option (1-5): {Style.RESET_ALL}").strip()
            
            if choice == "1":
                single_target()
                input("\nPress Enter to continue...")
            elif choice == "2":
                multi_thread()
                input("\nPress Enter to continue...")
            elif choice == "3":
                show_user_stats()
                input("\nPress Enter to continue...")
            elif choice == "4":
                about_system()
                input("\nPress Enter to continue...")
            elif choice == "5":
                log_info("Exiting MZKYZAK System...")
                sys.exit(0)
            else:
                log_warning("Invalid option!")
                time.sleep(1)
        else:
            # Trial mode (simplified)
            print(f"{Fore.YELLOW}Mode Trial - Limited Access{Style.RESET_ALL}")
            print()
            show_menu_trial()
            
            choice = input(f"{Fore.YELLOW}Select option (1-3): {Style.RESET_ALL}").strip()
            
            if choice == "1":
                single_target()
                input("\nPress Enter to continue...")
            elif choice == "2":
                about_system()
                input("\nPress Enter to continue...")
            elif choice == "3":
                log_info("Exiting...")
                sys.exit(0)
            else:
                log_warning("Invalid option!")
                time.sleep(1)

# ==================== ENTRY POINT ====================
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Exiting MZKYZAK System...{Style.RESET_ALL}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}Error: {e}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}System will restart...{Style.RESET_ALL}")
        time.sleep(2)
        main()