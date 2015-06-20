"""
@file
@brief Functions to remember a step was done, uses files.
"""
import os
import datetime


def mark_step(folder, step_name, content = ""):
    """
    create a file to remember was done (running it again takes times)
    
    @param      folder      folder where to write
    @param      step_name   step_name
    @param      content     what to write in the file
    @return                 created file name
    """
    name = os.path.join(folder, "log.step.{0}.txt".format(step_name))
    with open(name, "w", encoding="utf8") as f:
        f.write("# -- STEP {0} DONE --\n\n".format(step_name))
        f.write("# -- {0}\n\n".format(datetime.datetime.now()))
        if content is not None:
            f.write(content)
        f.write("\n# -- {0}".format(datetime.datetime.now()))
    return name
    
    
def is_step_done(folder, step_name):
    """
    checks a file was written with function @see fn mark_step
    
    @param      folder      folder where to write
    @param      step_name   step_name
    @return                 boolean
    """
    name = os.path.join(folder, "log.step.{0}.txt".format(step_name))
    if not os.path.exists(name):
        return False
    s = "# -- STEP {0} DONE --\n\n".format(step_name)
    with open(name, "r", encoding="utf8") as f:
        content = f.read()
    if content.startswith(s):
        with open(name, "a", encoding="utf8") as f:
            f.write("\n# skip {0}".format(datetime.datetime.now()))
        return True
    else:
        return False