
.. blogpost::
    :title: Create a wheel with an installed package
    :keywords: setup
    :date: 2017-11-08
    :categories: wheel

    It happens sometimes you install package but you don't remember
    exactly you did it. However, you would like to make a wheel
    from what is installed in folder ``site-packages``.
    There is probably a better way but I created a local
    folder orgnized this way:

    ::

        folder
          |- setup.py
          |- src
              |- __init__.py (empty)
              |- <__PACKAGE__>
              |- ... (the content)

    In ``setup.py``, I wrote:

    ::

        import sys
        import os
        from distutils.core import setup
        from setuptools import find_packages

        project_var_name = "__PACKAGE__"
        version = "0.2.1"
        path = "Lib/site-packages/" + project_var_name

        # sources
        packages = find_packages('src', exclude='src')
        package_dir = {k: "src/" + k.replace(".", "/") for k in packages}

        # data
        package_data = {}
        for r, d, f in os.walk('src'):
            for a in f:
                temp = os.path.join(r, a)
                name0 = temp
                if "__pycache__" in temp:
                    continue
                if temp.endswith(".py"):
                    continue
                temp = temp.replace("\\", "/")
                if not temp.startswith("src/"):
                    raise ValueError(temp)
                fold = os.path.dirname(temp)
                init = os.path.join(fold, "__init__.py")
                if not os.path.exists(init):
                    print("adding ", init)
                    with open(init, "w") as f:
                        pass
                temp = temp[4:]
                if temp == "__init__.py":
                    continue
                fold, name = os.path.split(temp)
                pack = fold.replace("/", ".")
                if pack not in package_data:
                    package_data[pack] = []
                package_data[pack].append(name)

        # setup
        setup(name=project_var_name,
              version=version,
              packages=packages,
              package_dir=package_dir,
              package_data=package_data)

    You get a wheel you can install in some other places
    and no zip or unzip is needed.
