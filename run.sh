#!/bin/bash

# Portfolio Dashboard Application Launcher
# This script sets up and runs the Streamlit application

echo "🚀 Starting Portfolio Dashboard Application..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed."
    echo "Please install Python 3.8 or higher."
    exit 1
fi

echo "✓ Python found: $(python3 --version)"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo ""
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    
    if [ $? -ne 0 ]; then
        echo "❌ Error: Failed to create virtual environment."
        exit 1
    fi
    echo "✓ Virtual environment created"
fi

# Activate virtual environment
echo ""
echo "🔌 Activating virtual environment..."
source venv/bin/activate

if [ $? -ne 0 ]; then
    echo "❌ Error: Failed to activate virtual environment."
    exit 1
fi

# Install/Update dependencies
echo ""
echo "📥 Installing dependencies..."
pip install -q -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Error: Failed to install dependencies."
    exit 1
fi

echo "✓ Dependencies installed"

# Run the Streamlit app
echo ""
echo "🎉 Launching application..."
echo "📍 The app will open in your browser at http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the server."
echo ""

streamlit run app.py

# Deactivate virtual environment on exit
deactivate
