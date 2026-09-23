# ROS 2 Package Structure — student_robotics

Created with:

```bash
cd robot_ws/src
ros2 pkg create --build-type ament_python student_robotics --dependencies rclpy
```

## Files and Their Roles

```
student_robotics/
├── package.xml              # package manifest (metadata + dependencies)
├── setup.py                 # setuptools install script (entry_points live here)
├── setup.cfg                # where installed scripts go (lib/student_robotics)
├── resource/
│   └── student_robotics     # empty marker file → ament package index
├── student_robotics/        # the Python module (imported code lives here)
│   ├── __init__.py
│   └── hello_node.py        # the node implementation
└── test/                    # lint test stubs run by `colcon test`
    ├── test_copyright.py
    ├── test_flake8.py
    └── test_pep257.py
```

### package.xml — the manifest

Read by colcon and rosdep (not by Python). Declares name, version,
description, maintainer, license, and dependencies. `<depend>rclpy</depend>`
is the only runtime dependency; the `<test_depend>` entries support the
lint tests. `<build_type>ament_python</build_type>` tells colcon this
package is installed with setuptools, not CMake.

### setup.py — installation and entry points

Executed by colcon during the build. Two jobs:

1. `data_files` installs `resource/student_robotics` into
   `share/ament_index/resource_index/packages/` (this is what makes the
   package discoverable by `ros2 pkg ...` commands) and copies
   `package.xml` into `share/student_robotics/`.
2. `entry_points` → `console_scripts` registers commands:

```python
'hello_node = student_robotics.hello_node:main'
```

This line is why `ros2 run student_robotics hello_node` works: it maps
the command name to the `main()` function in
`student_robotics/hello_node.py`.

### setup.cfg — script destination

Tells setuptools to place generated scripts under
`lib/student_robotics/` inside the install directory. Without it,
installed scripts would land where `ros2 run` does not look.

### resource/ — the discovery marker

`ros2 pkg list`, `ros2 pkg prefix`, and `ros2 pkg executables` work by
scanning `share/ament_index/resource_index/packages/`. The presence of
the (empty) marker file named `student_robotics` there is what makes the
package visible to the toolchain.

### The module directory

`student_robotics/student_robotics/` is a normal Python package (has
`__init__.py`, found by `find_packages()` in setup.py). `hello_node.py`
contains `HelloNode` (an `rclpy.node.Node` subclass named `hello_node`)
and a `main()` that initializes rclpy, spins, and cleans up on
interrupt.

## What Happens Between colcon build and ros2 run

1. `colcon build` runs setup.py: the module is copied into
   `install/student_robotics/lib/python3.10/site-packages/`, scripts are
   generated in `install/student_robotics/lib/student_robotics/`, and the
   marker + package.xml are placed in `install/student_robotics/share/`.
2. `source install/setup.bash` prepends the workspace's install tree to
   the environment (AMENT/COLCON prefix paths).
3. `ros2 run student_robotics hello_node` looks up the package in the
   ament index, finds the `hello_node` script, and executes it.

Skipping step 2 is the classic mistake: the build succeeds but
`ros2 run` cannot find the package.

## Metadata Conventions Used

- Version `0.1.0` in both package.xml and setup.py (kept consistent).
- Maintainer: don1379 (outlook address from git config).
- License: MIT, with a top-level `LICENSE` file in the repository.
