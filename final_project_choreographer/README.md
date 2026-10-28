# AI Mood-Aware Robot Choreographer

Physical AI応用1講座・最終課題用ROS 2パッケージ。

## Labels
- celebrate: 祝福・喜び
- calm: 休息・安らぎ
- sympathy: 共感・励まし

## Required
- ROS 2 Humble
- Gazebo
- CRANE+ V2 Gazebo package
- Python scikit-learn

## Build
cd ~/pai_ws
python3 -m pip install --user scikit-learn joblib
colcon build --symlink-install --packages-select final_project_choreographer
