import os

structure = {
    "_Kode_Program": {
        "Java_GUI_Desktop": {
            "src": {
                "main": {
                    "java": {
                        "com": {
                            "your_package": {
                                "gui": {
                                    "controller": {},
                                    "model": {},
                                    "service": {
                                        "ApiClient.java": "",
                                        "ProcessManager.java": ""
                                    },
                                    "MainApp.java": ""
                                }
                            }
                        }
                    },
                    "resources": {
                        "fxml": {},
                        "css": {},
                        "images": {}
                    }
                }
            },
            "pom.xml": "",
            "README_Java.md": ""
        },
        "Python_API_Backend": {
            "venv": {},  # Virtual environment folder (should not be committed)
            "app": {
                "__init__.py": "",
                "main.py": "",
                "models.py": "",
                "service.py": "",
                "utils.py": ""
            },
            "data": {
                "ekskul_data.csv": ""
            },
            "model": {
                "kmeans_model.joblib": ""
            },
            "tests": {},
            "requirements.txt": "",
            "run.py": "",
            "README_Python.md": ""
        },
        "Packaging": {
            "build_python_exe.bat": "",
            "build_java_jar.bat": ""
        }
    }
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, 'w') as f:
                f.write(content)

base_path = os.getcwd()  # Current working directory
create_structure(base_path, structure)