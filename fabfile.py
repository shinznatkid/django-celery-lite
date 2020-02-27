from fabric.api import local


def upload():
    try:
        local('rm -r ./dist')
    except:
        pass
    local('python setup.py sdist bdist_wheel')
    local('twine upload dist/*')
