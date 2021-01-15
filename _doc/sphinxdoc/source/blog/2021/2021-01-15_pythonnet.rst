
.. blogpost::
    :title: Install pythonnet on debian
    :keywords: python, debian, pythonnet
    :date: 2021-01-15
    :categories: installation

    **Step 1: install dotnet**

    From `Install the .NET SDK or the .NET Runtime on Debian
    <https://docs.microsoft.com/en-us/dotnet/core/install/linux-debian>`_.

    ::

        wget https://packages.microsoft.com/config/debian/10/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
        sudo dpkg -i packages-microsoft-prod.deb
        sudo apt-get update
        sudo apt-get install -y apt-transport-https
        sudo apt-get install -y dotnet-sdk-5.0
        sudo apt-get install -y aspnetcore-runtime-5.0
        sudo apt-get install -y dotnet-runtime-5.0

    Then build `pythonnet
    <https://github.com/pythonnet/pythonnet>`_:

    ::

        git clone https://github.com/pythonnet/pythonnet
        cd pythonnet
        python3.9 setup.py build_dotnet
        python3.9 setup.py bdist_wheel
