import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'turtlebot_swarm'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (
        'share/turtlebot_swarm/launch',
        glob('launch/*.py')
        ),

        (
        'share/turtlebot_swarm/worlds',
        glob('worlds/*.wbt')
        ),

        (
            os.path.join(
                'share',
                package_name,
                'resource'
            ),
            glob('resource/*')
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='manish',
    maintainer_email='manish@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
