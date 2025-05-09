#!/bin/bash

set -e  # Exit immediately if a command exits with a non-zero status

REPO_URL="https://github.com/Manikandan78/home-manager-config.git"
REPO_DIR="$HOME/home-manager-config"

echo "🔹 Updating system and installing dependencies..."
sudo apt update && sudo apt upgrade -y
sudo apt install -y git curl wget python3-venv python3-pip \
    postgresql postgresql-contrib nginx systemd

echo "✅ Dependencies installed."

# Fixing Nix daemon issues
echo "🔹 Checking Nix daemon..."
if ! systemctl is-active --quiet nix-daemon; then
    echo "❌ Nix daemon is not running. Restarting..."
    sudo systemctl restart nix-daemon
    sleep 2
    if systemctl is-active --quiet nix-daemon; then
        echo "✅ Nix daemon restarted successfully."
    else
        echo "❌ Failed to restart Nix daemon. Check logs with: journalctl -xe"
        exit 1
    fi
else
    echo "✅ Nix daemon is running."
fi

# Clone the repository if missing
if [ ! -d "$REPO_DIR" ]; then
    echo "🔹 Cloning Home Manager repository..."
    git clone "$REPO_URL" "$REPO_DIR" || {
        echo "❌ Failed to clone repository. Creating a new one..."
        mkdir -p "$REPO_DIR"
        cd "$REPO_DIR"
        git init
        touch home.nix
        echo "{ config, pkgs, ... }: { home.username = \"$USER\"; }" > home.nix
        git add home.nix
        git commit -m "Initial Home Manager config"
    }
else
    echo "✅ Repository found. Pulling latest updates..."
    cd "$REPO_DIR"
    git pull origin main || echo "⚠️ Failed to pull updates. Continuing..."
fi

# Install Home Manager if not installed
if ! command -v home-manager &> /dev/null; then
    echo "🔹 Installing Home Manager..."
    nix-channel --add https://github.com/nix-community/home-manager/archive/master.tar.gz home-manager
    nix-channel --update
    nix-env -iA nixpkgs.home-manager
    echo "✅ Home Manager installed."
fi

# Ensure home.nix exists
if [ ! -f "$REPO_DIR/home.nix" ]; then
    echo "🔹 Creating default home.nix..."
    echo "{ config, pkgs, ... }: { home.username = \"$USER\"; }" > "$REPO_DIR/home.nix"
fi

echo "🔹 Configuring Home Manager..."
home-manager switch || {
    echo "❌ Home Manager setup failed. Check your configuration."
    exit 1
}

echo "✅ Home Manager setup complete. It should now start automatically with the arrow prompt."
