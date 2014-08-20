

from argparse import ArgumentParser


class Options(object):

    def __init__(self, help_doc):
        self.argparser = ArgumentParser(help_doc)

    def group(self, help_doc):
        group_parser =  self.argparser.add_argument_group(help_doc)
        return GroupOptions(group_parser)

    @property
    def define(self):
       return  self.argparser.add_argument

    def parse_args(self):
        return self.argparser.parse_args()


class GroupOptions(object):
    def __init__(self, group_parser):
        self.group_parser = group_parser

    @property
    def define(self):
        return self.group_parser.add_argument

_options = None
def setup_options(doc):
    global _options
    _options = Options(doc)

def group(help_doc):
    return _options.group(help_doc)


def define(*args, **kw):
    return _options.define(*args, **kw)

def parse_args():
	return _options.parse_args()