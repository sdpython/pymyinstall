
.. blogpost::
    :title: Install pythonnet on debian is difficult
    :keywords: python, debian, pythonnet
    :date: 2021-01-15
    :categories: installation

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

    Unfortunately, *pythonnet* does not work with *dotnet*
    yet on linux. *mono* is still needed
    (see `Add the Mono repository to your system
    <https://www.mono-project.com/download/stable/#download-lin-debian>`_).

    ::

        sudo apt install apt-transport-https dirmngr gnupg ca-certificates
        sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
        echo "deb https://download.mono-project.com/repo/debian stable-stretch main" | sudo tee /etc/apt/sources.list.d/mono-official-stable.list
        sudo apt update
        sudo apt install mono-devel nuget
        mono --version

    The package `dotnetcore2 <https://pypi.org/project/dotnetcore2/>`_
    might be needed. This is a work in progress.
