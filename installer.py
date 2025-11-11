#!/usr/bin/env python3
"""
Auto Installer for YouTube View Simulator
Termux Installation Script
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run shell command with error handling"""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, 
                              capture_output=True, text=True)
        print(f"✅ {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        return False

def main():
    print("🚀 YouTube View Simulator - Auto Installer")
    print("=" * 50)
    
    # Update Termux packages
    if not run_command("pkg update -y && pkg upgrade -y", "Updating Termux packages"):
        print("❌ Failed to update packages")
        return
    
    # Install Python and dependencies
    if not run_command("pkg install python -y", "Installing Python"):
        print("❌ Failed to install Python")
        return
    
    # Install git for potential updates
    run_command("pkg install git -y", "Installing Git")
    
    # Install Python packages
    packages = [
        "pip install requests FreeProxy urllib3",
        "pip install --upgrade pip"
    ]
    
    for package_cmd in packages:
        if not run_command(package_cmd, f"Installing {package_cmd}"):
            print(f"❌ Failed to install {package_cmd}")
            return
    
    print("\n🎉 Installation completed successfully!")
    print("\n📖 Usage Instructions:")
    print("  1. Run: python yt_view.py")
    print("  2. Enter YouTube video URL")
    print("  3. Enter number of views")
    print("  4. Confirm and wait for results")
    print("\n⚠️  Remember: Educational purposes only!")

if __name__ == "__main__":
    main()
