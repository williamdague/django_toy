from fabric.api import local, lcd

def prepare_deployment():
    local('python manage.py test toy_app')
    local('git add -p && git commit')

def deploy():
    with lcd('/Users/bill/CIQ/front-end/django_toy/django_toy'):

        # With git...
        local('git pull /Users/bill/CIQ/front-end/django_toy/dev')

        ## With Mercurial...
        #local('hg pull /my/path/to/dev/area/')
        #local('hg update')

        # With both
        local('python manage.py migrate toy_app')
        local('python manage.py test toy_app')
#        local('/my/command/to/restart/webserver')
