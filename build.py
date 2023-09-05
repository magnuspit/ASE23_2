import subprocess

def build_project():
    subprocess.run(["python", "src/mycode.py"])
    subprocess.run(["python", "-m", "unittest", "src/test1.py"])
    subprocess.run(["python", "-m", "unittest", "src/test2.py"])

if __name__ == "__main__":
    build_project()
