# Aura Farming Video to ASCII

Transform your aura farming videos into stunning ASCII art and watch them play in your terminal! This Python project converts video frames to ASCII characters, creating a unique retro-style video experience right in your command line.

## Features

- **Video to ASCII Conversion**: Converts video files to ASCII art frames
- **Enhanced Visual Quality**: Auto-contrast, brightness adjustment, and edge detection
- **Customizable Settings**: Adjust width, height, FPS, and duration
- **Smooth Playback**: Optimized frame rate and terminal clearing
- **Interactive Control**: Press Ctrl+C to stop playback

## Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/aurafarming.git
   cd aurafarming
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your video file**
   - Place your video file in the project directory
   - Update the `VIDEO_PATH` variable in `ascii.py` to match your video filename
   - Or rename your video to `1751520327557.mp4`

4. **Run the Aura Farming ASCII video player**
   ```bash
   python ascii.py
   ```

## Configuration

You can customize the Aura Farming ASCII video player by modifying these variables in `ascii.py`:

```python
VIDEO_PATH = "your_video.mp4"  # Path to your video file
WIDTH = 48                     # ASCII output width
HEIGHT = 42                    # ASCII output height
FPS = 10                       # Frames per second
MAX_DURATION = 12              # Maximum duration in seconds (set to None for full video)
```

## How It Works

1. **Frame Extraction**: Uses OpenCV to read video frames
2. **Image Processing**: 
   - Converts to grayscale
   - Applies auto-contrast enhancement
   - Adjusts brightness and contrast
   - Combines edge detection with sharpening
3. **ASCII Conversion**: Maps pixel brightness to ASCII characters
4. **Terminal Display**: Clears screen and displays each frame

## Project Structure

```
aurafarming/
├── ascii.py              # Main ASCII video player script
├── requirements.txt      # Python dependencies
├── aura.mp4    # Sample video file
└── README.md            # This file
```

## Dependencies

- **opencv-python**: Video capture and frame processing
- **numpy**: Numerical operations and array handling
- **pillow**: Image processing and enhancement

## Usage Examples

### Basic Usage
```bash
python ascii.py
```

### Custom Video
1. Edit `ascii.py` and change `VIDEO_PATH = "your_video.mp4"`
2. Run: `python ascii.py`

### Adjust Settings
Modify the configuration variables for different effects:
- Lower `WIDTH`/`HEIGHT` for faster processing
- Higher `FPS` for smoother playback
- Adjust `MAX_DURATION` to limit video length

## Demo

Watch your aura farming videos transform into ASCII art! The player creates a mesmerizing retro-style animation that works on any terminal.

## Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## License

This project is open source and available under the [MIT License](LICENSE).

## Support the Project

If you find this Aura Farming ASCII video player cool and useful, please consider giving it a star!

**Why star this repo?**
- Unique video-to-ASCII conversion
- Easy to use and customize
- Beautiful terminal art
- Well-documented and maintained
- Great for demos and retro enthusiasts

**Your star helps:**
- Increase project visibility
- Motivate further development
- Help others discover this cool tool
- Show appreciation for open source

---

**Made with love for the terminal art community**

*Transform your aura farming videos into ASCII magic!*

