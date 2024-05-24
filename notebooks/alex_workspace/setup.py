from setuptools import setup, find_packages

setup(
    name='project_pokereader',
    version='1.0.0',
    description='A comprehensive Python package for machine learning model deployment with Streamlit, Docker, FastAPI, and Google Cloud Platform (GCP).',
    author='Yuri, Estelle, Emilia, Alex',
    author_email='alex.tm.chiu@gmail.com',
    packages=find_packages(),
    install_requires=[ #tbconfirmed
        'absl-py==2.1.0',
        'annotated-types==0.7.0',
        'anyio==4.3.0',
        'appnope==0.1.4',
        'argon2-cffi==23.1.0',
        'argon2-cffi-bindings==21.2.0',
        'array_record==0.5.1',
        'arrow==1.3.0',
        'astroid==3.2.2',
        'asttokens==2.4.1',
        'astunparse==1.6.3',
        'async-lru==2.0.4',
        'attrs==23.2.0',
        'Babel==2.15.0',
        'beautifulsoup4==4.12.3',
        'bleach==6.1.0',
        'cachetools==5.3.3',
        'certifi==2024.2.2',
        'cffi==1.16.0',
        'charset-normalizer==3.3.2',
        'click==8.1.7',
        'comm==0.2.2',
        'contourpy==1.2.1',
        'cycler==0.12.1',
        'debugpy==1.8.1',
        'decorator==5.1.1',
        'defusedxml==0.7.1',
        'dill==0.3.8',
        'dm-tree==0.1.8',
        'dnspython==2.6.1',
        'email_validator==2.1.1',
        'etils==1.7.0',
        'exceptiongroup==1.2.1',
        'executing==2.0.1',
        'fastapi==0.111.0',
        'fastapi-cli==0.0.4',
        'fastjsonschema==2.19.1',
        'ffmpeg-python==0.2.0',
        'flatbuffers==24.3.25',
        'fonttools==4.51.0',
        'fqdn==1.5.1',
        'fsspec==2024.5.0',
        'future==1.0.0',
        'gast==0.5.4',
        'google-auth==2.29.0',
        'google-auth-oauthlib==1.2.0',
        'google-pasta==0.2.0',
        'grpcio==1.64.0',
        'h11==0.14.0',
        'h5py==3.11.0',
        'httpcore==1.0.5',
        'httptools==0.6.1',
        'httpx==0.27.0',
        'idna==3.7',
        'imageio==2.34.1',
        'importlib_resources==6.4.0',
        'iniconfig==2.0.0',
        'ipdb==0.13.13',
        'ipykernel==6.29.4',
        'ipython==8.24.0',
        'ipywidgets==8.1.2',
        'isoduration==20.11.0',
        'isort==5.13.2',
        'jedi==0.19.1',
        'Jinja2==3.1.4',
        'joblib==1.4.2',
        'json5==0.9.25',
        'jsonpointer==2.4',
        'jsonschema==4.22.0',
        'jsonschema-specifications==2023.12.1',
        'jupyter==1.0.0',
        'jupyter-console==6.6.3',
        'jupyter-events==0.10.0',
        'jupyter-lsp==2.2.5',
        'jupyter_client==8.6.1',
        'jupyter_core==5.7.2',
        'jupyter_server==2.14.0',
        'jupyter_server_terminals==0.5.3',
        'jupyterlab==4.2.0',
        'jupyterlab_pygments==0.3.0',
        'jupyterlab_server==2.27.1',
        'jupyterlab_widgets==3.0.10',
        'keras==3.3.3',
        'kiwisolver==1.4.5',
        'lazy_loader==0.4',
        'libclang==18.1.1',
        'Markdown==3.6',
        'markdown-it-py==3.0.0',
        'MarkupSafe==2.1.5',
        'matplotlib==3.9.0',
        'matplotlib-inline==0.1.7',
        'mccabe==0.7.0',
        'mdurl==0.1.2',
        'mistune==3.0.2',
        'ml-dtypes==0.3.2',
        'namex==0.0.8',
        'nbclient==0.10.0',
        'nbconvert==7.16.4',
        'nbformat==5.10.4',
        'nest-asyncio==1.6.0',
        'networkx==3.3',
        'notebook==7.2.0',
        'notebook_shim==0.2.4',
        'numpy==1.26.4',
        'oauthlib==3.2.2',
        'opencv-python==4.9.0.80',
        'opt-einsum==3.3.0',
        'optree==0.11.0',
        'orjson==3.10.3',
        'overrides==7.7.0',
        'packaging==24.0',
        'pandas==2.2.2',
        'pandocfilters==1.5.1',
        'parso==0.8.4',
        'pexpect==4.9.0',
        'pillow==10.3.0',
        'platformdirs==4.2.2',
        'pluggy==1.5.0',
        'prometheus_client==0.20.0',
        'promise==2.3',
        'prompt-toolkit==3.0.43',
        'protobuf==3.20.3',
        'psutil==5.9.8',
        'ptyprocess==0.7.0',
        'pure-eval==0.2.2',
        'pyasn1==0.6.0',
        'pyasn1_modules==0.4.0',
        'pycparser==2.22',
        'pydantic==2.7.1',
        'pydantic_core==2.18.2',
        'Pygments==2.18.0',
        'pylint==3.2.1',
        'pyparsing==3.1.2',
        'pytesseract==0.3.10',
        'pytest==8.2.1',
        'python-dateutil==2.9.0.post0',
        'python-dotenv==1.0.1',
        'python-json-logger==2.0.7',
        'python-multipart==0.0.9',
        'pytz==2024.1',
        'PyYAML==6.0.1',
        'pyzmq==26.0.3',
        'qtconsole==5.5.2',
        'QtPy==2.4.1',
        'referencing==0.35.1',
        'requests==2.31.0',
        'requests-oauthlib==2.0.0',
        'rfc3339-validator==0.1.4',
        'rfc3986-validator==0.1.1',
        'rich==13.7.1',
        'rpds-py==0.18.1',
        'rsa==4.9',
        'scikit-image==0.23.2',
        'scikit-learn==1.4.2',
        'scipy==1.13.0',
        'screeninfo==0.8.1',
        'seaborn==0.13.2',
        'Send2Trash==1.8.3',
        'shellingham==1.5.4',
        'six==1.16.0',
        'sniffio==1.3.1',
        'soupsieve==2.5',
        'stack-data==0.6.3',
        'starlette==0.37.2',
        'tensorboard==2.16.2',
        'tensorboard-data-server==0.7.2',
        'tensorflow==2.16.1',
        'tensorflow-datasets==4.9.4',
        'tensorflow-estimator==2.15.0',
        'tensorflow-io-gcs-filesystem==0.37.0',
        'tensorflow-metadata==1.15.0',
        'termcolor==2.4.0',
        'terminado==0.18.1',
        'Theano==1.0.5',
        'threadpoolctl==3.5.0',
        'tifffile==2024.5.10',
        'tinycss2==1.0.0',
        'toml==0.10.2',
        'tomli==2.0.1',
        'tomlkit==0.12.5',
        'tornado==6.4',
        'tqdm==4.66.4',
        'traitlets==5.14.3',
        'typer==0.12.3',
        'types-python-dateutil==2.9.0.20240316',
        'typing_extensions==4.11.0',
        'tzdata==2024.1',
        'ujson==5.10.0',
        'uri-template==1.3.0',
        'urllib3==2.2.1',
        'uvicorn==0.29.0',
        'uvloop==0.19.0',
        'watchfiles==0.21.0',
        'wcwidth==0.2.13',
        'webcolors==1.13',
        'webencodings==0.5.1',
        'websocket-client==1.8.0',
        'websockets==12.0',
        'Werkzeug==3.0.3',
        'widgetsnbextension==4.0.10',
        'wrapt==1.14.1',
        'zipp==3.18.2',
    ],
)