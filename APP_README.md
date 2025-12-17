# 🚀 Portfolio Dashboard Application

An interactive web-based portfolio dashboard built with Streamlit to showcase skills, projects, and professional journey.

## ✨ Features

### 🏠 Home
- Professional introduction and about section
- Quick statistics and metrics
- Interactive journey timeline
- Social media connections

### 💼 Skills
- Categorized skill display (Programming, ML/AI, Web Dev, Tools)
- Visual proficiency bars for each skill
- Skills distribution analytics
- Technology stack showcase

### 📂 Projects
- Featured project cards with detailed descriptions
- Project statistics and metrics
- Technology stack for each project
- Project status indicators

### 📊 Analytics
- GitHub contribution trends
- Programming language distribution
- Project category breakdown
- Technology proficiency radar chart
- Real-time activity metrics

### 📧 Contact
- Interactive contact form
- Contact information display
- FAQ section
- Social media links

## 🛠️ Technology Stack

- **Framework:** Streamlit 1.29.0
- **Data Processing:** Pandas 2.1.4
- **Visualization:** Plotly 5.18.0
- **Image Processing:** Pillow 10.1.0
- **HTTP Requests:** Requests 2.31.0

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository:**
```bash
git clone https://github.com/akhilv24/akhilv24.git
cd akhilv24
```

2. **Create a virtual environment (recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## 🚀 Running the Application

1. **Start the Streamlit server:**
```bash
streamlit run app.py
```

2. **Access the application:**
   - Open your web browser
   - Navigate to `http://localhost:8501`
   - The dashboard will load automatically

## 📱 Usage

### Navigation
- Use the sidebar to navigate between different sections
- Each section provides different insights and information

### Interactive Features
- Hover over charts for detailed information
- Click on project buttons to view more details
- Fill out the contact form to send messages
- Explore different tabs within each section

## 🎨 Customization

### Modify Content
- Edit `app.py` to update personal information, skills, or projects
- Adjust the data in each section to match your portfolio

### Styling
- Custom CSS is included in the `app.py` file
- Modify the `st.markdown()` CSS section to change colors and styles

### Data
- Update skill levels, project details, and statistics directly in the code
- Add or remove sections as needed

## 📂 Project Structure

```
akhilv24/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── APP_README.md      # Application documentation
├── README.md          # Profile README
└── .gitignore         # Git ignore rules
```

## 🐛 Troubleshooting

### Common Issues

1. **Port already in use:**
```bash
streamlit run app.py --server.port 8502
```

2. **Module not found:**
```bash
pip install -r requirements.txt --upgrade
```

3. **Virtual environment issues:**
```bash
deactivate
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 🔧 Configuration

### Streamlit Config
Create a `.streamlit/config.toml` file for custom configuration:

```toml
[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f5f5f5"
textColor = "#262730"
font = "sans serif"

[server]
port = 8501
enableCORS = false
```

## 📈 Future Enhancements

- [ ] Add authentication system
- [ ] Integrate with GitHub API for real-time stats
- [ ] Add blog section
- [ ] Implement dark mode toggle
- [ ] Add multilingual support
- [ ] Include downloadable resume
- [ ] Add project filtering and search
- [ ] Integrate analytics tracking

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📄 License

This project is open source and available under the MIT License.

## 📧 Contact

For questions or feedback about this application:
- **Email:** akhilv2402@gmail.com
- **GitHub:** [@akhilv24](https://github.com/akhilv24)
- **LinkedIn:** [Akhil](https://www.linkedin.com/in/akhil2402/)

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Visualizations powered by [Plotly](https://plotly.com/)
- Icons and badges from [Shields.io](https://shields.io/)

---

**Made with ❤️ using Streamlit**
