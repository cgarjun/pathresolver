import os, imp
from nlogger.logger import logging


def get_template_dir():
    '''
    Returns a path resolver template envrionment variable value
    '''
    template_dir = os.getenv('PATHRESOLVER_TEMPLATE_DIR', None)
    return template_dir

def get_module(template_file):
    '''
    Retuns the imported module template
    '''
    template_dir = get_template_dir()
    abstpath = None
    if template_dir is not None:
        abspath_template_file = os.path.join(template_dir, '{0}.py'.format(template_file))
        module = imp.load_source(template_file, abspath_template_file)
        return module
    else:
        return None


class PathResolver(object):
    '''
    doctsting
    '''
    def __init__(self, token=None, template_file='template'):
        """
        docstring
        """
        self._token = token
        self._template_file = template_file

    def resolve_token(self, **kwargs):
        module = get_module(self.template_file)
        return module.__dict__.get(self._token).format(**kwargs)

    def get_token(self):
        module = get_module(self.template_file)
        return module.__dict__.get(self.token)

    def list_all_tokens(self):
        '''
        prints all tokens available in the template python file
        '''
        module = get_module(self.template_file)
        all_values = {key: value for key, value in module.__dict__.iteritems() if not (key.startswith('__') or key.startswith('_'))}
        for val in all_values:
            logging.info("{0}: {1}".format(val, all_values[val]))

    @property
    def token(self):
        """
        docstring
        """
        return self._token

    @property
    def template_file(self):
        """
        docstring
        """
        return self._template_file
