:: Jupyter start script for Python 3.5.4 in Windows


::@echo off

set PYTHON_HOME=C:/dev/miniconda/envs/py356

set PATH=%PYTHON_HOME%;%PYTHON_HOME%/Scripts;%PATH%
set JUPYTER_CONFIG_DIR=%~dp0
set JUPYTER_PATH=%JUPYTER_CONFIG_DIR%
set WORKING_DIR=%JUPYTER_CONFIG_DIR%/..
set JUPYTER_DATA_DIR=%JUPYTER_CONFIG_DIR%
set IPYTHONPATH=%JUPYTER_CONFIG_DIR%


:: add working dir as PYTHONPATH to avoid os.chdir explicitly in notebook
:: add RiskPal and FRTB projects
::set PYTHONPATH=%WORKING_DIR%;%WORKING_DIR%/../RiskPAL;%WORKING_DIR%/../FRTB/var_comparison_tool

echo %PYTHONPATH%


:: set JU::PYTER_KERNEL_FILE=%JUPYTER_DATA_DIR%/kernels/python354/kernel.json
:: rm %JUPYTER_KERNEL_FILE%
:: (
:: echo {"display_name": "Python 3.5.4","language": "python","argv": [
:: echo  "%PYTHON_HOME%/python",
:: echo  "-m", "ipykernel",
:: echo  "--ipython-dir=%JUPYTER_DATA_DIR%",
:: echo  "--profile=default",
:: echo  "--HistoryManager.enabled=False",
:: echo  "-f", "{connection_file}"
:: echo ]}
:: ) > %JUPYTER_KERNEL_FILE%



jupyter notebook --config=%JUPYTER_CONFIG_DIR%\jupyter_notebook_config.py --port=18888 --notebook-dir=%WORKING_DIR% --no-mathjax