from setuptools import find_packages, setup

package_name = 'student_robotics'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='don1379',
    maintainer_email='don1379@outlook.com',
    description='Student robotics training package: first ROS 2 Python node.',
    license='MIT',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'hello_node = student_robotics.hello_node:main',
        ],
    },
)
