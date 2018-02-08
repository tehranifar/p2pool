from distutils.core import setup, Extension

zcoin_lyra2_module = Extension('xzc_lyra2',
                               sources = ['lyra2module.c',
                                          'Lyra2Z.c',
                                          'Sponge.c',
                                          'Lyra2.c',
                                          'blake.c'],
                               include_dirs=['.'])

setup (name = 'xzc_lyra2',
       version = '1.0',
       description = 'Bindings for Lyra2 proof of work used by Zcoin',
       ext_modules = [zcoin_lyra2_module])
