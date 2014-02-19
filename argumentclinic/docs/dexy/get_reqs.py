import os.path
from pip.req import parse_requirements
import argumentclinic

req_file_path = '../../requirements.txt'
# This worked independent of dexy, and not within dexy,
# actual directory for execution was /home/catherine/proj/argument-clinic/argumentclinic/docs/dexy/.dexy/work/85/853c355a6eed8b5fab5bbf05c0d3dd8f-001-py

req_file_path = os.path.abspath(os.path.join(argumentclinic.__file__, '../../requirements.txt'))
reqs = parse_requirements(req_file_path)

def requirements_met():
    result = []
    for req in reqs:
        if req.check_if_exists():
            result.append("%s: satisfied by %s" % 
                           (str(req.req), req.satisfied_by))
        else:
            result.append("%s: not installed" % 
                           (str(req.req), ))
    return result

if __name__ == '__main__':
    result = requirements_met()
    print("\n".join(result))

