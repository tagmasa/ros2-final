# AI Mood-Aware Robot Choreographer

Physical AI応用1講座の最終課題です。

自然言語で入力された文章をAIが分類し、ROS 2を通じてGazebo上のCRANE+ V2に感情に対応した振付を実行させます。

## デモ分類

| ラベル | 意味 | 入力例 | ロボット動作 |
|---|---|---|---|
| `celebrate` | 喜び・祝福 | 子供が志望校に合格した！ | 大きく左右に動く祝福の振付 |
| `calm` | 休息・安らぎ | 会議続きで頭が疲れたので休みたい | 小さくゆっくり動く穏やかな振付 |
| `sympathy` | 共感・励まし | 仕事で大きなミスをして落ち込んでいる | 前傾と小さな動きによる励ましの振付 |

## システム構成

```text
自然言語入力
    ↓
AI文章分類
TF-IDF character n-gram + Logistic Regression
    ↓  /choreography_label
ROS 2 motion_executor
    ↓  /crane_plus_arm_controller/joint_trajectory
Gazebo上のCRANE+ V2
使用技術
•Python
•scikit-learn
•Google Colab
•ROS 2 Humble
•Gazebo
•CRANE+ V2
•Docker
ディレクトリ
•final_project_choreographer/: ROS 2パッケージ本体
•notebooks/: AIモデルの学習・評価用Google Colabノートブック
•docs/: 課題説明資料
実行方法
ROS 2 Docker環境内で実行します。
cd ~/pai_ws
source /opt/ros/humble/setup.bash
colcon build --symlink-install --packages-select final_project_choreographer
source install/setup.bash
Gazeboを起動します。
ros2 launch crane_plus_gazebo crane_plus_with_table.launch.py
別ターミナルで振付実行ノードを起動します。
ros2 run final_project_choreographer motion_executor
さらに別ターミナルで、文章分類ノードを起動します。
ros2 run final_project_choreographer mood_ai_node --ros-args -p prompt:="子供が志望校に合格した！"
注意
本システムは自然言語の感情的な傾向を簡易分類し、ロボットの身体表現へ変換する試作システムです。医療・心理的診断を目的とするものではありません。
