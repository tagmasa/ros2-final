from setuptools import find_packages, setup

package_name = 'final_project_choreographer'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml', 'model.joblib']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='YOUR_NAME',
    maintainer_email='YOUR_EMAIL@example.com',
    description='AI-driven robot choreographer for Physical AI final project',
    license='MIT',
    entry_points={
        'console_scripts': [
            'mood_ai_node = final_project_choreographer.mood_ai_node:main',
            'motion_executor = final_project_choreographer.motion_executor:main',
        ],
    },
)
