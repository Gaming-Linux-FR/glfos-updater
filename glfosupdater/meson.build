subdir('views')

moduledir = 'glfosupdater'

sources = [
  '__init__.py',
  'main.py',
]

configure_file(
  input: 'constants.py.in',
  output: 'constants.py',
  configuration: conf,
  install_dir: PY_INSTALLDIR.get_install_dir() / moduledir
)

PY_INSTALLDIR.install_sources(sources, subdir: moduledir)

configure_file(
  input: 'glfosupdater.in',
  output: 'glfos-updater',
  configuration: conf,
  install_dir: get_option('bindir')
)
