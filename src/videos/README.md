# Exercise Videos Folder

Place your local exercise video files (such as `.mp4`, `.mov`, `.webm`) in this folder.

### How to use a local video in `exercise_videos.py`:
Change the `video_url` for any exercise to point to the file path:
```python
"Incline Barbell Press": {
    "category": "Chest Exercises",
    "video_url": "src/videos/incline_barbell_press.mp4",  # <-- Local video path
    "target_muscle": "Upper Chest & Front Delts",
    ...
}
```

### Supported formats:
- `.mp4` (Recommended for all devices and web)
- `.mov` (Apple QuickTime)
- `.webm` (Web video)
