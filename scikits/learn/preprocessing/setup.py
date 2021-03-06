from os.path import join
import numpy


def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration

    config = Configuration('preprocessing', parent_package, top_path)

    config.add_extension(
        '_preprocessing',
        sources=[join('src', '_preprocessing.c')],
        include_dirs=[numpy.get_include()]
    )

    return config


if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())
