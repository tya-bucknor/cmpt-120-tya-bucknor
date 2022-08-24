import os
import platform

# get the path of this script.
DIR = os.path.dirname(__file__)

# get the proper path delimiter.
delimiter = "\\" if "Windows" in platform.platform() else "/"

test_files = ""

# dynamically build list of robot framework test files.
for index in range(1, 17):
    test_file = DIR + delimiter + "assignments" + delimiter + f"assignment-{index}" + delimiter + "test.robot"
    if not os.path.exists(test_file):
        continue
    test_files += f" {test_file}"

os.system(f"python3 -m robot {test_files}")