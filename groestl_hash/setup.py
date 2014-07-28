from distutils.core import setup, Extension

groestl_hash_module = Extension('skein_hash',
                               sources = ['skeinmodule.c',
                                          'skein.c',
										  'sph/skein.c',
                               include_dirs=['.', './sph'])


setup (name = 'Skein_hashs',
       version = '0.1',
       description = 'Bindings for Skein Used by MyriadCoin',
       ext_modules = [groestl_hash_module])
